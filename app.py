import platform
import pathlib
plt = platform.system()
if plt == 'Linux': pathlib.WindowsPath = pathlib.PosixPath

from fastai.vision.all import*
import gradio as gr
from gradio import Label

def oldornot(x): return x[0].isupper()

#/export
learn = load_learner('model.pkl')

#/export
categories = ['New Car','Old Car']

def classify_image(img):
    pred,idx,probs = learn.predict(img)
    return dict(zip(categories,map(float,probs)))

examples = ['new_car_2.jpg','new_car_4.jpg','old_car_7.jpg','old_car_12.jpg']


intf = gr.Interface(fn=classify_image, inputs=gr.Image(), outputs=Label(), examples=examples)


intf.launch(inline=False)
