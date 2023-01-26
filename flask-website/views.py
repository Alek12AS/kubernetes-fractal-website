'''Define the website routes and the appropriate responses.
'''
from flask import Blueprint, render_template, request # pylint: disable=import-error
from koch_snowflake import draw_snowflake

views = Blueprint(__name__, 'views')

@views.route('/koch-snowflake')
def koch_snowflake():
    '''Draw the fractal based on the order number given and display it on the webpage.'''
    args = request.args
    order = args.get('order')
    draw_snowflake(int(order))
    return render_template('koch_snowflake.html', order=order)
