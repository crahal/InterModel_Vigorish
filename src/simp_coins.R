set.seed(8675309)
##getting the outcomes.
##we'll combine a set of tosses from even coin with tosses from heavily weighted coin
x1<-rbinom(20,1,.5)
x2<-rbinom(20,1,.95)
x<-c(x1,x2)
##a function to compute the log-likelihood
ll<-function(x,p) {
  z<-log(p)*x+log(1-p)*(1-x)
  z<-sum(z)/length(z)
  exp(z)
}
##baseline prediction
p=.55
a0<-ll(x=x,p=p)
a0
f<-function(p,a) abs(p*log(p)+(1-p)*log(1-p)-log(a))
p0<-nlminb(.5,f,lower=0.001,upper=.999,a=a0)$par
p0

##enhanced prediction
p<-c(rep(.5,20),rep(.9,20))
a1<-ll(x=x,p=p)
p1<-nlminb(.5,f,lower=0.001,upper=.999,a=a1)$par
##the single-blind bet
ew<-(p1-p0)/p0
