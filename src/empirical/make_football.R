library("here")
imv<-function(y,p1,p2) {
  ##
  ll<-function(x,p) {
    z<-log(p)*x+log(1-p)*(1-x)
    z<-sum(z)/length(x)
    exp(z)
  }    
  loglik1<-ll(y,p1)
  loglik2<-ll(y,p2)
  getcoins<-function(a) {
    f<-function(p,a) abs(p*log(p)+(1-p)*log(1-p)-log(a))
    nlminb(.5,f,lower=0.001,upper=.999,a=a)$par
  }
  c1<-getcoins(loglik1)
  c2<-getcoins(loglik2)
  ew<-function(p1,p0) (p1-p0)/p0
  imv<-ew(c2,c1)
  imv
}

x<-read.csv(here("data", "football", "football_prediction_data.csv"))
x$year<-substr(x$season,6,9)

outer<-function(x) {
  L<-split(x,x$year)
  f<-function(x) {
    p0<-mean(x$outcome)
    imv(x$outcome,rep(p0,nrow(x)),x$prob.outcome...1.)
  }
  om<-sapply(L,f)
}

om_all<-outer(x)
write.csv(om_all, here("data", "football", "football_all.csv"))
om_England<-outer(x[x$country=="England",])
write.csv(om_England, here("data", "football", "football_England.csv"))
om_Netherlands<-outer(x[x$country=="Netherlands",])
write.csv(om_Netherlands, here("data", "football", "football_Netherlands.csv"))
