from flask import Flask, render_template
import os
# create a flask object (flask needs an object to represent the application)
app = Flask(__name__) 
 
# The route decorator '@app.route()' maps a function to a route on your website.  
# decorators are used to map a function, index(), to a web page, / or  
# i.e., when someone types in the home address of the web site, 
# flask will run the function index() 
# summary: type in a URL, flask check the URL, finds the associate function with it, runs the function,  collect responses, and send back the results to the browser.

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/aboutus/')
def aboutus():
	return render_template('aboutus.html')
	
@app.route('/books/')
def books():
	return render_template('books.html')

@app.route('/authors/')
def authors():
	return render_template('authors.html')
	
@app.route('/publishers/')
def publishers():
	return render_template('publishers.html')

def static_file_hash(filename):
  return int(os.stat(filename).st_mtime)


# The following function handles caching problems
# that prevent the local host from displaying
# the updated static files.
# Pasted directly from https://gist.github.com/Ostrovski/f16779933ceee3a9d181
@app.url_defaults
def hashed_url_for_static_file(endpoint, values):

    if 'static' == endpoint or endpoint.endswith('.static'):

        filename = values.get('filename')

        if filename:

            if '.' in endpoint:  # has higher priority

                blueprint = endpoint.rsplit('.', 1)[0]

            else:

                blueprint = None  # can be None too



            if blueprint:

                static_folder = app.blueprints[blueprint].static_folder

            else:

                static_folder = app.static_folder



            param_name = 'h'

            while param_name in values:

                param_name = '_' + param_name

            values[param_name] = static_file_hash(os.path.join(static_folder, filename))

            


	
# if app.py is run directly, i.e., as the main module, it will be assigned the value main # and if it's main go ahead and run the application. 
# if this application is imported, then the __name__ is no longer __main__ and  
# the code, app.run(), will not be executed 

if __name__ == "__main__":
	app.run() 
 
 
