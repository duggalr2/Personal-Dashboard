from bs4 import BeautifulSoup
from urllib.request import urlopen
import random, re, getpass
from robobrowser import RoboBrowser
# import getpass, random
# import time, re, os
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys


def hn_books():
    """
    Get's Scraped Book's to read off of hackernewsbooks.com (Have already completed 2013+)
    Write's to a file
    """
    url = 'http://hackernewsbooks.com/year/2013'
    soup = BeautifulSoup(urlopen(url))
    title = soup.find_all('h3', class_='title')
    with open('title_to_rate', 'a') as f:
        for i in title:
            i = i.text
            i = re.sub('([0-9]\.)', '', i)
            i = re.sub('([0-9])', '', i)
            i = i.strip()
            f.write(i + '\n')

def course_script():
    """
    Return's current courses + subject posts from ROSI account in a list
    Not abstract enough to make it work for anyone...
    """
    browser = RoboBrowser()
    browser.open('https://sws.rosi.utoronto.ca/sws/welcome.do?welcome.dispatch')
    form = browser.get_form(id='personForm')
    try:
        form['personId'].value = '1001561570'
        pswd = getpass.getpass('Password: ')
        form['pin'].value = pswd
        browser.submit_form(form)
    except:
        print('Error signing in..')

    browser.open('https://sws.rosi.utoronto.ca/sws/subjectpost/main.do?main.dispatch')
    x =browser.find_all('input', {"name": 'description'})
    subject_post = [x[i]['value'] for i in range(len(x)) if i%2]
    # summer course...

    # link = browser.find_all('table', class_='decorated')
    # course_link = []
    # for i in link:
    #     a = i.findAll('a')
    #     course_link.append(a[1]['href'])
    # for i in course_link:
    #     st = 'https://sws.rosi.utoronto.ca/' + i
    #     browser.open(st)
    #     print(browser)
        # x = browser.find_all('tr', class_='odd')
        # y = browser.find_all('tr', class_='even')
        # print(x)
    # browser.open('https://sws.rosi.utoronto.ca/sws/reg/course/list.do?listCourses.dispatch=1&collaborativeOrgCode=LT82MqC8zQM%3D&sessionCode=65PZTq%2B0B8s%3D&designationCode1=HF5ddYyMe3E%3D&status=axxVSEk7gsI%3D&coSecondaryOrgCode=LT82MqC8zQM%3D&sessionDescription=fr0MjoyA%2B9WSdPml%2Fqnatw%3D%3D&postCode=skTjwpNygB2Vie%2BjZGr89w%3D%3D&postOfferCncLimit=9MpRP4bTJ4M%3D&postAcpDuration=MIxCVNo4Ckg%3D&postDescription=tOK7DD2Ye3ZU%2Fjmb%2FoDMV7%2Fcr%2FTHDv6C45uX0gjavwo%3D&subjectCode1=Rah%2Bq4h88I4%3D&assocOrgCode=EcsTItcJNkw%3D&adminOrgCode=EcsTItcJNkw%3D&candidacySessionCode=Rxja0SrRHz0%3D&candidacyPostCode=Crv90qWQMFGcTpCbc5fk4A%3D%3D&postOfferCncAllowed=kZhlu1IV12g%3D&levelOfInstruction=BBxY5ww9wkA%3D&secondaryOrgCode=LT82MqC8zQM%3D&yearOfStudy=MIxCVNo4Ckg%3D&acpDuration=nE6Qm3OX5OA%3D&primaryOrgCode=EcsTItcJNkw%3D&typeOfProgram=1JMSKFClrnc%3D')
    # x = browser.find_all('tr', class_='odd')
    # y = browser.find_all('tr', class_='even')
    # course = [i.find('b').text for i in x]
    # b = [i.find('b').text for i in y]
    # course.extend(b)
    # return subject_post, course

if __name__ == '__main__':
    # hn_books()
    print(course_script())







##########################################
        #Don't Look at...
##########################################


### TODO: Easy script below, start with this, collect data (IMPT) and then,
##TODO: train a classifier to generate more useful book recommendations and not random ones;
##TODO: Instead of using amazon and wasting time; use stackoverflow csv and hackernews;
## TODO: Have an option to choose between the two or return a random one, if
##TODO I like it, save to current books, if not, show next book;
##TODO: Obv above needs to be checked if UOFT HAS it;

# chromedriver = '/Users/Rahul/Downloads/chromedriver'
# os.environ["webdriver.chrome.driver"] = chromedriver
# driver = webdriver.Chrome(chromedriver)
# driver.set_window_size(1024, 768)



## Script 1:
# def uoft_library_search(title):
#     driver.get('http://search.library.utoronto.ca/index?SearchFilter=6962')
#     time.sleep(2)
#     search = driver.find_element_by_name('Ntt')
#     search.send_keys(title)
#     search.submit()
#     time.sleep(5)
#     wait = WebDriverWait(driver, 15)
#     wait.until(EC.presence_of_element_located((By.ID, "num-records")))
#     num_records = driver.find_element_by_id('num-records').text
#     num_records = num_records.split()
#     grouped_record_links = []
#     book_dict = {}
#
#     if int(num_records[0]) == 0:
#         choose_book()
#
#     else:
#         print(title)
#         wait.until(EC.presence_of_element_located((By.CLASS_NAME, "hitlist-data-wrapper")))
#         wait.until(EC.presence_of_element_located((By.CLASS_NAME, "hitlist-title")))
#         wait.until(EC.presence_of_element_located((By.CLASS_NAME, "hitlist-holdings")))
#
#         y = driver.find_elements_by_class_name('hitlist-item-content')
#
#         for i in y:
#             try:
#                 x = i.find_element_by_class_name('hitlist-title')
#                 z = i.find_element_by_class_name('hitlist-holdings')
#                 z = (z.text).replace('\n', ' ')
#                 book_dict[x.text] = [z]
#             except:
#                 w = i.find_elements_by_tag_name('a')
#                 grouped_record_links.append(w[-1])
#
#     return book_dict, grouped_record_links
#
# ##TODO: WRITE ALL THE BOOKS (INCLUDING GROUPED) AND HOLDING INFO INTO TXT!
# ##TODO: SHOULD I DO THIS IN CLASSES INSTEAD;

# def stackoverflow_book():
#     with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/book_names') as f:
#         lines = f.readlines()
#         title = lines[random.randrange(0, 101)]
#         return title
#
# def hn_book():
#     with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/2017_hn.txt', 'r') as f:
#         lines = f.readlines()
#         title = lines[random.randrange(0, len(lines))]
#         return title

# def choose_book(): #gets a random book from Stackoverflow/HN and checks uoft library; if both in, returns them
#     hn_b = hn_book()
#     hn_b = hn_b.replace('\n', '')
#     x1, x2 = uoft_library_search(hn_b)
#     st_b = stackoverflow_book()
#     st_b = st_b.replace('\n', '')
#     x3, x4 = uoft_library_search(st_b)

    # if len(x2) > 0:
    #     for i in x2:
    #         driver.get()



# choose_book()



## Script 2:
# def amazon_search(user_search):
#     ## randomly select topic from list of topics; search on amazon;
#     ## or have a pre-list of topics and choice from that (like the amazon choices);
#     ## for now, i just use user_input;
#     chromedriver = '/Users/Rahul/Downloads/chromedriver'
#     os.environ["webdriver.chrome.driver"] = chromedriver
#     driver = webdriver.Chrome(chromedriver)
#     driver.set_window_size(1024, 768)
#     driver.get('https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin')
#     time.sleep(2)
#     username = driver.find_element_by_id('ap_email')
#     password = driver.find_element_by_id('ap_password')
#     username.send_keys('duggalr42@gmail.com')
#     pswd = getpass.getpass('Password: ')
#     password.send_keys(pswd)
#     print('Awesome, on sec!')
#     password.submit()
#     time.sleep(3)
#     search = driver.find_element_by_id('twotabsearchtextbox')
#     ## list of keywords; and search those;)
#     search.send_keys(user_search)
#     search.submit()
#     time.sleep(3)
#     for i in range(10):
#         # x = driver.find_element_by_xpath('//*[@id="result_%d"]/div/div/div/div[2]/div[1]/div[1]' % i)
#         x = driver.find_element_by_xpath('//*[@id="result_%d"]/div/div/div/div[2]/div[1]/div[1]/a/h2' % i)
#         print(x.text)

    ##TODO: there are a lot of different cases that could happen, ads pop up, recom's in between results, etc;
# amazon_search()



