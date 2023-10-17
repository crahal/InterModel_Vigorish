import pandas as pd
import os
import numpy as np
import seaborn as sns
from scipy.optimize import minimize
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold, KFold
from lightgbm import LGBMClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier

params = {
    'silent': True,
    # Other parameters
}

def wrangle_titanic(train_df):
    train_df = train_df.drop(['Ticket', 'Cabin'], axis=1)
    train_df['Title'] = train_df.Name.str.extract(' ([A-Za-z]+)\.', expand=False)
    train_df['Title'] = train_df['Title'].replace(['Lady', 'Countess','Capt', 'Col',
                                                 'Don', 'Dr', 'Major', 'Rev', 'Sir',
                                                 'Jonkheer', 'Dona'], 'Rare')
    train_df['Title'] = train_df['Title'].replace('Mlle', 'Miss')
    train_df['Title'] = train_df['Title'].replace('Ms', 'Miss')
    train_df['Title'] = train_df['Title'].replace('Mme', 'Mrs')
    title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5}
    train_df['Title'] = train_df['Title'].map(title_mapping)
    train_df['Title'] = train_df['Title'].fillna(0)
    train_df = train_df.drop(['Name', 'PassengerId'], axis=1)
    train_df['Sex'] = train_df['Sex'].map( {'female': 1, 'male': 0} ).astype(int)
    guess_ages = np.zeros((2,3))
    for i in range(0, 2):
        for j in range(0, 3):
            guess_df = train_df[(train_df['Sex'] == i) & \
                                (train_df['Pclass'] == j+1)]['Age'].dropna()
            age_guess = guess_df.median()
            guess_ages[i,j] = int(age_guess/0.5 + 0.5 ) * 0.5
    for i in range(0, 2):
        for j in range(0, 3):
            train_df.loc[(train_df.Age.isnull()) & (train_df.Sex == i) &
                         (train_df.Pclass == j+1), 'Age'] = guess_ages[i,j]
    train_df['Age'] = train_df['Age'].astype(int)
    train_df['AgeBand'] = pd.cut(train_df['Age'], 5)
    train_df.loc[train_df['Age'] <= 16, 'Age'] = 0
    train_df.loc[(train_df['Age'] > 16) & (train_df['Age'] <= 32), 'Age'] = 1
    train_df.loc[(train_df['Age'] > 32) & (train_df['Age'] <= 48), 'Age'] = 2
    train_df.loc[(train_df['Age'] > 48) & (train_df['Age'] <= 64), 'Age'] = 3
    train_df.loc[train_df['Age'] > 64, 'Age'] = 5
    train_df = train_df.drop(['AgeBand'], axis=1)
    train_df['FamilySize'] = train_df['SibSp'] + train_df['Parch'] + 1
    train_df['IsAlone'] = 0
    train_df.loc[train_df['FamilySize'] == 1, 'IsAlone'] = 1
    train_df = train_df.drop(['Parch', 'SibSp', 'FamilySize'], axis=1)
    train_df['Age*Class'] = train_df.Age * train_df.Pclass
    freq_port = train_df.Embarked.dropna().mode()[0]
    train_df['Embarked'] = train_df['Embarked'].fillna(freq_port)
    train_df['Embarked'] = train_df['Embarked'].map( {'S': 0, 'C': 1, 'Q': 2} ).astype(int)
    train_df['FareBand'] = pd.qcut(train_df['Fare'], 4)
    train_df.loc[train_df['Fare'] <= 7.91, 'Fare'] = 0
    train_df.loc[(train_df['Fare'] > 7.91) & (train_df['Fare'] <= 14.454), 'Fare'] = 1
    train_df.loc[(train_df['Fare'] > 14.454) & (train_df['Fare'] <= 31), 'Fare']   = 2
    train_df.loc[train_df['Fare'] > 31, 'Fare'] = 3
    train_df['Fare'] = train_df['Fare'].dropna().astype(int)
    train_df = train_df.drop(['FareBand'], axis=1)
    if 'Survived' in train_df.columns:
        X_train = train_df.drop("Survived", axis=1)
        Y_train = train_df["Survived"]
    else:
        X_train = train_df
        Y_train = None
    return X_train, Y_train


def get_scores(Y_test, y_class, y_prob, y_train, Y_log_pred_proba):

    def calc_r2(truth, pred, ybar_train):
        """Replicate FFC eval metric"""
        pred_err_sq = (truth - pred) ** 2
        sum_pred_err_sqr = pred_err_sq.sum()
        dev_sqr = (truth - ybar_train) ** 2
        sum_dev_sqr = dev_sqr.sum()
        r2 = 1 - (sum_pred_err_sqr / sum_dev_sqr)
        return r2

    def ll(x, p):
        """x is the truth, p is the guess"""
        z = (np.log(p) * x) + (np.log(1 - p) * (1 - x))
        return np.exp(np.sum(z) / len(z))

    def get_w(a, guess=0.5, bounds=[(0.001, 0.999)]):
        """argmin calc for 'w'"""
        res = minimize(minimize_me, guess, args=a,
                       options={'ftol': 0, 'gtol': 1e-09},
                       method='L-BFGS-B', bounds=bounds)
        return res['x'][0]

    def minimize_me(p, a):
        """ function to be minimized"""
        # abs(p*log(p)+(1-p)*log(1-p)-log(a))
        return abs((p * np.log(p)) + ((1 - p) * np.log(1 - p)) - np.log(a))

    def get_ew(w0, w1):
        """calculate the e(w) metric from w0 and w1"""
        return (w1 - w0) / w0

    y_prob = [x + 0.001 if x == 0 else x for x in y_prob]
    y_prob = np.array([x - 0.001 if x == 1 else x for x in y_prob])
    score_list = []
    score_list.append(metrics.log_loss(Y_test.to_list(), y_prob))
    score_list.append(metrics.accuracy_score(Y_test.to_list(), y_class))
    score_list.append(metrics.brier_score_loss(Y_test.to_list(), y_prob))
    score_list.append(metrics.f1_score(Y_test.to_list(), y_class))
    score_list.append(metrics.roc_auc_score(Y_test.to_list(), y_prob))
    score_list.append(metrics.jaccard_score(Y_test.to_list(), y_class))
    score_list.append(calc_r2(Y_test, y_prob, len(y_prob)*[np.mean(y_train)]))
    # Note: to get the IMV vs the benchmark, replace Y_log_pred_proba here with np.mean(y_train)
    score_list.append(get_ew(get_w(ll(Y_test, Y_log_pred_proba)), get_w(ll(Y_test, y_prob))))
    return score_list


def get_predictions(X_train, Y_train, X_test, Y_test):
    """Get predictions from the split data"""
    logreg = LogisticRegression()
    logreg.fit(X_train, Y_train)
    Y_log_pred_class = logreg.predict(X_test)
    Y_log_pred_proba = logreg.predict_proba(X_test)[:,1]
    log_scores = get_scores(Y_test, Y_log_pred_class, Y_log_pred_proba, Y_train, Y_log_pred_proba)

    svc = SVC(random_state=1000000, probability=True)
    svc.fit(X_train, Y_train)
    Y_svc_pred_class = svc.predict(X_test)
    svc = SVC(random_state=1000000, probability=True)
    svc.fit(X_train, Y_train)
    Y_svc_pred_proba = svc.predict_proba(X_test)[:,1]
    svc_scores = get_scores(Y_test, Y_svc_pred_class, Y_svc_pred_proba, Y_train, Y_log_pred_proba)

    knn = KNeighborsClassifier(n_neighbors = 3)
    knn.fit(X_train, Y_train)
    Y_knn_pred_class = knn.predict(X_test)
    Y_knn_pred_proba = knn.predict_proba(X_test)[:,1]
    knn_scores = get_scores(Y_test, Y_knn_pred_class, Y_knn_pred_proba, Y_train, Y_log_pred_proba)

    gaussian = GaussianNB()
    gaussian.fit(X_train, Y_train)
    Y_gau_pred_class = gaussian.predict(X_test)
    Y_gau_pred_proba = gaussian.predict_proba(X_test)[:,1]
    gaussian_scores = get_scores(Y_test, Y_gau_pred_class, Y_gau_pred_proba, Y_train, Y_log_pred_proba)

    decision_tree = DecisionTreeClassifier()
    decision_tree.fit(X_train, Y_train)
    Y_dt_pred_class = decision_tree.predict(X_test)
    Y_dt_pred_proba = decision_tree.predict_proba(X_test)[:,1]
    dt_scores = get_scores(Y_test, Y_dt_pred_class, Y_dt_pred_proba, Y_train, Y_log_pred_proba)

    lgbm = LGBMClassifier(objective='binary', random_state=5, verbose=-1)
    lgbm.fit(X_train, Y_train)
    Y_lgbm_pred_class = lgbm.predict(X_test)
    Y_lgbm_pred_proba = lgbm.predict_proba(X_test)[:,1]
    lgbm_scores = get_scores(Y_test, Y_lgbm_pred_class, Y_lgbm_pred_proba, Y_train, Y_log_pred_proba)

    random_forest = RandomForestClassifier(n_estimators=100)
    random_forest.fit(X_train, Y_train)
    Y_rf_pred_class = random_forest.predict(X_test)
    Y_rf_pred_proba = random_forest.predict_proba(X_test)[:,1]
    rf_scores = get_scores(Y_test, Y_rf_pred_class, Y_rf_pred_proba, Y_train, Y_log_pred_proba)

    baseline_pred_class = len(Y_test)*[0]
    baseline_pred_proba = len(Y_test)*[np.mean(Y_train)]
    baseline_scores = get_scores(Y_test, baseline_pred_class, baseline_pred_proba, Y_train, Y_log_pred_proba)
    score_holder = pd.DataFrame(list(zip(log_scores,
                                         svc_scores,
                                         gaussian_scores,
                                         lgbm_scores,
                                         rf_scores,
                                         baseline_scores)),
                        columns=['Logistic', 'SVC', 'Naive Bayes',
                                 'LightGBM', 'RF', 'Prevalence'],
                        index=['Log Loss', 'Accuracy', 'Brier Score Loss', 'F1', 'ROC-AUC', 'Jaccard', 'R2', 'IMV'])
    proba_holder = pd.DataFrame(list(zip(Y_log_pred_proba,
                                         Y_svc_pred_proba,
                                         Y_gau_pred_proba,
                                         Y_lgbm_pred_proba,
                                         Y_rf_pred_proba,
                                         baseline_pred_proba)),
                        columns=['Logistic', 'SVC', 'Naive Bayes',
                                 'LightGBM', 'RF', 'Baseline'])
    return score_holder, proba_holder


def titanic_main(data_path, table_path):
    train_df = pd.read_csv(os.path.join(data_path, 'titanic', 'train.csv'))
    print('Insample prevelance: ', np.mean(train_df['Survived']))
    X, y = wrangle_titanic(train_df)
    n_fold = 10
    skf = KFold(n_splits=n_fold, random_state=1234, shuffle=True)
#    score_holder = pd.DataFrame()
#    prob_holder = pd.DataFrame()
    imv_holder = []
    counter = 0
    for train_index, test_index in skf.split(X, y):
        X_train, X_test = X[X.index.isin(train_index)], X[X.index.isin(test_index)]
        y_train, y_test = y[y.index.isin(train_index)], y[y.index.isin(test_index)]
        if counter == 0:
            score_holder, prob_holder = get_predictions(X_train, y_train, X_test, y_test)
            imv_holder.append(score_holder.at['IMV', 'LightGBM'])
        else:
            score_temp, prob_temp = get_predictions(X_train, y_train, X_test, y_test)
            score_holder = score_holder + score_temp
            imv_holder.append(score_temp.at['IMV', 'LightGBM'])
            prob_holder = prob_holder.append(prob_temp)
        counter = counter + 1
    score_holder = (score_holder / n_fold).round(decimals=4)
    print(score_holder)
    print('IMV of LightGBM vs Logistic Regression, mean: ' + str(np.mean(imv_holder)))
    print('IMV of LightGBM vs Logistic Regression, std: ' + str(np.std(imv_holder)))
    score_holder.to_csv(os.path.join(table_path, 'titanic_table.csv'))

    def make_predictions_for_eval(data_path):
        train_df = pd.read_csv(os.path.join(data_path, 'titanic', 'train.csv'))
        test_df = pd.read_csv(os.path.join(data_path, 'titanic', 'test.csv'))
        X_train, y_train = wrangle_titanic(train_df)
        X_test, y_test = wrangle_titanic(test_df)
        lgbm = LGBMClassifier(objective='binary', random_state=5, verbose=-1)
        lgbm.fit(X_train, y_train)
        test_df['Survived'] = lgbm.predict(X_test)
        test_df[['PassengerId', 'Survived']].to_csv(os.path.join(data_path, 'titanic', 'titanic_for_eval.csv'),
                                                   index=False)

    make_predictions_for_eval(data_path)
    #return score_holder, prob_holder
