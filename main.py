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
        bot = self.bot
        
        # Get the page where the tweet is made
        bot.get('https://twitter.com/compose/tweet')
        # This is the classname for the compose tweet area
        postArea = find_element_by_class_name('public-DraftEditor-content')
        # # We are clicking on the area
        bot.find_element_by_class_name('public-DraftEditor-content').click()
        time.sleep(2)
        # # We are clearing any data that might be there
        postInput.clear()
        # # We are sending the page the post which we received from the parameters of the function
        postArea.send_keys(post)
        # We can use this command if we want to space to the next line
        postInput.send_keys(Keys.CONTROL + Keys.SHIFT + Keys.RETURN)


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
                        bot.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div[1]/div/article/div/div[6]/div[3]/div/div").click()
                        time.sleep(5)
                    except Exception as ex:
                        time.sleep(60)
                        print('There was an error')


   

mainAccount = TwitterBot('dabbing.developer@gmail.com', 'twitterFaker#6969', 'funny')


mainAccount.login()
# mainAccount.makePost('This is my first tweet from the bot')
mainAccount.likeTweet()






