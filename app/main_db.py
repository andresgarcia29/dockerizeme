import os
import random

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient(os.getenv("MONGO_URL"))


@app.route("/")
def main():
    return "Hello, world DB!"


@app.route("/create")
def create():
    collection = client.get_database("Test").get_collection("User")
    collection.insert_one({"Random Number": random.randint(0, 100)})
    return "Number Added Correctly"


@app.route("/see")
def see():
    collection = client.get_database("Test").get_collection("User")
    return str([item["Random Number"] for item in collection.find({})])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
