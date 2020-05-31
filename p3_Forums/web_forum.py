
from flask import Flask, render_template
from flask import request

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)


app.config['SECRET_KEY'] = 'hard to guess string'

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    # name is a field
    # DataRequired() validator ensures that the field is not submitted empty.
    
    submit = SubmitField('Submit')
    # submitfield is standard HTML fields, eg.
    # FileField -for- File upload field
    # BooleanField -for- Checkbox 

# Flask-WTF requires a secret key to be configured
# in the application because this key is part of the mechanism
# the extension uses to protect all forms against cross-site request forgery (CSRF) attacks.

# A CSRF (sea-surf)attack occurs when a malicious website sends requests to the
# application server on which the user is currently logged in.
# basically, this attack steal the 'session token' from the user
# Flask-WTF generates security tokens for all forms and stores them in the user session, which is
# protected with a cryptographic signature generated from the secret key.


@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)




'''

  why we require a session or a token??

A.> tokens and session help our state to remember,
    For example, in a online site, after we put bananas in a shopping cart,
    we don’t want our bananas to disappear when we go to another page to buy apples.
    ie. we want our purchase state to be remembered while we navigate through the online site!

    To overcome the stateless nature of HTTP requests, we could use either a session or a token.

    so, whenever user login, user get a session id cookies and these cookies sent along with over request

    But, in token auth., server creates a secrete token which it sent to the user and get stored at user side.
    

'''
