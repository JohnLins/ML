import gensim.downloader as api
model = api.load('word2vec-google-news-300')
import numpy as np

#print("king", model['king'])
#print("kid", model['kid'])

thing = np.array(model["word"] * model["bad"], dtype='f')
#print(model.most_similar(thing, [], topn=1) )
 
print(model.similar_by_vector(thing, topn=1, restrict_vocab=None) )