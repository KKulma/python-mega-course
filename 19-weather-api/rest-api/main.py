from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def api(station, date):
    filename = f'data_small/TG_STAID{str(station).zfill(6)}.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df[df['    DATE'] == date]['   TG'].squeeze()/10
    print(temperature)

    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }

# make sure that the app is run only if the main.py is executed directly and not imported by other scripts
if __name__ == "__main__":
    app.run(debug=True, port=5000) # make sure that if multiple apps are running simultanously then don't use the same port
