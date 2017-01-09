#Use the numbers to understand the path flow

import os
import re
from string import letters

import webapp2
import jinja2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

#2
#This class has two functions.
#The get function renders the rot13-form.html file
#Go to the rot13-form.html file to follow logic
class Rot13(BaseHandler):
    def get(self):
        self.render('rot13-form.html')

    def post(self):
        rot13 = ''
        text = self.request.get('text')
        if text:
            rot13 = text.encode('rot13')

        self.render('rot13-form.html', text = rot13)

#8
#regular expressions
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    #if it is not blank and matches regular expression
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

#Here we handle the optional email by use not and or
EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

#4
#renders the sign up form page
class Signup(BaseHandler):

    def get(self):
        self.render("signup-form.html")

    #6
    #gets the variables returned by the html form
    #applies algorithms
    def post(self):
        #If the files makes it through without error
        #the variable below remains as false
        #otherwise we render the error
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        #9
        #These are parameters we send back into rendering
        #Dictionary will grow with more parameters given in
        #by the below if not valid functions
        params = dict(username = username,
                      email = email)

        #7
        #Then we run each of the inputs through the
        #validation functions
        if not valid_username(username):
            params['error_username'] = "That's not a valid username."
            have_error = True

        if not valid_password(password):
            params['error_password'] = "That wasn't a valid password."
            have_error = True
        elif password != verify:
            params['error_verify'] = "Your passwords didn't match."
            have_error = True

        if not valid_email(email):
            params['error_email'] = "That's not a valid email."
            have_error = True

        #10
        #Lastly, if we have errors then render sign up page
        #With the username and email previously given
        #Else give us a welcome page with the username passed
        if have_error:
            self.render('signup-form.html', **params)
        else:
            #This redirects to handler which redirects to step 11
            self.redirect('/unit2/welcome?username=' + username)

#11
#Class that handles the welcome page
#Checks if valid username passed then go ahead
#Else return to sign up
class Welcome(BaseHandler):
    def get(self):
        username = self.request.get('username')
        if valid_username(username):
            self.render('welcome.html', username = username)
        else:
            self.redirect('/unit2/signup')

#1
#We have the different website handlers referenced
#Each path maps to the relevant class
app = webapp2.WSGIApplication([('/unit2/rot13', Rot13),
                               ('/unit2/signup', Signup),
                               ('/unit2/welcome', Welcome)],
                              debug=True)
