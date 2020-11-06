import numpy as np
import pandas as pd
import json
import pickle
import warnings
warnings.filterwarnings('ignore')

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import fbeta_score, accuracy_score, roc_auc_score

from data_cleaning import drop_columns, drop_rows, get_category, get_time, replace_missing_data
from feature_engineering import feat_goal_duration, feat_text, feat_time, scale_X

df = pd.read_csv('data/Kickstarter_merged.csv')

# data cleaning
print("Data cleaning.")
df = drop_columns(df)
df = drop_rows(df)
print("Data cleaning: categories.")
df = get_category(df)
print("Data cleaning: time.")
df = get_time(df)
df = replace_missing_data(df)
df.to_csv('data/Kickstarter_cleaned.csv',index=False)

print("Feature engineering.")
df = feat_goal_duration(df)
df = feat_text(df)
df = feat_time(df)
df.to_csv('data/Kickstarter_featured.csv',index=False)

print("Defining the model, train and test data.")
# Defining X and y
y = df.state_b_True
X = df.drop(columns='state_b_True')
print('Using the following features to predict the project state:')
print(X.columns)

# Splitting data into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)

# Write test data to csv
X_test.to_csv('data/X_test.csv',index=False)
y_test.to_csv('data/y_test.csv',index=False)

# Scaling non-dummy variables
X_train = scale_X(X_train)
X_test = scale_X(X_test)

print("Training the random forest model.")
# fit the logistic regression model
rf = RandomForestClassifier(n_estimators=100, random_state=42, max_features = 'sqrt', n_jobs=-1, verbose = 1)
rf.fit(X_train, y_train)

print("Done: saving the random forest model.")
rf_filename = 'models/random_forest_model.sav'
pickle.dump(rf, open(rf_filename, 'wb'))

print("Making predictions using the random forest model.")
# Predict y based on features in the test data
rf_y_pred = rf.predict(X_test)
rf_acc = accuracy_score(y_test, rf_y_pred)
rf_f = fbeta_score(y_test, rf_y_pred,beta=0.5)
rf_auc = roc_auc_score(y_test, rf_y_pred)

print("Training the adaboost model.")
ab = AdaBoostClassifier(random_state = 42)
ab.fit(X_train, y_train)

print("Done: saving the adaboost model.")
ab_filename = 'models/adaboost_model.sav'
pickle.dump(ab, open(ab_filename, 'wb'))

print("Making predictions using the adaboost model.")
# Predict y based on features in the test data
ab_y_pred = ab.predict(X_test)
ab_acc = accuracy_score(y_test, ab_y_pred)
ab_f = fbeta_score(y_test, ab_y_pred,beta=0.5)
ab_auc = roc_auc_score(y_test, ab_y_pred)

print('Results:')

print('Random forest accuracy: %.3f'%rf_acc)
print('Random forest f1-score: %.3f'%rf_f)
print('Random forest AUC: %.3f'%rf_auc)

print('Adaboost accuracy: %.3f'%ab_acc)
print('Adaboost f1-score: %.3f'%ab_f)
print('Adaboost AUC: %.3f'%ab_auc)
