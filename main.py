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
        mainAccount = Search(username, password, hashtag)
        mainAccount.login()
        mainAccount.scrollTweets()

startBot = TwitterBot('dabbing.developer@gmail.com', 'twitterFaker#6969', 'funny')
startBot.start()
