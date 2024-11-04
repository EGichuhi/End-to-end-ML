import sys 
import logging
from src.logger import logging 

#sys library will have information for exceptions

#parent exception. will give feedback on how message should look inside file
def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    #custom exception handling documentation, exc_tb is variable and inside you can find frame, code and filename
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name[{0}] line number [{1}] error message [{2}]".format(
    file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


#
class CustomException(Exception):
    #constructor
    def __init__(self, error_message, error_detail:sys):
        #inherit init function, inherit exception clss with respect to error message
        super().__init__(error_message)
        #error message variable  populating from parent function
        self.error_message=error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

""" 
if __name__=="__main__":

    try:
        a=1/0
    except Exception as e:
        logging.info("divide by zero")
        raise CustomException(e, sys)
"""