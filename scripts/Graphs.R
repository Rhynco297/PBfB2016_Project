#Set working directory & read in datafile
setwd("~/Documents/PBfB/Project/Reorganize")
Hours <- read.csv(file="Re_Hours.csv",head=TRUE,sep="\t")
library(wavelets) #Loading package for stackplot

#Make weeks and jobs a factor (Weeks will be a category later) & attach data
Hours$Week <- factor(Hours$Week)
Hours$Job <- factor(Hours$Job)

attach(Hours)

#Create a column with overtime hours (Total-Normal hrs)
Hours <- data.frame(Hours, Overtime = (Hours$hTotal - Hours$hNormal))

#Calculate total Normal and Overtime hours per week:
Totals <- aggregate(Hours$hNormal, by=list(Week=Hours$Week),FUN=sum)
Totals <- data.frame(Totals, aggregate(Hours$Overtime, by=list(Week=Hours$Week), FUN=sum))
attach(Totals)
#Rename the columns
names(Totals)[names(Totals)=="x"] <- "NormalH"
names(Totals)[names(Totals)=="x.1"] <- "Overtime"
#Rename the rows to the week numbers and take out Week columns
row.names(Totals) <- Totals$Week
Totals$Week <- NULL
Totals$Week.1 <- NULL
#Transpose the data so that it fits the desired format for barplot
Totals <- t(Totals)

#Create a stacked barplot:
barplot(as.matrix(Totals), 
    xlab='Weeks', ylab='Hours', main="Total worked hours per week",
    col=c("green","dark red"), legend=c("Normal hours","Overtime"),
    ylim=c(0,8000))
#And save to a png file
dev.copy(png,'Worked_Hours.png')
dev.off()