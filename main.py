#Selenium allows us to crawl all over the web 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# This is just for handling the timing in between requests
import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
     

    def makePost(self, post):
        postArea = 'public-DraftStyleDefault-block'


    def likeTweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+ hashtag +'&src=typed_query')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            for link in links:
                bot.get('https://twitter.com/' + link)
               
    
    def checkIfLoggedIn(self):
        bot = self.bot
        test = 'https://twitter.com/search?q=funny&src=typed_query'
        test2 = 'https://twitter.com/'
        bot.get(test2)
        email = bot.find_element_by_name('session[username_or_email]')
    
        if email == email:
            postArea = 'public-DraftStyleDefault-block'
            print('Not Logged in')
        else:
            print('All Is good')

    def loginFromHashtag(self):
        bot = self.bot
        bot.get('https://twitter.com/search?q=funny&src=typed_query')
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

        for i in range(1,3):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)
            print('scrolling')
            tweets = bot.find_elements_by_class_name('css-1dbjc4n')
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            for link in links:
                bot.get('https://twitter.com/' + link)
                try:
                    bot.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(60)
                    print(ex)

mainAccount = TwitterBot('dabbing.developer@gmail.com', 'twitterFaker#6969')

# Make sure that each functions logs in to prevent the error that we were getting with the mainAccount.login() 
#mainAccount.loginFromHashtag()
mainAccount.login()
mainAccount.likeTweet('funny')





