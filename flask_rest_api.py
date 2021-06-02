#!/usr/bin/env python3
"""
Flask runner to start the url shortening REST API service.
Author: Santhosh Balasa
Email: santhosh.kbr@gmail.com
Date: 1/June/2021
"""

from shorten_url import encode
from flask_restful import Api, Resource
from flask import Flask, request, jsonify


app = Flask(__name__)
api = Api(app)


@api.resource("/")
class ShortenURL(Resource):
    def post(self):
        long_url = request.get_json(force=True)
        return jsonify(
            {"long_url": long_url["long_url"], "shorten_url": encode(long_url)}
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
