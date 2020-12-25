import nltk
from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize  
import string
nltk.download('stopwords')
nltk.download('punkt')

text = """this is a bunch of text and words. is this is more text. And more key key word"""


stop_words = set(stopwords.words('english'))  
  
wordArr = [w for w in word_tokenize(text) if not w in stop_words]  
wordArr = [wordArr.lower() for wordArr in wordArr if wordArr.isalpha()]
  
print(text)  
print(wordArr)  



wordsByPopularity = [[],[]]
for i in range(len(wordArr)):
  if wordArr[i] in wordsByPopularity[0]:
    wordsByPopularity[1][int(wordsByPopularity[0].index(wordArr[i]))] += 1
    print("H:", wordsByPopularity[0].index(wordArr[i]))
    
  else: 
    wordsByPopularity[0].append(wordArr[i])
    wordsByPopularity[1].append(1)

zippedSortedWordsLists = sorted(zip(wordsByPopularity[0], wordsByPopularity[1]), key=None, reverse=True)

tuples = zip(*zippedSortedWordsLists)
wordsByPopularity[0], wordsByPopularity[1] = [ list(tuple) for tuple in  tuples]

print("Sorted", wordsByPopularity[1].sort())




print("Text", text, "\n")
print("Word", wordArr, "\n")
print("WordRank", wordsByPopularity, "\n")


