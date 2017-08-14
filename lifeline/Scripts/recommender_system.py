from cosine_similarity import CosineSimilarity

########################################
# General Recommender System
########################################

# TODO: NOT USING THIS RIGHT NOW... DECIDED TO MAKE A LOCAL REC SYSTEM INSTEAD BECAUSE ABSTRACT WOULD TAKE A LOT OF TIME

# TODO: Make this abstract enough to handle any data structure (main commmon ones..)
# TODO: Fix the docstrings


class RecommenderSystem(object):
    """
    Text-based Recommender System using Cosine Similarity
    """

    def __init__(self):
        pass
    #
    # def rating_prompt(self):
    #     """
    #     Ask's the user questions about what they would rate certain profiles;
    #     Allow's the recommender system to understand what type of profiles user likes
    #     """
    #     if self.type == list:
    #         pass
    #     elif self.type == dict:
    #         pass
    #     else:
    #         return "Sorry, we only support list's and dict's"
    #     # assert type(data) == list
    #     #
    #     # if file2 != None:
    #     #     with open(file1, 'a') as f, open(file2, 'a') as b:
    #     #         for i in range(len(data)):
    #     #             x = ' '.join(data[i])
    #     #             print(x)
    #     #             s = int(input('Enter a rating (based on title, 1 to 5): '))
    #     #             b.write(x + '\n')
    #     #             f.write(x + ' ' + str(s) + '\n')
    #     #
    #     # else:
    #     #     with open(file1, 'a') as f:
    #     #         for i in range(len(data)):
    #     #             x = ' '.join(data[i])
    #     #             print(x)
    #     #             s = int(input('Enter a rating (based on title, 1 to 5): '))
    #     #             f.write(x + ' ' + str(s) + '\n')
    #
    # def get_ratings(self):
    #     """
    #     """
    #     pass
    #
    # def generate_ratings(self):
    #     """
    #     """
    #     pass

    def calculate_rating(self, line, ratings, wordVectors, vocabSet, alg=0):
        """
        (To get best results, make sure you are consistent with the algoirthm choice
        ie. If wordVectors is using tf-idf3 weight, the title should also be using the same weighting...)
        Calculate's Rating of a Book;
        Parameter: -Line (what you want to get the rating of) must a be list
                   -Ratings: List of get ratings function
                   -Bag of Words: from bag of words function
                   -Vocab Set: from vocabSet function
                   -alg: default is bag of words using no tf-idf weighting
        """
        data_type = type(line)
        if data_type == list:
            t1 = [c.bag_of_words(vocabSet, i) for i in line]
            # t1 = self.bag_of_words(vocabSet, line)
            if alg == 1:
                t1 = c.tf_idf1(t1, vocabSet)
            elif alg == 2:
                t1 = c.tf_idf2(t1, vocabSet)
            elif alg == 3:
                t1 = c.tf_idf3(t1, vocabSet)
            t1 = [y for i in t1 for y in i]
            w = [c.cosine_similarity(i, t1) for i in wordVectors]
            for i in w:
                if type(i) == str:
                    return 'With our data, I cannot come up with a rating...'
            assert len(w) == len(ratings)
            y = [w[i] * ratings[i] for i in range(len(ratings))]
            return sum(y) / sum(w)
        elif data_type == dict:
            pass



    def test_recommender(self, data, ratings, wordVectors, vocabSet, num=0):
        """
        Return's Training error rate of Recommender System using existing Ratings File
        Train Data: 80% / Test Data: 20%
        Error Rate Calculation: Accepts a rating +/-1 of actual rating
        Parameter: -Parsed Data (needs to be in format of what you want rated!)
                   -Ratings: from get ratings function
                   -Bag of Words: from bag of words function
                   -Vocab Set: from vocabSet function
        """
        h = int(len(data) * 0.2)
        test_data = data[:h]
        error_count = 0
        test_data = [[i] for i in test_data]
        for i in range(len(test_data)):
            x = self.calculate_rating(test_data[i], ratings, wordVectors, vocabSet, num)
            print('Recommender gives: ', int(x), 'Actual Rating: ', ratings[i])
            if int(x) not in range(int(ratings[i]) - 1, int(ratings[i]) + 2):
                print(' '.join(str(i) for i in test_data[i]))
                error_count += 1
        return error_count / len(test_data)

    def recommend(self, data, ratings, wordVectors, vocabSet):
        """
        Test's the Recommender System against new data it hasn't seen before, returns Test error rate
        Error Rate Calculation: Accepts a rating +/-1 of actual rating
        Parameter: -Parsed Data; Must be 2D List; (needs to be in format of what you want rated!)
                   -Ratings: List of get ratings function
                   -Bag of Words: from bag of words function
                   -Vocab Set: from vocabSet function
        """
        assert type(data) == list
        for i in data:
            x = self.calculate_rating(i, ratings, wordVectors, vocabSet)
            print(' '.join(i), 'Rating: ', x)


if __name__ == '__main__':
    c = CosineSimilarity()
