from flask import Flask, request
import rest_app

app = Flask(__name__)

# local users storage
users = {}
# supported methods
@app.route('/users/get_user_data/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
  return rest_app.get_user_name(user_id)


app.run(host='127.0.0.1', debug=True, port=5001)