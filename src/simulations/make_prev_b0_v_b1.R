# Author: github.com/ben-domingue

##hold IMV constant
f<-function(b0,omega=0.01) {
  getp<-function(a) { #see eqn 7. this identies the isomorphic coin
    f<-function(p,a) abs(p*log(p)+(1-p)*log(1-p)-log(a))
    nlminb(.5,f,lower=0.001,upper=.999,a=a)$par
  }
  a<-1/(1+exp(-b0))
  w0<-getp(a)
  w1<-omega*w0+w0
  ##
  getp.inv<-function(p) { #see eqn 7. this identies the isomorphic coin
    f<-function(a,p) abs(p*log(p)+(1-p)*log(1-p)-log(a))
    nlminb(.5,f,lower=0.5,upper=.999,p=p)$par
  }
  a1<-getp.inv(w1)
  x<-rnorm(100000)
  ##
  llpart<-function(b1,a1,x) {
    p<-1/(1+exp(-1*(b0+b1*x)))
    l<-p*log(p)+(1-p)*log(1-p)
    abs(log(a1)-mean(l))
  }
  ## llp<-list()
  ## for (b1 in seq(0,1,length.out=25)) llp[[as.character(b1)]]<-llpart(b1,a1=a1,x=x)
  ## plot(seq(0,1,length.out=25),unlist(llp))
  b1<-optim(0,llpart,lower=0,upper=10,a1=a1,x=x,method="Brent")$par
  ##
  p<-1/(1+exp(-1*(b0+b1*x)))
  y<-rbinom(length(x),1,p)
  #r2<-cor(y,x)^2
  r2<-1-sum((y-p)^2)/sum((y-1/(1+exp(-b0)))^2)
  ##
  c(omega=omega,prev=a,b0=b0,b1=b1,r2=r2)
}
L<-list()
for (b0 in seq(0,.5,length.out=100)) L[[as.character(b0)]]<-f(b0,omega=0.01)
df1<-data.frame(do.call("rbind",L))
L<-list()
for (b0 in seq(0,.5,length.out=100)) L[[as.character(b0)]]<-f(b0,omega=.1)
df2<-data.frame(do.call("rbind",L))

getcol<-function(x,ran) {
  col<-colorRampPalette(c("blue", "red"))(500)
  xv<-seq(ran[1],ran[2],length.out=length(col))
  df<-data.frame(xv=xv,col=col)
  m<-outer(x,df$xv,function(x,y) abs(x-y))
  ii<-apply(m,1,which.min)
  df$col[ii]
}


##2=0.1, 1=0.01
yl<-max(c(df1$r2,df2$r2))
cols<-c('0.01'="black",'0.1'="red")
pdf("omega_r2.pdf",width=7,height=3)
par(mfrow=c(1,2),mar=c(3.3,3.3,1,1),mgp=c(2,1,0),lwd=2,oma=rep(.2,4))
plot(df1$b0,df1$b1,col=cols[1],ylim=c(0,3.6),xlim=c(-.37,.87),xaxt='n',type='l',lwd=4,lty=2,xlab=expression(beta[0]),ylab=expression(beta[1]))
axis(side=1,at=seq(0,.5,length.out=3))
n<-nrow(df1)
r2<-round(df1$r2[1],2)
txt<-bquote(R^2~"="~.(r2))
text(df1$b0[1],df1$b1[1],txt,pos=4,col=cols[1])
r2<-round(df1$r2[n],2)
txt<-bquote(R^2~"="~.(r2))
text(df1$b0[n],df1$b1[n],txt,pos=4,col=cols[1])
nn<-round(n/2)
text(df1$b0[nn],df1$b1[nn],pos=4.5,paste0("IMV=",unique(df1$omega)),col=cols[1])
#



lines(df2$b0,df2$b1,col=cols[2])
n<-nrow(df2)
r2<-round(df2$r2[1],2)
txt<-bquote(R^2~"="~.(r2))
text(df2$b0[1],df2$b1[1],txt,pos=2,col=cols[2])
r2<-round(df2$r2[n],2)
txt<-bquote(R^2~"="~.(r2))
text(df2$b0[n],df2$b1[n],txt,pos=2,col=cols[2])
nn<-round(n/2)
text(df2$b0[nn],df2$b1[nn],pos=2.5,paste0("IMV=",unique(df2$omega)),col=cols[2])

#####################
plot(df2$b1,df2$r2,type='l',col=cols[2],xlim=c(0,max(c(df1$b1,df2$b1))),ylim=c(0,yl),xlab=expression(beta[1]),ylab=expression(R^2))
lines(df1$b1,df1$r2,col=cols[1],lwd=4,lty=2)
legend("topleft",title=expression(omega),legend=names(cols),fill=cols,bty='n')
##
dev.off()


write.csv(df1, file = here('data', 'sims', 'prev_b0_v_b1', 'df1.csv'), row.names=FALSE)
write.csv(df2, file = here('data', 'sims', 'prev_b0_v_b1', 'df2.csv'), row.names=FALSE)
