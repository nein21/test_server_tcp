# app/view.py

from src.utils.logger import logger

class MessageView:
    @staticmethod
    def show_message(message):
        print(message)
        logger.info(message)

    @staticmethod
    def show_error(error):
        print(f"ERROR: {error}")
        logger.error(error)
