#!/usr/bin/env python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def main():
    return '''
     <form action="/echo_user_input" method="POST">
         <input name="user_input">
         <input type="submit" value="Submit!">
     </form>
     '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return "You entered: " + input_text







# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.sqlite3'

# db = SQLAlchemy(app)

# class MusicVideos(db.Model):
#     song = db.Column("Song_Name", db.string, primary_key=True)
#     video = db.Column(db.string(255))


# @app.route("/")
# def main():
#     return '''
#      <form action="/echo_user_input" method="POST">
#          <input name="user_input">
#          <input type="submit" value="Submit!">
#      </form>
#      '''

# @app.route("/echo_user_input", methods=["POST"])
# def echo_input():
#     input_text = request.form.get("user_input", "")
#     # get data from api
#     # save data to database
#     return "You entered: " + input_text

# class MusicVideos(db.Model):
#     song = db.Column("Song_Name", db.string, primary_key=True)
#     video = db.Column(db.string(255))