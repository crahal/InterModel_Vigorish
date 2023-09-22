% Set constants
GITHUB_URL = "https://raw.githubusercontent.com/";
GITHUB_REPO = "crahal/InterModel_Vigorish/main";
DATA_FILE_PATH = "/data/titanic/titanic3.csv";
rng(22092023);

% Load and preprocess data
github_data_url = GITHUB_URL + GITHUB_REPO + DATA_FILE_PATH;
options = weboptions('ContentReader', @readtable);
titanic = webread(github_data_url, options);

% Preprocessing
titanic.constant = ones(height(titanic), 1);
titanic.sex = double(ismember(titanic.sex, 'female'));

% Shuffle the dataset
numRows = height(titanic);
perm = randperm(numRows);
titanic = titanic(perm, :);

enhanced = {'constant', 'pclass', 'sex'};
y = titanic.survived;

% Initialize an array to store IMV scores
imv_scores = zeros(1, 10);

% Calculate the size of each fold
fold_size = floor(length(y) / 10);

% Loop through each fold
for fold = 1:10
    % Define the indices for this fold
    start_idx = (fold - 1) * fold_size + 1;
    end_idx = round(fold * fold_size);
    % Extract the training and testing data for this fold
    test_indices = start_idx:end_idx;
    train_indices = setdiff(1:length(y), test_indices);

    train = titanic(train_indices, :);
    test = titanic(test_indices, :);

    y_train = y(train_indices);
    y_test = y(test_indices);

    % Logistic regressions and predictions
    X_basic = [ones(size(train, 1), 1)]; % Adding a constant term
    X_enhanced = [ones(size(train, 1), 1), train.pclass, train.sex];
    logreg_basic = glmfit(X_basic, train.survived, 'binomial', 'link', 'logit');
    logreg_enhanced = glmfit(X_enhanced, train.survived, 'binomial', 'link', 'logit');

    X_test_basic = [ones(size(test, 1), 1)]; % Adding a constant term
    X_test_enhanced = [ones(size(test, 1), 1), test.pclass, test.sex];
    pred_basic = glmval(logreg_basic, X_test_basic, 'logit');
    pred_enhanced = glmval(logreg_enhanced, X_test_enhanced, 'logit');

    % Calculate IMV score for this fold
    imv_score = calculate_imv(pred_basic, pred_enhanced, y_test);
    imv_scores(fold) = imv_score;
end

% Calculate and display the min, max, and mean IMV scores
fprintf('IMV min: %f, max: %f, mean: %f\n', min(imv_scores), max(imv_scores), mean(imv_scores));

function imv = calculate_imv(p_baseline, p_enhanced, x)
    % Calculate 'a0' and 'a1'
    a0 = exp(sum(log(p_baseline) .* x ...
        + log(1 - p_baseline) .* (1 - x)) / length(x));
    a1 = exp(sum(log(p_enhanced) .* x ...
        + log(1 - p_enhanced) .* (1 - x)) / length(x));

    % Function to be minimized
    minimize_me = @(p, a) abs(p * log(p) ...
                    + (1 - p) * log(1 - p) - log(a));

    % Calculate 'w' using optimization
    options = optimset('fmincon');
    options.TolFun = 0;
    options.TolCon = 1e-9;

    res0 = fmincon(@(p) minimize_me(p, a0), 0.5, ...
        [], [], [], [], 0.001, 0.999, [], options);
    res1 = fmincon(@(p) minimize_me(p, a1), 0.5, ...
        [], [], [], [], 0.001, 0.999, [], options);
    w0 = res0(1);
    w1 = res1(1);

    % Calculate the imv metric:
    imv = (w1 - w0) / w0;
end
