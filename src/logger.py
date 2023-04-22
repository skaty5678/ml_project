# Import necessary libraries
import logging
import os
from datetime import datetime

# Set log file name based on current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Set log path to 'logs' directory in the current working directory
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)

# Create the 'logs' directory if it doesn't exist
os.makedirs(logs_path,exist_ok=True)

# Set the full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


# Configure the basic logger settings
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Set the log file path
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", # Set the log format
    level = logging.INFO  # Set the logging level to INFO

)




