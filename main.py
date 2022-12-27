from flask import Flask,redirect,url_for,render_template,request,jsonify
from users import Users
import jwt
import datetime

app=Flask(__name__)


app.config['SECRET_KEY'] = 'thisissecret'

@app.route('/',methods=['GET','POST'])
def Welcome():
    return jsonify(
        {"message":"Welcome",
        "Show All Users":"/users",
        "Show one user":"/users/Nameusuario",
        "Add User":"/users/add'",
        "Delete user": "users/delete/<string:username",
        "update":"users/update/<string:username"}
        )
#Mostrar todos los usuarios
@app.route('/users')
def ShowAllUsers():
    return jsonify(Users)

#Mostrar un usuario por su usuario
@app.route('/users/<string:username>')
def ShowOneUser(username):
    for user in Users:
        if username==user["Usuario"]:
            return jsonify(user)
        else:
            return "User no encontrado"
        
#Agregar usuario
@app.route('/users/add', methods=['POST'])
def AddUser():
    NewUser={"Primer nombre": request.json['Primer nombre'],
        "Segundo nombre":request.json['Segundo nombre'],
        "Primer apellido":request.json['Primer apellido'],
        "Segundo apellido":request.json['Segundo apellido'],
        "Edad":request.json['Edad'],
        "Genero":request.json['Genero'],
        "Empresa":request.json['Empresa'],
        "Email":request.json['Email'],
        "Telefono":request.json['Telefono'],
        "Celular":request.json['Celular'],
        "Dirección":request.json['Dirección'],
        "Usuario":request.json['Usuario'],
        "Contraseña":request.json['Contraseña']}
    Users.append(NewUser)
    return jsonify(Users)

#Eliminar User
@app.route('/users/delete/<string:username>',methods=['DELETE'])
def DeleteUser(username):
    UserToDelete=[user for user in Users if username==user['Usuario']]
    Users.remove(UserToDelete[0])
    return jsonify(Users)

#Actualizar Usuario
@app.route('/users/update/<string:username>', methods=['PUT'])
def UpdateUser(username):
    UserToUpdate=[user for user in Users if username==user['Usuario']]    
    if len(UserToUpdate) > 0:
        UserToUpdate[0]["Primer nombre"] =request.json['Primerx nombre']
        UserToUpdate[0]["Segundo nombre"]=request.json['Segundo nombre']
        UserToUpdate[0]["Primer apellido"]=request.json['Primer apellido']
        UserToUpdate[0]["Segundo apellido"]=request.json['Segundo apellido']
        UserToUpdate[0]["Edad"]=request.json['Edad']
        UserToUpdate[0]["Genero"]=request.json['Genero']
        UserToUpdate[0]["Empresa"]=request.json['Empresa']
        UserToUpdate[0]["Email"]=request.json['Email']
        UserToUpdate[0]["Telefono"]=request.json['Telefono']
        UserToUpdate[0]["Celular"]=request.json['Celular']
        UserToUpdate[0]["Dirección"]=request.json['Dirección']
        UserToUpdate[0]["Usuario"]=request.json['Usuario']
        UserToUpdate[0]["Contraseña"]=request.json['Contraseña']
        return jsonify(Users)
    
#////////////////////////////////////////////////////////////////////////
@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    if data['username']==Users[0]['Usuario']:
        if data['contraseña']==Users[0]['Contraseña']:  
            token = jwt.encode({'public_id' : data, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            return token.encode("UTF-8")
        else:
            response=jsonify({"message":"clave incorrecta"})   
            response.status=404
            return response               
    else:
        response=jsonify({"message":"user not found"})
        response.status_code=404
        return response
    
    
    
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)