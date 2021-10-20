#Reading the file
tweets <- read.csv(file.choose(),header=T)
print(tweets);

#Building the corpus/dataset
library(tm)
corpus <-iconv(tweets$tweet,to ="utf-8")
corpus <- Corpus(VectorSource(corpus))
inspect(corpus[1:5])

#Our dataset is already lowered through python btw -derek
#Clean text
corpus <- tm_map(corpus, tolower)
inspect(corpus[1:5])

#Our dataset already doesn't have punctuation -derek
corpus <- tm_map(corpus, removePunctuation)
inspect(corpus[1:5])

#But our dataset still has 19 and other numbers -derek
corpus <- tm_map(corpus, removeNumbers)
inspect(corpus[1:5])

#Our dataset also doesn't have stopword also -derek
cleanset <-tm_map(corpus,removeWords, stopwords('english'))
cleanset <-tm_map(corpus,removeWords, c('things','countries','bonjour','ago','dont','theyve','vaccines','vaccine'))
inspect(cleanset[1:5])

#our dataset already has no URLs and I am omitting the removal of URL from the video -derek

#Removal of white space
cleanset <-tm_map(cleanset, stripWhitespace)
inspect(cleanset[1:5])

#Term document matrix
tdm<-TermDocumentMatrix(cleanset)
tdm
tdm <- as.matrix(tdm)
tdm[1:100, 1:20]

#Bar plot
w<- rowSums(tdm)
w<- subset(w,w>25)
barplot(w,
        las=2,
        col = rainbow(10))

install.packages("wordcloud")
install.packages("wordcloud2")
#for word cloud - Ismael and Margaret
library(wordcloud)
wordcount <- sort(rowSums(tdm), decreasing = TRUE)
set.seed (100)
wordcloud(words = names(w), freq = w, max.words = 200, random.order = F, min.freq = 50)

install.packages("syuzhet")
install.packages("lubridate")
install.packages("ggplot2")
install.packages("scales")
install.packages("reshape2")
install.packages("dplyr")

#sentiment analysys - Ismael and Riane
library(syuzhet)
library(lubridate)
library(ggplot2)
library(scales)
library(reshape2)
library(dplyr)

#Read File
tweetsData <- read.csv('noStopWordTweets.csv',header=T)

library(tm)
tweets <-iconv(tweetsData$tweet,to ="utf-8")

#Obtain sentiment scores - Ismael
s <- get_nrc_sentiment(tweets)
head(s)
tweets[4]

get_nrc_sentiment('delay')

barplot(colSums(s), las = 2, col = rainbow(10), ylab = 'Count', main = 'Sentiment Scores') #Clyde Vincent