contatos = {
    "flavia@gmail.com": {'nome': "Flavia", 'idade': 44, 'telefone': '2333-2456'}
}

#contatos['chave'] KeyError

print(contatos.get('chave'))
print(contatos.get('chave', {}))
print(contatos.get('flavia@gmail.com', {}))