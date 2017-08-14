# from bs4 import BeautifulSoup
# import urllib
# from urllib.request import urlopen
# from IPython.display import Image
# from IPython.display import HTML



# Scraping puzzles

# r = urlopen('http://www.puzzle.dse.nl/arith/index_us.html')
# soup = BeautifulSoup(r)
# table = soup.find_all('table', class_='puzzle')
#
# with open ('new_random.csv', 'w', newline='') as csvfile:
#     for r in table:
#         tg = r.find_all('td', class_='pt ka')
#         rg = r.find_all('p', class_='qt')
#         for t, s in zip(tg, rg):
#             csvfile.write('%s, %s' % (t.text, s.text))

# Scraping Quotes

# q = urlopen('https://www.goodreads.com/quotes/tag/philosophy')
# soup = BeautifulSoup(q)
# div_q = soup.find_all('div', class_='quoteText')
# #
# with open('quotes3.csv', 'w') as csvfile:
#     for r in div_q:
#         csvfile.write(r.text)



# q = urlopen('https://www.goodreads.com/author/quotes/23551.Paul_Graham')
# soup = BeautifulSoup(q)
# div_q = soup.find_all('div', class_='quoteText')
# with open ('quotes_pg.csv', 'w') as csvfile:
#     for r in div_q:
#         csvfile.write(r.text)



# TODO: NEED TO FIGURE OUT WAY TO REMOVE WHITE LINES/NEW LINES IN FILE, REPLACE ISN"T WORKING FOR SOME REASON

import re
from string import whitespace


# q = urlopen('https://www.goodreads.com/author/quotes/23551.Paul_Graham')
# soup = BeautifulSoup(q)
#
# # this extracts all the script stuff from the webpage!
# [x.extract() for x in soup.find_all('script')]
#
# [y.extract() for y in soup.find_all('a')]
#
# div_q = soup.find_all('div', class_='quoteText')
#
#
# # with open('quotes_pg.csv', 'w') as csvfile:
# #     for r in div_q:
# #         #regular expression that removes whitespace
# #         # r = (r.get_text).replace('-', '')
# #         # r = r.replace(re.sub(r'/[^a-z0-9-]/g', '', r.text))
# #         csvfile.write(re.sub(r'\n\s*\n', r'\n\n\n', r.get_text().strip(), flags=re.M))
#
#
# # Replacing '-' with nothing; fileinput is a reallly good library!
import fileinput
# for line in fileinput.FileInput('quotes_pg.csv',inplace=1):
#         print (line.replace('-','').rstrip())

# method rstrip() returns a copy of the string in which all chars have been stripped from the end of the string

# q = urlopen('https://www.goodreads.com/quotes/tag/knowledge')
# soup = BeautifulSoup(q)
#
# [x.extract() for x in soup.find_all('script')]
# [x.extract() for x in soup.find_all('a')]
#
# div_knowledge = soup.find_all('div', class_='quoteText')
#
# with open('quotes3.csv', 'w') as randfile:
#         for know in div_knowledge:
#                 randfile.write(re.sub(r'\n\s*\n', r'\n\n\n', know.get_text().strip(), flags=re.M))
# randfile.close()
#
# for line in fileinput.FileInput('quotes3.csv', inplace=1):
#         print (line.replace(',','').rstrip())


# q = urlopen('http://calendar.artsci.utoronto.ca/crs_csc.htm#courses')
# # soup = BeautifulSoup(q)
# #
# # [x.extract() for x in soup.find_all('span')]
# #
# # a_course = soup.find_all('a')

# with open('uoft_courses.csv', 'w') as uoftfile:
#     for course in a_course:
#         print(course)


# TODO: NEED TO FIGURE THIS OUT!
# with open('uoft_courses.csv', 'w') as uoftfile:
#     for cs in a_course:
#         uoftfile.write(re.sub(r'<\S\D\w+=.[abc]\w+\w[abc][.]\w+[#]\w+["][>]\w+[<][/]\w+[>]', '', cs.text))
# #         csvfile.write(re.sub(r'\n\s*\n', r'\n\n\n', r.get_text().strip(), flags=re.M))








