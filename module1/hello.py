import os
from flask import Flask

server = Flask(__name__)


@server.route('/hello')
def hello():
    return "Hello World!!"


if __name__ == '__main__':
    server.run()
