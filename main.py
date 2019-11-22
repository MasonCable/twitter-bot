# This is where we handle the twitter api
from apiHandler import ApiFunctions
from searchHandlers import Search


class TwitterBot:
    def __init__(self, username, password, hashtag):
        self.username = username
        self.password = password
        self.hashtag = hashtag

    def start(self):
        username = self.username
        password = self.password
        hashtag = self.hashtag
        tokens = {
            '1',
            '2',
            '3',
            '4'
        }

        mainAccount = Search(username, password, hashtag)
        apiAccount = ApiFunctions(tokens)
    
        apiAccount.getTl()
        mainAccount.login()
        mainAccount.scrollTweets()




startBot = TwitterBot('dabbing.developer@gmail.com', 'twitterFaker#6969', 'funny')
startBot.start()
