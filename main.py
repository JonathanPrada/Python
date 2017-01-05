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
#Python web framework compatible with Google App Engines
import webapp2
import cgi

#Month list
months = ['January','February','March','April','May'
,'June','July','August','September','October','November','December']

#build a dictionary that maps name of the months
#to the first three letters of each of the months themselves
#so for m in months = january
#dict('jan':january)
#store dictionary in month abbvs
month_abbvs = dict((m[:3].lower(),m) for m in months)

#Checks valid months
def valid_month(month):
    if month:
        #takes first three letters of month and lowercases it
        #prepare the key for the dictionary
        short_month = month[:3].lower()
        #use Get function on dictionary to return the month
        #using the user value that was converted into a key
        return month_abbvs.get(short_month)

#Checks valid day
def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day > 0 and day <=31:
            return day

#Checks valid_year(year)
def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year > 1900 and year < 2020:
            return year

#uses the cgi method to escape code in text fields
def escape_html(s):
    return cgi.escape(s, quote = True)

#form that creates an empty field
#has a button to submit values
#sends to url /testform
#uses the method post and goes to
#post function
#GET includes data in the url and are used for fetching documents
#POST includes data in the request text, used for updating data

form = """
<form method="post" action="/">
        What is your birthday?
        <br>

        <label>
        month
                    <input type="text" name="%(month)s">
        </label>

        <label>
        day
                    <input type="text" name="%(day)s">
        </label>

        <label>
        year
                    <input type="text" name="%(year)s">
        </label>
        <div style="color: red">%(error)s</div>

        <br>
        <br>
        <input type = "submit">
</form>
"""

#main page inherits from webapp2's requestHandler
#This is what draws the form
class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        #We assign the error message using our escape function
        self.response.out.write(form % {"error": error,
                                        "month": escape_html(month),
                                        "day": escape_html(day),
                                        "year": escape_html(year)})

    def get(self):
        #global response object that this framework uses
        #it sets a header with content type, we use
        #commented out because its making us send html
        #as plain text, so by commenting out on google app engine
        #default type is html
        #----> self.response.headers['Content-Type'] = 'text/plain'
        #Then we are writing a string 'Hello World!'
        #self.response.write('Hello World!')
        #We can also print out our form stored in the form variable
        self.write_form()

    #When the form is submitted this runs
    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not (month and day and year):
            self.write_form("that does not look right to me",
                            user_month, user_year, user_day)
        else:
            self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks! Thats a totally valid day!")

#URL Mapping Section
#One url just '/'
#maps to handler called MainPage
#Second url will be handled by testform
app = webapp2.WSGIApplication([('/', MainPage), ('/thanks', ThanksHandler)], debug=True)
