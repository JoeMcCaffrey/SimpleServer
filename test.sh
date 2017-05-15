curl -X	GET	http://localhost:4000/key

curl -X	POST http://localhost:4000/set	-d	'{"key": "value"}'	-H	"Content-Type: application/json"

curl -X	GET	http://localhost:4000/key

curl -X	POST http://localhost:4000/commit

curl -X	POST http://localhost:4000/set	-d	'{"key": "2"}'	-H	"Content-Type: application/json"

curl -X	GET	http://localhost:4000/key

curl -X	POST http://localhost:4000/commit

curl -X	DELETE	http://localhost:4000/set -d '"key"' -H	"Content-Type: application/json"

curl -X	GET	http://localhost:4000/key

curl -X	POST http://localhost:4000/commit

curl -X	GET	http://localhost:4000/key
