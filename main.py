# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#webapp2 is a lightweight
#Python web framework compatible with Google App Engine’s
import webapp2

#form that creates an empty field
#has a button to submit values
#sends to url /testform
#uses the method post and goes to
#post function
#GET includes data in the url and are used for fetching documents
#POST includes data in the request text, used for updating data

form = """
    <form method="post" action="/testform">
        <input name="q">
        <input type="submit">
    </form>
"""

#main page inherits from webapp2's requestHandler
#This is what draws the form
class MainPage(webapp2.RequestHandler):
    def get(self):
        #global response object that this framework uses
        #it sets a header with content type, we use
        #commented out because its making us send html
        #as plain text, so by commenting out on google app engine
        #default type is html
        #----> self.response.headers['Content-Type'] = 'text/plain'
        #Then we are writing a string 'Hello World!'
        self.response.write('Hello World!')
        #We can also print out our form stored in the form variable
        self.response.write(form)

#Gets called when we post to TestHandler
class TestHandler(webapp2.RequestHandler):
    def post(self):
        #gets the parameter from the client side
        q = self.request.get("q")
        #writes out the value of q to /testform
        self.response.out.write(q)
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write(self.request)

#URL Mapping Section
#One url just '/'
#maps to handler called MainPage
#Second url will be handled by testform
app = webapp2.WSGIApplication([
    ('/', MainPage), ('/testform', TestHandler)
], debug=True)
