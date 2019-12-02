# This is where we handle the twitter api
# from apiHandler import ApiFunctions
from searchHandlers import Search
# Remember to send apiHandler the tokens
from cred import access_token, access_token_secret, consumer_key, consumer_secret


class TwitterBot:
    def __init__(self, username, password, hashtag):
        self.username = username
        self.password = password
        self.hashtag = hashtag
      
    def start(self):
        username = self.username
        password = self.password
        hashtag = self.hashtag
        

        # runs the search Handlers code
        mainAccount = Search(username, password, hashtag)
        
        # apiAccount = ApiFunctions(self.hashtag)
    
        # apiAccount.getTl()
        # runs the search Handlers code
        mainAccount.login()
        mainAccount.scrollTweets()
 







startBot = TwitterBot('dabbing.developer@gmail.com', 'twitterFaker#6969', 'funny')
startBot.start()
