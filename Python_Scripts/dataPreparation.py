import pandas as pd
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from corpus_toolkit import corpus_tools as ct
tok=RegexpTokenizer(r'\w+')
lem=WordNetLemmatizer()
stopWords=set(stopwords.words('english'))

def main():
    print("\nStart of Script\n")
    data=pd.read_csv('./datasets/vaccines.csv')
    max=len(data)
    results=[]
    for i in range(0,max):#C WILL NEVER DIE
        results.append(cleaner((data.iloc[i]['tweet'])))
    results=pd.DataFrame(results)
    results.to_csv("./test.csv",index=False)#this is just easier for me to inspect than with print()
    
    frequency=ct.frequency(results['tweet'])
    corp_key=ct.keyness(frequency,frequency)
    print(ct.head(corp_key,hits=100))
    print("\nEND OF SCRIPT\n")

def cleaner(data):#to clean the tokens
    tokens=tok.tokenize(data.lower())
    results=[]
    for token in tokens:#index        
        if token not in stopWords:
            token=lem.lemmatize(token)
            results.append(token)
    return {'tweet':results}

main()