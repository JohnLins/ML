import nltk
nltk.download('stopwords')
nltk.download('punkt')

from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize

text = "This is a bunch of text!"
stopWords = set(stopwords.words("english"))

words = word_tokenize(text)

filteredText = []

for i in words:
  if i not in stopWords:
    filteredText.append(i)

print(filteredText)