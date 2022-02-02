import os
import subprocess
from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource

def CheckProc():
	checkProc = subprocess.check_output("pgrep -lf ssh | wc -l", shell=True)
	print 'checkProc: ', checkProc
	if int(checkProc) != 2:
		print 'no process'
	else:
		print 'check process'


app = Flask (__name__)
api = Api(app)

QUERY = {
	'test1' : {'test': 'test sample'},
	'test2' : {'test': 'test query'},
}

def abort_check(test):
	if test not in QUERY:
		abort(404, message="QUERY {} doesn't exist".format(test))

parser = reqparse.RequestParser()
parser.add_argument('test')

class Query(Resource):
	def get(self, test):
		abort_check(test)
		return QUERY[test]

	def delete(self, test):
		abort_check(test)
		del QUERY[test]
		return '', 204

	def put(self, test):
		args = parser.parse_args()
		test = {'test': arge['test']}
		QUERY[test] = test
		return test, 201

class QueryList(Resource):
	def get(self):
		return QUERY

	def post(self):
		args = parser.parse_args()
		test_id = 'test%d' % (len(QUERY) + 1)
		QUERY[test_id] = {'test': args['test']}
		return QUERY[test_id], 201
	
api.add_resource(QueryList, '/tests/')
api.add_resource(Query, '/tests/<string:test_id>')

@app.route('/')
def Test_Page():
	return "This is Test Page"

@app.route('/json_test')
def Hello_json():
	data = {'name' : 'jungwoo', 'age' : '29'}
	return jsonify(data)

@app.route('/server_info')
def server_json():
	data = { 'server_name' : '127.0.0.1', 'server_port' : '5000' }
	return jsonify(data)

@app.route('/success/<name>')
def success(name):
	return 'welcome %s ' % name

@app.route('/login', methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		user = request.form['myName']
		return redirect(url_for('success', name=user))
	else:
		user = request.args.get('myName')
		return redirect(url_for('success', name=user))


@app.route('/TestSample')
def Test_Sample():
	return "This is Test Sample"

@app.route('/TestQuery', methods = ['POST'])
def TestQuery():
	test = request.get_json()
	return jsonify(test)

@app.route('/environments/<language>')
def environments(language):
	return jsonify({"language":language})


if __name__ == "__main__":
	CheckProc()
	app.run(debug=True)
#app.run(host="127.0.0.1", port="8080")

