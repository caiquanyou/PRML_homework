rm(list = ls())
Sys.setenv(R_MAX_NUM_DLLS=999)
options(stringsAsFactors = F)
library(leaps)
library(Hmisc)
library(MASS)
library(car)
#读取数据
trainning_data<-read.csv(file = '2019年回归分析期中考试数据.csv',header = T,encoding = 'UTF-8',stringsAsFactors = TRUE)
#缺失值处理
missing_data<-as.matrix(apply(trainning_data,2, function(x){sum(is.na(x))/length(x)*100}))
#找出缺失值大于50%的特征，删除该特征
miss_feature<-names(which(missing_data[,1]>=50))
clean_data<-trainning_data[,-match(miss_feature,names(trainning_data))]
# 按照列，替换每一列的NA值为该列的平均值
clean_data=apply(clean_data,2,function(x){
  x[is.na(x)]=mean(x,na.rm = T)
  return(x)
})
clean_data<-as.data.frame(clean_data)
#这里也找到简单的Hmisc包里面的impute实现同样的功能
for(i in seq(1,68)){clean_data[,i]<-impute(clean_data[,i],median)}
lm_1<-lm(RA~GENDER+DRWITHGL+NRWITHGL+RAXISLEG+RANTECHA+RWTW+RNCONPRE+HEIGHT+WEIGHT+TOUW+SBLOPRE+DBLOPRE+PULSE+CHAOD1+ETEST+TRT+
             AMB11+AMB21+AMB31+AMB41+DRUGIF+PREGQ+SGAR+LSMK+COSTM+BULBP+TUTOR1+TUTOR2+NTON+MSMK+HSMK+MH+FH+FW+BED+IFTAI+BULB+
             TUTOR+CELLP+NOONS+EYE+EYE1+SITE+STR+PLACE5+SHIFT+IFDOU+ALLERGY+DRNBASE+NRNBASE+DOMEYE+RPR+JTR+YTR+RCORCU+DAI1+DAI2+MB+ACI+BCI+CCI+DCI+total+st1 +st2+INCM+PREG,data= clean_data)
#假设检验
qqPlot(lm_1,id.method='identify',simulate = TRUE,labels=row.names(RA),main='Q-Q plot')
durbinWatsonTest(lm_1)
ncvTest(lm_1)
#par(mfrow=c(2,2))
#plot(lm_1)
#逐步向后回归
step(lm_1, direction = "backward")
#MASS包的stepAIC函数进行逐步向后回归
##stepAIC(lm_1, direction = "backward")
#选取AIC最小的模型结果
lm_2<-lm(RA~ GENDER + DRWITHGL + RAXISLEG + RANTECHA + RNCONPRE + 
               CHAOD1 + AMB41 + FH + FW + CELLP + STR + DRNBASE + NRNBASE + 
               DOMEYE + RPR + YTR + RCORCU + DAI1 + DAI2 + MB + total + 
               PREG,data= clean_data)
summary(lm_2)
lm_3<-lm(RA ~ GENDER + DRWITHGL + RAXISLEG + RANTECHA + CHAOD1 + 
               AMB41 + CELLP + DRNBASE + NRNBASE + 
               RPR + YTR + RCORCU + DAI1 + PREG,data=clean_data)
summary(lm_3)
#全子集回归法
lm_sub<-regsubsets(RA~GENDER+DRWITHGL+NRWITHGL+RAXISLEG+RANTECHA+RWTW+RNCONPRE+HEIGHT+WEIGHT+TOUW+SBLOPRE+DBLOPRE+PULSE+CHAOD1+ETEST+TRT+ AMB11+AMB21+AMB31+AMB41+DRUGIF+PREGQ+SGAR+LSMK+COSTM+BULBP+TUTOR1+TUTOR2+NTON+MSMK+HSMK+MH+FH+FW+BED+IFTAI+BULB+ TUTOR+CELLP+NOONS+EYE+EYE1+SITE+STR+PLACE5+SHIFT+IFDOU+ALLERGY+DRNBASE+NRNBASE+DOMEYE+RPR+JTR+YTR+RCORCU+DAI1+ DAI2+MB+ACI+BCI+CCI+DCI+total+st1+st2+INCM+PREG,data=clean_data,really.big=T,nbest=4)
plot(lm_sub,scale="adjr2")
#选最大adjr2拟合
lm_4<-lm(RA~GENDER+NRWITHGL+RAXISLEG+RANTECHA+DRNBASE+RPR+YTR+ RCORCU,data = clean_data)
summary(lm_4) 
#异常值检验
outlierTest(lm_4)
yichang<-c(995,409,815,872,286,315,603,2018,993)
c1_data<-clean_data[-yichang,]
cook_dis <- cooks.distance(lm_4)
plot(cook_dis, pch="*", cex=2, main="Influential Obs by Cooks distance") 
abline(h = 4*mean(cook_dis, na.rm=T), col="red")
text(x=1:length(cook_dis)+1, y=cook_dis, labels=ifelse(cook_dis>4*mean(cook_dis, na.rm=T),names(cook_dis),""), col="red") 
influential<-which(cook_dis>4*mean(cook_dis, na.rm=T))
c2_data<-c1_data[-influential,]
#重新拟合
lm_5<-lm(RA~GENDER+NRWITHGL+RAXISLEG+RANTECHA+DRNBASE+RPR+YTR+ RCORCU,data = c2_data)
summary(lm_5)
#对所选模型进行假设检验
par(mfrow=c(2,2))
plot(lm_5)
#测试数据集预测
test_data<-read.csv(file = '测试集.CSV')
yucezhi = predict(lm_5, newdata = test_data)
test_data$RA_预测=yucezhi
for(i in seq(1,8)){
  if(test_data$RA_预测[i]>0.5){
    test_data$视力[i]<-"远视"
  } 
  else if(test_data$RA_预测[i]<(-0.5)){
    test_data$视力[i]<-"近视"
  } else{
    test_data$视力[i]<-"正常"
  }
}
test_data[,c(72,73)]
write.csv(test_data,"预测结果.csv")

sessionInfo()
save.image(file = "mid_test.RData")
