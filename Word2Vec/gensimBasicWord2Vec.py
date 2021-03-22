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





#3rd parties's lab:
"""

from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot
# define training data
sentences = [['this', 'is', 'the', 'first', 'sentence', 'for', 'word2vec'],
			['this', 'is', 'the', 'second', 'sentence'],
			['yet', 'another', 'sentence'],
			['one', 'more', 'sentence'],
			['and', 'the', 'final', 'sentence']]
# train model
model = Word2Vec(sentences, min_count=1)
# fit a 2d PCA model to the vectors
X = model[model.wv.vocab]
pca = PCA(n_components=2)
result = pca.fit_transform(X)
# create a scatter plot of the projection
pyplot.scatter(result[:, 0], result[:, 1])
words = list(model.wv.vocab)
for i, word in enumerate(words):
	pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()

"""
