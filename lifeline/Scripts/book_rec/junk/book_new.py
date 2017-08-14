import os, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from urllib.request import urlopen


# chromedriver = '/Users/Rahul/Downloads/chromedriver'
# os.environ["webdriver.chrome.driver"] = chromedriver
# driver = webdriver.Chrome(chromedriver)
# driver.set_window_size(1024, 768)

# def uoft_library_url(title):
#     driver.get('http://search.library.utoronto.ca/index?SearchFilter=6962')
#     time.sleep(2)
#     search = driver.find_element_by_name('Ntt')
#     search.send_keys(title)
#     search.submit()
#     wait = WebDriverWait(driver, 15)
#     wait.until(EC.presence_of_element_located((By.ID, "num-records")))
#     return driver.current_url


# with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/book_names') as f, open(
#         '/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/2017_hn.txt') as b, open(
#     '/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/book_url', 'a') as w:
#     st_lines = f.readlines()
#     hn_lines = b.readlines()
#     st = [line.replace('\n', '') for line in st_lines]
#     hn = [line.replace('\n', '') for line in hn_lines]
#     for i in range(5, 51):
#         x = uoft_library_url(st[i])
#         y = uoft_library_url(hn[i])
#         w.write(x)
#         w.write('\n')
#         w.write(y)
#         w.write('\n')

##TODO: SEND URLS TO PARSE AND SAVE IN TXT FILE;

import json
def url_parse(url):
    soup = BeautifulSoup(urlopen(url))
    t = soup.find_all('div', class_='hitlist-data-wrapper')
    title = {}
    holding_info = []
    with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/info', 'a') as f:
        for i in t:
            x = i.find('div', class_='hitlist-title').text
            x = x.replace('\n', '')
            y = soup.find('div', class_='hitlist-holdings').text
            y = y.replace('\n', '')
            title[x] = [y]
        json.dump(title, f)
        f.write('\n')

# print(url_parse('http://search.library.utoronto.ca/search?N=6962&Ntx=mode+matchallpartial&Nu=p_work_normalized&Np=1&Ntt=Code%20Complete%20(2nd%20edition)%20by%20Steve%20McConnell&Ntk=Anywhere'))


def url():
    with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/book_url') as f:
        lines = f.readlines()
        for i in lines[:20]:
            i = i.replace('\n', '')
            url_parse(i)
url()

# with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/info') as f:
#     lines = f.readlines()
#     print(lines[1])








# def rating_prompt(data):
#     """I rate books on a scale of 1 to 5; List of titles as input"""
#     with open('book_rating', 'a') as f, open('new_book_file', 'a') as b:
#         for i in range(len(data)):
#             x = ' '.join(data[i])
#             print(x)
#             s = int(input('Enter a rating (based on title, 1 to 5): '))
#             b.write(x + '\n')
#             f.write(x + ' ' + str(s) + '\n')
#
# def get_raw_ratings():
#     """Retrieve all the Ratings of the Book's that are rated; Book_Rating File"""
#     with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/book_rating') as b:
#         rating_lines = b.readlines()
#         ratings = []
#     for i in rating_lines:
#         i = i.replace('\n', '')
#         i = i.split()
#         ratings.append(i[-1])
#     return ratings
#
# def vocab_set(data):
#     """Create a Vocab Set; Data from New_Book_file"""
#     new_set = set([])
#     for w in data:
#         new_set = new_set | set(w)
#     return list(new_set)
#
# def bag_of_words(vocabSet, row):
#     """Create's Word Vector using a Bag of Word Approach from VocabSet and a Title"""
#     returnVec = [0] * len(vocabSet)
#     for word in row:
#         if word in vocabSet:
#             returnVec[vocabSet.index(word)] += 1
#     return returnVec
#
# def cosine_similarity(x1, x2):
#     """Calculate's Cosine Similarity"""
#     vec1 = np.array(x1)
#     vec2 = np.array(x2)
#     dot = np.dot(vec1, vec2)
#     magnitude1 = np.linalg.norm(vec1)
#     magnitude2 = np.linalg.norm(vec2)
#     if magnitude1 != 0 and magnitude2 != 0:
#         return (dot / (magnitude1 * magnitude2))
#     return 'With our data, I cannot come up with a rating...'
#
# def get_rating(line, wordVectors, vocabSet):
#     """Calculate's the Rating of a Book; Input: Title, Bag of Words, Vocab Set"""
#     ratings = get_raw_ratings()
#     t1 = bag_of_words(vocabSet, line)
#     w = [cosine_similarity(i, t1) for i in wordVectors]
#     for i in w:
#         if type(i) == str:
#             return 'With our data, I cannot come up with a rating...'
#     assert len(w) == len(ratings)
#     y = [w[i]*int(ratings[i]) for i in range(len(ratings))]
#     return sum(y) / sum(w)
#
# # Initialize Global Variables to Save Time
# raw_data = parse_lines(get_raw_data('new_book_file'))
# vocabSet = vocab_set(raw_data)
# wordVectors = [bag_of_words(vocabSet, i) for i in raw_data]
#
# def train_recommender():
#     """Test's the with book's that already have ratings to see an approximate error rate; 80%/20%"""
#     rating = get_raw_ratings()
#     h = int(len(raw_data)*0.2)
#     test_data = raw_data[:h]
#     error_count = 0
#     for i in range(len(test_data)):
#         x = get_rating(test_data[i], wordVectors, vocabSet)
#         # print('Recommender gives: ', int(x), 'Actual Rating: ', rating[i])
#         if int(x) not in range(int(rating[i])-1, int(rating[i])+2):
#             error_count += 1
#     return error_count / len(test_data)
#
# def test_rec(data):
#     """Test's the data that doesn't have ratings; Takes List of Titles as Input"""
#     for i in data:
#         x = get_rating(i, wordVectors, vocabSet)
#         if x == 'With our data, I cannot come up with a rating...':
#             with open("can't_classify.txt", 'a') as b: #Keep track of the title's that can't be classified
#                 b.write(' '.join(i) + '\n')
#         else:
#             print(' '.join(i), 'Rating: ', x)
#
# def generate_ratings():
#     """
#     Looks at the Title to Rate File; 50% of Data is manually Rated, 50% is based of previous rating's
#     Put's the Title both into New Book File and Book Rating
#
#     """
#     titles_to_generate = get_raw_data('title_to_rate')
#     titles_to_generate = parse_lines(titles_to_generate)
#     h = int(len(titles_to_generate)*0.50)
#     manual_data = titles_to_generate[:h]
#     rest_data = titles_to_generate[h:]
#     rating_prompt(manual_data)
#     print('Done the Manual Rating...')
#     with open('book_rating', 'a') as f, open('new_book_file', 'a') as b:
#         for i in rest_data:
#             rec = get_rating(i, wordVectors, vocabSet)
#             if rec != 'With our data, I cannot come up with a rating...':
#                 x = ' '.join(i)
#                 b.write(x + '\n')
#                 f.write(x + ' ' + str(int(rec)) + '\n')
#     print('Done!')
#     with open('title_to_rate', 'w'): #empty the title_to_rate file
#         pass



#
#
# if __name__ == '__main__':
#     print(get_recommendation())












############################################
    #DON'T WORRY ABOUT THE STUFF BELOW...
############################################

# def lkj():
#     '''Don't Worry about this, I just had to create it because I messed up before'''
#     with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/book_rating') as b:
#         r = b.readlines()
#     rating = []
#     for i in r:
#         i = i.replace('\n', '')
#         i = i.split()
#         rating.append(i[:-1])
#
#     with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/new_book_file', 'a') as f:
#         for i in rating:
#             f.write(' '.join(i) + '\n')
#
#
# def hn_raw_data():
#     with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/2017_hn.txt') as f:
#         lines = f.readlines()
#         lines = [line.replace('\n', '') for line in lines]
#         return lines
#
# def st_raw_data():
#     with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/book_names') as f:
#         lines = f.readlines()
#         lines = [line.replace('\n', '') for line in lines]
#         return lines
#
# def remove_duplicate():
#     '''Returns all Non-Duplicates from HN and ST File (I messed it up before, ignore this...)'''
#     hn = get_raw_data('2017_hn.txt')
#     st = get_raw_data('book_names')
#     actual = get_raw_data('new_book_file')
#     hn = parse_lines(hn)
#     st = parse_lines(st)
#     non_duplicates = []
#     for i in st:
#         x = ' '.join(i)
#         if x not in actual:
#             # non_duplicates.append(i)
#             with open('new_book_file', 'a') as b:
#                 b.write(x + '\n')
#     for i in hn:
#         x = ' '.join(i)
#         if x not in actual:
#             # non_duplicates.append(i)
#             with open('new_book_file', 'a') as b:
#                 b.write(x + '\n')
#     # return non_duplicates






# def rating_prompt(filename):
#     """I rate people on a scale of 1 to 5; 2D List of Names/Urls as Input"""
#     lines = parse_file(filename)
#     for i in lines:
#         print(i)
#     # with open('linkedin_rating.txt', 'w') as f:
#     #     for line in lines[:40]:
#     #         line = ' '.join(line)
#     #         print(line)
#     #         s = int(input('Enter a rating (based on title, 1 to 5): '))
#     #         f.write(line + ' ' + str(s) + '\n')
#
# rating_prompt('linkedin_rec_people.txt')
#
# def get_ratings():
#     """Retrieve all the Ratings of the Linkedin People that are rated; Linkedin Rating File"""
#     with open('linkedin_rating.txt') as f:
#         lines = f.readlines()
#     lines = [line.replace('\n', '') for line in lines]
#     rating = [int(line[-1]) for line in lines]
#     return rating
#
# def vocab_set(data):
#     """Create a Vocab Set; Data from Linkedin Rating File"""
#     assert type(data) == list
#     new_set = set([])
#     for i in data:
#         new_set = new_set | set(i)
#     y = list(new_set)
#     for i in ['at', 'in', 'a', 'better', 'of', 'is', '|', '@', 'LLC']:
#         if i in y:
#             x = y.index(i)
#             del y[x]
#     return y
#
# def bag_of_words(vocabSet, row):
#     """Create's Word Vector using a Bag of Word Approach from VocabSet and a Title"""
#     returnVec = [0] * len(vocabSet)
#     for word in row:
#         if word in vocabSet:
#             returnVec[vocabSet.index(word)] += 1
#     return returnVec
#
# def cosine_similarity(x1, x2):
#     """Calculate's Cosine Similarity"""
#     vec1 = np.array(x1)
#     vec2 = np.array(x2)
#     dot = np.dot(vec1, vec2)
#     magnitude1 = np.linalg.norm(vec1)
#     magnitude2 = np.linalg.norm(vec2)
#     if magnitude1 != 0 and magnitude2 != 0:
#         return (dot / (magnitude1 * magnitude2))
#     return 'With our data, I cannot come up with a rating...'
#
#
#
# # input_data, ratings = get_clean_data('linkedin_rec_people.txt'), get_ratings()
# # print(len(input_data), len(ratings))
# # Initialize Global Variables to Save Time
# # input_data, ratings = get_clean_data('linkedin_rating.txt')
# # assert len(ratings) == len(input_data)
# # vocab_list = vocab_set(input_data)
# # input_bag_of_words = [bag_of_words(vocab_list, i) for i in input_data]
#
#
#
#
# def parse_url(url):
#     """Input: URL; Output: A list title with person's description"""
#     # TODO: CHANGE THE PASSWORD WAY!!!
#     result = requests.get('https://www.linkedin.com/', auth=HTTPBasicAuth('duggalr42@gmail.com', 'Umakant12'))
#     result = requests.get('https://www.linkedin.com/in/alex-cui-aa679974/')
#     print(result.content)
# # parse_url('https://www.linkedin.com/in/alex-cui-aa679974/')
#
#
# def get_recommendation(line):
#     """Calculate's the Rating of a Person; Input: Url, Bag of Words, Vocab Set"""
#     t1 = bag_of_words(vocab_list, line)
#     w = [cosine_similarity(i, t1) for i in initial_data_bag_of_words]
#     for i in w:
#         if type(i) == str:
#             return 'With our data, I cannot come up with a rating...'
#     y = [w[i]*int(ratings[i]) for i in range(len(ratings))]
#     return sum(y) / sum(w)
#
# def test_recommender():
#     for i in range(len(description_data)):
#         x = get_recommendation(description_data[i])
#         print('Recommender gives: ', x, 'Actual Rating: ', ratings[i])
#
# def get_rec_title(li):
#     assert type(li) == list
#     name = li[:2]
#     li = li[2:-1]
#     x = get_recommendation(li)
#     return 'Name: ', ' '.join(name), 'Recommender gives: ', x
#
# def get_random_rec():
#     y = random.randrange(len(description_data)-1)
#     x = description_data[y]
#     w = initial_data[y]
#     name, link = w[:2], w[-2]
#     rec = get_recommendation(x)
#     return 'Recommender recommendes: ' + ' '.join(name) + ': ' + link + ' ' + 'with rating: ' + ' ' + str(int(rec))

# get_random_rec()
# get_rec_title(['John', 'Aloi', 'Associate', 'Professor', 'Teaching', 'Stream', 'https://www.linkedin.com/in/diane-horton-503402a/'])
# get_rec_title(['John', 'Aloi', 'Google', 'Software', 'Engineer', 'https://www.linkedin.com/in/diane-horton-503402a/'])




