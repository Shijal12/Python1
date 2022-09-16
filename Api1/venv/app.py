from flask import Flask, request, jsonify
import json 
app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def index():
      
       if request.method == "GET":
            with open(r'C:/Users/User/Desktop/Flask_Task/venv/data.json', 'r') as openfile:
              json_object = json.load(openfile)

            return jsonify(json_object)
            
            #Create an API to return  firstname, lastname in lowercase along with status in JSON format  based on id provided.
@app.route('/api/users/<int:id>', methods=['GET']) #127.0.0.1:5000/api/users/1001
def username(id):
    with open('data.json', mode='r', encoding='utf-8') as file:
        employees = json.load(file)
        emp_name = dict()
        try:
            for record in employees:
                if record['id'] == id:
                    emp_name['firstName'] = record['firstName'].upper()
                    emp_name['lastName'] = record['lastName'].upper()
                    break
            if len(emp_name) == 0:
                raise ValueNotFound
            else:
                return jsonify({
                    'status': 200,
                    'message': 'Record retrieval successful',
                    'data': emp_name,
                    })
        except ValueNotFound:
            return jsonify({
                'status': 404,
                'message': 'Record not found',
                'data': {},
            })

  # return "hello world!!"
if __name__=='__main__':
    app.run(debug=True)
