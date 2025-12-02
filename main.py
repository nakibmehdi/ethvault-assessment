from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage note will contains Dict of notes
notes = []
current_id = 1 #unique id


# Create note
@app.route('/notes', methods=['POST'])
def create_note():
    global current_id
    data = request.get_json()

    new_note = {
        "id": current_id,
        "title": data.get("title"),
        "content": data.get("content")
    }
    current_id += 1
    notes.append(new_note)

    return jsonify(new_note), 201


# get all notes
@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)


# Get specific note
@app.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    note = next((n for n in notes if n["id"] == note_id), None)
    if not note:
        return jsonify({"error": "Note not found"}), 404
    return jsonify(note)


# Update note
@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    note = next((n for n in notes if n["id"] == note_id), None)
    if not note:
        return jsonify({"error": "Note not found"}), 404

    data = request.get_json()
    note["title"] = data.get("title", note["title"])
    note["content"] = data.get("content", note["content"])

    return jsonify(note)


# Delete note
@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    global notes
    notes = [n for n in notes if n["id"] != note_id]
    return jsonify({"message": f"Note {note_id} deleted"})


if __name__ == '__main__':
    app.run(debug=True)
