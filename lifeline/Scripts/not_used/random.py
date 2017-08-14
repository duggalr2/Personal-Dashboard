from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
from urllib.request import urlopen
import getpass, random
import facebook, time, re, os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


## Script that retrives courses of my Rosi;
def course_script():
    browser = RoboBrowser()
    browser.open('https://sws.rosi.utoronto.ca/sws/welcome.do?welcome.dispatch')
    form = browser.get_form(id='personForm')
    form['personId'].value = '1001561570'
    form['pin'].value = ''
    browser.submit_form(form)
    browser.open('https://sws.rosi.utoronto.ca/sws/timetable/main.do?main.dispatch')
    x =browser.find('table', class_='decorated')
    rows = x.find_all('tr')
    y = [row.findAll('td') for row in rows]
    return y[2][0].text, y[3][0].text
# course_script()

def event_script():
    r = urlopen('https://www.marsdd.com/events/')
    soup = BeautifulSoup(r)
    x = soup.find_all('div', class_='large-8 columns title-box')
    y = soup.find_all('div', class_='large-8 columns info-box')
    # name = [i.find_all('p', class_='event-sponsor') for i in x]

    links = [i.find_all('h5', class_='event-title') for i in x]
    nons = [w.find('a') for z in links for w in z]

    name_text = [x.text for x in nons]
    links_text = [x['href'] for x in nons]
    rest_info = [z.find_all('p') for z in y]
    rest_text = [i for i in rest_info]
    rest_array = [[y.text for y in i] for i in rest_text]

    for i in range(len(links_text)):
        rest_array[i].append(links_text[i])
    major_dict = dict(zip(name_text, rest_array))
    return major_dict
# event_script()

def uoftentrepren_events():
    r = urlopen('http://entrepreneurs.utoronto.ca/entrepreneurshipweek/')
    soup = BeautifulSoup(r)
    x = soup.find_all('table')
    events = [i.findAll('td') for i in x]
    mon = [i for i in events[0]]
    tues = [i for i in events[1]]
    wed = [i for i in events[2]]
    thurs = [i for i in events[3]]
    fri = [i for i in events[4]]
    event_dict = {}
    list_fin = []
    list_fin.extend([mon] + [tues] + [wed] + [thurs] + [fri])
    index = 0
    while index < len(list_fin):
        for i in range(len(list_fin[index])):
            if i % 2==0:
                times = list_fin[index][i]
                names = list_fin[index][i+1]
                event_dict[names.text] = times.text
        index += 1
    return event_dict
# uoftentrepren_events()

def fbevent_script(): #returns last 25 events off fb CSSU page in dict with name + time;
    graph = facebook.GraphAPI(access_token='EAACEdEose0cBADcrUMwKfl8L2q0Lg2JHCh02CoaNIfyx30dw2uC8tW6jNYXFpLgjTUVYOVjTJPrbrkTLXbhfBxUk1Ox2q4pc66qhpJZAQY7RNuJ7uZBlyPwtfZBwWY67fMZATR6AsR4A4TZAL7SxFEYpRtyTZCbhPxxAZAhlw3ZCgbP86iZCDZAoZCb4PbjlC3wwroZD', version='2.2')
    # post = graph.get_object(id='209528585813702/events')
    # feed = graph.get_object(id='209528585813702/feed')
    # ex = graph.get_object(id='209528585813702/events/1858394044444283/')
    page = graph.get_object(id='443810255705810/events')
    events = page['data']
    # {'name': 'CSSU + Connected Lab Hack Night', 'timezone': 'America/Toronto', 'location': 'BA 3200',
    #  'end_time': '2017-03-17T23:00:00-0400', 'id': '158807627970964', 'start_time': '2017-03-17T17:30:00-0400'}
    start_times = [i['start_time'] for i in events]
    name_event = [i['name'] for i in events]
    fin_dic = {}
    index = 0
    for i in start_times:
        y = i.replace('T', ' ')
        y = y.split()
        y[1] = re.sub('[-]\d+', ' ', y[1])
        y[1] = y[1].replace(y[1][5:], '')
        y[1] = time.strptime(y[1], "%H:%M")
        y[1] = time.strftime("%I:%M %p", y[1])
        y[1] = y[1].replace(' ', '')
        y[1] = y[1].strip()
        y[1] = datetime.strptime(y[1], '%I:%M%p').time()
        fin_dic[name_event[index]] = y
        index += 1
    return fin_dic

# x = fbevent_script()
# with open('fbevents.csv', 'w') as csvfile: ## Writing the events to the csv file;
#     writer = csv.writer(csvfile)
#     li = [[key] for key in x]
#     index = 0
#     for k in x.keys():
#         writer.writerows([li[index]])
#         writer.writerows([[x[k][0]]])
#         writer.writerows([[x[k][1]]])
#         index += 1

# fields = ['name', 'date', 'start_time']
# with open('fbevents.csv', 'r') as f:
#     l = f.readlines()
#     i = 0
#     y = 0
#     while i < len(l):
#         if y > 2:
#             y = 0
#         l[i] = l[i].replace('\n', '')
#         w = dict(zip([fields[y]], [l[i]]))
#         print(w)
#         i += 1
#         y += 1

## Converts 24 hour time to 12 hour time;
# timevalue_24hour = '17:00'
# t = time.strptime(timevalue_24hour, "%H:%M")
# timevalue_12hour = time.strftime( "%I:%M %p", t)
# timevalue_123hour = datetime.strptime('1:33PM', '%I:%M%p').time()
# print(timevalue_123hour)
# print(type(timevalue_123hour))


## Script 1:
def uoft_library_search(title):
    chromedriver = '/Users/Rahul/Downloads/chromedriver'
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.set_window_size(1024, 768)
    driver.get('http://search.library.utoronto.ca/index?SearchFilter=6962')
    time.sleep(2)
    search = driver.find_element_by_name('Ntt')
    search.send_keys(title)
    search.submit()
    time.sleep(5)
    y = driver.find_elements_by_class_name('hitlist-item-content')
    print(title)
    for i in y:
        print(i.text)
        print('-----------------------------------------------------------------')

    # x.find_element_by_tag_name('a').click()
    # time.sleep(2)
    # try:
    #
    #     driver.find_element_by_xpath('// *[ @ id = "book_results"] / header / div[1] / h2').click()
    #     time.sleep(3)
    #     x = driver.find_elements_by_class_name('hitlist-title')
    #     titles = [i.text for i in x]
    #     y = driver.find_elements_by_class_name('hitlist-data-wrapper')
    #     print(title)
    #     for i in y:
    #         print(i.text)
    #         print('-----------------------------------------------------------------')
    #
    # except:
    #     print('Not Found')

# uoft_library_search('machine learning')

### TODO: Easy script below, start with this, collect data (IMPT) and then,
##TODO: train a classifier to generate more useful book recommendations and not random ones;
##TODO: Instead of using amazon and wasting time; use stackoverflow csv and hackernews;
## TODO: Have an option to choose between the two or return a random one, if
##TODO I like it, save to current books, if not, show next book;
##TODO: Obv above needs to be checked if UOFT HAS it;

def stackoverflow_book():
    with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_names') as f:
        lines = f.readlines()
        title = lines[random.randrange(0, 101)]
        return title

def hn_book():
    with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/2017_hn.txt', 'r') as f:
        lines = f.readlines()
        title = lines[random.randrange(0, len(lines))]
        return title

def choose_book(): #gets a random book from Stackoverflow/HN and checks uoft library; if both in, returns them
    hn_b = hn_book()
    st_b = stackoverflow_book()
    # uoft_library_search(hn_b)
    uoft_library_search(st_b)

# choose_book()






## Script 2:

def amazon_search(user_search):
    ## randomly select topic from list of topics; search on amazon;
    ## or have a pre-list of topics and choice from that (like the amazon choices);
    ## for now, i just use user_input;
    chromedriver = '/Users/Rahul/Downloads/chromedriver'
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.set_window_size(1024, 768)
    driver.get('https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin')
    time.sleep(2)
    username = driver.find_element_by_id('ap_email')
    password = driver.find_element_by_id('ap_password')
    username.send_keys('duggalr42@gmail.com')
    pswd = getpass.getpass('Password: ')
    password.send_keys(pswd)
    print('Awesome, on sec!')
    password.submit()
    time.sleep(3)
    search = driver.find_element_by_id('twotabsearchtextbox')
    ## list of keywords; and search those;)
    search.send_keys(user_search)
    search.submit()
    time.sleep(3)
    for i in range(10):
        # x = driver.find_element_by_xpath('//*[@id="result_%d"]/div/div/div/div[2]/div[1]/div[1]' % i)
        x = driver.find_element_by_xpath('//*[@id="result_%d"]/div/div/div/div[2]/div[1]/div[1]/a/h2' % i)
        print(x.text)

    ##TODO: there are a lot of different cases that could happen, ads pop up, recom's in between results, etc;
# amazon_search()


def hn_books(): ## scraped off hn;
    url = 'http://hackernewsbooks.com/year/2017'
    soup = BeautifulSoup(urlopen(url))
    title = soup.find_all('h3', class_='title')
    with open('2017_hn.txt', 'w') as f:
        for i in title:
            i = i.text
            i = re.sub('([0-9]\.)', '', i)
            i = re.sub('([0-9])', '', i)
            i = i.strip()
            f.write(i + '\n')

# hn_books()
#
# import sys
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# from PyQt5.QtWebKit import *
# from lxml import html
#
# class Render(QWebPage):
#     def __init__(self, url):
#         self.app = QApplication(sys.argv)
#         QWebPage.__init__(self)
#         self.loadFinished.connect(self._loadFinished)
#         self.mainFrame().load(QUrl(url))
#         self.app.exec_()
#
#     def _loadFinished(self, result):
#         self.frame = self.mainFrame()
#         self.app.quit()
#
# url = 'http://pycoders.com/archive/'
# #This does the magic.Loads everything
# r = Render(url)
# #result is a QString.
# result = r.frame.toHtml()

# import time
# start = time.struct_time()
# print('helo')
# print('helo')
# print('helo')
# print('helo')
# end = time.struct_time()
# x = start - end

# t = time.process_time()
# print('helo')
# print('helo')
# print('helo')
# print('helo')
# elapsed_time = time.process_time() - t
# print(elapsed_time)
#
# from timeit import default_timer as timer
# start = timer()
# print('helo')
# print('helo')
# print('helo')
# print('helo')
# end = timer()
# print(end - start)



