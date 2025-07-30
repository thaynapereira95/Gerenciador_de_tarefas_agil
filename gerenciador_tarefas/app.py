from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
ARQUIVO = 'tarefas.json'


def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def salvar_tarefas(tarefas):
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)


tarefas = carregar_tarefas()

@app.route('/')
def index():
    return render_template('index.html', tarefas=tarefas)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    titulo = request.form.get('titulo')
    descricao = request.form.get('descricao')
    if titulo and descricao:
        tarefas.append({'titulo': titulo, 'descricao': descricao})
        salvar_tarefas(tarefas)
    return redirect('/')

@app.route('/remover/<int:index>')
def remover(index):
    if 0 <= index < len(tarefas):
        tarefas.pop(index)
        salvar_tarefas(tarefas)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
