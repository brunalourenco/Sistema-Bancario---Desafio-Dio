# Sistema Bancário - Desafio Dio
Repositório para Sistema Bancário desenvolvido em Python para Bootcamp da DIO.

## Problema de negócio
O banco XPTO deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

## Requisitos Funcionais

|Requisito |Operação |Descrição|
|-------|---------|---------|
|RF-001|Usuario| A v1 do projeto trabalha apenas com 1 usuario, dessa forma nao precisamos nos preocupar em identificar qual e o numero da agencia e conta bancaria.|
|RF-002|Deposito|Deve ser possivel depositar valores positivos para a minha conta bancaria. Todos os depositos devem ser armazenados em uma variavel e exibidos na operaçao de extrato.|
|RF-003|Saque|O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que nao sera possivel sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variavel e exibidos na operação de extrato.|
|RF-004|Extrato|Essa operacao deve listar todos os depositos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Nao foram realizadas movimentacoes.Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:1500.45 = R$ 1500.45|

