'''
EQUIPE:
Henrique Martins - RM 563620
Henrique Texeira - RM 563088
Henrique Pacheco - RM 562086

TITULO: Utilizamos o site FSymbols para personalizar o titulo em ASCII ART e simbolos. 
OS: Utilizamos o módulo OS para limpar o terminal e deixar o programa mais limpo.
'''

import os

usuarios = []
agendamentos = []

def exibir_titulo():
    print('-=≡≣ *======================================================================* ≣≡=-')
    print('''

██████╗░██╗░░██╗  ░░░░░░  ░██████╗██╗░██████╗████████╗███████╗███╗░░░███╗░█████╗░
╚════██╗██║░░██║  ░░░░░░  ██╔════╝██║██╔════╝╚══██╔══╝██╔════╝████╗░████║██╔══██╗
░█████╔╝███████║  █████╗  ╚█████╗░██║╚█████╗░░░░██║░░░█████╗░░██╔████╔██║███████║
░╚═══██╗██╔══██║  ╚════╝  ░╚═══██╗██║░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║██╔══██║
██████╔╝██║░░██║  ░░░░░░  ██████╔╝██║██████╔╝░░░██║░░░███████╗██║░╚═╝░██║██║░░██║
╚═════╝░╚═╝░░╚═╝  ░░░░░░  ╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝
          
''')
    print('-=≡≣ *======================================================================* ≣≡=-')
    
def exibir_opcoes():
    print(f'''
1. Agendar Teleconsulta
2. Listar Agendamentos
3. Reagendar Teleconsulta
4. Cancelar Agendamento
5. Sair
''')


def menu_cadastro():
    exibir_titulo()
    print('''
1. Cadastrar Usuário
2. Fazer Login
3. Sair
''')

def validar_cpf():
    while True:
        cpf = input("Digite seu CPF (apenas números): ").strip()

        # Tentando converter o CPF para int e verificar o comprimento
        try:
            cpf = int(cpf)

            # Verifica se o CPF tem 11 dígitos
            if len(str(cpf)) != 11:
                print("❌ O CPF deve conter exatamente 11 dígitos.")
                continue

            return cpf  # Retorna o CPF se for válido
        except ValueError:
            print("❌ CPF inválido. Deve conter apenas números.")
            continue

def validar_senha():
    while True:
        senha = input("Digite uma senha: ").strip()

        # Verifica se a senha não está vazia
        if not senha:
            print("❌ Senha não pode ser vazia.")
            continue
        
        return senha  # Retorna a senha se for válida

def cadastrar_usuario():
    try:
        print("\n=== CADASTRO DE USUÁRIO ===")
        
        cpf = validar_cpf()  # Chama a função de validação do CPF
        senha = validar_senha()  # Chama a função de validação da senha

        # Verificar se o CPF já está cadastrado
        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                print("❌ CPF já cadastrado.")
                return  # Sai da função sem continuar

        # Adiciona o novo usuário à lista
        usuarios.append({"cpf": cpf, "senha": senha})
        print("🡆 Usuário cadastrado com sucesso!")

    except Exception as e:
        print(f"❌ Erro ao cadastrar usuário: {e}")


def limpar_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

# Lista para armazenar os usuários
usuarios = []

# Função para validar o CPF
def validar_cpf():
    while True:
        cpf = input("Digite seu CPF (apenas números): ").strip()

        # Tentando converter o CPF para int e verificar o comprimento
        try:
            cpf = int(cpf)

            # Verifica se o CPF tem 11 dígitos
            if len(str(cpf)) != 11:
                print("❌ O CPF deve conter exatamente 11 dígitos.")
                continue

            return cpf  # Retorna o CPF se for válido
        except ValueError:
            print("❌ CPF inválido. Deve conter apenas números.")
            continue

# Função para validar a senha
def validar_senha():
    while True:
        senha = input("Digite uma senha: ").strip()

        # Verifica se a senha não está vazia
        if not senha:
            print("❌ Senha não pode ser vazia.")
            continue
        
        return senha  # Retorna a senha se for válida

# Função para cadastrar o usuário
def cadastrar_usuario():
    try:
        print("\n=== CADASTRO DE USUÁRIO ===")
        
        cpf = validar_cpf()  # Chama a função de validação do CPF
        senha = validar_senha()  # Chama a função de validação da senha

        # Verificar se o CPF já está cadastrado
        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                print("❌ CPF já cadastrado.")
                return  # Sai da função sem continuar

        # Adiciona o novo usuário à lista
        usuarios.append({"cpf": cpf, "senha": senha})
        print("🡆 Usuário cadastrado com sucesso!")

    except Exception as e:
        print(f"❌ Erro ao cadastrar usuário: {e}")

# Função para fazer login
def login():
    try:
        print("\n=== LOGIN ===")
        
        cpf = validar_cpf()  # Valida o CPF
        senha = input("Digite sua senha: ").strip()  # Solicita a senha

        # Verifica se o CPF está cadastrado
        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                if usuario["senha"] == senha:
                    print("✅ Login bem-sucedido!")
                    return  # Login bem-sucedido
                else:
                    print("❌ Senha incorreta.")
                    return  # Senha incorreta
        
        # Se o CPF não estiver cadastrado
        print("❌ CPF não cadastrado.")

    except Exception as e:
        print(f"❌ Erro ao fazer login: {e}")


if __name__ == "__main__":
    while True:
        exibir_titulo()
        exibir_opcoes()
        usuario_opcao = int(input('Escolha uma opção: '))

        if usuario_opcao == '1':
            cadastrar_usuario()
        elif usuario_opcao == '2':
            login()
        elif usuario_opcao == '0':
            print("👋 Até logo!")
            break
        else:
            print("❌ Opção inválida.")
        
        input("\nPressione ENTER para continuar...")