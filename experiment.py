import os
import webapp2

#Contains our basic html form
#Inside the form we are adding the hidden inputs
form_html = """
<form>
<h2>Add a Food</h2>
<input type="text" name="food">
%s
<button>Add</button>
</form>
"""

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

#Inherits from class Handler
class MainPage(Handler):
    def get(self):

        #draw the form
        output = form_html
        output_hidden = ""

        #Gets any all the items attached to food in the url
        items = self.request.get_all("food")
        if items:
            output_items = ""

            #for each item in items
            for item in items:
                #build a list, where individual items are stored like this
                #[<input type="hidden" name="food" value="item">]
                output_hidden = output_hidden + (hidden_html % item)

                #build a list, where individual items are stored like this
                #[item_html = "<li>item</li>"]
                output_items = output_items + (item_html % item)

            #put all of values of the output_items list into the shopping list
            output_shopping = shopping_list_html % output_items
            #put the complete shopping list at end of output
            output = output + output_shopping

        #we substitute items in output with our hidden list items
        output = output % output_hidden

        #we write it
        self.write(output)

app = webapp2.WSGIApplication([('/', MainPage),], debug=True)
