#https://github.com/twintproject/twint/wiki/Configuration

import twint

c=twint.Config()
#c.Search="donald trump"
c.Search="president duterte"
c.Lang='en'
c.Custom['tweet']=['tweet']
c.Limit=10000 #hehe
c.Store_csv=True
c.Filter_retweets=True
c.Output="./datasets/du30.csv"
#for some reason i have to explicitly say that i want it to write at the root directory

twint.run.Search(c)