# errors file for displaying error pages
from flask import render_template
from . import main

# the error handler
@main.app_errorhandler(404)
def four_O_four(error):
    '''
    function that renders the error 404 page
    '''
    render_template(four_O_four.html),404
