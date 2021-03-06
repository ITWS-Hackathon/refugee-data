library(wordcloud)
library(wordcloud2)
library(RColorBrewer)
library(tm)
library(tmap)

tweetDS <- read.csv("/Users/yasmine/Downloads/github/jjsalesplatform/refugee-data/data/frequency_results.csv")

text <- tweetDS$Words
docs <- Corpus(VectorSource(text))

#docs <- tm::tm_map(docs, content_transformer(tolower))
#docs <- tm_map(docs, removeWords, stopwords("english"))

dtm <- TermDocumentMatrix(docs) 
matrix <- as.matrix(dtm) 
words <- sort(rowSums(matrix),decreasing=TRUE) 
df <- data.frame(word = names(words),freq=words)

#set.seed(1234) # for reproducibility 
#wordcloud(words = df$word, freq = df$freq, min.freq = 2, max.words=200, random.order=FALSE, rot.per=0.35, colors=brewer.pal(8, "Dark2"))
wordcloud2(data=df, size=1.5, color='random-dark', rotateRatio = 1)
# letterCloud(data=df, "Ukraine", color='random-dark', size=1, backgroundColor="white")
           