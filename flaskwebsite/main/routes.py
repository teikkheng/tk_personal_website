from flask import render_template, request, Blueprint, url_for


main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home():
    image_file = url_for("static", filename="profile_pics/" + "my_picture.jpg")
    return render_template("home.html", title="Home", image_file=image_file)


@main.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", title="Portfolio")


@main.route("/kueh")
def kueh():
    return render_template("kueh.html", title="Kueh Classifier")


@main.route("/dogs")
def dogs():
    return render_template("dogs.html", title="Dog Breed Classifier")
