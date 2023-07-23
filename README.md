# FakenewsPredictor
A logistic regression model trained on fake news dataset from kaggle, to predict whether a news item is real or fake


# Fake News Predictor

This is a Python code that demonstrates a simple fake news predictor using the Logistic Regression algorithm. The code reads a CSV dataset containing news articles and their corresponding labels (real or fake), performs data preprocessing, and then trains a Logistic Regression model for prediction.

## Prerequisites

Before running this code, make sure you have the following installed:

- Python 3.x
- Required Python libraries: numpy, pandas, re, nltk, sklearn

You can install the required libraries using `pip`:
```bash
pip install numpy pandas nltk scikit-learn
```

## How to Use

1. Clone or download the repository to your local machine.

2. Ensure that the `train.csv` file is present in the same directory as the Python script.

3. Run the Python script. The script will perform the following steps:

## Data Preprocessing

- Read the CSV dataset `train.csv`.
- Check for and handle any missing values in the dataset.
- Combine the "author" and "title" columns to create a new "content" column.
- Remove any non-alphabetic characters, convert the text to lowercase, tokenize it, and apply stemming to reduce words to their root form.
- Prepare the features (X) and labels (Y) for training the model.

## Training The Model

- Create a TF-IDF vectorizer to convert the text data into numerical vectors.
- Split the dataset into training and testing sets.
- Train a Logistic Regression model on the training data and evaluate its accuracy on both training and testing sets.

## Making a Predictive System

- Demonstrate the predictive system by predicting the label of the first article in the test set.
- Print the predicted label ("the news is real" or "news is fake") and the actual label for comparison.

Please note that this code is a basic example and may not yield optimal results on all datasets. Improvements and fine-tuning can be done based on the specific requirements and characteristics of your dataset.

For more details on the implementation, you can refer to the original Colaboratory notebook where this code was generated:
[Original Colaboratory Notebook](https://colab.research.google.com/drive/1LSNm1ogfgM5PKW4TwsoXbpJkFmldbSbw)
