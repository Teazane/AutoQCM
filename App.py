from flask import Flask
from app_src.config import Config

app = Flask(__name__)
app.config.from_object(Config)

if __name__ == '__main__':
    app.run(debug=True)