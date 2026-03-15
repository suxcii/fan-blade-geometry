# app.py — serve index.html and any files in the same folder, with useful prints
from flask import Flask, send_from_directory
import os, sys, traceback

app = Flask(__name__, static_folder=".", static_url_path="")

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

# serve any other file in this folder (JS, css, images, fonts)
@app.route("/<path:path>")
def static_proxy(path):
    safe = os.path.normpath(path)
    return send_from_directory(app.static_folder, safe)

if __name__ == "__main__":
    try:
        print("Working dir:", os.getcwd())
        print("Files here:", sorted(os.listdir(".")))
        print("Python:", sys.executable, sys.version.splitlines()[0])
        print("Starting server on http://127.0.0.1:5000/  — press CTRL+C to quit\n")
        # debug=True for auto-reload and better error messages
        app.run(host="127.0.0.1", port=5000, debug=True)
    except Exception:
        traceback.print_exc()
        sys.exit(1)