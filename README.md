# Laptop Price Prediction
  This is a machine learning project that aims to predict the price of a laptop based on its specifications. The project uses a dataset of laptops from various brands and models, along with their specifications and prices. The model is built using Python and scikit-learn, and the web application is built using Streamlit.
## Table of Contents
1. Installation
2. Usage
3. Dataset
4. Model Training
5. Web Application

## 1. Installation
To run this project, you will need to have Python 3 installed on your system, along with the following libraries:

- pandas
- numpy
- scikit-learn
- streamlit
## 2. Usage
To use this project, you can simply clone this repository and run the app.py script using the following command:

`streamlit run app.py`

This will launch the web application in your default browser. You can then enter the specifications of the laptop you want to predict the price for, and the model will output a predicted price.

## 3. Dataset 
The dataset used in this project is sourced from various e-commerce websites, and includes laptops from popular brands such as Dell, HP, Lenovo, and Apple. The dataset includes the following features:

You can find the dataset [click here](https://github.com/badalsde/Laptop-Price-Predictor/blob/master/laptop_data.csv)
- Brand
- Model
- Processor
- RAM
- Storage Type
- Storage Size
- Screen Size
- GPU
- Price

The dataset has been preprocessed to handle missing values and categorical variables.

## 4. Model Training
The machine learning model used in this project is a Random Forest Regression model, trained using the scikit-learn library. The model has been trained on the laptop dataset, and achieves a mean absolute error of less than $100.

The model has been saved as a pipe.pkl file, which is loaded by the app.py script.

## 5. Web Application
The web application is built using the Streamlit framework, and allows users to enter the specifications of a laptop and get a predicted price. The application includes a simple user interface with input fields for each specification, as well as an output field for the predicted price.

To run the web application, simply run the app.py script using the following command:

`streamlit run app.py`

### Contributing
If you find any issues or have any suggestions for this project, feel free to create a pull request or submit an issue.
