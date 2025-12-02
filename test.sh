
curl -X POST http://127.0.0.1:5000/notes \
     -H "Content-Type: application/json" \
     -d '{"title": "First Note", "content": "This is my first note"}'


curl http://127.0.0.1:5000/notes

curl http://127.0.0.1:5000/notes/1

curl -X PUT http://127.0.0.1:5000/notes/1 \
     -H "Content-Type: application/json" \
     -d '{"title": "Updated Note", "content": "Updated content"}'


curl -X DELETE http://127.0.0.1:5000/notes/1
