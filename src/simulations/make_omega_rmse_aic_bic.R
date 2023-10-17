
ff<-function(arg) {
    for (i in 1:length(arg)) assign(names(arg)[i],arg[[i]])
    rmsfun<-function(z) sqrt(mean(z^2))
    r2<-function(y,p) 1-sum((y-p)^2)/sum((y-mean(y))^2)
    auc<-function(y,p) {
        library(pROC)
        au<-pROC::auc(response=y,predictor=p)
        au
    }
    f1<-function(y,p) {
        library(MLmetrics)
        pred<-ifelse(p>.5,1,0)
        if (length(unique(pred))==1) f1<-NA else f1<-F1_Score(y_pred=pred, y_true=y)
    }
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
    x<-rnorm(N)
    p<-1/(1+exp(-1*(b0+b*x)))
    y<-rbinom(length(x),1,p)
    y2<-rbinom(length(x),1,p)
    df<-data.frame(x=x,p=p,y=y,y2=y2)
############################################
    m1<-glm(y~x,df,family="binomial")
    m2<-glm(y~x+I(x^2),df,family="binomial")
    df$fit<-predict(m1,type="response")
    df$fit2<-predict(m2,type="response")
    ##
    om0<-imv(df$y2,df$fit2,df$fit)
    aic0<-m2$aic-m1$aic
    library(flexmix)
    bic0<-BIC(m2)-BIC(m1)
    audelta0<-auc(df$y2,df$fit)-auc(df$y2,df$fit2)
    r2delta0<-r2(df$y2,df$fit)-r2(df$y2,df$fit2)
    f1delta0<-f1(df$y2,df$fit)-f1(df$y2,df$fit2)
    rms0<-rmsfun(df$fit2-df$fit)
############################################
    ##x plus noise
    df$xnoise<-df$x+rnorm(N,mean=0,sd=S)
    ##
    m3<-glm(y~xnoise,df,family="binomial")
    df$fit3<-predict(m3,type="response")
    ##
    om<-imv(df$y2,df$fit3,df$fit)
    aic<-m3$aic-m1$aic
    bic<-BIC(m3)-BIC(m1)
    audelta<-auc(df$y2,df$fit)-auc(df$y2,df$fit3)
    r2delta<-r2(df$y2,df$fit)-r2(df$y2,df$fit3)
    f1delta<-f1(df$y2,df$fit)-f1(df$y2,df$fit3)
    rms<-rmsfun(df$fit3-df$fit)
############################################
    ##cloglog
    m4<-glm(y~x,df,family=binomial(link='cloglog'))
    df$fit4<-predict(m4,type="response")
    ##
    omp<-imv(df$y2,df$fit4,df$fit)
    aicp<-m4$aic-m1$aic
    bicp<-BIC(m4)-BIC(m1)
    audeltap<-auc(df$y2,df$fit4)-auc(df$y2,df$fit4)
    r2deltap<-r2(df$y2,df$fit)-r2(df$y2,df$fit4)
    f1deltap<-f1(df$y2,df$fit)-f1(df$y2,df$fit4)
    rmsp<-rmsfun(df$fit4-df$fit)
#############################################
    c(N=N,b=b,S=S,b0=b0,
      om0=om0,aic0=aic0,bic0=bic0,auc0=audelta0,r20=r2delta0,f10=f1delta0,rms0=rms0,#overfit
      om=om,aic=aic,bic=bic,auc=audelta,r2=r2delta,f1=f1delta,rms=rms,#noise
      omp=omp,aicp=aicp,bicp=bicp,aucp=audeltap,r2p=r2deltap,f1p=f1deltap,rmsp=rmsp #wrong link
      )
}


b0<-0 #c(0,1)
b<-runif(5000,min=0,max=1)#0.5 #b<-c(.01,.1,.5)
N<-c(log10(1000))
N<-round(10^(N))
S<-0.3
z<-expand.grid(b=b,N=N,S=S,b0=b0)
L<-list()
for (i in 1:nrow(z)) L[[i]]<-list(N=z$N[i],b=z$b[i],S=z$S[i],b0=z$b0[i])
L1<-L
##
b0<-0 #c(0,1)
b<-.5
N<-runif(5000,log10(50),log10(25000))
N<-round(10^(N))
S<-0.3
z<-expand.grid(b=b,N=N,S=S,b0=b0)
L<-list()
for (i in 1:nrow(z)) L[[i]]<-list(N=z$N[i],b=z$b[i],S=z$S[i],b0=z$b0[i])
L2<-L
##
library(parallel)
#L1<-mclapply(L1,ff,mc.cores=10)
L2<-mclapply(L2,ff)
#df1<-data.frame(do.call("rbind",L1))
df2<-data.frame(do.call("rbind",L2))



pf<-function(x,y,col,txt,tail=FALSE,ci=TRUE,...) {
    m<-loess(y~x)
    pm<-predict(m,se=TRUE)
    lines(m$x,pm$fit,col=col,...)
    if (tail) {
        nn<-length(m$x)
        text(m$x[nn],fitted(m)[nn],pos=4,txt,col=col,cex=.9)
    }
    text(m$x[1],fitted(m)[1],pos=2,txt,col=col,cex=.9)
    cc<-col2rgb(col)
    c1<-rgb(cc[1],cc[2],cc[3],max=255,alpha=45)
    if (ci) polygon(c(m$x,rev(m$x)),c(pm$fit+1.96*pm$se.fit,rev(pm$fit-1.96*pm$se.fit)),col=c1,border=NA)

    return(list(m$x, pm$fit, pm$se*1.96))
}

######################################
#pdf("~/Dropbox/Apps/Overleaf/BinaryPrediction/ben_figures/IC.pdf",width=7.5,height=2.5)
#                                        #cols<-colorRampPalette(c("blue", "red"))(3)

















cols<-c("black","blue","red")
metrics<-c("rms"="RMSE","om"="IMV","aic"="AIC","bic"="BIC")
par(mfrow=c(1,4),mgp=c(2,1,0),mar=c(3,3,1,.1),oma=rep(.1,4))

for (nm in names(metrics)) {
    z<-c(df2[[nm]],df2[[paste0(nm,'0')]],df2[[paste0(nm,'p')]])
    #ylim<-quantile(z,c(.025,.975),na.rm=TRUE)
    if (nm!='om') ylim<-c(0,10) else ylim<-c(0,.035)
    if (nm=="rms") ylim<-c(0,0.075)
    x<-df2
    x$ln<-log10(x$N)
    plot(NULL,xlim=c(0.4,1.3*log10(max(x$N))),ylim=ylim,xaxt="n",xlab="N",ylab=metrics[nm])
    #abline(v=unique(log10(df1$N)),col='gray',lty=2)
    xb<-unique(x$b)
    if (nm=='rms') legend("topright",bty='n',legend=bquote(beta~"="~.(xb)))
    abline(h=0,col='gray')
    ran<-range(x$N)
    xl<-c(50,500,25000)
    axis(side=1,at=log10(xl),labels=xl)
    y<-x[order(x$N),]
    ##
    out <- pf(y$ln,y[[paste0(nm,'0')]],col=cols[1],expression(x^2),lwd=2,tail=TRUE)
    write.csv(out[[1]], here('data', 'sims', 'omega_rmse_aic_bic', paste0(nm,'_x_x2', '.csv')))
    write.csv(out[[2]], here('data', 'sims', 'omega_rmse_aic_bic', paste0(nm,'_fit_x2', '.csv')))
    write.csv(out[[3]], here('data', 'sims', 'omega_rmse_aic_bic', paste0(nm,'_se_x2', '.csv')))
    out <- pf(y$ln,y[[nm]],col=cols[2],expression(x+epsilon),lwd=2,tail=TRUE)
    write.csv(out[[1]], here('data', 'sims', 'omega_rmse_aic_bic', paste0(nm,'_x_xepsilon','.csv')))
    write.csv(out[[2]], here('data', 'sims', 'omega_rmse_aic_bic', paste0(nm,'_fit_xepsilon','.csv')))
    write.csv(out[[3]], here('data', 'sims', 'omega_rmse_aic_bic', paste0(nm,'_se_xepsilon','.csv')))
    out <- pf(y$ln,y[[paste0(nm,'p')]],col=cols[3],'cloglog',lwd=2,tail=TRUE)
    write.csv(out[[1]], here('data', 'sims', 'omega_rmse_aic_bic', paste0(nm,'_x_cloglog','.csv')))
    write.csv(out[[2]], here('data', 'sims', 'omega_rmse_aic_bic', paste0(nm,'_fit_cloglog','.csv')))
    write.csv(out[[3]], here('data', 'sims', 'omega_rmse_aic_bic', paste0(nm,'_se_cloglog','.csv')))
}



dev.off()
