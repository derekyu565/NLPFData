import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sid_obj=SentimentIntensityAnalyzer()

def main():
    print("\nStart of Script\n")
    #data=pd.read_csv('./DTRUMP.csv')
    data=pd.read_csv('./datasets/du30.csv')
    max=len(data)
    results=[]
    for i in range(0,max):#C WILL NEVER DIE
        results.append(sentimentLabel(data.iloc[i]['tweet']))
    results=pd.DataFrame(results)
    results.to_csv("./datasets/labelledDU30.csv",index=False)
    print("\nEND OF SCRIPT\n")

def sentimentLabel(data):#VADER sentiment analyzer
    sentiment_dict=sid_obj.polarity_scores(data)
    if sentiment_dict['compound']>= 0.05:
        label="Positive"
    elif sentiment_dict['compound']<= -0.05:
        label="Negative"
    else:
        label="Neutral"
    return {'sentiments':tokens,'labels':label}

main()