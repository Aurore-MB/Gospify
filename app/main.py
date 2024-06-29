
from flask import Flask, render_template, send_file
import os

app = Flask(__name__)


app.config['DOWNLOAD_PATH'] =  os.path.join(app.root_path, 'data', 'music')

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/music")
def get_music():
    return render_template("music.html")

@app.route("/playlists")
def get_playlist():
    return render_template("playlist.html")


@app.route("/audios/<filename>")
def get_audio(filename):
    target_path = os.path.join(app.config['DOWNLOAD_PATH'], filename)
    return send_file(target_path)


if __name__ == "__main__":
    app.run(port=4001, host='0.0.0.0', debug=True)