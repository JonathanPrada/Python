import os
import jinja2
import webapp2

#using os library, concatenate two file names. the current directory
#and then the word templates, so mydirectory/templates
template_dir = os.path.join(os.path.dirname(__file__), 'templates')

#Instantiate the jinja2 environment
#When we render templates tell jinja to look in the directory defined
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

#Contains the html which describes the hidden inputs
hidden_html = """
<input type="hidden" name="food" value="%s">
"""

#List item that goes inside the shopping_list_htm
item_html = "<li>%s</li>"

#Renders the shopping list
shopping_list_html = """
<br>
<br>
<h2>Shopping List</h2>
<ul>
%s
</ul>
"""

#Contains method called write
class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    #render_str and render are functions commonly used
    #takes a file name and extra parameters
    def render_str(self, template, **params):
        #we use the jinja_env, this tells jinja
        #to get template and give it a file name
        t = jinja_env.get_template(template)
        #returns parameters
        return t.render(params)

    #takes a template and extra parameters
    def render(self, template, **kw):
        #self.write which writes to browser wraps renders_str
        self.write(self.render_str(template, **kw))

#Inherits from class Handler
class MainPage(Handler):
    def get(self):
        #Gets any all the items attached to n in the url
        n = self.request.get("n")
        #If n was specified
        #convert into int as all get requests expect strings
        if n:
            n = int(n)
        #return the empty form
        self.render("shopping_list.html", n=n)

        # #draw the form
        # output = form_html
        # output_hidden = ""

        # #Gets any all the items attached to food in the url
        # items = self.request.get_all("food")
        # if items:
        #     output_items = ""

        #     #for each item in items
        #     for item in items:
        #         #build a list, where individual items are stored like this
        #         #[<input type="hidden" name="food" value="item">]
        #         output_hidden = output_hidden + (hidden_html % item)

        #         #build a list, where individual items are stored like this
        #         #[item_html = "<li>item</li>"]
        #         output_items = output_items + (item_html % item)

        #     #put all of values of the output_items list into the shopping list
        #     output_shopping = shopping_list_html % output_items
        #     #put the complete shopping list at end of output
        #     output = output + output_shopping

        # #we substitute items in output with our hidden list items
        # output = output % output_hidden

        # #we write it
        # self.write(output)

#Inherits from class Handler
class FizzBuzzHandler(Handler):
    def get(self):
        #gets the url n = number assigned, defaults to 0
        n = self.request.get("n", 0)
        #shorter way of converting to int
        n = n and int (n)
        #calls the render method
        self.render("fizzbuzz.html", n = n)

app = webapp2.WSGIApplication([('/', MainPage),
    ('/fizzbuzz', FizzBuzzHandler),
    ], debug=True)
