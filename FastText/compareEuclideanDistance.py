import fasttext
import numpy as np 

PRETRAINED_MODEL_PATH = '/tmp/lid.176.bin'
model = fasttext.load_model(PRETRAINED_MODEL_PATH)

first = np.array(model['lion'])


target = np.array(model['big'])
print(target)


second = np.array(model['cat'])



print("First: ", np.linalg.norm(first - target))
print("Second: ", np.linalg.norm(second - target))
  
