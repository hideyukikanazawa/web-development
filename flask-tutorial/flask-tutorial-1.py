from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
user = ""

@app.route("/")
def home():
    return render_template("index.html", content=["peiwen", "zhanhui", "junxiong"])


@app.route("/login/<name>/")
def login(name):
    global user
    user = name
    return f"<h1>Heyyyyyy {user}! Welcome</h1>"


@app.route("/unauthorized/")
def unauthorized():
    return f"<h2>Sorry {user}, you're not authorized to view this page :(</h2><br>"


@app.route("/admin/")
def admin():
    if user == "hidey":
        return f"<h1>Welcome {user}! You are logged in to admin console!"
    else:
        return redirect(url_for(endpoint="unauthorized"))


if __name__ == "__main__":
    app.run(host="localhost", port="1313", debug=True)