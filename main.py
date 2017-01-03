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
                    <input type="text" name="month">
        </label>

        <label>
        day
                    <input type="text" name="day">
        </label>

        <label>
        year
                    <input type="text" name="year">
        </label>

        <br>
        <br>
        <input type = "submit">

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
        #self.response.write('Hello World!')
        #We can also print out our form stored in the form variable
        self.response.write(form)

    def post(self):
        user_month = valid_month (self.request.get('month'))
        user_day = valid_day (self.request.get('day'))
        user_year = valid_year (self.request.get('year'))

        if not (user_month and user_day and user_year):
            self.response.write(form)
        else:
            self.response.write("Thanks! Thats a totally valid day!")

#URL Mapping Section
#One url just '/'
#maps to handler called MainPage
#Second url will be handled by testform
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
