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
