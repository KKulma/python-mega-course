from flask import Flask, render_template

app = Flask(__name__)

# it will run at localhost:5000
@app.route('/')
def home():
    # refers to a file name stored in the templates folder
    # return render_template(home.html)
    return render_template('home.html')
@app.route('/about/')
def about():
    return render_template('about.html')

# if this script is executed, it assigns '__main__' to __name__, if it's imported by another script, __name___ will equal '00-flask', or a script name
if __name__ == "__main__":
    app.run(debug=True)
