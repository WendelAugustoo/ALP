from valida_cpf import valida_cpf
from valida_data import valida_data
import random

def cadastrar():
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    cpf = input("Digite seu CPF (no formato xxx.xxx.xxx-xx): ")
    while(not valida_cpf(cpf)):
        print("CPF invalido")
        cpf = input("Digite seu CPF (no formato xxx.xxx.xxx-xx): ")

    nascimento = input("Digite sua data de nascimento (no formato DD/MM/AAAA): ")
    while(not valida_data(nascimento)):
        print("Data de nacimento invalida")
        nascimento = input("Digite sua data de nascimento (no formato DD/MM/AAAA): ")

    rendaBruta = input("Digite sua renda bruta: ")


    print(f"Cadastro realizado para {nome} {sobrenome}")

def mensagem():
     mensagens = [
         "A persistência realiza o impossível",
         "Seus sonhos não precisam de plateia, eles só precisam de você",
         "A persistência é o caminho do êxito",
         "No meio da dificuldade encontra-se a oportunidade"]

     aleatoria = random.choice(mensagens)

     print(f"{aleatoria}")

def sair():
    print("Bye Bye!")