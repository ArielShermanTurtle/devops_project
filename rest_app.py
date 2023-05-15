import db_connector
from flask import Flask, request

app = Flask(__name__)

# local users storage
users = {}
# supported methods

def get_user_name(user_id):
    user_name_from_db = get_user_name_from_db(user_id)
    #todo: check if not error/ not empty Sting
    #other to send a diffrent message
    return db_connector.get_user_name_from_db(user_id)