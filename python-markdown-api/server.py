import os
import sys
from flask import Flask, request
from flask_cors import CORS
import markdown2

app = Flask(__name__, template_folder="views")
CORS(app)

@app.route("/")
def index():
   return "Hello world!"


@app.route("/md", methods=['POST'])
def compile():
    print(request.data)
    data = request.get_json()
    md = data.get('markdown', '')
    return markdown2.markdown(md)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False, threaded=True)
