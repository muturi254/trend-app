from . import main

# View to the main index page
@main.route('/')
def index():
    return '<h1> Hello World </h1>'
