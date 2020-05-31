# https://www.facebook.com/<your-name>,
# http://localhost:5000/user/Deepanshu
# 

from flask import Flask
app = Flask(__name__)

#view function

@app.route('/user/<name>')
def user(name):
 return '<h1>Hello, {}!</h1>'.format(name)


if __name__ == '__main__':
 app.run()
