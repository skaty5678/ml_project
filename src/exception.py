import sys  # Importing the sys module to access information about the runtime environment.
from src.logger import logging  # Importing the logging module from src.logger package.


def error_message_detail(error, error_detail:sys):
    # Defining a function error_message_detail to return the error message along with the error details like filename, line number.
    _,_,exc_tb = error_detail.exc_info()  # Get the exception type, value, and traceback object.
    file_name = exc_tb.tb_frame.f_code.co_filename  # Extract the filename from the traceback object.
    error_message = "error occured in python script [{0}] line number[{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)  # Forming the error message string.
    )

    return error_message

class CustomException(Exception):
    # Defining a custom exception class to log the error message using the error_message_detail function.
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)


    def __str__(self):
        return self.error_message


if __name__ == '__main__':
    try:
        a=1/0  # Creating a ZeroDivisionError exception by dividing 1 by 0.

    except Exception as e:
        logging.info('divide by zero')  # Logging the error message.
        raise CustomException(e,sys)  # Raising the custom exception with the error message and details.
