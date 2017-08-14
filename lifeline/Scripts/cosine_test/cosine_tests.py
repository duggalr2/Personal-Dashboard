import unittest
from cosine_similarity import CosineSimilarity

class TestCosineMethods(unittest.TestCase):

    def testRatingPrompt(self):
        x = CosineSimilarity()
        self.assertEqual([2, 3, 3, 4, 5], x.get_ratings('test_rating'))

    def testVocabSet(self):
        x = CosineSimilarity()
        raw_data = [['Sheets', 'Term', 'Bigwig', 'Valuations', 'Look', 'Line', 'Briefs', 'Intricacies'],
                    ['Safe', 'Option'],
                    ['Incandescence'], ['Capital', 'Innovation', 'Finance', 'Venture'],
                    ['Systems', 'Introduction', 'Database'],
                    ['Transactional', 'Systems', 'Information'], ['Graphics', 'Principles', 'Practice', 'Computer'],
                    ['Conformity', 'Instincts', 'Worst', 'ACLU', 'Cowardice'],
                    ['Things', 'Checklist', 'Manifesto', 'Right'],
                    ['Your', 'Deals', 'Capitalist', 'Smarter', 'Than', 'Venture', 'Lawyer']]

        v = x.vocabSet(raw_data)

        rightv = ['Cowardice', 'ACLU', 'Principles', 'Worst', 'Intricacies', 'Checklist', 'Database', 'Finance',
                  'Manifesto', 'Bigwig', 'Incandescence', 'Innovation', 'Computer', 'Practice', 'Valuations', 'Term',
                  'Look', 'Option', 'Instincts', 'Sheets', 'Your', 'Briefs', 'Transactional', 'Venture', 'Information',
                  'Conformity', 'Safe', 'Than', 'Capital', 'Introduction', 'Graphics', 'Systems', 'Capitalist',
                  'Lawyer', 'Things', 'Smarter', 'Deals', 'Line', 'Right']

        self.assertEqual(len(rightv), len(v))
        for i in rightv:
            self.assertIn(i, v)

    def testBagWords(self):
        x = CosineSimilarity()
        w = [['Line', 'Look', 'Done', 'io']]
        y = ['Line', 'Look', 'Option', 'Briefs', 'Intricacies', 'Valuations', 'Term', 'Safe', 'Sheets', 'Bigwig']
        self.assertEqual([[1, 1, 0, 0, 0, 0, 0, 0, 0, 0]], [x.bag_of_words(y, i) for i in w])
