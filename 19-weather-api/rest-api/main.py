from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def api(station, date):
    temperature=23
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }

# make sure that the app is run only if the main.py is executed directly and not imported by other scripts
if __name__ == "__main__":
    app.run(debug=True, port=5000) # make sure that if multiple apps are running simultanously then don't use the same port
