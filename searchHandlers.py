from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class  Search:
    def __init__(self, username, password, hashtag):
        self.username = username
        self.password = password
        self.hashtag = hashtag
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
        time.sleep(3)

    def scrollTweets(self):
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
                        # bot.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div[1]/div/article/div/div[6]/div[3]/div/div").click()
                        time.sleep(5)
                    except Exception as ex:
                        time.sleep(60)
                        print('There was an error')
