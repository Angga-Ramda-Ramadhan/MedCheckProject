import pandas as pd
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from imblearn.over_sampling import ADASYN, SMOTE
from sklearn.metrics import roc_curve, classification_report


class ModelImplementation:


    def modelplusmetrics(self, model_name, x_train, x_test, y_train, y_test):
        model = model_name
        model_fit = model.fit(x_train, y_train)
        model_pred = model_fit.predict(x_test)

        print("Rekap Performa Model: \n", classification_report(model_pred, y_test))
        