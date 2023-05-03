from flask import Flask,jsonFy,request
import mysql.connector

app= Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="*********",
  database="empresaadvance"
)

@app.route('/api/empresaadvance/nome', methods=['GET'])
def get_nome():
   
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM funcionarios")
    nome = mycursor.fetchall()
    return jsonify(nome)

@app.route('/api/empresaadvance/adiconar', methods=['POST'])
def add_cadastro():
    
    nome = request.json['nome']
    idade = request.json['idade']
    cargo = request.json['cargo']

    
    mycursor = mydb.cursor()
    sql = "INSERT INTO funcionarios (nome) VALUES (%s)"
    val = (nome, idade, cargo)
    mycursor.execute(sql, val)
    mydb.commit()

    
    return jsonify({'message': 'Cadastro adicionado com sucesso!'})



@app.route('/api/empresaadvance/deletar', methods=['DELETE'])
def delete_cadastro(cadastro_id):
    
    mycursor = mydb.cursor()
    sql = "DELETE FROM funcionarios WHERE id = %s"
    val = (cadastro_id,)
    mycursor.execute(sql, val)
    mydb.commit()