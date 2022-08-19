from flask import Flask,render_template
# import markdown2
import os


app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html',the_title='么 Itnaava 么')

@app.route("/blog")
def blog_page():
    l=list_dir('C://Users//surya//Desktop//Void//Antlia//么 Itnaava 么//pages//blog')
    return render_template('blog.html',file_list=l)
    
def list_dir(path):
    dir_list=os.listdir(path)
    return dir_list

# def md_to_html():

app.run(debug=True)
