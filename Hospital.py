"""
Sistema de Atendimento Hospitalar - Evolução SA2
"""
from collections import deque  # Biblioteca Nativa 1: Para gerenciamento eficiente da fila
from datetime import datetime  # Biblioteca Nativa 2: Para registrar data e hora dos atendimentos

# O 'deque' substitui a lista simples para melhorar a performance ao remover elementos do início
pacientes = deque()

# Matriz (lista de listas) que guardará o histórico de quem já foi chamado/atendido
# Cada linha será: [Horário do Atendimento, Nome do Paciente, Sintomas, Prioridade]
matriz_historico = []

def cadastro_paciente():
    '''
    O objetivo dessa função é cadastrar o paciente e deninir o grau de prioridade dele(a).
    essa função recebe as informações do usuario (paciente) e define a qual classificação de risco do paciente, utiliza
    estruturas estruturas condicionais, funções nativas, dicionário, manipulação de listas usando "append" e a bibloteca datetime.now
    '''

    # Recebe os dados básicos do paciente
    nome = input("\nNome: ").strip()
    idade = int(input("Idade: "))
    sintoma = input("Sintomas: ").strip()

    # Exibe as opções de classificação de risco
    print("\n1 - \033[91mEmergência\033[0m")
    print("2 - \033[93mUrgente\033[0m")
    print("3 - \033[92mNormal\033[0m")

    opcao = input("Prioridade: ")

    # Define a prioridade de acordo com a opção escolhida
    if opcao == "1":
        prioridade = "Emergência"
    elif opcao == "2":
        prioridade = "Urgente"
    else:
        prioridade = "Normal"

    # Registro do horário atual de entrada usando datetime
    horario_entrada = datetime.now()
    #HORA, MINUTOS, SEGUNDOS. O caractere % indica que o próximo caractere não deve ser interpretado literalmente, mas sim como uma instrução de formatação.

    # Dicionário representando a entidade Paciente (Atividade 2)
    paciente = { 
        "Nome": nome,
        "Idade": idade,
        "Sintomas": sintoma,
        "Prioridade": prioridade,
        "Horario_Entrada": horario_entrada
    }

    # Adiciona o paciente na fila. No deque, usamos o append normalmente
    pacientes.append(paciente)  

    print(f"\nPaciente {nome} cadastrado com sucesso às {horario_entrada}!")
    

def listar_paciente():
    '''
    O objetivo dessa função é criar uma lista de paciente, definindo uma fila de pacientes.
    E resolve as dúvidas dos pacientes e dos funcioários em relação a organização e quantidade dos pacientes.
    Nessa funcão utiliza-se manipulação de lista, uma etrutura de repetição que informa o tamanho e informações da lista.
    '''

    # Verifica se existem pacientes aguardando atendimento
    if len(pacientes) == 0:
        print("\nNenhum paciente na fila de espera!")
        return
    
    print("\n--- FILA DE PACIENTES EM ESPERA ---")

    # Percorre toda a fila exibindo os pacientes cadastrados
    for i, p in enumerate(pacientes, start=1):     
        print(f"{i}º - {p['Nome']} | Prioridade: {p['Prioridade']} | Entrada: {p['Horario_Entrada']}")