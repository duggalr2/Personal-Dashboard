import random, cProfile
from cosine_similarity import CosineSimilarity

####################################################################################
                # RECOMMENDS BOOKS BASED ON THE SIMILARITY OF TITLE
####################################################################################

# TODO: GET SUMMARY OF BOOKS; DO COSINE SIMILARITY
# TODO: Implement a clustering algorithm to see if I can use genre as a well

def get_raw_data(filename):
    """
    Get Raw Data for a File
    """
    with open(filename) as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines]
        return lines

def parse_lines(lines):
    # TODO: Fix this function, make it more efficient...
    """
    Remove all Punctuation and Common Words
    """
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
    # new_lines = [[y.replace(line, '') for y in line if len(y) <= 2] for line in new_lines]
    new_lines = [[y for y in line if len(y) > 3] for line in new_lines]
    new_lines = [list(set(line)) for line in new_lines] #remove duplicates..
    return new_lines

# Initialized Global Variables for program to run faster..
x = CosineSimilarity()
raw_data = parse_lines(get_raw_data('new_book_file'))
print(raw_data)
# ratings = x.get_ratings('book_rating')
# vocabSet = x.vocabSet(raw_data)
# wordVectors = [x.bag_of_words(vocabSet, i) for i in raw_data]
# test_raw_data = raw_data[:10]
# test_vocab_set = x.vocabSet(test_raw_data)
# test_word_vectors = [x.bag_of_words(test_vocab_set, i) for i in test_raw_data]
# t1_test = x.tf_idf1(test_word_vectors, test_vocab_set)
# print(test_raw_data)
# print(test_vocab_set)

def getRecommendation():
    """
    Calculate's a rating by randomly selecting a title from Parsed Data;
    Return's if rating >= 3
    """
    t3 = x.tf_idf3(wordVectors, vocabSet)
    while True:
        a = raw_data[random.randrange(len(raw_data) - 1)]
        r = x.calculate_rating(a, ratings, t3, vocabSet, alg=3)
        if int(r) >= 3:
            return 'We Recommend: ' + '"' + ' '.join(a) + '"' + ' ' + 'Rating:' + ' ' + str(r)

def main_prompt(wordVec, i=0):
    """
    Return's a rating from the recommender system by entering a title
    """
    print(
        'To ensure this goes smoothly, make sure the weightings you used for your wordVectors is the same as i')
    print('Ex: If you are using tf-idf2, i should equal 2')
    ran = input('Press enter to continue...')
    while True:
        s = input('Enter a title (to exit, type: "done"): ')
        if s == 'done' or s == '':
            break
        s = s.split()
        w = []
        w.append(s)
        r = x.calculate_rating(w, ratings, wordVec, vocabSet, alg=i)
        print('I predict you will give this book a...', r)

def time_function():
    """
    Calculate the timing's of particular functions
    """
    cProfile.run('train_recommender()')
    cProfile.run('main_prompt(t3_wordVectors, i=3)')

# if __name__ == "__main__":
#     # t1_wordVectors = x.tf_idf1(wordVectors, vocabSet)
#     # err_t1 = x.testRecommenderExisting(raw_data, ratings, t1_wordVectors, vocabSet, num=3)
#     # t2_wordVectors = x.tf_idf2(wordVectors, vocabSet)
#     # err_t2 = x.testRecommenderExisting(raw_data, ratings, t2_wordVectors, vocabSet, num=3)
#     t3_wordVectors = x.tf_idf3(wordVectors, vocabSet)
#     main_prompt(t3_wordVectors, i=3)
    # err_t3 = x.testRecommenderExisting(raw_data, ratings, t3_wordVectors, vocabSet, num=3)
    # print(err_t3)