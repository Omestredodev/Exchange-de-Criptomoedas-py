from getpass import getpass
import random
import os
print(os.getcwd())  # Obter o diretório de trabalho atual
# Inicializar cotações das criptomoedas
cotacoes = {
    'Bitcoin': 50.0,   # Valor inicial fictício
    'Ethereum': 25.0,  # Valor inicial fictício
    'Ripple': 5.0      # Valor inicial fictício
}

# Diretório para salvar os arquivos de histórico de extrato
HISTORICO_DIR = "historico_extrato"

# Verificar se o diretório existe, caso contrário, criá-lo
if not os.path.exists(HISTORICO_DIR):
    os.makedirs(HISTORICO_DIR)

# Inicializar dados dos usuários (saldos e extratos)
dados_usuarios = {}

def gerar_variacao():
    """Gera uma variação aleatória entre -5% e +5%."""
    return random.uniform(-0.05, 0.05)

def atualizar_cotacao(valor, variacao):
    """Atualiza a cotação com base na variação fornecida e arredonda para 2 casas decimais."""
    novo_valor = valor * (1 + variacao)
    return round(novo_valor, 2)

def atualizar_cotacoes(cotacoes):
    """Atualiza todas as cotações de criptomoedas."""
    for moeda in cotacoes:
        variacao = gerar_variacao()
        cotacoes[moeda] = atualizar_cotacao(cotacoes[moeda], variacao)

def cadastrar_usuario(usuarios):
    print("Cadastro de Usuário")
    cpf = input("CPF (Somente números): ")

    # Verificar se o CPF já está cadastrado no arquivo
    if any(usuario['cpf'] == cpf for usuario in carregar_usuarios()):
        print("CPF já cadastrado.")
        return

    password = getpass("Senha (6 dígitos numéricos): ")
    nome = input("Nome: ")
    pais = input("País (sigla do seu país): ")

    # Validar a senha
    if len(password) != 6 or not password.isdigit():
        print("A senha deve ter 6 dígitos numéricos.")
        return

    # Validar o CPF (apenas para fins de validação básica)
    if len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido.")
        return

    # Validar o país do usuário
    if pais.upper() != "BR":
        print("Nossa corretora atua apenas no Brasil.")
        return

    # Criar um dicionário com os dados do usuário
    usuario = {
        'cpf': cpf,
        'password': password,
        'nome': nome,
        'pais': pais.upper()
    }

    # Adicionar o usuário à lista de usuários
    usuarios.append(usuario)

    # Adicionar o usuário ao arquivo usuarios.txt
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{cpf},{password},{nome},{pais.upper()}\n")

    # Criar arquivo para o histórico de extrato do usuário
    with open(os.path.join(HISTORICO_DIR, f"{cpf}_extrato.txt"), "w") as arquivo:
        arquivo.write("Histórico de Extrato\n")

    # Inicializar dados financeiros do usuário
    dados_usuarios[cpf] = {
        'saldo': 0.0,
        'extrato': []
    }

    print("Seus dados foram analisados e cadastrados com sucesso, seja bem-vindo à nossa plataforma! ")

def fazer_login(usuarios, cotacoes):
    print("Login")
    cpf = input("CPF (Somente números): ")
    password = getpass("Senha (6 dígitos numéricos): ")

    # Verificar se o CPF e a senha correspondem a um usuário cadastrado
    for usuario in usuarios:
        if usuario['cpf'] == cpf and usuario['password'] == password:
            print("Login bem-sucedido!")
            atualizar_cotacoes(cotacoes)
            return usuario  # Retorna o usuário logado

    print("CPF ou senha inválidos.")
    return None

def carregar_usuarios():
    usuarios = []
    try:
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(',')
                usuario = {
                    'cpf': dados[0],
                    'password': dados[1],
                    'nome': dados[2],
                    'pais': dados[3]
                }
                usuarios.append(usuario)
                # Inicializar dados financeiros do usuário se ainda não estiverem carregados
                if dados[0] not in dados_usuarios:
                    dados_usuarios[dados[0]] = {
                        'saldo': 0.0,
                        'extrato': []
                    }
    except FileNotFoundError:
        pass
    return usuarios

def consultar_saldo(usuario_logado):
    if solicitar_senha(usuario_logado):
        cpf = usuario_logado['cpf']
    saldo = dados_usuarios[cpf]['saldo']
    print(f"Saldo atual: R$ {saldo:.2f}")

def consultar_extrato(usuario_logado):
    if solicitar_senha(usuario_logado):
        cpf = usuario_logado['cpf']
        extrato = dados_usuarios[cpf]['extrato']
        if not extrato:
            print("Nenhuma transação registrada.")
        else:
            for transacao in extrato:
                print(transacao)

def depositar(usuario_logado):
    cpf = usuario_logado['cpf']
    valor = float(input("Valor para depósito: R$ "))
    dados_usuarios[cpf]['saldo'] += valor
    dados_usuarios[cpf]['extrato'].append(f"Depósito: R$ {valor:.2f}")
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    extrato_atualizado(usuario_logado)

def sacar(usuario_logado):
    if solicitar_senha(usuario_logado):
        cpf = usuario_logado['cpf']
        valor = float(input("Valor para saque: R$ "))
        if dados_usuarios[cpf]['saldo'] >= valor:
            dados_usuarios[cpf]['saldo'] -= valor
            dados_usuarios[cpf]['extrato'].append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            extrato_atualizado(usuario_logado)
        else:
            print("Saldo insuficiente para realizar o saque.")

def extrato_atualizado(usuario_logado):
    cpf = usuario_logado['cpf']
    extrato = dados_usuarios[cpf]['extrato']
    print("\n=== Extrato Atualizado ===")
    if not extrato:
        print("Nenhuma transação registrada.")
    else:
        for transacao in extrato:
            print(transacao)
    saldo = dados_usuarios[cpf]['saldo']
    print(f"Saldo atual: R$ {saldo:.2f}\n")

def salvar_extrato(usuario_logado):
    cpf = usuario_logado['cpf']
    extrato = dados_usuarios[cpf]['extrato']
    with open(os.path.join(HISTORICO_DIR, f"{cpf}_extrato.txt"), "a") as arquivo:
        for transacao in extrato:
            arquivo.write(transacao + "\n")

def comprar_criptomoedas(usuario_logado):
    if solicitar_senha(usuario_logado):
        cpf = usuario_logado['cpf']
        print("Cotações atuais:")
        for moeda, cotacao in cotacoes.items():
            print(f"{moeda}: R$ {cotacao:.2f}")
    
        moeda = input("Qual criptomoeda deseja comprar? ")
        if moeda not in cotacoes:
            print("Criptomoeda inválida.")
            return
        
        valor = float(input(f"Quantos R$ deseja investir em {moeda}? "))
        if dados_usuarios[cpf]['saldo'] >= valor:
            dados_usuarios[cpf]['saldo'] -= valor
            dados_usuarios[cpf]['extrato'].append(f"Compra de {moeda}: R$ {valor:.2f}")
            print(f"Compra de {moeda} no valor de R$ {valor:.2f} realizada com sucesso.")
            extrato_atualizado(usuario_logado)
            salvar_extrato(usuario_logado)  # Salvar o extrato após a compra
        else:
            print("Saldo insuficiente para realizar a compra.")

def vender_criptomoedas(usuario_logado):
    cpf = usuario_logado['cpf']
    print("Cotações atuais:")
    for moeda, cotacao in cotacoes.items():
        print(f"{moeda}: R$ {cotacao:.2f}")
    
    moeda = input("Qual criptomoeda deseja vender? ")
    if moeda not in cotacoes:
        print("Criptomoeda inválida.")
        return
    
    valor = float(input(f"Quantos R$ deseja obter vendendo {moeda}? "))
    dados_usuarios[cpf]['saldo'] += valor
    dados_usuarios[cpf]['extrato'].append(f"Venda de {moeda}: R$ {valor:.2f}")
    print(f"Venda de {moeda} no valor de R$ {valor:.2f} realizada com sucesso.")
    extrato_atualizado(usuario_logado)
    salvar_extrato(usuario_logado)  # Salvar o extrato após a venda

def solicitar_senha(usuario_logado):
    password = input("Digite sua senha novamente: ")
    if password == usuario_logado['password']:
        return True
    else:
        print("Senha incorreta.")
        return False

def loop_principal():
    usuarios = carregar_usuarios()

    print("=== BetCoin ===")
    while True:
        operacao = input("Você gostaria de fazer login (L) ou cadastrar um novo usuário (C)? ").upper()

        if operacao == "L":
            usuario_logado = fazer_login(usuarios, cotacoes)
            if usuario_logado:
                while True:
                    menu_principal()
                    opcao = input("Escolha uma opção: ")
                    if opcao == '1':
                        consultar_saldo(usuario_logado)
                    elif opcao == '2':
                        consultar_extrato(usuario_logado)
                    elif opcao == '3':
                        depositar(usuario_logado)
                    elif opcao == '4':
                        sacar(usuario_logado)
                    elif opcao == '5':
                        comprar_criptomoedas(usuario_logado)
                    elif opcao == '6':
                        vender_criptomoedas(usuario_logado)
                    elif opcao == '7':
                        atualizar_cotacoes(cotacoes)
                        print("Cotações atualizadas.")
                    elif opcao == '8':
                        print("Saindo...")
                        break
                    else:
                        print("Opção inválida.")
        elif operacao == "C":
            cadastrar_usuario(usuarios)
        else:
            print("Operação inválida. Por favor, digite 'L' para login ou 'C' para cadastro.")

def menu_principal():
    print("=== Menu Principal ===")
    print("1. Consultar saldo")
    print("2. Consultar extrato")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Comprar criptomoedas")
    print("6. Vender criptomoedas")
    print("7. Atualizar cotação")
    print("8. Sair")

if __name__ == "__main__":
    loop_principal()
