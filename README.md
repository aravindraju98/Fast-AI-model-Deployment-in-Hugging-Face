Project Overview:
This project aims to differentiate between old and new cars using a basic Neural Network (NN) built with Fast.ai. The model is trained on a dataset containing images of both old and new cars and is deployed using the Hugging Face Spaces platform.

Project Structure:

    Data Collection: Images of old and new cars are collected using the DuckDuckGo image search API.
    Data Preparation: Images are downloaded and organized into separate folders for old and new cars.
    Model Building: A basic Neural Network model is constructed using Fast.ai library, utilizing transfer learning with ResNet-18 architecture.
    Model Training: The model is trained on the dataset, fine-tuned to improve performance, and evaluated using metrics such as accuracy and error rate.
    Model Exporting: The trained model is exported for deployment on the Hugging Face Spaces platform.
    Deployment: The deployed model can be accessed via the provided Hugging Face Spaces link.

Files Included:

    Project_3_NN.ipynb: Jupyter Notebook containing the project code.
    requirements.txt: Text file containing the list of required Python packages for seamless deployment on Hugging Face Spaces.
    labels.csv: CSV file containing image paths and corresponding labels for training data.
    model: Folder containing the exported model for deployment.

Instructions:

    Data Collection: Ensure access to DuckDuckGo image search API and execute the provided code to collect images.
    Model Building: Run the notebook to build and train the Neural Network model.
    Model Exporting: Export the trained model using the provided code.
    Deployment: Use the Hugging Face Spaces platform to deploy the exported model and share the provided link for access.

Conclusion:
This project demonstrates the process of building and deploying a basic Neural Network model for image classification tasks. It provides a foundation for further exploration and refinement of deep learning techniques for car classification and similar applications.
