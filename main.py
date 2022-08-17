from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html',the_title='么 Itnaava 么')

@app.route("/blog")
def blog_page():
    return render_template('')     
app.run(debug=True)
