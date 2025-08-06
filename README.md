💰 BetCoin – Simulador de Corretora de Criptomoedas



BetCoin é um simulador de corretora de criptomoedas desenvolvido em Python.
O projeto permite o cadastro e login de usuários, movimentação de saldo, compra e venda de criptomoedas fictícias e registro de extratos financeiros, com cotações que se atualizam dinamicamente.

✨ Funcionalidades
Cadastro e Login de Usuários

Validação de CPF e senha de 6 dígitos.

Armazenamento em arquivo usuarios.txt.

Gerenciamento Financeiro

Depósitos e saques com registro no extrato.

Saldo atualizado em tempo real.

Histórico salvo em arquivos separados por usuário (historico_extrato/).

Negociação de Criptomoedas

Compra e venda de Bitcoin, Ethereum e Ripple.

Cotações variam aleatoriamente entre -5% e +5% a cada atualização.

Segurança e Histórico

Confirmação de senha para operações sensíveis.

Extrato atualizado e persistido em arquivo para cada usuário.

📂 Estrutura do Projeto
bash
Copiar
Editar
BetCoin/
│
├── historico_extrato/       # Armazena o extrato individual de cada usuário
├── usuarios.txt             # Base de dados simples de usuários cadastrados
├── betcoin.py               # Código principal do sistema
└── README.md                # Documentação do projeto
🚀 Como Executar o Projeto
Clone este repositório ou baixe os arquivos:

bash
Copiar
Editar
git clone https://github.com/seuusuario/BetCoin.git
cd BetCoin
Execute o script principal com Python 3:

bash
Copiar
Editar
python betcoin.py
Escolha uma opção no menu inicial:

L para Login

C para Cadastro

🖥️ Menu Principal
markdown
Copiar
Editar
=== Menu Principal ===
1. Consultar saldo
2. Consultar extrato
3. Depositar
4. Sacar
5. Comprar criptomoedas
6. Vender criptomoedas
7. Atualizar cotação
8. Sair
📌 Exemplo de Uso
1️⃣ Cadastro de Usuário
vbnet
Copiar
Editar
CPF (Somente números): 12345678901
Senha (6 dígitos numéricos): 123456
Nome: João
País (sigla do seu país): BR
2️⃣ Login e Depósito
yaml
Copiar
Editar
CPF: 12345678901
Senha: 123456
Valor para depósito: R$ 1000.00
3️⃣ Compra de Criptomoeda
ruby
Copiar
Editar
Cotações atuais:
Bitcoin: R$ 50.00
Ethereum: R$ 25.00
Ripple: R$ 5.00

Qual criptomoeda deseja comprar? Bitcoin
Quantos R$ deseja investir em Bitcoin? 500
Compra de Bitcoin no valor de R$ 500.00 realizada com sucesso.
🛠️ Tecnologias Utilizadas
Python 3.x

os – manipulação de arquivos e diretórios

getpass – entrada de senha oculta

random – variação de cotações

📄 Licença
Este projeto é de uso educacional e não representa uma corretora real.
Sinta-se livre para estudar, modificar e evoluir este código.