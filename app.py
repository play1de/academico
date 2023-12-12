import os
import csv
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inserir_time', methods=['GET', 'POST'])
def inserir_time():
    if request.method == 'POST':
        nome = request.form['nome_time']
        itinerario = request.form['itinerario']
        nota1 = request.form['nota1']
        nota2 = request.form['nota2']
        nota3 = request.form['nota3']

        with open('brasileirao2023.csv', 'a', newline='') as csvfile:
            fieldnames = ['Nome', 'Itinerario', 'Nota1', 'Nota2', 'Nota3']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not os.path.exists('rendimentos.csv'):
                writer.writeheader()

            writer.writerow({'Nome': nome, 'Itinerario': itinerario, 'Nota1': nota1, 'Nota2': nota2, 'Nota3': nota3})

    return render_template('inserir_time.html')

@app.route('/exibir_tabela')
def exibir_tabela():
    todos = []
    with open('brasileirao2023.csv','r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ordem = row['classif']
            nome = row['nome']
            todos.append({'Classif':ordem,'Nome': nome})

    print(todos)
    return render_template('exibir_tabela.html', todos=todos)

if __name__ == '__main__':
    app.run(debug=True)
