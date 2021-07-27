simdata<-function(N,b0,b1,b2) {
  gen.data<-function(x,z,b0=0,b1=.5,b2=1) {
    k<-exp(b0+b1*x+b2*z)
    #k<-exp(.3+.5*x+.2*z)
    p<-k/(1+k)
    y<-rbinom(length(x),1,p)
    y
  }
  ##
  x<-rnorm(N)
  z<-rnorm(N)
  train<-data.frame(x=x,y=gen.data(x,b0=b0,b1=b1,b2=b2,z=z),z=z)
  x<-rnorm(N)
  z<-rnorm(N)
  test<-data.frame(x=x,y=gen.data(x,b0=b0,b1=b1,b2=b2,z=z),z=z)
  list(train=train,test=test)
}


simfun<-function(df.tr,df.test,fm1,fm2) {
  ll<-function(x,p) {
    z<-log(p)*x+log(1-p)*(1-x)
    z<-sum(z)/length(z)
    exp(z)
  }
  f<-function(p,a) abs(p*log(p)+(1-p)*log(1-p)-log(a))
  ##
  m0<-glm(fm1,df.tr,family="binomial") #baseline
  m1<-glm(fm2,df.tr,family="binomial")
  prev<-mean(df.tr$y)
  #get predictions in new data
  y<-df.test$y
  p0<-predict(m0,type="response",data.frame(x=df.test$x,z=df.test$z))
  p1<-predict(m1,type="response",data.frame(x=df.test$x,z=df.test$z))
  a0<-ll(x=y,p=p0)
  a1<-ll(x=y,p=p1)
  coin0<-nlminb(.5,f,lower=0.001,upper=.999,a=a0)$par
  coin1<-nlminb(.5,f,lower=0.001,upper=.999,a=a1)$par
  ##the single-blind bet
  ew<-(coin1-coin0)/coin0
  ##r2
  r2<-1-sum((y-p1)^2)/sum((y-mean(df.tr$y))^2)
  #r2.0<-1-sum((y-p0)^2)/sum((y-mean(df.tr$y))^2)
  #r2.del<-(r2-r2.0)/r2.0
  ##auc
  suppressPackageStartupMessages(library(pROC, quiet=TRUE))
  #ro<-roc(y,p1)
  au<-pROC::auc(response=y,predictor=p1, quiet=TRUE)
  #ro0<-roc(y,p0)
  #au.del<-(au-auc(ro0))/auc(ro0)
  ##f1
  suppressPackageStartupMessages(library(MLmetrics, quiet=TRUE))
  pred<-ifelse(p1>.5,1,0)
  if (length(unique(pred))==1) f1<-NA else f1<-F1_Score(y_pred=pred, y_true=y)
  ##
  tr<-list(prev=prev,ew=ew,
           #ew2=ew2,
           r2=r2,
           #r2.del=r2.del,
           auc=au,
           #auc.del=au.del,
           f1=f1
  )
  unlist(tr)
}


pf<-function(b,mat,ylim=c(0,1),...) {
  labels<-list(ew="IMV",
               ew0="IMV",
               r2=expression(R^2),
               f1=expression(F[1]),
               auc="AUC")
  lp<-function(x,y) {
    m<-loess(y~x)
    tmp<-cbind(m$x,fitted(m))
    tmp[order(tmp[,1]),]
  }
  plot(NULL,xlim=c(min(0,min(b)),1.27*max(b)),ylim=ylim,...) #,mat$ew,pch=19,cex=0,col=c1,ylim=c(0,1),xlab=expression(beta[0]),ylab=paste("Metric (alt=",nm,")",sep=""))
  for (nm in names(mat)) {
    tmp<-lp(b,mat[[nm]])
    lines(tmp,lwd=2,col=ifelse(nm %in% c('ew',"ew0"),'red','blue'))
    nn<-nrow(tmp)
    nm2<-gsub(".del","",nm,fixed=TRUE)
    nm2<-gsub(".diff","",nm2,fixed=TRUE)
    iii<-match(nm2,names(labels))
    text(tmp[nn,1],tmp[nn,2],labels[[iii]],col=ifelse(nm2 %in% c('ew',"ew0"),'red','blue'),pos=4)
  }
  NULL
}



nsamp<-1000
set.seed(10101010)
b0La<-runif(nsamp,min=0,max=1)
b1La<-runif(nsamp,min=0,max=1)
b2La<-rep(.3,length(b1La)) #runif(nsamp,min=1,max=5)
dat1<-list()
for (i in 1:length(b0La)) simdata(N=2000,b0=b0La[i],b1=b1La[i],b2=b2La[i])->dat1[[i]]
##
results<-list()
for (i in 1:length(dat1)) {
  r1<-simfun(df.tr=dat1[[i]]$train,df.test=dat1[[i]]$test,fm1="y~1",fm2="y~x")
  results[[i]]<-c(b0=b0La[i],b1=b1La[i],b2=b2La[i],r1)
}
mat.noz<-data.frame(do.call("rbind",results))


gendata<-function(b0Lb,b1Lb,b2Lb) {
  nsamp<-length(b0Lb)
  dat2<-list()
  for (i in 1:length(b0Lb)) simdata(N=2000,b0=b0Lb[i],b1=b1Lb[i],b2=b2Lb[i])->dat2[[i]]
  ##
  base0<-base<-results<-list()
  for (i in 1:length(dat2)) {
    r2<-simfun(df.tr=dat2[[i]]$train,df.test=dat2[[i]]$test,fm1="y~x",fm2="y~x+z")
    results[[i]]<-c(b0=b0Lb[i],b1=b1Lb[i],b2=b2Lb[i],r2)
    r1<-simfun(df.tr=dat2[[i]]$train,df.test=dat2[[i]]$test,fm1="y~1",fm2="y~x")
    r20<-simfun(df.tr=dat2[[i]]$train,df.test=dat2[[i]]$test,fm1="y~1",fm2="y~x+z")
    base[[i]]<-r1
    base0[[i]]<-r20
  }
  base<-data.frame(do.call("rbind",base))
  base0<-data.frame(do.call("rbind",base0))
  mat.wz<-data.frame(do.call("rbind",results))
  mat.wz$r2.del<-(mat.wz$r2-base$r2)/base$r2
  mat.wz$auc.del<-(mat.wz$auc-base$auc)/base$auc
  mat.wz$f1.del<-(mat.wz$f1-base$f1)/base$f1
  mat.wz$r2.diff<-(mat.wz$r2-base$r2)
  mat.wz$auc.diff<-(mat.wz$auc-base$auc)
  mat.wz$f1.diff<-(mat.wz$f1-base$f1)
  mat.wz$ew0<-base0$ew
  mat.wz
}
nsamp<-1000
##
set.seed(10101010)
b0Lb<-rep(0,nsamp)
b1Lb<-rep(.5,nsamp)
b2Lb<-runif(nsamp,min=0,max=1)
mat.wz1<-gendata(b0Lb,b1Lb,b2Lb)
##
set.seed(10101010)
b0Lb<-rep(0.5,nsamp)
b1Lb<-rep(.5,nsamp)
b2Lb<-runif(nsamp,min=0,max=1)
mat.wz2<-gendata(b0Lb,b1Lb,b2Lb)
##
##
set.seed(10101010)
b0Lb<-rep(0.5,nsamp)
b1Lb<-rep(.1,nsamp)
b2Lb<-runif(nsamp,min=0,max=1)
mat.wz3<-gendata(b0Lb,b1Lb,b2Lb)

library(here)
to = here('data', 'sims', 'mat_noz.csv')
write.csv(mat.noz, file=to)
to = here('data', 'sims', 'mat_wz1.csv')
write.csv(mat.wz1, file=to)
to = here('data', 'sims', 'mat_wz2.csv')
write.csv(mat.wz2, file=to)
to = here('data', 'sims', 'mat_wz3.csv')
write.csv(mat.wz3, file=to)
