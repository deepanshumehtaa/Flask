# https://www.facebook.com/<your-name>,
# http://localhost:5000/user/Deepanshu
# cd/p1

from flask import Flask
from flask import request   # to access the data which sent to the user function
from flask import jsonify  

app = Flask(__name__)

# route with HTTP Methods
# by-default .route only answer to 'GET' requests
@app.route('/', methods = ['POST'])  

#view function
# the "endpoint" is an identifier that is used
# to determining which logical unit of your code should handle the request. 
def hello():
        message = request.get_json(force = 1)  # getting the data filled by user
        name = message['name']

        response = {
                'greeting' : 'Hey,' + name + '!'
                }
        
	return jsonify(response)

 
#@app.route('/user/<name>')
#def user(name):
#	return '<h1>Hello, {}!</h1>'.format(name)

@app.errorhandler(404)
def page_not_found(e):
        return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
        return render_template('500.html'), 500

if __name__ == '__main__':
	app.run(debug=1)
