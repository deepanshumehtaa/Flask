from flask import Flask
app = Flask(__name__)

@app.route('/')     # Routes, refring the web page, 
					# "/" this shows 'root url' or 'index page'
					
					
def index():        # also known as "view functions"
 return '<h1>Hello World, by Deepanshu !! </h1>'

# app.add_url_rule('/', 'index', index)   # equalent to above