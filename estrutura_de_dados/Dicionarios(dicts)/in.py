contatos = {
    "flavia@gmail.com": {'nome': "Flavia", 'idade': 44, 'telefone': '2333-2456'},
    "maria@gmail.com": {'nome': "Maria", 'idade': 22, 'telefone': '8765-2443'},
    "lucas@gmail.com": {'nome': "Lucas", 'idade': 29, 'telefone': '1213-3543'},
    "gabriel@gmail.com": {'nome': "Gabriel", 'idade': 25, 'telefone': '9786-2321'},
    "otavio@gmail.com": {'nome': "Otavio", 'idade': 32, 'telefone': '5673-3249'},
}

resultado = "flavia@gmail.com" in contatos
print(resultado)

resultado = "cassia@gmail.com" in contatos
print(resultado)

resultado = "altura" in contatos["lucas@gmail.com"]
print(resultado)

resultado = "idade" in contatos["lucas@gmail.com"]
print(resultado)