
# app/model.py

class Message:
    def __init__(self, content):
        self.content = content

    def process(self):
        return f"Respuesta: {self.content}".upper()
