# -*- coding: utf-8 -*-
"""Fake News Predictor

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LSNm1ogfgM5PKW4TwsoXbpJkFmldbSbw
"""

import numpy as np
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import nltk
nltk.download('stopwords')

print(stopwords.words('english'))

"""Data Preprocessing

"""

news_dataset = pd.read_csv('train.csv' , error_bad_lines = False , engine = "python")

news_dataset.head(20)

news_dataset.isnull().sum()

news_dataset.head(20)

news_dataset = news_dataset.fillna('')
news_dataset.isnull().sum()

#since the text data is very large, we will only use the title and author
#for that , we combine both

news_dataset['content'] = news_dataset['author']+' '+ news_dataset['title']
news_dataset['content'].head()

X = news_dataset.drop(columns='label', axis=1)
Y = news_dataset['label']

print(X.head())
print(Y.head())

"""Stemming"""

port_stem = PorterStemmer()

def stemming(content):
  stemmed_content = re.sub('[^a-zA-Z]',' ',content)
  stemmed_content = stemmed_content.lower()
  stemmed_content = stemmed_content.split()
  stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
  stemmed_content = ' '.join(stemmed_content)
  return stemmed_content

news_dataset['content'] = news_dataset['content'].apply(stemming)

news_dataset['content'].head()

X = news_dataset['content'].values
Y = news_dataset['label'].values

for i in range(20):
  print(Y[i])

#Tf = term frequency  idf-> inverse document frequency
vectorizer = TfidfVectorizer()
vectorizer.fit(X)
X = vectorizer.transform(X)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2 ,random_state=2)

print(Y_train)

"""Training The model"""

model = LogisticRegression()
model.fit(X_train , Y_train)

X_train_prediction = model.predict(X_train)
training_accuracy = accuracy_score(X_train_prediction,Y_train)
print(training_accuracy)

X_test_prediction = model.predict(X_test)
testing_accuracy = accuracy_score(X_test_prediction,Y_test)
print(testing_accuracy)

"""Making a Predictive System"""

X_new = X_test[0]

prediction = model.predict(X_new)
print(prediction)
if(prediction[0]==0):
  print("the news is real")
else:
  print("news is fake")

print(Y_test[0])
