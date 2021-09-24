from corpus_toolkit import corpus_tools as ct
import re#NLTK's regex isn't as intuitive plus naanad nako aning builtin regex sa python
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
stopWords=set(stopwords.words('english'))
import string 
import pandas as pd

cleanData=pd.read_csv('./vaccinesCleanData.csv')
stemmedData=pd.read_csv('./maggieTokensStemmed.csv')
lemmedData=pd.read_csv('./maggieTokensLemmed.csv')


tweets=cleanData['tweet'].to_numpy()# values() is deprecated
stemTokens=list(stemmedData['0'].to_numpy())#yes i am lazy
lemTokens=list(lemmedData['0'].to_numpy())

#because for some reason it reads the string as individual characters
test=[]
#so i used word_tokenize to force it to read the strings as tokens and not as a list of characters
[test.append(word_tokenize(str(tweets[i]))) for i in range(0,len(tweets))]
tweets=test
test=[]

#removal of stopwords
for i in range(len(tweets)):
	sublist=[]
	#this list comprehension is how i was able to preserve the [[],[],[],[]] characteristic for tweets variable
	[sublist.append(word) for word in tweets[i] if word not in stopWords and word !='&']
	test.append(sublist)
#preparing to use test as an empty list again
#tweets=pd.DataFrame(test);
tweets=test
tweets=pd.DataFrame({"tweet":[" ".join(tweet) for tweet in tweets]})
tweets.to_csv("./noStopWordTweets.csv",index=False)
'''
#this block of code could have been a for loop
test=[]
pattern='[0-9]'
#numerical characters managed to get converted into float in ct.frequency() for some reason so i decided to remove them nalang
stemTokens=[re.sub(pattern,'',str(stemTokens[i])) for i in range(0,len(stemTokens))]
test=[]#yes i am not creative with variable names this is why work in backend
pattern='[0-9]'
lemTokens=[re.sub(pattern,'',str(lemTokens[i])) for i in range(0,len(lemTokens))]
#this block of code could have been a for loop

#getting the different frequency chu2 sa mga lists/datasets
clean_freq=ct.frequency(tweets)
stem_freq=ct.frequency(stemTokens)
lem_freq=ct.frequency(lemTokens)

#this is to change the top n samples you want to print out with ct.head()
hits=10

#the block of code to print out the keyness
stem_corp_key=ct.keyness(clean_freq,stem_freq, effect="log-ratio")
print("Target: tweets| Reference : stemmed tokens")
ct.head(stem_corp_key,hits=hits)
print('\n')
lem_corp_key=ct.keyness(clean_freq,lem_freq, effect="log-ratio")
print("Target: stem| Reference : lemmed tokens")
ct.head(lem_corp_key,hits=hits)
#the block of code to print out the keyness
'''