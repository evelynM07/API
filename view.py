from flask import Flask, jsonify
from main import app, con

@app.route('/Livros', methods=['GET'])
def livros():
    cur = con.cursor()
    cur.execute('SELECT id_livro, titulo, autor, ano_publicacao FROM livros')
    livros = cur.fetchall()
    livros_dic = []
    for livro in livros:
        livros_dic.append({
            'id_livro': livro[0]
            , 'titulo': livro[1]
            , 'autor': livro[2]
            , 'ano_publicacao': livro[3]
        })
        return jsonify(mensagens='Lista de livros', livros=livros_dic)