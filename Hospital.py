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

def chamar_paciente():
    '''
    O objetivo dessa função é chamar um paciente e apagá-lo da lista assim que for chamado.
    evita que o mesmo paciente seja chamado mais de uma vez, evitando erros ou confusão.
    As estruturas utilizadas foram: Operadores lógicos, manipulação de lista, estrutura condicional, a 
    biblioteca datetime e adiciona um lista à uma matriz (matriz.histórico).
    '''
    print("\nCHAMAR PACIENTE")
    if len(pacientes) == 0:
        print("Fila vazia. Nenhum paciente para chamar.")
        return

    # O popleft() remove o primeiro elemento de forma eficiente (Biblioteca queue/collections)
    proximo = pacientes.popleft()
    # Obtém o horário em que o paciente foi chamado
    horario_chamada = datetime.now()

    print(f"Próximo paciente: {proximo['Nome']} (Prioridade: {proximo['Prioridade']})")
    print(f"Encaminhado para o consultório às {horario_chamada}.")

    # Alimenta a Matriz (Atividade 1) criando uma nova linha (lista) no histórico
    dados_atendimento = [horario_chamada, proximo['Nome'], proximo['Sintomas'], proximo['Prioridade']]
    matriz_historico.append(dados_atendimento)

def buscar_paciente():

        '''

        O objetivo dessa função é buscar um paciente na lista verificando se ele existe ou não.
        Ajuda a saber se um paciente está cadastrado e informa suas informações.
        Nessa função foram utilizadas as seguintes estruturas: estrutura de repetição, operadores lógicos, estruturas 
        condicionais e algumas funções nativas do python.
        '''
        print("\nBUSCAR PACIENTE")
        if len(pacientes) == 0:
            print("Fila de espera vazia.")
            return
        
        # Nome informado pelo usuário para realizar a busca
        nome_busca = input("Nome para buscar paciente: ").strip().lower()
        encontrado = False

        for posicao, paciente in enumerate(pacientes, start=1):
            if nome_busca in paciente["Nome"].lower():
                print("\nPaciente encontrado na fila de espera!")
                print(f"Posição na fila: {posicao}")
                print(f"Nome: {paciente['Nome']}")
                print(f"Idade: {paciente['Idade']}")
                print(f"Sintomas: {paciente['Sintomas']}")
                print(f"Prioridade: {paciente['Prioridade']}")
                print(f"Horário de Entrada: {paciente['Horario_Entrada']}")
                # Indica que o paciente foi localizado
                encontrado = True  

        if not encontrado:
            print("Paciente não encontrado na fila de espera.")


def mostrar_estatisticas():
        '''
        O objetivo da função é definir a quantidade de pacientes que se encaixam em cada classificação de risco.
        facilita a gestão de dados por classificação e mostra a quantidade de consultas que estão em cada tipo de lista.
        utilizamos estrutura de repetição, estruturas condicionais e informa o tamanho da lista usando o "len".
        '''
        print("\nESTATÍSTICAS HOSPITALARES (EM ESPERA):\n")
        # Contadores para cada nível de prioridade
        emergencia = 0
        urgente = 0
        normal = 0

        # Conta quantos pacientes existem em cada classificação
        for paciente in pacientes:
            if paciente["Prioridade"] == "Emergência":
                emergencia += 1
            elif paciente["Prioridade"] == "Urgente":
                urgente += 1
            else:
                normal += 1

        print("Total de pacientes aguardando:", len(pacientes))
        print("Emergência:", emergencia)
        print("Urgente:", urgente)
        print("Normal:", normal)


def exibir_historico_matriz():
    '''
    O objetivo desta função é exibir o histórico dos pacientes que já foram atendidos.
    Os dados são armazenados em uma matriz, onde cada linha representa um atendimento
    realizado contendo horário, nome do paciente, sintomas e prioridade.
    Nesta função são utilizadas estruturas de repetição, manipulação de matrizes,
    acesso por índices e formatação de saída no terminal.
    '''
   
    print("\n--- RELATÓRIO DE PACIENTES ATENDIDOS (MATRIZ) ---")
    # Verifica se existe histórico de atendimento
    if len(matriz_historico) == 0:
        print("Nenhum atendimento foi realizado ainda.")
        return
    
    # Cabeçalho da tabela de atendimentos realizados
    print(f"{'HORÁRIO':<10} | {'PACIENTE':<15} | {'SINTOMAS':<20} | {'PRIORIDADE':<12}")
    print("-" * 65)

    # Varredura da matriz usando índices (Atividade 1 - Acesso por dois índices)
    for linha in range(len(matriz_historico)):
        horario = matriz_historico[linha][0]
        nome = matriz_historico[linha][1]
        sintoma = matriz_historico[linha][2]
        prioridade = matriz_historico[linha][3]
        
        print(f"{horario:<10} | {nome:<15} | {sintoma:<20} | {prioridade:<12}")

def menu():
    '''
    O objetivo desta função é controlar o funcionamento geral do sistema.
    Ela exibe o menu principal, recebe a opção escolhida pelo usuário e
    direciona para a funcionalidade correspondente.
    Nesta função são utilizadas estruturas de repetição, estruturas condicionais
    e chamadas de funções.
    '''
    # Loop principal do sistema
    while True:
        print("\nHOSPITAL - SISTEMA DE TRIAGEM (SA2)")
        print("1 - Cadastrar paciente")
        print("2 - Lista de pacientes em espera")
        print("3 - Chamar próximo paciente")
        print("4 - Buscar paciente")
        print("5 - Estatísticas de espera")
        print("6 - Ver Relatório de Atendidos (Matriz)")
        print("0 - Sair")

        # Recebe a opção escolhida pelo usuário
        opcao = input("Escolha uma opção: ")

        # Direciona o usuário para a funcionalidade selecionada
        if opcao == "1":
            cadastro_paciente()
        elif opcao == "2":
            listar_paciente()
        elif opcao == "3":
            chamar_paciente()
        elif opcao == "4":
            buscar_paciente()
        elif opcao == "5":
            mostrar_estatisticas()
        elif opcao == "6":
            exibir_historico_matriz()
        elif opcao == "0":
            print("\nEncerrando o sistema...")
            break
        else:
            print("Opção inválida!")
# Execução do sistema
menu()