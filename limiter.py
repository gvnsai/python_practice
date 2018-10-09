from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app=Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api')
@limiter.limit("5 per day")
def api():
	return 'hello'


if __name__ == '__main__':
	app.run(debug=True)