from email import message
import requests
import json
from flask import Flask, jsonify, request
app = Flask(__name__)

f= open('jsonfiles.json','a+')
json_object = json.loads(f.read())



#Read JSON data
@app.route('/', methods = ['GET','POST','DELETE'])
def read_data():
    try:
        if request.method == 'GET':
            return jsonify(json_object)
        else:
            return jsonify({'error':"data not found"})
    except FileNotFoundError:
        return({
            'Status': 404,
            'error':'Resource error'
        })


#Get data passing name parameter
@app.route('/api/name/<string:n>',methods = ['GET'])
def get_by_name(n):
    try:
        if(request.method == 'GET'):   
            for item in json_object:
                if item['name'] == n:
                    res= jsonify({'status':"Success",
                    "name":item['name'],
                    "country_code":item['alpha_two_code'],
                    "website":item['web_pages'],
                    'country':item['country']})   
        return res

    except FileNotFoundError:
        return({
            'Status': 404,
            'error':'Resource error'
        })
     
if __name__ == '__main__':
    app.run(debug=True)

#INSERT DATA
@app.route('/api/insert', methods = ['POST'])
def insert_cart():
    try:
     if request.method == 'POST':  
        body = request.get_json()      
        json_object.append(body)

        with open('example.json','w') as insert_data:
            json.dump(json_object,insert_data)

        return jsonify({
            '':200,
            'amessage': 'New item added successfully',
            'item':body
        })   

    except FileNotFoundError:
        return({
            'Status': 404,
            'error':'Resource error'
        })


# @app.route('/api/update/<string:name>',methods =['PUT'])
# def update(name):
#     if request.method == 'PUT':
    
#      try:
#         for item in json_object:
#             if item['name'] == name:
#                item['name']="Updated"           
                    
#         read_write_file("example.json","w",item['name'])
#         return jsonify({"status":"success"})  

#      except ValueError:
#         return jsonify({
#             'status': 'Error',
#             'message':'given name not found'
            
#         })    