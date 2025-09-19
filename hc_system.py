'''
EQUIPE:
Henrique Martins - RM 563620
Henrique Texeira - RM 563088
Henrique Pacheco - RM 562086

TITULO: Utilizamos o site FSymbols para personalizar o titulo em ASCII ART e simbolos. 
OS: Utilizamos o módulo OS para limpar o terminal e deixar o programa mais limpo.
'''

cpfs = []
senhas = []

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
    usuario_opcao = int(input('Escolha uma opção: '))

def menu_cadastro():
    exibir_titulo()
    print('''
1. Cadastrar Usuário
2. Fazer Login
3. Sair
''')

def cadastrar_usuario():
    try:
        usuario_cpf = int(input('Digite seu CPF (apenas números): '))
        cpfs.append(usuario_cpf)
        usuario_senha = input('Digite sua senha: ')
        senhas.append(usuario_senha)
    except ValueError as e:
        print('ERRO: CPF invalido, digite apenas números.')
    finally:
        print('🡆 Usuário cadastrado com sucesso!')


cadastrar_usuario()