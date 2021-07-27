###########################################
########### From C_prediction.R ###########
###########################################

source('./src/big_fun.R')
load(file='./data/HRS/df.Rdata')
df$nhome<-ifelse(df$nhome=='1.yes',1,0)

df<-df[df$age>=60,]

conds<-c("hibp","diab","cancr","lung","heart","strok","psych","arthr","proxy","dead")

fm1<-formula("outcome~1")
fm2<-formula("outcome~age")
conds<-c("hibp","diab","cancr","lung","heart","strok","psych","arthr","proxy","dead")
out<-list()
for (cond in conds) {
  df[[cond]]->df$outcome
  out[[cond]]<-bigfun(df[!is.na(df$age),],fm1,fm2)
}
ew<-do.call("rbind",out)

wrapper<-function(df,fm1,fm2,conds) {
  out<-list()
  window<-1.5
  for (yr in seq(60,90,by=1)) {
    df.age<-df[abs(df$age-yr)<window,]
    for (cond in conds) {
      x<-df.age
      x[[paste(cond,sep='')]]->x$outcome
      tmp<-x[,all.vars(fm2)]
      x<-x[rowSums(is.na(tmp))==0,]
      if (nrow(x)>1000) {
        ew<-bigfun(x,fm1=fm1,fm2=fm2)
        out[[paste(cond,yr)]]<-c(cond,yr,ew[c(1,4)],nrow(x))
      }
    }
  }
  out
}

fm1<-formula("outcome~1")
fm2<-formula("outcome~raracem+ragender")
out1<-wrapper(df,fm1,fm2,conds=conds)
out1a<-do.call("rbind",out1)
fm1<-formula("outcome~raracem+ragender")
fm2<-formula("outcome~raracem+ragender+raedyrs")
out1<-wrapper(df,fm1,fm2,conds=conds)
out1b<-do.call("rbind",out1)
fm1<-formula("outcome~raracem+ragender+raedyrs")
fm2<-formula("outcome~raracem+ragender+raedyrs+cog")
out1<-wrapper(df,fm1,fm2,conds=conds)
out1c<-do.call("rbind",out1)
fm1<-formula("outcome~1")
fm2<-formula("outcome~raracem+ragender")
out2<-wrapper(df,fm1,fm2,conds=conds)
out2a<-do.call("rbind",out2)
fm1<-formula("outcome~raracem+ragender")
fm2<-formula("outcome~raracem+ragender+raedyrs")
out2<-wrapper(df,fm1,fm2,conds=conds)
out2b<-do.call("rbind",out2)
fm1<-formula("outcome~raracem+ragender+raedyrs")
fm2<-formula("outcome~raracem+ragender+raedyrs+grip+gait")
out2<-wrapper(df,fm1,fm2,conds=conds)
out2c<-do.call("rbind",out2)


write.csv(out1a, file='./data/HRS/out1a.csv')
write.csv(out1b, file='./data/HRS/out1b.csv')
write.csv(out1c, file='./data/HRS/out1c.csv')
write.csv(out2c, file='./data/HRS/out2c.csv')
