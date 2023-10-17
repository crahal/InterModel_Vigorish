# Author: github.com/ben-domingue

library(pROC)
library(MLmetrics)
library(here)
print("We're running: make_p0_v_p1.R")

getvals<-function(df) {
  ##r2
  r21<-1-sum((df$y2-df$p1)^2)/sum((df$y2-mean(df$y))^2)
  r22<-1-sum((df$y2-df$p2)^2)/sum((df$y2-mean(df$y))^2)
  r2.true<-1-sum((df$y2-df$p)^2)/sum((df$y2-mean(df$y))^2)
  au1<-pROC::auc(response=df$y2,predictor=df$p1)
  au2<-pROC::auc(response=df$y2,predictor=df$p2)
  au.true<-pROC::auc(response=df$y2,predictor=df$p)
  pred<-ifelse(df$p1>.5,1,0)
  if (length(unique(pred))==1) f11<-NA else f11<-F1_Score(y_pred=pred, y_true=df$y2)
  pred<-ifelse(df$p2>.5,1,0)
  if (length(unique(pred))==1) f12<-NA else f12<-F1_Score(y_pred=pred, y_true=df$y2)
  pred<-ifelse(df$p>.5,1,0)
  if (length(unique(pred))==1) f1.true<-NA else f1.true<-F1_Score(y_pred=pred, y_true=df$y2)
  imv<-function(y,p1,p2) {
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
  }
  ew1<-imv(df$y2,mean(df$y),df$p1)
  ew2<-imv(df$y2,mean(df$y),df$p2)
  ew12<-imv(df$y2,df$p2,df$p1)
  ew.true<-imv(df$y2,mean(df$y),df$p)
  ew.or1<-imv(df$y2,df$p1,df$p)
  ew.or2<-imv(df$y2,df$p2,df$p)
  c(R21=r21,R22=r22,R2.true=r2.true,
    AUC1=au1,AUC2=au2,AUC.true=au.true,
    F11=f11,F12=f12,F1.true=f1.true,
    IMV1=ew1,IMV2=ew2,IMV12=ew12,IMV.true=ew.true,
    IMV.or1=ew.or1,
    IMV.or2=ew.or2)
}

simfun<-function(N=1000,delta,MD) {
  p<-rbeta(N,a,b)
  p<-MD+(1-2*MD)*p
  #p<-runif(N,2*MD,1-2*MD)
  y<-rbinom(N,1,p)
  y2<-y #rbinom(N,1,p)
  ##
  delta1<-sample(c(-1,1),N,replace=TRUE) #runif(N,-1*delta,delta)
  delta2<-sample(c(-1,1),N,replace=TRUE) #runif(N,-1*delta,delta) runif(N,-1*delta,delta)
  ##
  p1<-p+delta1*delta
  p2<-p+delta2*delta
  data.frame(p=p,p1=p1,p2=p2,y=y,y2=y2)
}

N<-1000
MD<-.2
a<-1
dfL<-list()
for (b in c(1)) {
  L<-list()
  for (i in 1:2000) {
    delta<-runif(1,min=0,max=MD)
    z<-simfun(delta=delta,N=N,MD=MD)
    L[[i]]<-c(mean=MD+(1-2*MD)*(a/(a+b)),delta=delta,getvals(z)) #    p<-2*MD+(1-4*MD)*p
  }
  dfL[[as.character(b)]]<-data.frame(do.call("rbind",L))
}

pdf("C:\\Dropbox\\InterModel_Vigorish\\chicco_oracle.pdf",width=6,height=4)
#par(mfcol=c(4,length(dfL)),mgp=c(2,1,0),mar=c(3,2,1,1),oma=rep(.1,4))
par(mfcol=c(2,2),mgp=c(2,1,0),mar=c(3,2,1,1),oma=rep(.1,4))
pf<-function(x,y,col,txt,...) {
  tmp<-cbind(x,y)
  tmp<-tmp[order(tmp[,1]),]
  x<-tmp[,1]
  y<-tmp[,2]
  m<-loess(y~x)
  pm<-predict(m,se=TRUE)
  lines(m$x,pm$fit,lwd=2,col=col,...)
  text(m$x[1],fitted(m)[1],pos=2,txt,col=col,cex=.9)
  cc<-col2rgb(col)
  c1<-rgb(cc[1],cc[2],cc[3],max=255,alpha=45)
  polygon(c(m$x,rev(m$x)),c(pm$fit+1.96*pm$se.fit,rev(pm$fit-1.96*pm$se.fit)),col=c1,border=NA)
  output1 <- data.frame("fitted"=pm$fit, "SE"=pm$se)
  output <- data.frame(m$x)
  write.csv(output, file = here('data', 'sims', 'p0_v_p1', paste0("omega", "_m_", counter,".csv")))
  write.csv(output1, file = here('data', 'sims', 'p0_v_p1', paste0("omega", "_pm_", counter,".csv")))
}
counter = 0
for (i in 1:length(dfL)) {
  df<-dfL[[i]]
  for (nm in c("R2","AUC","F1","IMV")) {
    f<-function(z,nm) {
      index<-grep(nm,names(z))
      unlist(z[,index])
    }
    yl<-lapply(dfL,f,nm=nm)
    yl<-range(lapply(yl,range))
    ##
    zz<-c(df[[paste(nm,"1",sep="")]],df[[paste(nm,".or",sep='')]])
    #yl<-range(zz,na.rm=TRUE)
    yl<-c(-.05,1)
    plot(NULL,xlim=range(df$delta),ylim=yl,xlab='',ylab='')
    mtext(side=1,expression(delta),line=2)
    #if (nm=="R2") legend("topleft",bty='n',legend=round(df$mean[1],3))
    pf(df$delta,df[[paste(nm,"1",sep="")]],col='red','')
    counter = counter + 1
    pf(df$delta,df[[paste(nm,".true",sep='')]],col='black','',lty=1)
    counter = counter + 1
    legend("topleft",bty='n',nm)
    abline(h=0,col='gray')    
    ## if (nm=="IMV") {
    ##     pf(df$delta,df$IMV.or1,col='blue','',lty=2)
    ##     pf(df$delta,df$IMV.or2,col='red','',lty=2)
    ## }
    if (nm=="R2") legend("topright",bty='n',lty=c(1,1,1),col=c("red","black"),c("p1","p"))
    #if (nm=="IMV") legend("topright",bty='n',lty=c(2,2),col=c("blue","red"),c("Oracle, p1","Oracle, p2"))
  }
}
dev.off()
#write.csv(df, file = "C:\\Dropbox\\InterModel_Vigorish\\chicco_omega.csv")
