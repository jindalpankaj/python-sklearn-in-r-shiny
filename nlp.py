# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 15:09:53 2020
@author: Pankaj Jindal
"""

# This is a project to begin learning NLP; influenced by a Thinkful webinar.
import pandas as pd
import numpy as np
import sklearn
import re
import matplotlib.pyplot as plt

data = pd.read_csv('https://github.com/Thinkful-Ed/data-201-resources/raw/master/hotel-reviews.csv')

# data.columns

# data.head(3).address

# data[["name","reviews.rating", "reviews.text","reviews.title"]]

# data.head()

# data.values

# type(data)

# data.index

data = data[["name","reviews.rating", "reviews.text","reviews.title"]]
data.rename(columns={'name':'hotel_name', 
                     "reviews.rating":"review_rating", 
                     "reviews.text":"review_comment", 
                     "reviews.title":"review_title"}, inplace = True)


# removing blank reviews and replacing with ""
data["review_comment"] = data["review_comment"].fillna("")
data["review_title"] = data["review_title"].fillna("")

# concatinating review title and review comment as review
data["review"] = data["review_title"] + " " + data["review_comment"]
data = data[["hotel_name","review","review_rating"]]
data.rename(columns = {"review_rating":"rating"}, inplace = True)

# removing non-text and digit characters using regular expressions
data["review"] = data["review"].str.replace(r'\?|\.|\!|\'|\(|\)|,|-|\d',"")

# lowercase all characters
data["review"] = data["review"].str.lower()

# checking if there are any blank review
# sum(data["review"].isna())

# removing blank ratings
sum(~data["rating"].isna())
data = data[~data["rating"].isna()]
# data.shape
# data.head(3)

# kinds of ratings
data["rating"].value_counts()

# keeping only 0 to 5 ratings and removing others
data = data[data["rating"].isin([0,1,2,3,4,5])]

# plotting
# data["rating"].value_counts().plot(kind = "bar")

# bag of words
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(max_features = 10000)
X = vectorizer.fit_transform(data["review"])
bag_of_words = pd.DataFrame(X.toarray(), columns = vectorizer.get_feature_names())
bag_of_words.head(2)

# modeling
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
trained_model = model.fit(bag_of_words, data["rating"])

def funcPredictRating(inputText):
  inputText = [inputText]
  X_test = vectorizer.transform(inputText).toarray()
  predicted_rating = trained_model.predict(X_test)
  return predicted_rating
  
# testing. making predictions.
# test_review = ["Absolutely wonderful."]
# X_test = vectorizer.transform(test_review).toarray()
# predicted_rating = trained_model.predict(X_test)
# print("Predicted rating is: " + str(predicted_rating))
