# Author: github.com/ben-domingue

#In this case, we associated to the positive data instances the values Beta(a, b) distribution and associated to the negative data instances the values
#Beta(c, d) distribution with a, b, c, d ranging from 1 to 15.
#Digital Object Identifier 10.1109/ACCESS.2021.3084050

print('Working on: make_plot_metrics_v_diff_v_prev')
getvals<-function(x,y) {
  ##r2
  r2<-1-sum((y-x)^2)/sum((y-mean(y))^2)
  ##auc
  library(pROC)
  au<-pROC::auc(response=y,predictor=x)
  ##f1
  library(MLmetrics)
  pred<-ifelse(x>.5,1,0)
  if (length(unique(pred))==1) f1<-NA else f1<-F1_Score(y_pred=pred, y_true=y)
  ##imv
  ll<-function(x,p) {
    z<-log(p)*x+log(1-p)*(1-x)
    z<-sum(z)/length(z)
    exp(z)
  }    
  f<-function(p,a) abs(p*log(p)+(1-p)*log(1-p)-log(a))
  ##
  a0<-ll(x=y,p=mean(y))
  a1<-ll(x=y,p=x)
  coin0<-nlminb(.5,f,lower=0.001,upper=.999,a=a0)$par
  coin1<-nlminb(.5,f,lower=0.001,upper=.999,a=a1)$par
  ##the single-blind bet
  ew<-(coin1-coin0)/coin0
  c(R2=r2,AUC=au,F1=f1,IMV=ew)
}
simfun<-function(N=5000,a=9,b=15,c=15,d=8) {
  p0<-rbeta(N,a,b)
  p1<-rbeta(N,c,d)
  x<-c(p0,p1)
  y<-rbinom(length(x),1,x)
  vals<-getvals(x,y)
  list(a=a,b=b,c=c,d=d,x=x,y=y,metric=vals)
}

L<-list()
for (i in 1:1000) {
  vals<-runif(4,min=1,max=15)
  ma<-vals[1]/(vals[1]+vals[2])
  mb<-vals[3]/(vals[3]+vals[4])
  if (ma>mb) vals<-c(vals[3],vals[4],vals[1],vals[2])
  L[[i]]<-simfun(a=vals[1],b=vals[2],c=vals[3],d=vals[4])
}

f<-function(z) {
  for (i in 1:length(z)) assign(names(z)[i],z[[i]])
  p<-(c/(c+d))-(a/(a+b))
  c(Difference=p,Prevalence=abs(.5-mean(y)),metric)
}
l<-lapply(L,f)
x<-data.frame(do.call("rbind",l))
to = here('data', 'sims', 'metrics_v_diff_v_prev', "metrics_v_diff_v_prev.csv")
write.csv(x, file=to)