import fasttext

PRETRAINED_MODEL_PATH = '/tmp/lid.176.bin'
model = fasttext.load_model(PRETRAINED_MODEL_PATH)

word2vec = model['John'] + model['Eric'] 
print(word2vec)


vec2word = model['james']
print(vec2word)
