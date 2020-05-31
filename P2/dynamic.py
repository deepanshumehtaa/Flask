# https://www.facebook.com/<your-name>,
# http://localhost:5000/user/Deepanshu
# 

from flask import Flask, render_template
app = Flask(__name__)


# route decorater, use for telling our app
# that whenever a user visits our app-domain ('/') or for given .route(),
# it execute the function given just below,
# so, it is a mapping function which map url with the particular web-page
@app.route('/')
def user():
	return render_template('index.html')   # templete
 

@app.route('/user/<name>')   # name is a variable, always decleared in <>
                             # for int type, <int:id>
def user(name):
        return render_template('user.html', name=name)

# templete are un-idirectional and they sense info. from the
# server to the browser,
# in order to post info to server, we need 'web forms'.
# POST requests, provides access to the user information through request.form.

if __name__ == '__main__':
	app.run(debug=1)
