#start-server--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#cd WebDevFlask/
#set FLASK_APP=app.py
#set FLASK_ENV=development
#flask run --host=0.0.0.0
#* Running on http://127.0.0.1:5000/
#http://192.168.0.9:8080
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from __future__ import unicode_literals
from flask import render_template
from flask import request
from flask import Flask
from flask_bootstrap import Bootstrap
import yt_dlp
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
downloads_path = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Downloads"

@app.route("/")
def index():
    return render_template(
        "index.html",
        downloads_path = downloads_path
    )
@app.route('/',methods=['post',"get"])
def index_dl():
    url = request.form.get("url")
    cpdl_msg = f"{url}をダウンロードしました"
    mode = request.form.get("output_mode")
    save = request.form.get("savepath")
    if mode == "mp3":
        ydl_opts = {
            'format': 'bestaudio[ext=mp3]/bestaudio[ext=m4a]/bestaudio',
            "outtmpl":save + r"\%(title)s.%(ext)s"
                    }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    else:
        ydl_opts = {"outtmpl":save + r"\%(title)s.%(ext)s"}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])    
    return render_template(
        "index.html",
        complete_dlmsg = cpdl_msg,
        downloads_path = downloads_path
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=8080)