import sys

class CustomException(Exception):
    def __init__(self, message:str, get_detailed:Exception=None):
        self.error_msg = self.get_error_mod(message, get_detailed)
        super().__init__(self.error_msg)


    @staticmethod 

    def get_error_mod(message:str, get_detailed): 
        _, _, frame = sys.exc_info() 
        file_n= frame.tb_frame.f_code.co_filename if frame else "Unknown"
        line_no = frame.tb_lineno if frame else "Unknown"

        return( f"{message} | Error: {get_detailed} | File: {file_n} | Line: {line_no}")

def __str__(self):
        return self.error_msg
    

