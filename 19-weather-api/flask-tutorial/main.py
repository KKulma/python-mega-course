from flask import Flask, render_template

app = Flask("Website")

@app.route("/home/")
def home():
    return render_template("flask-tutorial.html")

@app.route("/about/")
def about():
    return render_template("about.html")

# make sure that if multiple apps are running simultanously then don't use the same port
app.run(debug=True, port=5001)