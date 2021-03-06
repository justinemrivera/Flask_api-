from mock_data import mock_data
import json
from flask import Flask, render_template
app = Flask(__name__)

me = {
    "name": "Justine",
    "last": "Rivera",
    "email": "test@mail.com",
    "age": 30,
    "hobbies": [],
    "address": {
            "street": "main",
            "number": "42"
    }
}


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return f"{me['name']} {me['last']}"


@app.route("/about/email")
def get_email():
    return me["email"]


@app.route("/about/address")
def get_addres():
    address = me["address"]
    return address["number"] + " " + address["street"]


@app.route("/api/catalog")
def get_catalog():
    cat = [
        {"id": "123123", "title": "Strawberry"},
        {"_id": "789261874", "title": "orange juice"}
    ]

    return json.dumps(mock_data)


# end point /api/categories
# return a string
# a for loop and print each dictionary
# print just the category

@app.route("/api/categories")
def get_categories():
    print("getting cats")
    categories = []
    for product in mock_data:
        cat = product["category"]
        if cat not in categories:
            categories.append(cat)

    return json.dumps(categories)



app.run(debug=True)
