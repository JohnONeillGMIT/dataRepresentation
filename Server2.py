#IT WORKS!!!!!!!!!!! 04/01/2020
from flask import Flask, jsonify, request, abort
from DAO import emplDirectoryDAO#>pip install mysql-connector-python


app = Flask(__name__, static_url_path='',static_folder='.')
def index():
    return '<h1>DRProject</h1>'

#curl "http://127.0.0.1:5000/empldirectory"
@app.route('/empldirectory')
def getAll():
    results = emplDirectoryDAO.getAll()
    return jsonify(results)

# curl "http://127.0.0.1:5000/empldirectory/10001"
@app.route('/empldirectory/<int:id>')
def findByID(id):
    foundID = emplDirectoryDAO.findByID(id)

    return jsonify(foundID)


#curl -i -H "Content-Type:application/json" -X POST -d "{\"first_name\":\"Dave\",\"surname\":\"Evans\",\"Ext\":\"100104\"}" http://127.0.0.1:5000/empldirectory
@app.route('/empldirectory', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    #other checking
    employee = {
        "first_name": request.json['first_name'],
        "surname": request.json['surname'],
        "Ext": request.json['Ext'],
    }
    values = (employee["first_name"],employee["surname"],employee["Ext"])
    newID = emplDirectoryDAO.create(values)
    employee['id'] = newID
    return jsonify(employee)

#curl -i -H "Content-Type:application/json" -X PUT -d "{\"first_name\":\"a\"}" http://localhost:5000/empldirectory/10008
@app.route('/empldirectory/<int:id>', methods=['PUT'])
def update(id):
    findEmpl = emplDirectoryDAO.findByID(id)
    if not findEmpl:
      abort(404)
    if not request.json:
        abort(400)
    reqJson = request.json

    if 'first_name' in reqJson:
        findEmpl['first_name']= reqJson['first_name']
    if 'surname' in reqJson:
        findEmpl['surname']= reqJson['surname']
    if 'Ext' in reqJson and type(reqJson['Ext']) is not int:
        abort(400)
        findEmpl['Ext']= reqJson['Ext']
    values = (findEmpl['first_name'],findEmpl['surname'],findEmpl['Ext'],findEmpl['id'])
   
    emplDirectoryDAO.update(values)
    return jsonify(findEmpl)
 
    
#curl -X DELETE http://localhost:5000/empldirectory/10008
@app.route('/empldirectory/<int:id>', methods=['DELETE'])
def delete(id):
    emplDirectoryDAO.delete(id)
    return jsonify({"done":True})

if __name__== '__main__':
    app.run(debug= True)