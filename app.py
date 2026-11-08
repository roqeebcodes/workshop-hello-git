import os
import socket
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return ("<h1>hello-git</h1><p>Built from Git by Source-to-Image</p>"
            "<p>pod: " + socket.gethostname() + "</p>")


@app.route("/healthz")
def healthz():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
