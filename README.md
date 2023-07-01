# CRIME-VISION 
Advanced Crime Classification With Deep Learning
Crime Vision is a deep learning model that utilizes the Densenet121 architecture to predict crime types based on input images. This model is designed to assist law enforcement agencies, security organizations, and researchers in identifying and categorizing crime scenes.
- Demo Video: https://drive.google.com/file/d/1DVFUZD6qXZTbewMP2s9hM09xMFTQ06YL/view?usp=sharing

## Installation

### Get the code
```
git clone --recursive https://github.com/harsh-kashyap0201/crime-vision.git
```

### Requirements
The main requirements are listed below

- Python 3.6.10
- Pandas
- Numpy
- Flask
- Tensorflow

### Dataset
`CRIME-VISION` uses the [UCF Crime Dataset](https://www.kaggle.com/datasets/odins0n/ucf-crime-dataset) for Crime Classification.
Crime Vision was trained on a diverse dataset of crime-related images. The dataset contains various types of crimes, such as theft, assault, vandalism, and more. The dataset was carefully curated and labeled by experts to ensure accurate training and evaluation of the model.
Download and save the Crime UCF Crime Dataset in the current folder.

### Usage
To use Crime Vision you can use the following command to run the model
```
python app.py
```
## Technical Architecture:
Crime Vision utilizes the Densenet121 architecture as its backbone. Densenet121 is a CNN model that has shown strong performance in image classification tasks. It consists of a series of densely connected blocks, which allow for effective feature reuse and promote gradient flow throughout the network.

The model is composed of convolutional layers, followed by dense blocks, transition layers, and a global average pooling layer. The final output layer uses softmax activation to produce the predicted probabilities for each crime type.
![image](https://github.com/harsh-kashyap0201/crime-vision/assets/77957756/24c3adab-c2d9-4c0e-a1ac-811bc9319c0c)

## Demo Video: 
https://github.com/harsh-kashyap0201/crime-vision/assets/77957756/4462b38b-c59e-4fcd-89c9-0fb00b8041e9

## Web application screenshots 
![image](https://github.com/harsh-kashyap0201/crime-vision/assets/77957756/c5f239c5-1acf-408d-b6c3-9c289a62957f)
![image](https://github.com/harsh-kashyap0201/crime-vision/assets/77957756/9295f25e-096f-40dc-bdba-8ba911b83eef)

## Contributing
Contributions to Crime Vision are welcome! If you want to contribute to this project, please follow the
