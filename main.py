from flask import Flask, render_template
import markdown2
import os

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html', the_title='么 Itnaava 么')

@app.route("/blog")
def blog_page():
    dir_lis = list_dir('pages/blog')
    d={}
    for i in dir_lis:
        temp, article_info = md_to_html("pages/blog/"+i)
        article_info['url']="/"+article_info['slug']
        if (i[:-3]==article_info['slug']):
            d[article_info['title']]=[article_info['date']]+[article_info['url']]
    return render_template('blog.html', file_dict=d)

@app.route("/blog/<url>")
def md_test(url):
    with open('templates/new.html', 'w') as f:
        body, article_info = md_to_html("pages/blog/"+url+'.md')
        body = "{% extends 'base.html' %} {% block body %}\n"+'<p class=post_date>' + \
            article_info['date']+'</p>\n'+'<h1>'+article_info['title']+'</h1>\n' + \
            '<h2 class="subtitle">' + \
            article_info['subtitle']+'</h2>\n'+body+"\n{% endblock %}"
        f.writelines(body)
    return render_template('new.html')

@app.errorhandler(404)
def page_404(e):
    return render_template('404.html'),404

def list_dir(path):
    dir_list = os.listdir(path)
    return dir_list

def md_to_html(file_path):
    with open(file_path) as f:
        content = f.read()
    html_cont = markdown2.markdown(
        content, extras=['metadata', 'fenced-code-blocks', 'pyshell'])
    meta_data = html_cont.metadata
    return html_cont, meta_data

if __name__ == '__main__':
    app.run(debug=True)
