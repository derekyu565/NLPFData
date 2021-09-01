import twint

c=twint.Config()
c.Search="President Duterte"
c.Lang='en'
c.Custom['tweet']=['tweet']
c.Limit=6000
c.Store_csv=True
c.Output="./du30.csv"

twint.run.Search(c)