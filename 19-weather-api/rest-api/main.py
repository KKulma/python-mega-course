from flask import Flask, render_template
import pandas as pd

port = 5000

app = Flask(__name__)
stations = pd.read_csv('data_small/stations.txt', skiprows=17)[['STAID','STANAME                                 ']]

@app.route("/")
def home():
    return render_template("home.html",
                           stations_tbl=stations.to_html(index=False),
                           port=port
                           )

@app.route("/api/v1/<station>/<date>")
def station_date(station, date):
    filename = f'data_small/TG_STAID{str(station).zfill(6)}.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df[df['    DATE'] == date]['   TG'].squeeze()/10
    print(temperature)

    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }

@app.route("/api/v1/<station>")
def station(station):
    filename = f'data_small/TG_STAID{str(station).zfill(6)}.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])

    return {
        "station": station,
        "data": df.to_dict(orient='records')
    }

@app.route("/api/v1/year/<station>/<year>")
def station_year(station, year):
    filename = f'data_small/TG_STAID{str(station).zfill(6)}.txt'
    df = pd.read_csv(filename, skiprows=20)
    df = df[df['    DATE'].astype(str).str.startswith(year)]

    return {
        "station": station,
        "data": df.to_dict(orient='records')
    }

# make sure that the app is run only if the main.py is executed directly and not imported by other scripts
if __name__ == "__main__":
    app.run(debug=True, port=port) # make sure that if multiple apps are running simultanously then don't use the same port
