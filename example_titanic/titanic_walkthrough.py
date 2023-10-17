import numpy as np
import pandas as pd
from scipy.optimize import minimize
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression


def ll(x, p):
    z = (np.log(p) * x) + (np.log(1 - p) * (1 - x))
    return np.exp(np.sum(z) / len(z))


def get_w(a, guess=0.5, bounds=[(0.5, 0.999)]):
    res = minimize(minimize_me, guess, args=a,
                   options={'ftol': 0, 'gtol': 1e-09},
                   method='L-BFGS-B', bounds=bounds)
    return res['x'][0]


def minimize_me(p, a):
    return abs((p * np.log(p)) + ((1 - p) * np.log(1 - p)) - np.log(a))


def calculate_imv(y_basic, y_enhanced, y):
    ll_basic = ll(y, y_basic)
    ll_enhanced = ll(y, y_enhanced)
    w0 = get_w(ll_basic)
    w1 = get_w(ll_enhanced)
    return (w1 - w0) / w0


if __name__ == "__main__":
    # Load and preprocess data
    titanic = pd.read_csv('../data/titanic/titanic3.csv')
    titanic['constant'] = 1
    titanic['sex'] = titanic['sex'].map({'female': 1, 'male': 0})
    titanic = titanic.sample(frac = 1, random_state=22092023)
    # Define the number of folds
    num_folds = 10

    # Calculate the fold size
    fold_size = len(titanic) // num_folds

    # Initialize an array to store IMV scores
    imv_list = []

    # Loop through each fold
    for fold in range(num_folds):
        # Define the indices for this fold
        start_idx = fold * fold_size
        end_idx = (fold + 1) * fold_size

        # Extract the training and testing data for this fold
        test = titanic.iloc[start_idx:end_idx]
        train = pd.concat([titanic.iloc[:start_idx], titanic.iloc[end_idx:]])

        y_train = train['survived'].values
        y_test = test['survived'].values

        # Initialize and fit the logistic regression model for basic and enhanced features
        logreg = LogisticRegression(C=1e99, fit_intercept=False)
        logreg.fit(train[['constant']], y_train)
        pred_basic = logreg.predict_proba(test[['constant']])[:, 1]

        logreg.fit(train[['constant', 'pclass', 'sex']], y_train)
        pred_enhanced = logreg.predict_proba(test[['constant', 'pclass', 'sex']])[:, 1]

        # Calculate and append the IMV score for this fold
        imv_list.append(calculate_imv(pred_basic, pred_enhanced, y_test))

    # Print the minimum, maximum, and mean IMV scores
    print("IMV min: %s, max: %s, mean: %s" %
          (np.min(imv_list), np.max(imv_list), np.mean(imv_list)))
