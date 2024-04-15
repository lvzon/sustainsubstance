library(ggplot2)
library(reshape2)
hpss <- read.delim("hertwich-peters-2009-selection.csv", header = TRUE, as.is=TRUE)
dfss <- melt(hpss, id.vars = "country")
dfss$country <- factor(dfss$country, levels=unique(dfss$country))
ggplot(data = dfss, aes(x = country, y = value, fill = variable)) + geom_bar(stat="identity") + coord_flip() + ylab("greenhouse gas emission from consumption (kg CO2eq per person per day)") + scale_fill_grey(start = 1, end = 0)

