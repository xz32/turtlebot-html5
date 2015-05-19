import config
from flask import Response, render_template

MIME_DICT = {
    "js": "text/javascript",
    "css": "text/css",
    "imgs": "image/png",
    "libraries": "text/javascript",
    "data": "text/csv",
    "sounds": "audio/vnd.wav"
}


@config.app.route("/<file_type>/<filename>", methods=["GET"])
def get_static(file_type, filename):
    with open(file_type + "/" + filename) as f:
        res = Response(f.read(), mimetype=MIME_DICT[file_type])
        return res


@config.app.route("/<filename>", methods=["GET"])
def get_html(filename):
    return render_template(filename)


@config.app.route("/sayer/<name>", methods=["GET"])
def get_sayer(name):
    return render_template("sayer.html", name=name)


@config.app.route("/", methods=["GET"])
def get_index():
    return render_template("index.html")


@config.app.route("/controller/<name>", methods=["GET"])
def get_controller_page(name):
    return render_template("controller.html", name=name)
