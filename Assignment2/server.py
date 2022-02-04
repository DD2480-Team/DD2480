# gist source:
# https://gist.github.com/gene1wood/118e075c2af3effc13cec799a5d3661d

from __future__ import print_function
import sys
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'HEAD', 'POST'])
@app.route('/<path:path>', methods=['GET', 'HEAD', 'POST'])
def show_payload(path):
    print('Path : /{}'.format(path))
    print(json.dumps({'form': request.form}), file=sys.stderr)
    return "success"