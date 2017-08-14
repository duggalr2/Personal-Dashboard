import facebook
from bs4 import BeautifulSoup
from urllib.request import urlopen

def uoft_events():
    soup = BeautifulSoup(urlopen('https://www.utoronto.ca/events'))
    x = soup.find_all('table')
    w = soup.find_all('tr')
    z = soup.find_all('td', class_='views-field views-field-title views-align-left') #link + name
    a = soup.find_all('td', class_='views-field views-field-field-eventdate') #date
    for i in range(5):
        del z[0]
    titles = [y.text.replace('\n', '') for y in z]
    links = [y.find('a', href=True)['href'] for y in z]
    final_li = list(zip(titles, links))
    return final_li

def uoft_eng():
    url = 'http://www.engineering.utoronto.ca/engineering-events/'
    soup = BeautifulSoup(urlopen(url))
    x = soup.find_all('div', class_='col-lg-3 col-md-3 col-sm-6 col-xs-6 eventContainer')
    titles = [i.find('h4').text for i in x]
    dates = [i.find('p').text for i in x]
    return list(zip(titles, dates))

def uoft_cs():
    url = 'http://web.cs.toronto.edu/news/events.htm'
    soup = BeautifulSoup(urlopen(url))
    x = soup.find_all('td', class_='ipf-calendar-nongraphical-event-tdright')
    t = soup.find_all('td', class_='ipf-calendar-nongraphical-event-tdleft')
    dates = [i.text.replace('\n', '') for i in t]
    titles = [x[i].text for i in range(len(x)) if i % 2]
    links = [x[i].find('a')['href'] for i in range(len(x)) if i % 2 == 0]
    fi = list(zip(titles, links, dates))
    return fi

def facebook_events(page_id):
    graph = facebook.GraphAPI(
        access_token='EAACEdEose0cBABdqtQpGQFp6CIw4q627bi4lMPMTEMmBvaUanz8ZCyFQHBJRelbb2Rd5B2XtOsHcIZCnU12270ZBaAIEUTrOAZCQg6wULVx5ozPaEFAMXezrgbfHRQ2BZCPkEgySupJZC6oIt2oIbD9MiZAMbqAjpstZCuZBzEcqRZCoFXv6ZBfoUdqMV3MGnQLP1sZD',
        version='2.2')
    page = graph.get_object(id=page_id+'/events')
    events = page['data']
    start_times = [i['start_time'] for i in events]
    name_event = [i['name'] for i in events] ##times not in sql time format;
    return list(zip(name_event, start_times))

def facebook_pg():
    li = ['UofTCompSci', 'MaRSCentre']
    x = facebook_events(li[0])
    y = facebook_events(li[1])


##TODO: BELOW IS HOW YOU ADD AUTOMATIC SCHEDULING; (implement this after everything is complete)
    #TODO: threading will definitely be used for fb; need to get pernament fb token;
# import schedule
# import time
#
# def job():
#     print("I'm working...")
#
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
#
# while 1:
#     schedule.run_pending()
#     time.sleep(1)