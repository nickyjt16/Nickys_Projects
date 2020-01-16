import flask
from flask import request, jsonify
import sqlite3
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

#helper function for returning all notes
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return "<h1>Nicky's Coding Challenge to Claranet</h1><p>This is the homepage of my API site.</p>"

#Create
@app.route('/api/v1/resources/notes/', methods=['POST'])
def api_create():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    newNote = request.args.get('newNote')
    user = request.args.get('user')
    params = (newNote, user)
    conn.execute('INSERT INTO Notes (Note, User) VALUES (?, ?)', params)
    conn.commit()
    conn.close()
    return "Your new note has been logged in the system"

#Read (or list as specified in the brief)
@app.route('/api/v1/resources/notes/all', methods=['GET'])
@app.route('/api/v1/resources/notes/', methods=['GET'])
def api_listAll():
    conn = sqlite3.connect('notes.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    allNotes = cur.execute('SELECT * FROM Notes;').fetchall()

    return jsonify(allNotes)    

#Update or Delete
@app.route('/api/v1/resources/notes/update', methods=['PUT', 'DELETE'])
def api_update():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    #sql = "SELECT
    if request.method == 'PUT':
        id = request.args.get('ID')
        return null
    if request.method == 'DELETE':
        #TODO
        return null
        
app.run()