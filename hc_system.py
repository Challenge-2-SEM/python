"""
EQUIPE:
Henrique Martins - RM 563620
Henrique Texeira - RM 563088
Henrique Pacheco - RM 562086

TITULO: Utilizamos o site FSymbols para personalizar o titulo em ASCII ART e simbolos.
OS: Utilizamos o módulo OS para limpar o terminal e deixar o programa mais limpo.
"""

import os

# Lista para armazenar os dados.
usuarios = []
consultas = []

# Funções para o menu.
def exibir_titulo():
    """
    Função para exibir titulo personalizado no terminal.
    """
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

def limpar_terminal():
    """
    Função para limpar a tela do terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar_e_limpar():
    """
    Pausa a execução para o usuário ler a mensagem e depois limpa o terminal.
    """
    input("\nPressione Enter para continuar...")
    limpar_terminal()

def eh_numerico(texto):
    """
    Verifica se uma string contém apenas dígitos de '0' a '9'.
    """
    for caractere in texto:
        if caractere not in "0123456789":
            return False
    return True

# Funções para o usuário.
def cadastrar_usuario():
    """
    Função para cadastrar usuários, solicitando NOME, CPF e senha.
    """
    limpar_terminal()
    print('-=≡≣ *============* ≣≡=-')
    print('|  Cadastro de Usuário  |')
    print('-=≡≣ *============* ≣≡=-')

    # Validação do nome.
    while True:
        nome = input("\nDigite seu nome completo: ").strip()
        if len(nome) > 1 and ' ' in nome:
            break
        else:
            print("ERRO: Por favor, digite seu nome completo.")
            
    # Validação do cpf
    while True:
        cpf = input(f"Digite seu CPF (apenas números): ")
        if len(cpf) == 11 and eh_numerico(cpf):
            cpf_ja_existe = False
            for u in usuarios:
                if u["cpf"] == cpf:
                    cpf_ja_existe = True
                    break
            
            if cpf_ja_existe:
                print("ERRO: CPF já cadastrado.")
                pausar_e_limpar()
                return
            
            break 
        else:
            print("ERRO: CPF inválido. Digite 11 números.")

    # Validação da senha
    while True:
        senha = input("Digite sua senha (mínimo 4 caracteres): ")
        if len(senha) >= 4:
            break
        else:
            print("ERRO: A senha deve ter no mínimo 4 caracteres.")

    usuarios.append({"nome": nome, "cpf": cpf, "senha": senha})
    print("\nUsuário cadastrado com sucesso!")
    pausar_e_limpar()

def login():
    """
    Função para fazer login. Se bem-sucedido, retorna o DICIONÁRIO do usuário.
    """
    limpar_terminal()
    print('-=≡≣ *======* ≣≡=-')
    print("|  Área de Login  |")
    print('-=≡≣ *======* ≣≡=-')
    cpf = input(f"\nDigite seu CPF: ")
    senha = input("Digite sua senha: ")

    for u in usuarios:
        if u["cpf"] == cpf and u["senha"] == senha:
            primeiro_nome = u['nome'].split()[0]
            print(f"\nLogin bem-sucedido, {primeiro_nome}!")
            pausar_e_limpar()
            return u
            
    print("\nERRO: CPF ou senha incorretos.")
    pausar_e_limpar()
    return None

# Funções para a consulta.
def agendar_consulta(cpf):
    """
    Agenda uma nova consulta com validação de data e hora.
    """
    limpar_terminal()
    print('-=≡≣ *=========* ≣≡=-')
    print('|  AGENDAR CONSULTA  |')
    print('-=≡≣ *=========* ≣≡=-')

    # Validar a data
    while True:
        data_valida = False
        data = input("\nDigite a data da consulta (dd/mm/aaaa): ")
        try:
            if len(data) == 10 and data[2] == '/' and data[5] == '/':
                partes_da_data = data.split('/')
                dia = int(partes_da_data[0])
                mes = int(partes_da_data[1])
                ano = int(partes_da_data[2])

                if 1 <= dia <= 31 and 1 <= mes <= 12 and ano >= 2025:
                    data_valida = True
        except (ValueError, IndexError):
            data_valida = False
        
        if data_valida: 
            break
        else: 
            print("ERRO: Data inválida. Use o formato dd/mm/aaaa com valores corretos.")
    
    # Validar a hora
    while True:
        hora_valida = False
        hora = input("Digite a hora da consulta (hh:mm): ")
        try:
            if len(hora) == 5 and hora[2] == ':':
                partes_da_hora = hora.split(':') 
                h = int(partes_da_hora[0])
                m = int(partes_da_hora[1])
                
                if 0 <= h <= 23 and 0 <= m <= 59:
                    hora_valida = True
        except (ValueError, IndexError):
            hora_valida = False

        if hora_valida: 
            break
        else: 
            print("ERRO: Hora inválida. Use o formato hh:mm com valores corretos.")

    consultas.append({"cpf": cpf, "data": data, "hora": hora})
    print("\nConsulta agendada com sucesso!")
    pausar_e_limpar()

def listar_consultas(cpf):
    """
    Lista todas as consultas agendadas para o CPF do usuário logado.
    """
    limpar_terminal()
    print('-=≡≣ *=======* ≣≡=-')
    print("|  SUAS CONSULTAS  |")
    print('-=≡≣ *=======* ≣≡=-')
    
    minhas_consultas = []
    for c in consultas:
        if c["cpf"] == cpf:
            minhas_consultas.append(c)
    
    if not minhas_consultas:
        print("\nNenhuma consulta encontrada.")
        return False
        
    indice = 1
    for consulta in minhas_consultas:
        print(f"\n{indice}. {consulta['data']} ás {consulta['hora']}")
        indice = indice + 1
    return True

def reagendar_consulta(cpf):
    """
    Reagenda uma consulta.
    """
    if not listar_consultas(cpf):
        pausar_e_limpar()
        return

    minhas_consultas = []
    for c in consultas:
        if c["cpf"] == cpf:
            minhas_consultas.append(c)
    
    try:
        num_consulta = input("\nQual consulta deseja reagendar? (Digite o número): ")
        num = int(num_consulta)
        
        if 1 <= num <= len(minhas_consultas):
            consulta_original = minhas_consultas[num - 1]
            print(f"\n|  REAGENDAR CONSULTA  |")
            print("(Deixe em branco para manter o valor atual)")

            # Validação da nova data
            while True:
                nov_data = f"Nova data ({consulta_original['data']}): "
                nova_data_input = input(nov_data)
                
                if not nova_data_input:
                    nova_data = consulta_original['data']
                    break

                data_valida = False
                try:
                    if len(nova_data_input) == 10 and nova_data_input[2] == '/' and nova_data_input[5] == '/':
                        partes_data = nova_data_input.split('/')
                        dia = int(partes_data[0])
                        mes = int(partes_data[1])
                        ano = int(partes_data[2])

                        if 1 <= dia <= 31 and 1 <= mes <= 12 and ano >= 2025:
                            data_valida = True
                            nova_data = nova_data_input
                except (ValueError, IndexError):
                    data_valida = False
                
                if data_valida:
                    break
                else:
                    print("ERRO: Data inválida. Tente novamente.")

            # Validação da nova hora
            while True:
                prompt_hora = f"Nova hora ({consulta_original['hora']}): "
                nova_hora_input = input(prompt_hora)

                if not nova_hora_input:
                    nova_hora = consulta_original['hora']
                    break
                
                hora_valida = False
                try:
                    if len(nova_hora_input) == 5 and nova_hora_input[2] == ':':
                        partes_hora = nova_hora_input.split(':')
                        h = int(partes_hora[0])
                        m = int(partes_hora[1])
                        
                        if 0 <= h <= 23 and 0 <= m <= 59:
                            hora_valida = True
                            nova_hora = nova_hora_input
                except (ValueError, IndexError):
                    hora_valida = False
                
                if hora_valida:
                    break
                else:
                    print("ERRO: Hora inválida. Tente novamente.")
            
            consulta_original["data"] = nova_data
            consulta_original["hora"] = nova_hora
            
            print("\nConsulta atualizada com sucesso!")
        else:
            print("\nOpção inválida. Número fora do intervalo.")
            
    except ValueError:
        print("\nERRO: Por favor, digite um número válido.")
    
    finally:
        pausar_e_limpar()

def cancelar_consulta(cpf):
    """
    Cancela uma consulta.
    """
    if not listar_consultas(cpf):
        pausar_e_limpar()
        return

    minhas_consultas = []
    for c in consultas:
        if c["cpf"] == cpf:
            minhas_consultas.append(c)
    
    try:
        numero_string = input("\nQual consulta deseja cancelar? (Digite o número): ")
        num = int(numero_string)
        
        if 1 <= num <= len(minhas_consultas):
            consulta_para_remover = minhas_consultas[num-1]
            consultas.remove(consulta_para_remover)
            print("\nConsulta cancelada com sucesso!")
        else:
            print("\nOpção inválida. Número fora do intervalo.")
            
    except ValueError:
        print("\nERRO: Por favor, digite um número válido.")
    
    finally:
        pausar_e_limpar()

# Funções para o menu principal
def menu_principal():
    """
    Menu inicial do sistema.
    """
    while True:
        limpar_terminal()
        exibir_titulo()
        print(f"\n1. Cadastrar Usuário")
        print("2. Fazer Login")
        print("0. Sair")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            usuario_logado = login()
            if usuario_logado:
                menu_consultas(usuario_logado)
        elif opcao == "0":
            limpar_terminal()
            print("Saindo do programa... Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")
            pausar_e_limpar()

def menu_consultas(usuario):
    """
    Submenu de gerenciamento de consultas.
    """
    primeiro_nome = usuario['nome'].split()[0]
    cpf_usuario = usuario['cpf']

    while True:
        limpar_terminal()
        exibir_titulo()
        print(f"\nOlá, {primeiro_nome}! Seja bem-vindo(a).") 
        print("\n1. Agendar Consulta")
        print("2. Reagendar Consulta")
        print("3. Cancelar Consulta")
        print("4. Listar Minhas Consultas")
        print("0. Fazer Logout")
        opcao = input(f"\nEscolha uma opção: ")

        if opcao == "1":
            agendar_consulta(cpf_usuario)
        elif opcao == "2":
            reagendar_consulta(cpf_usuario)
        elif opcao == "3":
            cancelar_consulta(cpf_usuario)
        elif opcao == "4":
            listar_consultas(cpf_usuario)
            pausar_e_limpar()
        elif opcao == "0":
            print("\nFazendo logout...")
            pausar_e_limpar()
            break
        else:
            print("\nOpção inválida. Tente novamente.")
            pausar_e_limpar()

# Inicializar o programa
menu_principal()