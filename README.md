# Fast.AI Car Age Classifier

A deep learning model built with Fast.AI that classifies cars as either "old" or "new". The model is deployed on Hugging Face Spaces and achieves high accuracy in distinguishing between vintage and modern vehicles.

## Features
- Binary image classification (Old vs New cars)
- Built using Fast.AI and ResNet18 architecture 
- Deployed on Hugging Face Spaces
- ~80% accuracy on validation set
- Interactive web interface for real-time predictions

## Technical Details
- Training data scraped from DuckDuckGo image search
- ResNet18 pre-trained model with fine-tuning
- Data augmentation using random transforms
- Batch size of 16 with 20% validation split
- One epoch of fine-tuning

## Live Demo
Try it out: [Car Classifier on Hugging Face](https://huggingface.co/spaces/grover101/NeuralNet)

## Installation
```bash
pip install -r requirements.txt
```

## Usage
1. Load model:
```python
learn = load_learner('model.pkl')
```

2. Make predictions:
```python
pred, idx, probs = learn.predict(image)
```

![image](https://github.com/user-attachments/assets/a893dd9d-f35f-4511-8bb2-e0cf2bd73b24)


## Repository Structure
```
├── notebooks/
│   └── Fast_AI_Car_Classifier.ipynb
├── app.py
├── model.pkl
├── requirements.txt
└── README.md
```

## Author
Aravind Raju
