
print('hi')

from pytube import YouTube
from flask import Flask, send_file
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

app = Flask(__name__)

@app.route('/')
def index():
    return {'message': 'Hello, World!'}


@app.route("/yt/<id>")
def get_video(id):
  print("Downloading video..." + id)
  yt = YouTube("https://www.youtube.com/watch?v=" + id)
  if (yt.length > 60):
    print("Video is greater than 60 seconds, please try again")
    return {
      "status": "error",
      "message": "Video is greater than 60 seconds, please try again"
    }
  ys = yt.streams.get_highest_resolution()
  ys.download(filename="video.mp4")
  return send_file("./video.mp4", mimetype="video/mp4")


api = Api(app)
CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})
