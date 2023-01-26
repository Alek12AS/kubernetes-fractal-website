'''Run Flask Framework.
'''
from flask import Flask # pylint: disable=import-error
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
