
from decimal import Decimal
import random

import LetterFrequency

def gen(row, col, no_bigtable, probability_test):
    if row < 1 or col < 1:
        return

    # sum of all probabilities should be 100%
    total = Decimal('0.0')
    for ch, prob in LetterFrequency.EnglishAlphabet.iteritems():
        total += Decimal(prob)
#    print total
    assert total.compare(Decimal('100.000')) == 0

    test_iterations = 1000000

    if no_bigtable:
        charTable = {}
        sorted_keys = sorted(LetterFrequency.EnglishAlphabet.keys())
        total = Decimal('0.0')
        for ch in sorted_keys:
            prob = Decimal(LetterFrequency.EnglishAlphabet[ch]) / Decimal('100.0')
            charTable[ch] = float(total + prob)
            total = total + prob
        assert total == Decimal('1.0')

        rng = random.SystemRandom()

        if probability_test:
            results = {}
            for ch in sorted_keys:
                results[ch] = 0

            for i in xrange(0, test_iterations):
                prob = rng.random()
                for ch in sorted_keys:
                    if prob < charTable[ch]:
                        results[ch] = results[ch] + 1
                        break

            print 'char result expected diff'
            for ch in sorted_keys:
                result = results[ch]*100.0/float(test_iterations)
                expected = LetterFrequency.EnglishAlphabet[ch]
                
                print ch, result, expected, result-float(expected)

        for i in xrange(0, row):
            for j in xrange(0, col):
                prob = rng.random()
                for ch in sorted_keys:
                    if prob < charTable[ch]:
                        print ch,
                        break
            print ''

    else:
        charTable = []
        for letter, prob in LetterFrequency.EnglishAlphabet.iteritems():
            charTable.extend([letter for i in xrange(0, int((Decimal(prob)*1000).to_integral_exact()))])
        assert len(charTable) == 100000

        rng = random.SystemRandom()

        if probability_test:
            results = {}
            for ch in LetterFrequency.EnglishAlphabet.keys():
                results[ch] = 0

            number_of_keys = len(charTable)
            for i in xrange(0, test_iterations):
                pos = rng.randrange(0, number_of_keys)
                results[charTable[pos]] = results[charTable[pos]] + 1

            print 'char result expected diff'
            for ch in sorted(results.keys()):
                result = results[ch]*100.0/float(test_iterations)
                expected = LetterFrequency.EnglishAlphabet[ch]
                
                print ch, result, expected, result-float(expected)

        for i in xrange(0, row):
            for j in xrange(0, col):
                print charTable[rng.randrange(0, number_of_keys)],
            print ''

#import cProfile
#cProfile.run('gen(4, 4, False, True)')

if __name__ == '__main__':
    gen(4, 4, True, False)

