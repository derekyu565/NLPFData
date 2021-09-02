import pandas as pd

''' tapolan ko to delete
data=pd.read_csv("./datasets/labelledDTRUMP.csv")
positives=data.query("labels == 'Positive'")
neutrals=data.query("labels == 'Neutral'")
negatives=data.query("labels == 'Negative'")

print('TRUMP')
print(len(data),'\n',"Positive Sentiments:",len(positives),'\n',"Neutral Sentiments:",len(neutrals),'\n',"Negative Sentiments:",len(negatives),'\n')

'''
data=pd.read_csv("./datasets/labelledDU30.csv")
positives=data.query("labels == 'Positive'")
neutrals=data.query("labels == 'Neutral'")
negatives=data.query("labels == 'Negative'")

[print(negatives.iloc[i]['sentiments'],'\n\n')for i in range(0,len(negatives))]

negatives.to_csv('./datasets/negativeDU30Sentiments.csv')

#print('DU30')
#print(len(data),'\n',"Positive Sentiments:",len(positives),'\n',"Neutral Sentiments:",len(neutrals),'\n',"Negative Sentiments:",len(negatives),'\n')