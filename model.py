from fastai.vision.all import *
from fastai.vision.widgets import *
import json

path = Path('..')
vocab = []

def get_x(r): 
    # f = r['image']
    # return (data_path/f[0]/f[1]/f[2]/f[3]/f)
    return 0

def get_y(r): return r['labels']

def splitter(df):
    train = df.index[df['train']].tolist()
    valid = df.index[~df['train']].tolist()
    return train,valid

with open(path/'vocab.txt') as f:
    for line in f:
        vocab.append(line.strip())

def predict_ingredients(img_path):
    print(img_path)
    img = PILImage.create(img_path)
    # display(img.to_thumb(128,128))
    preds = learn.predict(img)
    preds_list = preds[-1].tolist()
    pred_idxs = [preds_list.index(elem) for elem in preds_list if(elem > 0.2)]
    pred_dict = {}
    pred_list = []
    for idx in pred_idxs:
        pred_dict[idx] = vocab[idx]
        pred_list.append(vocab[idx])
    return pred_list

learn = load_learner('v3.pkl')

