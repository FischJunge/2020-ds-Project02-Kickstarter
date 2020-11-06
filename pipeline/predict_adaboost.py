import sys
import pandas as pd
import pickle
from feature_engineering import scale_X
from sklearn.metrics import fbeta_score, accuracy_score, roc_auc_score

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv)) 

# Get the locations of the files
ab_model = sys.argv[1]
X_test_path = sys.argv[2]
y_test_path = sys.argv[3]

# Load the model from disk
loaded_ab_model = pickle.load(open(ab_model, 'rb'))

# Load the test data from disk
X_test = pd.read_csv(X_test_path)
y_test = pd.read_csv(y_test_path)

# Scaling non-dummy variables
X_test = scale_X(X_test)

print("Making predictions using the adaboost model.")
# Predict y based on features in the test data
ab_y_pred = loaded_ab_model.predict(X_test)
ab_acc = accuracy_score(y_test, ab_y_pred)
ab_f = fbeta_score(y_test, ab_y_pred,beta=0.5)
ab_auc = roc_auc_score(y_test, ab_y_pred)

print('Results:')

print('Adaboost accuracy: %.3f'%ab_acc)
print('Adaboost f1-score: %.3f'%ab_f)
print('Adaboost AUC: %.3f'%ab_auc)