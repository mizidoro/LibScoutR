from flask import Flask
from robot import Robot
import threading
import pprint

app = Flask(__name__)


@app.route("/")
def hello_world():
    return f"Searching for the book: {robot.user_want_book()}"


robot = Robot()
threading.Thread(target=robot.main).start()

# robot.organize_shelve("Biography")
