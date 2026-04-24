a = int(input())
b = int(input())
PROD = a * b
print('PROD =', PROD)














#def menor(*args):
#    menor_numero = args[0]
#    
#    for numero in args:
#        if numero < menor_numero:
#            menor_numero = numero
#    
#    return menor_numero
#print(menor(2227, 444, 1334, 6522, 3224, 871))


#def contar_vogais(palavra):
#    palavra = palavra.strip()
#
#    if not palavra:
#        return 'Palavra inválida'
#
#    contador = 0
#
#    for letra in palavra:
#        if letra.lower() in 'aeiou':
#            contador += 1
#    
#    return f'{contador} vogais'

#palavra = input('Insira uma palavra: ')
#print(contar_vogais(palavra))


#def login(usuario, senha):
#    usuario = usuario.strip()
#    senha = senha.strip()
#    if not usuario or not senha:
#        return 'Preencha todos os campos!'
#    
#    if len(senha) < 6:
#        return 'A senha deve ter pelo menos 6 caracteres!'
#    
#    return 'Login Enviado com Sucesso!'
#
#usuario = input('Usuário: ')
#senha = input('Senha: ')
#print(login(usuario, senha))
  

#def idade_valida(idade):
#    if idade < 0 or idade > 140:
#        return 'Idade Inválida'
#    
#    elif idade < 18:
#        return 'Menor de Idade'
#    
#    else:
#        return 'Maior de Idade'
#
#idade = int(input('Idade: '))
#print(idade_valida(idade))
    
#def nome_valido(nome, sobrenome):
#    nome = nome.strip()
#    sobrenome = sobrenome.strip()
#    if not nome or not sobrenome:
#        return 'Nome Invalido!'
#    
#    return f'Olá, {nome.title()} {sobrenome.title()}!'
#
#nome = input('Nome: ')
#sobrenome = input('Sobrenome: ')
#print(nome_valido (nome, sobrenome))


#def Saudação(nome):
#    nome = nome.strip()
#    if not nome:
#        return 'Nome Inválido!'
#    return f'Olá, {nome.title()}!'
#
#nome = input('Nome: ')
#print(Saudação(nome))