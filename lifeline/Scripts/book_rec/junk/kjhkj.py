import getpass, random
from pprint import pprint
import time, re, os, json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

##TODO: MOST IMPT: NEED TO FIND A BETTER WAY THAN SELENIUM TO COMPLETE THE FUNCTIONALITY!

### TODO: Easy script below, start with this, collect data (IMPT) and then,
##TODO: train a classifier to generate more useful book recommendations and not random ones;
##TODO: Instead of using amazon and wasting time; use stackoverflow csv and hackernews;
## TODO: Have an option to choose between the two or return a random one, if
##TODO I like it, save to current books, if not, show next book;
##TODO: Obv above needs to be checked if UOFT HAS it;

chromedriver = '/Users/Rahul/Downloads/chromedriver'
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.set_window_size(1024, 768)


## Script 1:
def uoft_library_search(title):
    driver.get('http://search.library.utoronto.ca/index?SearchFilter=6962')
    time.sleep(2)
    search = driver.find_element_by_name('Ntt')
    search.send_keys(title)
    search.submit()
    time.sleep(5)
    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_element_located((By.ID, "num-records")))
    num_records = driver.find_element_by_id('num-records').text
    num_records = num_records.split()
    grouped_record_links = []
    book_dict = {}

    if int(num_records[0]) == 0:
        choose_book()

    else:
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "hitlist-data-wrapper")))
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "hitlist-title")))
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "hitlist-holdings")))

            y = driver.find_elements_by_class_name('hitlist-item-content')

            for i in y:
                try:
                    x = i.find_element_by_class_name('hitlist-title')
                    z = i.find_element_by_class_name('hitlist-holdings')
                    z = (z.text).replace('\n', ' ')
                    book_dict[x.text] = [z] ##dict of book title and holding info
                except:
                    w = i.find_elements_by_tag_name('a')
                    grouped_record_links.append(w[1])
        except:
            choose_book()

    if len(book_dict) == 0:
        choose_book()

    return book_dict

def stackoverflow_book():
    with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/book_names') as f:
        lines = f.readlines()
        title = lines[random.randrange(0, len(lines))]
        return title

def hn_book():
    with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/2017_hn.txt', 'r') as f:
        lines = f.readlines()
        title = lines[random.randrange(0, len(lines))]
        return title

def choose_book(): #gets a random book from Stackoverflow/HN and checks uoft library; if both in, returns them
    hn_b = hn_book()
    hn_b = hn_b.replace('\n', '')
    x1 = uoft_library_search(hn_b)
    st_b = stackoverflow_book()
    st_b = st_b.replace('\n', '')
    x2 = uoft_library_search(st_b)
    return x1, x2

def save():
    with open("book_db.txt",'a') as f:
        for i in range(2):
            hn_info, st_info = choose_book()
            json.dumps([hn_info, st_info], f)
            f.write('\n')
        print('Done')
save()

##TODO: SAVE THE FIRST 5 BOOKS WITH HOLDING INFO IN TXT FILE.....

def book_prompt():
    ##TODO: Delete the Yes's from the original file; <--create a separate function for this;
    while True:
        d = json.loads(open('book_db.txt'))
        print(d)
        break
        # pprint(hn_info)
        # pprint(st_info)
        # with open('book_data_collection.txt') as f:
        #     try:
        #         user_choice = int(input('Enter 1 or 2 if you like a book or enter any letter to continue.. '))
        #         if user_choice == 1:
        #             for i in hn_info:
        #                 f.write(i + ' YES')
        #         elif user_choice == 2:
        #             for i in st_info:
        #                 f.write(i + ' NO')
        #     except:
        #         print('Okay, choosing next...')
        #         continue

# book_prompt()