import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np
import re

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

import os
print(os.getcwd())  
@dataclass
#if you defining only variable ,it is better to use dataclass
# if it has other fuctions it is better to go with class __init__
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method component")

        try:
            df=pd.read_csv("src/notebook/data/StudentsPerformance.csv")
            # read_csv() → a pandas function that reads data from a CSV file and loads it into a DataFrame.

            # Normalize column names: remove leading/trailing spaces, lowercase, and replace non-alphanumeric characters with underscores
            df.columns = [re.sub(r'[^0-9a-zA-Z_]+', '_', c.strip().lower()) for c in df.columns]
            logging.info('Read the dataset as DataFrame and normalized column names')

            # Create artifacts directory if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            #save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False,header=True)

            # Split into train and test sets
            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            #save train and test sets
            train_set.to_csv(self.ingestion_config.train_data_path,index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            #return the file paths 
            return( 
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )




        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()


'''
Purpose of this block

if __name__ == "__main__":
This is a Python convention.
It ensures that the code inside this block runs only when you execute this script directly,
not when you import it in another script.

Why we create the object here?

obj = DataIngestion()
We create the DataIngestion object to call its method initiate_data_ingestion().
The class defines how ingestion works, but doesn’t run automatically — 
we need to create an object to actually use it.
'''
     
