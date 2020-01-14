import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
    return "<h1>Nicky's Coding Challenge to Claranet</h1><p>This is the homepage of my API site.</p>"

#Create
@app.route('/api/v1/resources/entries/create', methods=['POST'])
def api_create():
    #TODO
    return null

#Read (or list as specified in the brief)
@app.route('/api/v1/resources/entries/all', methods=['GET'])
def api_listAll():
    conn = sqlite3.connect('entries.db')
    #conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM tblNotes;').fetchall()

    return jsonify(all_books)    

#Update or Delete
@app.route('/api/v1/resources/entries/update', methods=['PUT', 'DELETE'])
def api_update():
    if request.method == 'PUT':
        #TODO
        return null
    if request.method == 'DELETE':
        #TODO
        return null
        
#Error Handler
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 Error</h1><p>Sorry, there's been an error</p>", 404
 
app.run()