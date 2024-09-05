import os 
import sys
from flask import Flask 
from src.logger import logging 
from src.exception import CustomException
app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():

    try: 
        raise Exception("We are just testing our Exception file")
    except Exception as e: 
        ML = CustomException(e, sys)
        logging.info(ML.error_message
                     )
    logging.info("Just for testing purpose")

    return "Welcome to MLOps modular coding tutorial and exception file is working perfectly" 


if __name__ == '__main__':
    app.run(debug = True)