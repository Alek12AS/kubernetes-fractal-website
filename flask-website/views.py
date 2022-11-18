from flask import Blueprint, render_template, request
from koch_snowflake import draw_snowflake

views = Blueprint(__name__, 'views')

@views.route('/koch-snowflake')
def koch_snowflake():
    args = request.args
    order = args.get('order')
    draw_snowflake(int(order))
    return render_template('koch_snowflake.html', order=order)