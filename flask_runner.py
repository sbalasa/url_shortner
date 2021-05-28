#!/usr/bin/env python3
"""
Main Flask runner to start the url shortening web service.
Author: Santhosh Balasa
Email: santhosh.kbr@gmail.com
Date: 28/May/2021
"""

from shorten_url import encode
from flask import Flask, request, render_template

# Global
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home_page():
    """
    Function to serve GET or POST Web page.
    """
    long_url = request.form.get("long_url")
    if request.method == "POST":
        encoded_url = "http://Santhosh_tinyurl/" + encode(long_url)
        return render_template("results.html", **locals())
    return render_template("short_urls.html")

app.run(host='0.0.0.0', port=8080)
