bigfun<-function(df,fm1,fm2,nfold=10) { #CV prediction function within dataframe df for two logistic regerssion models (based on formulas fm1 & fm2)
    ##
    outcome<-all.vars(formula(fm1))[1]
    vars<-unique(c(all.vars(formula(fm1)),all.vars(formula(fm2))))
    tmp<-df[,vars]
    df<-df[rowSums(is.na(tmp))==0,]
    ##
    predfun<-function(x,outcome) {
        #in/out
        oos<-x[x$oos,]
        x<-x[!x$oos,]
        ##Models
        m<-glm(fm1,x,family="binomial")
        oos$m1<-predict(m,oos,type="response")
        m<-glm(fm2,x,family="binomial")
        oos$m2<-predict(m,oos,type="response")
        ##ll
        ll<-function(x,p,outcome) {
            z<-log(x[[p]])*x[[outcome]]+log(1-x[[p]])*(1-x[[outcome]])
            z<-sum(z)/length(z)
            exp(z)
        }
        ##r2, https://www.pnas.org/content/117/15/8398
        r2<-1-sum((oos[[outcome]]-oos$m2)^2)/sum((oos[[outcome]]-mean(x[[outcome]],na.rm=TRUE))^2)
        ##
        c(ll(oos,'m1',outcome=outcome),ll(oos,'m2',outcome=outcome),r2)
    }
    ##
    out<-list()
    ids<-unique(df$hhidpn)
    ids<-data.frame(hhidpn=ids,gr=sample(1:nfold,length(ids),replace=TRUE))
    df<-merge(df,ids)
    for (ii in 1:nfold) {
        df$oos <- df$gr==ii
        out[[ii]]<-predfun(df,outcome=outcome)
    }
    mat<-do.call("rbind",out)
    nn<-ncol(mat)
    x<-colMeans(mat[,-nn]) #no r2
    ##
    prev<-mean(df[[outcome]],na.rm=TRUE)
    getp<-function(a) {
        f<-function(p,a) abs(p*log(p)+(1-p)*log(1-p)-log(a))
        nlminb(.5,f,lower=0.001,upper=.999,a=a)$par
    }
    gp<-Vectorize(getp)
    p<-numeric()
    for (i in 1:length(x)) p[i]<-gp(x[i])
    ##
    bet<-function(tp,ap) (tp-ap)/ap
    ew<-bet(p[2],p[1])
    ##
    c(prev,p,ew,mean(mat[,nn]))
}


getp<-function(a) { #see eqn 7. this identifies the isomorphic coin
    f<-function(p,a) abs(p*log(p)+(1-p)*log(1-p)-log(a))
    nlminb(.5,f,lower=0.001,upper=.999,a=a)$par
}

proc<-function(x) {
    #
    x$prevalence->prev
    NULL->x$prevalence
    gp<-Vectorize(getp)
    p<-list()
    for (i in 1:ncol(x)) p[[colnames(x)[i] ]]<-gp(x[,i])
    ##
    bet<-function(tp,ap) (tp-ap)/ap
    w<-list()
    allmod<-c("van","std","spl")
    test<-allmod %in% names(p)
    for (nm in allmod[test]) w[[nm]]<-bet(p[[nm]],p$base)
    data.frame(prev,x,p,w)
}
