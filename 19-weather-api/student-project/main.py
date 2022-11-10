from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>/")
def api(word):
    df = pd.read_csv('dictionary.csv')
    definition = df[df['word'] == str(word).lower()]['definition'].squeeze()
    # print(definition)
    return {
        "defintion": definition,
        "word": word
    }

# make sure that the app is run only if the main.py is executed directly and not imported by other scripts
if __name__ == "__main__":
    app.run(debug=True, port=5002) # make sure that if multiple apps are running simultanously then don't use the same port