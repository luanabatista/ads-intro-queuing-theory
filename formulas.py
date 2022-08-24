import math 

# Taxa média de chegada (λ) em horas
mediaChegada = 165

# Pontos de atendimento
atendentes = 5

# Taxa média de atendimento do sistema Mi (μ) em horas
mediaAtendimento = 15*atendentes

#- Tempo médio de espera apenas na Fila (Wq)
tempoFila = mediaChegada/(mediaAtendimento*(mediaAtendimento-mediaChegada))
print(tempoFila)

#- Tempo médio que um cliente permanece no sistema, esperando na Fila + Tempo de Atendimento (W)
tempoSistema = 1/(mediaAtendimento-mediaChegada)
print(tempoSistema)

# quantidade de funcionarios ideal 
funcIdeal = math.ceil(mediaChegada/(mediaAtendimento/atendentes))
print(funcIdeal)

# quantidade ajuste atendimento por hora
atendIdeal = math.ceil(mediaChegada/atendentes)
print(atendIdeal)