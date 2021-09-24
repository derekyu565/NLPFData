import pandas as pd
import io
import numpy as np
import preprocessor as p
from PIL import Image
import matplotlib.pyplot as plt
df = pd.read_csv('./datasets/vaccines.csv')
df_double = df # With the duplicated rows, incase we need it sa futue but idk why we would
df = df.drop_duplicates()
df.shape
import re
REPLACE_NO_SPACE = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\|)|(\()|(\))|(\[)|(\])|(\%)|(\$)|(\>)|(\<)|(\{)|(\})")
REPLACE_WITH_SPACE = re.compile("(<br\s/>,br\s/>?)|(-)|(/)|(:).")

tweetsArr=[]
for line in df['tweet']:
  #send to tweet processor
  tempL = p.clean(line)
  #remove punctuation
  tempL= REPLACE_NO_SPACE.sub("",tempL.lower())#convert all tweets to lower case
  tempL = REPLACE_WITH_SPACE.sub(" ",tempL)
  tweetsArr.append(tempL)

tweetsArr

df = pd.DataFrame(data=tweetsArr, columns=['tweet'])
df

import nltk.corpus
import re
i=0
for index, row in df.iterrows():
    new_string=re.sub('[^a-zA-Z0-9]',' ',row['tweet'])
    cleaned_string=re.sub('\s+',' ',new_string)
    if row['tweet'] != cleaned_string:
        df.at[i, 'tweet'] = cleaned_string
    i+=1


#word count with stemming and lemmatization -Derek
from nltk.tokenize import RegexpTokenizer, word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
stopWords=set(stopwords.words('english'))
ps=PorterStemmer()
lem=WordNetLemmatizer()
tweets=df['tweet'].tolist()

stemmedTokens=[]
lemmatizedTokens=[]
maggieTokens=[]
stemmedMaggieTokens=[]
lemmedMaggieTokens=[]
for i in range (0,len(tweets)):#When in doubt write it like in C yes my brain stopped working
    tokens=word_tokenize(tweets[i])
    for word in tokens:
        if word not in stopWords:
            maggieTokens.append(word)
            stemmed=ps.stem(word)
            stemmedMaggieTokens.append(stemmed)
            lemmed=lem.lemmatize(word)
            lemmedMaggieTokens.append(lemmed)

maggieTokens=pd.DataFrame(maggieTokens)
maggieTokens.to_csv('maggieTokens.csv',index=False)

stemmedMaggieTokens=pd.DataFrame(stemmedMaggieTokens)
stemmedMaggieTokens.to_csv('maggieTokensStemmed.csv',index=False)
lemmedMaggieTokens=pd.DataFrame(lemmedMaggieTokens)
lemmedMaggieTokens.to_csv('maggieTokensLemmed.csv',index=False)

#topNumber=45
#from nltk.probability import FreqDist
#freqDistStemmed=FreqDist(stemmedTokens)
#top=freqDistStemmed.most_common(topNumber)
#top=pd.DataFrame(top)
#top.to_csv('stemmedCount.csv',index=False)#looking through csv is easier for me kay i have a small screen
#
#freqDistLemmed=FreqDist(lemmatizedTokens)
#top=freqDistLemmed.most_common(topNumber)
#top=pd.DataFrame(top)
#top.to_csv('lemmedCount.csv',index=False)