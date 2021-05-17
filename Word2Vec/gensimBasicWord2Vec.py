from gensim.models import Word2Vec
import numpy as np

sentences = [['this', 'is', 'a', 'sentence', 'about', 'school'],
			['school', 'has', 'students', 'and', 'teachers'],
			['teachers', 'teach', 'the', 'students'],
			['the', 'students', 'learn'],
			['the', 'teachers', 'make', 'money']]

model = Word2Vec(sentences, min_count=1)

first = model['students']
target =  model['learn']
second = model['teachers']

print("First: ", np.linalg.norm(target - first))
print("Second: ", np.linalg.norm(target - second))
