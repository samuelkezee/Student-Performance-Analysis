import os
import sys
import dill

import numpy as np
import pandas as pd
from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_models(X_train,y_train,X_test,y_test,models,params):
    try:
        report={}

        for i in range (len(list(models))):
            model=list(models.values())[i]
                # ---->LinearRegression() object
                # list(models.keys())[0] → "linear_reg"
                # param["linear_reg"] → {"learning_rate": 0.01}

            para=params[list(models.keys())[i]]

            #hyper parameter tuning 
            gs=GridSearchCV(model,para,cv=3)

            gs.fit(X_train,y_train)


            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)
                
            # model.fit(X_train,y_train)# train the model

            y_train_predict=model.predict(X_train)
            y_test_predict=model.predict(X_test)


            train_model_score=r2_score(y_train,y_train_predict)
            test_model_score=r2_score(y_test,y_test_predict)

            report[list(models.keys())[i]]=test_model_score
        return report
        
        
    except  Exception as e:
        raise CustomException(e,sys)
    
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    