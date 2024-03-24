import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output

import tensorflow as tf


# Load dataset. of Titanic
dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv') # training data
dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv') # testing data
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')

#print(dftrain.head()) #output of 5-rows(due to .head) in train data
#print(dfeval.head()) #output of 5-rows(due to .head) in test data

#print(dftrain.describe()) #represent the statistics of train data
#print(dfeval.describe()) #represent the statistics of test data

#print(dftrain.shape) #represent the shape of train data 


dftrain.sex.value_counts().plot(kind='barh') #plotting the graph as barh that will show the distribution of male and female
#plt.show() # to show the graph 

CATEGORICAL_COLUMNS = ['sex', 'n_siblings_spouses', 'parch', 'class', 'deck',
                       'embark_town', 'alone']
NUMERIC_COLUMNS = ['age', 'fare']  # 2 columns are numeric

feature_columns = [] # create an empty list 

for feature_name in CATEGORICAL_COLUMNS:
    #print(feature_name)  #print the feature name to show how feature_name is in loop in CATEGORICAL_COLUMNS
    vocabulary = dftrain[feature_name].unique()
    # print(vocabulary) # -->to print the vocabulary having feature_name unique values use it whenever u need visual representation of the vocabulary and .unique() values by simpk=ly removing comment given in the starting of the line 
    feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary))

for feature_name in NUMERIC_COLUMNS:
  feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

#print(feature_columns)

