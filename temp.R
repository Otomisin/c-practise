hell0 <- c(1, 2, 3)
print ("hello")

mdf <- data.frame("cat" = c("A","B","C"), values = c(12,10,15))
# View(mdf)

mygraph <- ggplot (mdf, aes(x = cat , y = values)) +
     geom_bar(stat = "Identity", color = "#f24747", fill = "#19af46")+
     ggtitle("My Test Bar Graph")

mygraph
