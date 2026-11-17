import sys
import logging

def error_message_detail(error: Exception, error_detail: sys) -> str:

    #extract detailed information including file name , line number and error message

    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    line_number = exc_tb.tb_lineno
    error_message = f"Error occured in python script: [{file_name}] at line number [{line_number}]: {str(error)}"

    logging.error(error_message)

    return error_message

class MyException(Exception):

    def __init__(self, error_message : str, error_detail: sys):

        #initialize the USvisaException with detailed error message

        super().__init__(error_message)

        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:

        #Return string reperesentation of error message
        return self.error_message