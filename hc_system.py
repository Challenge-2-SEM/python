'''
EQUIPE:
Henrique Martins - RM 563620
Henrique Texeira - RM 563088
Henrique Pacheco - RM 562086

TITULO: Utilizamos o site FSymbols para personalizar o titulo em ASCII ART e simbolos. 
OS: Utilizamos o módulo OS para limpar o terminal e deixar o programa mais limpo.
'''

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

exibir_titulo()
exibir_opcoes()