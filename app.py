import os
import csv
from flask import Flask, render_template, request, redirect, url_for
from operator import itemgetter, attrgetter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inserir_time', methods=['GET', 'POST'])
def inserir_time():
    if request.method == 'POST':
        nome = request.form['nome']
        golsM = request.form['golsM']
        golsS = request.form['golsS']

        with open(verificar_arquivo(), 'a', newline='') as csvfile:
            ordered_fieldnames = ['nome', 'golsM', 'golsS']
            writer = csv.DictWriter(csvfile, fieldnames=ordered_fieldnames)
            writer.writerow({'nome': nome, 'golsM': golsM, 'golsS': golsS})

    return render_template('inserir_time.html')

@app.route('/exibir_tabela')
def exibir_tabela():
    todos = []
    arquivo = verificar_arquivo()
    with open(arquivo,'r',encoding="utf8",errors="ignore", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            nome = row['nome']
            golsM = row['golsM']
            golsS = row['golsS']
            todos.append({'nome': nome, 'golsM': golsM, 'golsS': golsS, 'Sgols':int(golsM) - int(golsS)})

        print(todos.sort(reverse=True,key=classificar))

    return render_template('exibir_tabela.html', todos=todos)

def verificar_arquivo():
    arquivo = os.path.join(os.path.dirname(os.path.realpath(__file__)),'static','brasileirao2023.csv')
    if(not os.path.isfile(arquivo)):
        with open(arquivo, 'a', encoding="utf8",errors="ignore", newline='') as logfile:
            logfile.write("nome,golsM,golsS")
    return arquivo

def classificar(e):
    return e['Sgols']
        
if __name__ == '__main__':
    app.run(debug=True)
