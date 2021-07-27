#####################################
########### From A_data.R ###########
#####################################

library(foreign)

##rand file, available here: https://www.rand.org/well-being/social-and-behavioral-policy/centers/aging/dataprod.html
read.dta('./data/HRS/randhrs1992_2016v1_archive_STATA/randhrs1992_2016v1.dta')->x

##hhidpn,sex, race, education
df<-x[,c("hhidpn","ragender","raracem","raedyrs","raddate","rabyear")]
#year, cog,
L<-list()
for (w in 3:12) {
  age<-x[[paste("r",w,"agey_m",sep='')]]
  cog<-x[[paste("r",w,"cogtot",sep="")]]
  prox<-x[[paste("r",w,"status",sep="")]]
  cog<-ifelse(prox=="1.cog meas",cog,NA)
  int.date<-x[[paste("r",w,"iwend",sep="")]]
  cesd<-x[[paste("r",w,"cesd",sep="")]]
  lonely<-x[[paste("r",w,"flone",sep="")]]
  iadl<-x[[paste("r",w,"iadlza",sep="")]]
  nhome<-x[[paste("r",w,"nhmliv",sep="")]]
  if (w>3) wealth<-x[[paste("h",w,"atotb",sep="")]] else rep(NA,nrow(x))->wealth
  conds<-c("hibp","diab","cancr","lung","heart","strok","psych","arthr")
  for (nm in conds) assign(nm,x[[paste("r",w,nm,sep="")]])
  tmp<-data.frame(hhidpn=x$hhidpn,cog=cog,int.date=int.date,wave=w,age=age,cesd=cesd,iadl=iadl,wealth=wealth,nhome=nhome,lonely=lonely)
  for (nm in conds) tmp[[nm]]<-get(nm)
  L[[as.character(w)]]<-merge(df,tmp,all.x=TRUE)
}


df<-data.frame(do.call("rbind",L))
df<-df[!is.na(df$cog),]

for (nm in conds) {
  df[[nm]]->z
  df[[nm]]<-ifelse(z=="0.no",0,NA)
  df[[nm]]<-ifelse(z=="1.yes",1,df[[nm]])
}

#status: proxy respondent
L<-list()
for (w in 1:13) {
  prox<-x[[paste("r",w,"proxy",sep="")]]
  prox<-ifelse(prox=="1.proxy",1,0)
  L[[as.character(w)]]<-data.frame(hhidpn=x$hhidpn,prox=prox,w=w)
}
prox<-data.frame(do.call("rbind",L))
prox<-prox[!is.na(prox$prox) & prox$prox==1,]
id<-paste(prox$hhidpn,prox$w-1)
df$proxy<-ifelse(paste(df$hhidpn,df$wave) %in% id,1,0)
##death
as.POSIXct(df$raddate*24*60^2,origin = "1960-01-01")->df$ddate.raw
as.POSIXct(df$int.date*24*60^2,origin = "1960-01-01")->df$iwend.raw
delta<-df$ddate.raw - df$iwend.raw
df$dead<-ifelse(delta<365*2,1,0)
##next test
L<-list()
for (w in 3:12) {
  prox<-x[[paste("r",w,"proxy",sep="")]]
  int.date<-x[[paste("r",w,"iwend",sep="")]]
  tmp<-data.frame(hhidpn=x$hhidpn,prox=prox,w=w,int.date=int.date)
  L[[as.character(w)]]<-tmp
}
tmp<-data.frame(do.call("rbind",L))
tmp<-tmp[!is.na(tmp$int.date),]
tmp<-tmp[tmp$prox=='0.not proxy',]
id<-paste(tmp$hhidpn,tmp$w-1)
df$inhrs<-ifelse(paste(df$hhidpn,df$wave) %in% id,1,0)

##status
st<-ifelse(df$inhrs==1 & df$proxy==0,1,NA)
st<-ifelse(df$proxy==1,2,st)
st<-ifelse(df$dead==1 & is.na(st),3,st)
st<-ifelse(is.na(st),4,st)
table(df$wave,st)
df$status<-c("eligible","proxy","dead","attrit")[st]

##grip & gait
load("./data/HRS/grip_gait.Rdata")
df<-merge(df,x,all.x=TRUE)
##now add next wave health obs
conds<-c("hibp","diab","cancr","lung","heart","strok","psych","arthr")
for (nm in conds) {
  tmp<-df[,c("hhidpn","wave",nm)]
  names(tmp)[3]<-paste(nm,'.next',sep='')
  tmp$wave<- tmp$wave - 1
  df<-merge(df,tmp,all.x=TRUE)
}

#df<-df[df$wave<=11,]




conds<-c("hibp","diab","cancr","lung","heart","strok","psych","arthr")
tmp<-df[,c("hhidpn","wave",conds)]
tmp$wave<-tmp$wave -1
#names(tmp)[-(1:2)]<-paste(conds,".next",sep='')
for (nm in conds) {
  ii<-grep(nm,names(df))
  df<-df[,-ii]
}
df<-merge(df,tmp,all.x=TRUE)

save(df,file='./data/HRS/df.Rdata')


#####################################
######## From A2_grip_gait.R ########
#####################################

read.dat.dct <- function(dat, dct, labels.included = "no") {
  #from http://stackoverflow.com/questions/14224321/reading-dat-and-dct-directly-from-r
  temp <- readLines(dct)
  temp <- temp[grepl("_column", temp)]
  switch(labels.included,
         yes = {
           pattern <- "_column\\(([0-9]+)\\)\\s+([a-z0-9]+)\\s+(.*)\\s+%([0-9]+)[a-z]\\s+(.*)"
           classes <- c("numeric", "character", "character", "numeric", "character")
           N <- 5
           NAMES <- c("StartPos", "Str", "ColName", "ColWidth", "ColLabel")
         },
         no = {
           pattern <- "_column\\(([0-9]+)\\)\\s+([a-z0-9]+)\\s+(.*)\\s+%([0-9]+).*"
           classes <- c("numeric", "character", "character", "numeric")
           N <- 4
           NAMES <- c("StartPos", "Str", "ColName", "ColWidth")
         })
  metadata <- setNames(lapply(1:N, function(x) {
    out <- gsub(pattern, paste("\\", x, sep = ""), temp)
    out <- gsub("^\\s+|\\s+$", "", out)
    out <- gsub('\"', "", out, fixed = TRUE)
    class(out) <- classes[x] ; out }), NAMES)
  metadata[["ColName"]] <- make.names(gsub("\\s", "", metadata[["ColName"]]))
  myDF <- read.fwf(dat, widths = metadata[["ColWidth"]],
                   col.names = metadata[["ColName"]])
  if (labels.included == "yes") {
    attr(myDF, "col.label") <- metadata[["ColLabel"]]
  }
  myDF
}

getvars<-function(tmp,letter,wave) {
  names(tmp)->nms
  gsub(paste("^",letter,sep=""),"J",nms)->nms
  nms->names(tmp)
  tmp[,c("JI816","JI851","JI852","JI853")]->grip
  for (i in 1:ncol(grip)) ifelse(grip[,i]>1000,NA,grip[,i])->grip[,i]
  apply(grip,1,max,na.rm=TRUE)->grip
  ifelse(!is.finite(grip),NA,grip)->grip
  #rowMeans(grip,na.rm=TRUE)->grip
  tmp[,c("JI823","JI824")]->gait
  for (i in 1:ncol(gait)) ifelse(gait[,i]>1000,NA,gait[,i])->gait[,i]
  rowMeans(gait,na.rm=TRUE)->gait
  ifelse(grip>80,NA,grip)->grip
  ifelse(gait>30,NA,gait)->gait
  data.frame(wave=wave,hhid=tmp$HHID,pn=tmp$PN,grip=grip,gait=gait)->tmp
}

L<-list()
##2004
read.dat.dct(dat='./data/HRS/h04da/H04I_R.da',dct='./data/HRS/h04sta/H04I_R.dct')->tmp
getvars(tmp,letter='J',wave=7)->L[['2004']]

##2006
read.dat.dct(dat='./data/HRS/h06da/H06I_R.da',dct='./data/HRS/h06sta/H06I_R.dct')->tmp
getvars(tmp,letter='K',wave=8)->L[['2006']]

##2008
read.dat.dct(dat='./data/HRS/h08da/H08I_R.da',dct='./data/HRS/h08sta/H08I_R.dct')->tmp
getvars(tmp,letter='L',wave=9)->L[['2008']]

##2010
read.dat.dct(dat='./data/HRS/h10da/H10I_R.da',dct='./data/HRS/h10sta/H10I_R.dct')->tmp
getvars(tmp,letter='M',wave=10)->L[['2010']]

##2012
read.dat.dct(dat='./data/HRS/h12da/H12I_R.da',dct='./data/HRS/h12sta/H12I_R.dct')->tmp
getvars(tmp,letter='N',wave=11)->L[['2012']]

##2014
read.dat.dct(dat='./data/HRS/h14da/H14I_R.da',dct='./data/HRS/h14sta/H14I_R.dct')->tmp
getvars(tmp,letter='O',wave=12)->L[['201']]

do.call("rbind",L)->x
data.frame(x)->x
as.character(as.numeric(x$hhid)*1000+as.numeric(x$pn))->x$hhidpn
NULL->x$hhid
NULL->x$pn
x[!is.na(x$grip) | !is.na(x$gait),]->x

ifelse(x$gait<1,NA,x$gait)->x$gait
log(x$gait)->x$gait

save(x,file='./data/HRS/grip_gait.Rdata')
write.csv(df, file='./data/HRS/hrs_desc.csv')
