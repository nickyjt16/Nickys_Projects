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
    response_object = {'status': 'success'}
    post_data = request.get_json()
    newNote = post_data.get('note')
    newUser = post_data.get('user')
    sql = """INSERT INTO Notes (Note, User) VALUES (?,?)"""
    conn = sqlite3.connect('notes.db')
    cur = conn.cursor()
    params = (newNote, newUser)
    cur.execute(sql, params)
    conn.commit()
    conn.close()
    return jsonify(response_object)

#Read (or list as specified in the brief)
@app.route('/api/v1/resources/notes/all', methods=['GET'])
@app.route('/api/v1/resources/notes/', methods=['GET'])
def api_listAll():
    response_object = {'status': 'success'}
    conn = sqlite3.connect('notes.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    allNotes = cur.execute('SELECT * FROM Notes;').fetchall()
    response_object['notes'] = allNotes
    conn.close()
    return jsonify(response_object)    

#Update or Delete
@app.route('/api/v1/resources/notes/<noteID>', methods=['PUT', 'DELETE'])
def api_update(noteID):
    response_object = {'status': 'success'}
    conn = sqlite3.connect('notes.db')
    cur = conn.cursor()
    #sql = "SELECT
    if request.method == 'PUT':
        return null
    if request.method == 'DELETE':
        sql = """DELETE FROM Notes WHERE id = ?"""
        params = noteID
    cur.execute(sql, params)
    conn.commit()
    conn.close()
    return jsonify(response_object)  
        
if __name__ == '__main__':
    app.run()