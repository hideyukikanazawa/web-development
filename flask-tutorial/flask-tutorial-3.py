from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/admin/<usr>/")
def user(usr):
    return render_template("user.html", user=usr)


if __name__ == "__main__":
    app.run(host="localhost", port="1313", debug=True)