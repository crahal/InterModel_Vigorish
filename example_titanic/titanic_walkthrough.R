  library(readr)
  set.seed(22092023)
  
  ll<-function(x,p) {
    z<-log(p)*x+log(1-p)*(1-x)
    z<-sum(z)/length(z)
    exp(z)}
  
  get_w<-function(a) {
    f<-function(p,a) abs(p*log(p)+(1-p)*log(1-p)-log(a))
    nlminb(.5,f,lower=0.001,upper=.999,a=a)$par}
  
  minimize_me <- function(p, a) {
    return(abs((p * log(p)) + ((1 - p) * log(1 - p)) - log(a)))}
  
  calculate_imv <- function(y_basic, y_enhanced, y) {
    ll_basic <- ll(y, y_basic)
    ll_enhanced <- ll(y, y_enhanced)
    w0 <- get_w(ll_basic)
    w1 <- get_w(ll_enhanced)
    return((w1 - w0) / w0)}
  
  # Load and preprocess data
  titanic <- read.csv('../data/titanic/titanic3.csv')
  titanic$constant <- 1
  titanic$sex <- ifelse(titanic$sex == "female", 1, 0)
  titanic = titanic[sample(1:nrow(titanic)), ]
  prev = mean(titanic$survived)
  imv_list <- c()
  k_folds <- 10
  
  for (i in 1:k_folds) {
    # Calculate fold boundaries
    fold_size <- floor(nrow(titanic) / k_folds)
    fold_start <- (i - 1) * fold_size + 1
    fold_end <- round(i * fold_size)
  
    # Create train and test sets based on fold boundaries
    train <- titanic[-(fold_start:fold_end), ]
    test <- titanic[fold_start:fold_end, ]
    
    y_train <- train$survived
    y_test <- test$survived
    
    # Logistic regressions and predictions
    logreg_basic <- glm(survived ~ constant - 1,
                        data = train, family = binomial(link = "logit"))
    logreg_enhanced <- glm(survived ~ constant + pclass + sex - 1,
                           data = train, family = binomial(link = "logit"))
    
    pred_basic <- predict(logreg_basic,
                          newdata = data.frame(constant = test$constant),
                          type = "response")
    
    pred_enh <- predict(logreg_enhanced, newdata = test,
                        type = "response")
    
    imv_list <- c(imv_list, calculate_imv(pred_basic, pred_enh, y_test))
  }
  
  cat("IMV min:", min(imv_list), ", max:", max(imv_list),
      ", mean:", mean(imv_list), ", stdev:", sd(imv_list), ", prev: ", prev)