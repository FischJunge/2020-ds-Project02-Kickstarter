import sys
import pandas as pd
import pickle
from feature_engineering import scale_X
from sklearn.metrics import fbeta_score, accuracy_score, roc_auc_score

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv)) 

# Get the locations of the files
rf_model = sys.argv[1]
X_test_path = sys.argv[2]
y_test_path = sys.argv[3]

# Load the model from disk
loaded_rf_model = pickle.load(open(rf_model, 'rb'))

# Load the data from disk
X_test = pd.read_csv(X_test_path)
y_test = pd.read_csv(y_test_path)

# Scaling non-dummy variables
X_test = scale_X(X_test)

print("Making predictions using the random forest model.")
# Predict y based on features in the test data
rf_y_pred = loaded_rf_model.predict(X_test)
rf_acc = accuracy_score(y_test, rf_y_pred)
rf_f = fbeta_score(y_test, rf_y_pred,beta=0.5)
rf_auc = roc_auc_score(y_test, rf_y_pred)

print('Results:')

print('Random forest accuracy: %.3f'%rf_acc)
print('Random forest f1-score: %.3f'%rf_f)
print('Random forest AUC: %.3f'%rf_auc)
