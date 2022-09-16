from flask import Flask, request, jsonify
import json 
app = Flask(__name__)
@app.route('/api/', methods = ['GET', 'POST'])
def index():
      
       if request.method == "GET":
            with open(r'jsonfiles.json', 'r') as openfile:
              json_object = json.load(openfile)

            return jsonify(json_object)
            
#Create an API to return  firstname, lastname in lowercase along with status in JSON format  based on id provided.
@app.route('/api/users/<int:id>', methods=['GET']) #127.0.0.1:5000/api/users/7
def username(id):
    with open('jsonfiles.json', mode='r', encoding='utf-8') as file:
        employees = json.load(file)
        emp_name = dict()
        try:
            for employee in employees:
                if employee['id'] == id:
                    emp_name['first_name'] = employee['first_name'].lower()
                    emp_name['last_name'] = employee['last_name'].lower()
                    break
            if len(emp_name) == 0:
                raise 
            else:
                return jsonify({
                    'status': 200,
                    'message': 'Record retrieval successful',
                    'data': emp_name,
                    })
        except:
            return jsonify({
                'status': 404,
                'message': 'Record not found',
                'data': {},
            })

#Create an api where you take first_name, last_name, convert them to uppercase,
@app.route('/api/question/<int:id>', methods=['GET']) #127.0.0.1:5000/api/question/8
def name(id):
    with open('jsonfiles.json', mode='r', encoding='utf-8') as file:
        employees = json.load(file)
        emp_name = dict()
        try:
            for employee in employees:
                if employee['id'] == id:
                    emp_name['first_name'] = employee['first_name'].upper()
                    emp_name['last_name'] = employee['last_name'].upper()
                    break
            if len(emp_name) == 0:
                raise
            else:
                return jsonify({
                    'status': 200,
                    'message': 'Record retrieval successful',
                    'data': emp_name,
                    })
        except :
            return jsonify({
                'status': 404,
                'message': 'Record not found',
                'data': {},
            })

#Create an API to delete record based on id and return success message of id provided. 
@app.route('/api/delete/<int:id>',methods = ['GET', 'POST'])
def delete(id):
    f= open('jsonfiles.json','r')
    data = json.loads(f.read())
    f.close()
    try:
        for i in range(len(data)):
            try:
                if(data[i]['id']==id):
                    item1 = data[i]
                    del data[i]
            except:
                pass
        with open ('jsonfiles.json','w') as e:
            e.write(json.dumps(data))
        status = {'status':'success'}
        return f'<pre>{json.dumps(status,indent=4)}</pre><pre>{json.dumps(item1,indent=4)}</pre>'
    except:
        return '<p>Item not found</p>'

#insertnew record
@app.route('/api/insert/', methods = ['GET', 'POST', 'PUT'])
def insert():
    f= open('jsonfiles.json','r')
    data = json.loads(f.read())
    f.close()
    nd = {
            "id": data[-1]['id']+1,
            "email": "sanaya.ghimire@reqres.in",
            "first_name": "sanaya",
            "last_name": "ghimire",
            "avatar": "https://reqres.in/img/faces/9-image.jpg"
        }
    data.append(nd)
    with open ('jsonfiles.json','w') as e:
        e.write(json.dumps(data))
    status = {'status':'success'}
    return (f"<pre>{json.dumps(status,indent=4)}<pre><pre>{json.dumps(data[-1],indent=4)}</pre>")
#update
@app.route('/api/update/<int:id>',methods = ['GET','POST','PUT'])
def update(id):
    f= open('jsonfiles.json','r')
    data = json.loads(f.read())
    f.close()
    try:
        for i in range(len(data)):
            try:
                if(data[i]['id']==id):
                    lst=data[i]['email'].split('@')
                    
                    item1=lst[0]+'@fusemachines.com'
                    data[i]['email']=item1
            except:
                pass
        with open ('jsonfiles.json','w') as e:
            e.write(json.dumps(data))
        status = {'status':'success'}
        return f'<pre>{json.dumps(status,indent=4)}</pre><pre>{json.dumps(item1,indent=4)}</pre>'
    except:
        return '<p>Item not found</p>'
  # return "hello world!!"
if __name__=='__main__':
    app.run(debug=True)
