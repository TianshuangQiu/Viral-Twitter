import twint


c = twint.Config()
c.Username = "twitter"

twint.run.Search(c)