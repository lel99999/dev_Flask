from django.http import request
from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

# configuration
DEBUG = True

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

SYSTEMS = [
    {
        'name': 'system1.example.com',
        'ip': '10.100.4.101',
        'service':{
            'ssh': '22',
            'http':'80',
            'dns': '53',
            'https': '443',
        }
     },
    {
        'name': 'system2.example.com',
        'ip': '10.100.4.102',
        'service':{
            'ssh': '22',
            'http':'80',
            'dns': '53',
            'https': '443',
        }
     },
    {
        'name': 'system3.example.com',
        'ip': '10.100.4.103',
        'service':{
            'ssh': '22',
            'http':'80',
            'dns': '53',
            'https': '443',
        }
     },
    {
        'name': 'system4.example.com',
        'ip': '10.100.4.104',
        'service':{
            'ssh': '22',
            'http':'80',
            'dns': '53',
            'https': '443',
        }
     },
    {
        'name': 'system5.example.com',
        'ip': '10.100.4.105',
        'service':{
            'ssh': '22',
            'http':'80',
            'dns': '53',
            'https': '443',
        }
     },
    
]

# instantiate app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/systems', methods=['GET', 'POST'])
def all_systems():
    return jsonify({
        'status': 'success',
        'systems': SYSTEMS
    })

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status':'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read'),
        })
        response_object['message'] = 'book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)
#   return jsonify({
#       'status': 'success',
#       'books': BOOKS
#   })

if __name__ == '__main__':
    app.run()
