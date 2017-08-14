import numpy as np
import timeit, random
import cProfile
from timeit import Timer

##############################################################################################################
    #RECOMMENDS BOOKS BASED ON THE SIMILARITY OF TITLE: Document Distance Algorithm..
    ##TODO: Next Steps:
    #TIME THIS: I think this is pretty inefficient and could be a lot faster!
    #Think about ways in which I can further improve the accuracy:
        # one of them is to weigh some of the must-reads more than the others; (see Chp.7(ML) classification imbalance..)
    #Time the algorithm and think about ways to improve it; Measure ratio of 1.0MB file and get it to the lowest possible sec possible;

## Function Timings: O(n) Time;
# 1152522 function calls in 6.461 seconds <-- 300 Books
# 768346 function calls in 4.604 seconds <-- 200 Books
# 384196 function calls in 2.410 seconds <-- 100 Books
# 192115 function calls in 1.102 seconds <-- 50 Books
##############################################################################################################

def hn_raw_data():
    with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/2017_hn.txt') as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines]
        return lines

def st_raw_data():
    with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/book_names') as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines[:50]]
        return lines

def parse_gen(lines):
    ran = [':', '.', 'Edition', '(', ')', ',', '-', '&']
    rn = ['nd', 'rd', 'th']
    new_lines = []
    for line in lines:
        for i in ran:
            if i in line:
                line = line.replace(i, '')
        y = line.split()
        for w in y:
            if w in rn:
                y.remove(w)
        new_lines.append(y)
    return new_lines

def get_ratings():
    with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/book_rating') as b:
        rating_lines = b.readlines()
        ratings = []
    for i in rating_lines:
        i = i.replace('\n', '')
        i = i.split()
        ratings.append(i[-1])
    return ratings

def vocab_set(data):
    new_set = set([])
    for w in data:
        new_set = new_set | set(w)
    return list(new_set)

def bag_of_words(vocabSet, row):
    returnVec = [0] * len(vocabSet)
    for word in row:
        if word in vocabSet:
            returnVec[vocabSet.index(word)] += 1
    return returnVec

def cosine_similarity(x1, x2): # used the bag-of-model with cosine similarity approach;
    vec1 = np.array(x1)
    vec2 = np.array(x2)
    dot = np.dot(vec1, vec2)
    magnitude1 = np.linalg.norm(vec1)
    magnitude2 = np.linalg.norm(vec2)
    if magnitude1 != 0 and magnitude2 != 0:
        return (dot / (magnitude1 * magnitude2))
    return 'With our data, I cannot come up with a rating...'

##Combining a bit of st and hn;
raw_data_clean = parse_gen(hn_raw_data())
st_clean_data = parse_gen(st_raw_data())
raw_data_clean.extend(st_clean_data)
vocab_list = vocab_set(raw_data_clean)
raw_bag_of_words = [bag_of_words(vocab_list, i) for i in raw_data_clean]

def rating_prompt(data): #get ratings of the books;
    # data = raw_data_clean[110:]
    with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/book_rating', 'a') as f:
        for i in range(len(data)):
            x = ' '.join(data[i])
            print(x)
            s = int(input('Enter a rating (based on title, 1 to 5): '))
            f.write(x + ' ' + str(s) + '\n')

def recomennder_prompt(line):
    ratings = get_ratings()
    t1 = bag_of_words(vocab_list, line)
    w = [cosine_similarity(i, t1) for i in raw_bag_of_words]
    for i in w:
        if type(i) == str:
            return 'With our data, I cannot come up with a rating...'
    print(len(w), len(ratings))
    # assert len(w) == len(ratings)
    y = [w[i]*int(ratings[i]) for i in range(len(ratings))]
    return sum(y) / sum(w)

def train_recommender(): #this compares the ratings of the 50 stackoverflow books with my actual ratings of the books;
    ##20% Error rate...but, anything over the rating (even by +/- 0.5 isn't included...);
    test1 = st_raw_data()
    test1 = parse_gen(test1)
    with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/book_rating') as b:
        lines = b.readlines()
        lines = [line.replace('\n', '') for line in lines]
        ratings = []
        for i in lines:
            i = i.replace('\n', '')
            i = i.split()
            ratings.append(i[-1])
    ratings1 = ratings[100:]
    assert len(test1[:-1]) == len(ratings1)
    error_count = 0
    for t in range(len(ratings1)):
        x = recomennder_prompt(test1[t])
        print(range((int(ratings1[t]) -1), (int(ratings1[t]) + 1)))
        print(int(x))
        if int(x) not in range((int(ratings1[t]) -1), (int(ratings1[t]) + 1)):
            error_count += 1
        print('Recommender says: ', x, 'Actual Rating: ', ratings1[t])
    print(error_count/len(ratings1))
#train_recommender()


def test_rec(data): #
    '''Takes Data as Input; Test's the data that doesn't have ratings'''
    for i in data:
        x = recomennder_prompt(i)
        if x == 'With our data, I cannot come up with a rating...':
            with open("can't_classify.txt", 'a') as b:
                b.write(' '.join(i) + '\n')
        else:
            with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/book_rating', 'a') as f, open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/book_names', 'a') as b:
                f.write(' '.join(i) + ' ' + str(int(x)) + '\n')
                b.write(' '.join(i) + '\n')
    # with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/test_alg.txt') as f:
    #     lines = f.readlines()
    #     lines = [line.replace('\n', '') for line in lines]
    # test_data = parse_gen(lines)
    # cannot_classify = [] #keep track of the books it can't classify;
    # for i in test_data:
    #     x = recomennder_prompt(i)
    #     print('Title of Book: ' + '"' + ' '.join(i) + '"')
    #     if x == 'With our data, I cannot come up with a rating...':
    #         cannot_classify.append(' '.join(i))
    #     print('Rating is: ' , x) ##Rating is pretty accurate!

# cProfile.run('test_rec()')

## All the Test Data should be in test_alg.txt file!
## Once Data is Tested and added to the new text file, the test_alg.txt is deleted.
def generate_ratings(filename): #90% of ratings generated from test_rec() and 10% from me;
    with open(filename) as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines]
    data = parse_gen(lines)
    h = int(len(data) * 0.10)
    my_data = data[:h]
    test_data = data[h:]
    ## Make sure the data that I am rating is written into the book names file!
    # with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/book_names', 'a') as f:
    #     for i in my_data:
    #         f.write(' '.join(i) + '\n')
    test_rec(test_data[2])
    test_rec(test_data)
    print('Done')
    # rating_prompt(my_data)
# generate_ratings('test_alg.txt')

# r = get_ratings()
# print(len(r))


##Django: Button 1
def get_recommendation(title): #enter a random title and get a recommendation;
    try:
        t = title.split()
    except:
        print('Enter a Title (No Author as of now..)')
    x = recomennder_prompt(t)
    with open('/Users/Rahul/Desktop/Side_projects/project_2/lifeline/Scripts/book_rec/get_recommendation', 'a') as f:
        f.write(title + ': ' + str(x) + '\n')
    print('According to my guess, I think you would rate,', title + '-->', int(x))

##Django: Button 2
def get_random_book(): #get a random book that the system thinks you will like;
    while True:
        a = raw_data_clean[random.randrange(len(raw_data_clean)-1)]
        x = recomennder_prompt(a)
        # return "I Recommend:" + ' ' + ' '.join(a) + ' ' + str(int(x))
        if int(x) >= 4:
            print('We Recommend: ' + '"' + ' '.join(a) + '"', 'Rating:', int(x))
            break

## Used to Time Functions:
# cProfile.run('get_random_book()')

# if __name__ == '__main__':
#     get_random_book()


