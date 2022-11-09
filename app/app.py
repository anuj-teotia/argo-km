from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def home():
	return json.dumps({'result': 'Argo-KM'})

if __name__== "__main__":
	app.run(host='0.0.0.0',port=80)