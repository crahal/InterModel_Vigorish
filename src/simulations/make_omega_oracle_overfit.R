# Author: github.com/ben-domingue

library(parallel)
library(here)

ff<-function(arg) {
  for (i in 1:length(arg)) assign(names(arg)[i],arg[[i]])
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
    imv
  }
  x<-rnorm(N)
  p<-1/(1+exp(-b*x))
  y<-rbinom(length(x),1,p)
  y2<-rbinom(length(x),1,p)
  df<-data.frame(x=x,p=p,y=y,y2=y2)
  m<-glm(y~x,df,family="binomial")
  df$fit<-predict(m,type="response")
  ##
  om<-imv(df$y2,rep(mean(df$y),nrow(df)),df$fit)
  om.oracle<-imv(df$y2,df$fit,df$p)
  om.overfit<-imv(df$y,df$fit,df$p)
  ##
  c(N=N,b=b,om=om,om.oracle=om.oracle,om.overfit=om.overfit)
}
b<-c(.01,.1,.5)
N<-runif(5000,log10(50),log10(10000))
N<-round(10^(N))
z<-expand.grid(b=b,N=N)
L<-list()
for (i in 1:nrow(z)) L[[i]]<-list(N=z$N[i],b=z$b[i])
L<-mclapply(L,ff, mc.cores=1)
x<-data.frame(do.call("rbind",L))
x$ln<-log10(x$N)
xx<-split(x,x$b)
pf<-function(x,y,col,txt,name) {
  m<-loess(y~x)
  pm<-predict(m,se=TRUE)
  my.output <- data.frame("mx"=m$x, "predict"=pm$fit, "se"=pm$se.fit)
  library(here)
  to = here('..', '..', 'data', 'sims', paste0(txt, "_", name,".csv"))
  write.csv(my.output, file=to)
}

for (i in 1:length(xx)) {
  plot(NULL,xlim=c(1,log10(10000)),ylim=c(-.14,.23),xaxt="n",xlab="N",ylab="IMV")
  legend("bottomright",bty="n",paste("b=",names(xx)[i],sep=""))
  abline(h=0,col='gray')
  axis(side=1,at=log10(c(50,100,500,1000,5000,10000)),c(50,100,500,1000,5000,10000))
  y<-xx[[i]]
  y<-y[order(y$ln),]
  pf(y$ln,y$om,col=cols[1],"omega_0", names(xx)[i])
  pf(y$ln,y$om.overfit,col=cols[2],"overfit", names(xx)[i])
  pf(y$ln,y$om.oracle,col=cols[3],"oracle", names(xx)[i])
}