# ads-intro-queuing-theory

Trabalho 1 de implementação de aplicativo de avaliação de desempenho de sistemas, utilizando os conceitos referentes à Teoria das Filas. Comando da atividade:

> Questão de Implementação: Considere a seguinte situação hipotética. Em um aeroporto internacional, na véspera de Natal, a empresa de aviação aérea AIR CONFORT, recebe um grande número de clientes todos os anos. Ao passar do tempo notou-se que durante esta data, 24/dezembro, recebem em média 165 usuários por hora, além disso a capacidade de atendimento de cada funcionário que realiza o check-in é de 15 por hora, sendo 5 atendentes no total. 

> Desenvolver um programa que informe o tempo de espera de um cliente nesta fila, calcule também o tempo estimado para permanência no Sistema considerando essas informações. Caso a empresa não consiga atender a esse público neste dia, qual seria a configuração ideal do sistema para o referido público de chegada por hora ? Implemente então uma mensagem que informe o cenário ideal para o ADM do sistema, para que o mesmo possa convocar ou escalar mais funcionários para atender a esta situação-demanda, ou ainda informar quantos clientes cada um dos 5 funcionários teria que atender por hora, em caso de impossibilidade de adição de atendentes extras.

Com base nisso uma aplicação Python foi desenvolvida, nela existe uma interface que recebe:
- A quantidade média de usuários que chegam por hora
- A capacidade de atendimento de cada funcionário
- A quantidade de atendentes no local

E diante das informações  retorna:
- O tempo de espera de um cliente nesta fila
- O tempo estimado de permanência no sistema
- A quantidade necessária de atendentes que devem ser contratados para que o sistema fique balanceado 
- A quantidade de atendimentos que os servidores atuais teriam que efetuar para que o sistema fique balanceado
