import math
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class DataEntryForm(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # Declaração das variáveis de entrada e saída
        self.taxa_chegada = ttk.IntVar(value=165)
        self.qtd_atendentes = ttk.IntVar(value=5)
        self.taxa_atendimento_atd = ttk.IntVar(value=15)
        self.taxa_atendimento = ttk.IntVar(value=self.taxa_atendimento_atd.get()*self.qtd_atendentes.get())

        self.tempo_fila = ttk.StringVar(value="")
        self.tempo_sistema = ttk.StringVar(value="")
        self.qtd_ideal_atd = ttk.StringVar(value="")
        self.taxa_ideal_atd = ttk.StringVar(value="")

        # Exibição de título de instrução
        hdr_txt = "Por favor insira as informações de atendimento da empresa" 
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # Criação dos campos de input
        self.create_form_entry("Taxa de Chegada - λ:\n(em horas)", self.taxa_chegada)
        self.create_form_entry("Pontos de Atendimento - M:\n(unidades)", self.qtd_atendentes)
        self.create_form_entry("Taxa de Atendimento:\n(por atendente em horas)", self.taxa_atendimento_atd)
        self.create_form_entry("Taxa de Atendimento - μ:\n(total em horas)", self.taxa_atendimento, READONLY)
        # Criação dos botões
        self.create_buttonbox()

        # Exibição de título de resultado
        hdr_txt = "Resultado"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=(20,10))

        # Criação dos campos de output
        self.create_form_entry("Tempo Estimado de Espera\nna Fila (Wq):", self.tempo_fila, READONLY)
        self.create_form_entry("Tempo Estimado de\nPermanência no Sistema (W):", self.tempo_sistema, READONLY)
        self.create_form_entry("Quantidade Ideal de\nAtendentes (M):", self.qtd_ideal_atd, READONLY)
        hdr_txt = "Ou"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50, anchor=CENTER)
        hdr.pack(fill=X, pady=(3,3))
        self.create_form_entry("Taxa Média de Atendimento\nIdeal (μ/atendente):", self.taxa_ideal_atd, READONLY)

    # Função executada quando é alterado a taxa de atendimento por atendente
    def on_change(self):
        self.taxa_atendimento.set(self.taxa_atendimento_atd.get()*self.qtd_atendentes.get())

    # Função de criação de novo campo
    def create_form_entry(self, label, variable, state = NORMAL):
        """Create a single form entry"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label, width=28)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable, state=state, validate="all", validatecommand=self.on_change)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    # Função de criação dos botões
    def create_buttonbox(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        # Cria botão de 'Enviar'
        sub_btn = ttk.Button(
            master=container,
            text="Enviar",
            command=self.on_submit,
            bootstyle=PRIMARY,
            width=8,
        )
        sub_btn.pack(side=RIGHT, padx=5)

        # Cria botão de 'Cancelar'
        cnl_btn = ttk.Button(
            master=container,
            text="Cancelar",
            command=self.on_cancel,
            bootstyle=DANGER,
            width=8,
        )
        cnl_btn.pack(side=RIGHT, padx=5)

    # Função executada ao clicar em 'Enviar'
    def on_submit(self):
        # Executa a função 'on_change' em caso de mudanças
        self.on_change()
        """Evaluate the results"""

        # Chama a função que calcula o Tempo de Espera de um cliente na fila
        valor_tempo_fila, tempo_fila = self.get_tempo_fila(self)
        self.tempo_fila.set(tempo_fila)

        # Chama a função que calcula o Tempo Estimado de Permanência no Sistema
        valor_tempo_sistema, tempo_sistema = self.get_tempo_sistema(self)
        self.tempo_sistema.set(tempo_sistema)

        # Chama a função que calcula a Quantidade Ideal de Atendentes
        self.qtd_ideal_atd.set(self.get_qtd_ideal_atd(self))

        # Chama a função que calcula a Taxa Ideal de Atendimento
        self.taxa_ideal_atd.set(self.get_taxa_ideal_atd(self))
        
        # Imprime os resultados sem tratamento de exceções
        print("\n---------- RESULTADO AVALIAÇÃO DE DESEMPENHO ----------\n")
        print("Tempo de Espera na Fila (Wq): " + valor_tempo_fila)
        print("Tempo de Permanência no Sistema (W): " + valor_tempo_sistema)
        print("Quantidade Ideal de Atendentes (M): " + self.qtd_ideal_atd.get())
        print("Taxa de Atendimento Ideal (μ): " + self.taxa_ideal_atd.get()+"\n")
        
    # Função executada ao clicar no botão 'Cancelar'
    def on_cancel(self):
        """Cancel and close the application."""
        self.quit()

    #### FUNÇÕES REFERENTES AOS CÁLCULOS DE AVALIAÇÃO DE DESEMPENHO ####
    
    @staticmethod
    def get_tempo_fila(self):
        if self.taxa_atendimento.get() == self.taxa_chegada.get(): 
            return "-", "-"
        else:
            tempo = self.taxa_chegada.get()/(self.taxa_atendimento.get()*(self.taxa_atendimento.get()-self.taxa_chegada.get()))
            return self.str_result( tempo)

    @staticmethod
    def get_tempo_sistema(self):
        if self.taxa_atendimento.get() == self.taxa_chegada.get(): 
            return "-", "-"
        else:
            tempo = 1/(self.taxa_atendimento.get()-self.taxa_chegada.get())
            return self.str_result(tempo)

    # Configuração ideal do sistema 
    #  Implemente então uma mensagem que informe o cenário ideal para o ADM do sistema, 
    # para que o mesmo possa convocar ou escalar mais funcionários para atender a esta 
    # situação-demanda, ou ainda informar quantos clientes cada um dos 5 funcionários 
    # teria que atender por hora, em caso de impossibilidade de adição de atendentes extras.
    @staticmethod
    def get_qtd_ideal_atd(self):
        qtd_ideal_atd = math.ceil(self.taxa_chegada.get()/(self.taxa_atendimento.get()/self.qtd_atendentes.get()))
        if (qtd_ideal_atd*self.taxa_atendimento_atd.get() == self.taxa_chegada.get()):
            qtd_ideal_atd += 1
        return str(qtd_ideal_atd) + " atendentes"

    @staticmethod
    def get_taxa_ideal_atd(self):
        taxa_ideal_atd = math.ceil(self.taxa_chegada.get()/self.qtd_atendentes.get())
        if (taxa_ideal_atd*self.qtd_atendentes.get() == self.taxa_chegada.get()):
            taxa_ideal_atd += 1
        return str(taxa_ideal_atd) + " atendimentos/h"

    # Função que realiza o tratamento de exceção e de erros para os cálculos de tempo
    @staticmethod
    def str_result(tempo):
        # Recebe o parâmetro do tempo já calculado
        result = ""
        # Se for menor que zero, então o sistema está desbalanceado e o tempo tende ao infinito
        if tempo < 0:
            # Define resultado infinito
            result = "∞"
        # Caso contrário, verifica a quantidade de horas, minutos e segundos do sistema e retorna
        else:
            horas = math.floor(tempo)
            minutos = math.floor((tempo-horas)*60)
            segundos = math.floor(((tempo-horas)*60-minutos)*60)
            # Define o resultado como as horas, minutos e segundos
            result = str(horas)+"h "+str(minutos)+"min "+str(segundos)+"s"

        # Por fim retorna o parâmetro tempo e o resultado tratado
        return (str(tempo), result)

# Código que executa a aplicação, exibindo assim a tela
if __name__ == "__main__":
    app = ttk.Window("Avaliação de Desempenho", "litera")
    DataEntryForm(app)
    app.mainloop()
