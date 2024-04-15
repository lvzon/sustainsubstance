library(ggplot2)
library(reshape2)
pec <- read.delim("iea-primary-energy-consumption-2011.csv", header = TRUE, as.is=TRUE)
pec$region <- factor(pec$region, levels=unique(pec$region))
ggplot(data = pec, aes(x=region, y=average.primary.energy.consumption..kWh.person.day.)) + geom_bar(stat="identity") + coord_flip() + ylab("\naverage kWh per person per day") + xlab("") + geom_text(aes(label = average.primary.energy.consumption..kWh.person.day.), hjust = 1.3, size = 3, color="white") + theme(axis.text=element_text(size=9), axis.title=element_text(size=9), plot.title=element_text(size=10, face="bold")) + ggtitle("PRIMARY ENERGY CONSUMPTION (2011)\n")




