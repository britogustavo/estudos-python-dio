contato = {
    "gustavo@gmail.com": {"Nome": "Gustavo", "Telefone": "2345-6546"}
}
print(contato)

contato.update({"gustavo@gmail.com": {"Nome": "Gu"}})
print(contato)

contato.update({"gustavo@gmail.com": {"Nome": "Gu", "Telefone": "2435-4345"}})
print(contato)
