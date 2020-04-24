from fastai.text import *

def load_model(path= "./flaskwebsite/static/models/", model_name="sarcasm.pkl"):
    learn = load_learner(path, model_name)
    return learn

def predict(str, learn):
    pred_class, _, _ = learn.predict(str)
    return int(pred_class)
