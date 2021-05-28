import string
import pickle
import random

from flask import Flask, render_template

# Global
app = Flask(__name__)
PICKLED_FILE = "cached_urls.pickle"


def get_cached_urls():
    with open(PICKLED_FILE, "rb") as p:
        list_of_short_urls = pickle.load(p)
    return list_of_short_urls


def store_cached_urls(list_of_short_urls, short_url, long_url):
    list_of_short_urls.update({short_url: long_url})
    with open(PICKLED_FILE, "wb") as p:
        pickle.dump(list_of_short_urls, p, protocol=pickle.HIGHEST_PROTOCOL)


def encode(long_url):
    list_of_short_urls = get_cached_urls()
    if long_url not in list_of_short_urls:
        res = ""
        for _ in range(8):
            res += random.choice(string.ascii_letters + string.digits)
        list_of_short_urls[res] = long_url
        store_cached_urls(list_of_short_urls, res, long_url)
        return res
    else:
        for k, v in list_of_short_urls.items():
            if v == long_url:
                return k


@app.route("/", methods=["GET", "POST"])
def home_page():
    return render_template("short_urls.html")


app.run(host="0.0.0.0", port=8080)
