# Import required libraries
import os
import sys
from src.exception import CustomException #Custom Exception class
from src.logger import logging #Custom logging module
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass #Dataclass module for creating configuration classes


# Dataclass for data ingestion configuration
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artefacts','train.csv') #Training data file path
    test_data_path: str = os.path.join('artefacts','test.csv') #Test data file path
    raw_data_path: str = os.path.join('artefacts','data.csv') #Raw data file path

# Class for data ingestion
class dataingestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()  #Data ingestion configuration


    # Method for initiating data ingestion process
    def initiate_data_ingestion(self):
        logging.info('entered the data ingestion method or component')
        try:
            df = pd.read_csv('notebook/data/stud.csv')  #Read data from CSV file
            logging.info('read the data as dataframe')  #Log message

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)  #Create directories if not exist
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)  #Save raw data to CSV file

            logging.info('train test split initiated')

            train_set,test_set = train_test_split(df, test_size=0.2, random_state=42)  # Perform train-test split
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True) # Save training data to CSV file
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True) # Save testing data to CSV file

            logging.info('Ingestion of the data is completed')
            
            # Return training and testing data file paths
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        # Catch exceptions and raise custom exception
        except Exception as e:
            raise CustomException(e,sys)

if __name__=='__main__':
    obj = dataingestion()
    obj.initiate_data_ingestion()