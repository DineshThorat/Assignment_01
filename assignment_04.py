# Assignment No_04
# Name:Dinesh Ashok Thorat
# Roll No : 63
# TITLE: Generating Unigrams,Bigrams and Trigrams in nltk (paragraph).

from nltk.util import ngrams

#Function for generating n_grams
def n_grams(n):
  #sample input
  para = '''Python is an open source community language, so numerous 
            independent programmers are continually building libraries 
            and functionality for it. Professionally, Python is great for 
            backend web development, data analysis, artificial 
            intelligence, and scientific computing. '''
  grams = ngrams(para.split(), n)

  for i in grams:
    print(i)


#input for each n-gram
print("Unigrams:")
n_grams(1)
print("\nBigrams:")
n_grams(2)
print("\nTrigrams:")
n_grams(3)

#OUTPUT:
# Unigrams:
# ('Python',)
# ('is',)
# ('an',)
# ('open',)
# ('source',)
# ('community',)
# ('language,',)
# ('so',)
# ('numerous',)
# ('independent',)
# ('programmers',)
# ('are',)
# ('continually',)
# ('building',)
# ('libraries',)
# ('and',)
# ('functionality',)
# ('for',)
# ('it.',)
# ('Professionally,',)
# ('Python',)
# ('is',)
# ('great',)
# ('for',)
# ('backend',)
# ('web',)
# ('development,',)
# ('data',)
# ('analysis,',)
# ('artificial',)
# ('intelligence,',)
# ('and',)
# ('scientific',)
# ('computing.',)

# Bigrams:
# ('Python', 'is')
# ('is', 'an')
# ('an', 'open')
# ('open', 'source')
# ('source', 'community')
# ('community', 'language,')
# ('language,', 'so')
# ('so', 'numerous')
# ('numerous', 'independent')
# ('independent', 'programmers')
# ('programmers', 'are')
# ('are', 'continually')
# ('continually', 'building')
# ('building', 'libraries')
# ('libraries', 'and')
# ('and', 'functionality')
# ('functionality', 'for')
# ('for', 'it.')
# ('it.', 'Professionally,')
# ('Professionally,', 'Python')
# ('Python', 'is')
# ('is', 'great')
# ('great', 'for')
# ('for', 'backend')
# ('backend', 'web')
# ('web', 'development,')
# ('development,', 'data')
# ('data', 'analysis,')
# ('analysis,', 'artificial')
# ('artificial', 'intelligence,')
# ('intelligence,', 'and')
# ('and', 'scientific')
# ('scientific', 'computing.')

# Trigrams:
# ('Python', 'is', 'an')
# ('is', 'an', 'open')
# ('an', 'open', 'source')
# ('open', 'source', 'community')
# ('source', 'community', 'language,')
# ('community', 'language,', 'so')
# ('language,', 'so', 'numerous')
# ('so', 'numerous', 'independent')
# ('numerous', 'independent', 'programmers')
# ('independent', 'programmers', 'are')
# ('programmers', 'are', 'continually')
# ('are', 'continually', 'building')
# ('continually', 'building', 'libraries')
# ('building', 'libraries', 'and')
# ('libraries', 'and', 'functionality')
# ('and', 'functionality', 'for')
# ('functionality', 'for', 'it.')
# ('for', 'it.', 'Professionally,')
# ('it.', 'Professionally,', 'Python')
# ('Professionally,', 'Python', 'is')
# ('Python', 'is', 'great')
# ('is', 'great', 'for')
# ('great', 'for', 'backend')
# ('for', 'backend', 'web')
# ('backend', 'web', 'development,')
# ('web', 'development,', 'data')
# ('development,', 'data', 'analysis,')
# ('data', 'analysis,', 'artificial')
# ('analysis,', 'artificial', 'intelligence,')
# ('artificial', 'intelligence,', 'and')
# ('intelligence,', 'and', 'scientific')
# ('and', 'scientific', 'computing.')