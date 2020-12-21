import nltk
nltk.download('stopwords')
nltk.download('punkt')

from nltk.tokenize import word_tokenize

text = "This is a bunch of text! and a repeeted"

words = word_tokenize(text)

wordNumbers = []

for i in range(len(words)):
  for j in range(i-1):
    
    print("i: ", i, "J: ", j)
    if words[j] == words[i]:
      wordNumbers.append(j)
      print("Repeat: ", words[i])
  j = j + 1
    
  wordNumbers.append(i)
  print("::::::", i)
print(words)
print(wordNumbers)
