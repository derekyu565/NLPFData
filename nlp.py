import twint

c=twint.Config()
c.Search="tiktok"
c.Lang='en'
c.Custom['tweet']=['tweet']
c.Limit=5069 #hehe
c.Store_csv=True
c.Output="./tiktok.csv"
#for some reason i have to explicitly say that i want it to write at the root directory

twint.run.Search(c)