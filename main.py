#Selenium allows us to crawl all over the web 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# This is just for handling the timing in between requests
import time




class TwitterBot:
    def __init__(self, username, password, hashtag):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
        self.hashtag = hashtag
        self.postArea = 'public-DraftStyleDefault-block'

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
        time.sleep(3)

    def makePost(self, post):
        postArea = 'public-DraftStyleDefault-block'
        bot = self.bot
        
        postInput =  bot.find_element_by_class_name(postArea)

        postInput.clear()
        postInput.send_keys(post)
        postInput.send_keys(Keys.RETURN)

    # This function was built when I had a problem with being logged out afer the initial link change

    def logBackIn(self):
        bot = self.bot
        hashtag = self.hashtag
        bot.get('https://twitter.com/search?q='+ hashtag +'&src=typed_query')
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(10)

    def likeTweet(self):
        bot = self.bot
        hashtag = self.hashtag
        bot.get('https://twitter.com/search?q='+ hashtag +'&src=typed_query')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)
            
            tweetLinks = [i.get_attribute('href') for i in bot.find_elements_by_xpath("//a[@dir='auto']")]
            

            for i in bot.find_elements_by_xpath("//a[@dir='auto']"):
                filteredLinks = list(filter(lambda x: 'status' in x, tweetLinks))
                # HANDLING THE ITEMS WITHIN THE ARRAY
                # print(filteredLinks)
                for link in filteredLinks:
                    print(link)
                    bot.get(link)
                    try:
                        # bot.find_element_by_class_name('r-yyyyoo').click()
                        # bot.find_element_by_xpath("//div[@data-testid='like']").click()
                        time.sleep(5)
                    except Exception as ex:
                        time.sleep(60)
                        print(ex)

            # for link in links:
            #     bot.get('https://twitter.com/' + link)
            #     print(link)
                # try:
                #     bot.find_element_by_class_name('HeartAnimation').click()
                #     time.sleep(10)
                # except Exception as ex:
                #     time.sleep(60)
                #     print(ex)
        
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

mainAccount = TwitterBot('dabbing.developer@gmail.com', 'twitterFaker#6969', 'funny')


mainAccount.login()
mainAccount.likeTweet()






