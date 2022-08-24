import math
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class DataEntryForm(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # form variables
        self.taxa_chegada = ttk.IntVar(value=165)
        self.qtd_atendentes = ttk.IntVar(value=5)
        self.taxa_atendimento_atd = ttk.IntVar(value=15)
        self.taxa_atendimento = ttk.IntVar(value=self.taxa_atendimento_atd.get()*self.qtd_atendentes.get())
        self.tempo_fila = ttk.StringVar(value="")
        self.tempo_sistema = ttk.StringVar(value="")
        self.qtd_ideal_atd = ttk.StringVar(value="")
        self.taxa_ideal_atd = ttk.StringVar(value="")

        # form header
        hdr_txt = "Por favor insira as informações de atendimento da empresa" 
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # form entries
        self.create_form_entry("Taxa de Chegada - λ:\n(em horas)", self.taxa_chegada)
        self.create_form_entry("Pontos de Atendimento - M:\n(unidades)", self.qtd_atendentes)
        self.create_form_entry("Taxa de Atendimento:\n(por atendente em horas)", self.taxa_atendimento_atd)
        self.create_form_entry("Taxa de Atendimento - μ:\n(total em horas)", self.taxa_atendimento, READONLY)
        self.create_buttonbox()

        # form header
        hdr_txt = "Resultado"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=(20,10))

        self.create_form_entry("Tempo Estimado de Espera\nna Fila (Wq):", self.tempo_fila, READONLY)
        self.create_form_entry("Tempo Estimado de\nPermanência no Sistema (W):", self.tempo_sistema, READONLY)
        self.create_form_entry("Quantidade Ideal de\nAtendentes (M):", self.qtd_ideal_atd, READONLY)

        hdr_txt = "Ou"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50, anchor=CENTER)
        hdr.pack(fill=X, pady=(3,3))

        self.create_form_entry("Taxa Média de Atendimento\nIdeal (μ/atendente):", self.taxa_ideal_atd, READONLY)

    def on_change(self):
        self.taxa_atendimento.set(self.taxa_atendimento_atd.get()*self.qtd_atendentes.get())

    def create_form_entry(self, label, variable, state = NORMAL):
        """Create a single form entry"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label, width=28)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable, state=state, validate="all", validatecommand=self.on_change)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def create_buttonbox(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Enviar",
            command=self.on_submit,
            bootstyle=PRIMARY,
            width=8,
        )
        sub_btn.pack(side=RIGHT, padx=5)

        cnl_btn = ttk.Button(
            master=container,
            text="Cancelar",
            command=self.on_cancel,
            bootstyle=DANGER,
            width=8,
        )
        cnl_btn.pack(side=RIGHT, padx=5)

    def on_submit(self):
        self.on_change()
        """Evaluate the results"""

        valor_tempo_fila, tempo_fila = self.get_tempo_fila(self)
        self.tempo_fila.set(tempo_fila)
        valor_tempo_sistema, tempo_sistema = self.get_tempo_sistema(self)
        self.tempo_sistema.set(tempo_sistema)
        self.qtd_ideal_atd.set(self.get_qtd_ideal_atd(self))
        self.taxa_ideal_atd.set(self.get_taxa_ideal_atd(self))
        
        print("\n---------- RESULTADO AVALIAÇÃO DE DESEMPENHO ----------\n")
        print("Tempo de Espera na Fila (Wq): " + valor_tempo_fila)
        print("Tempo de Permanência no Sistema (W): " + valor_tempo_sistema)
        print("Quantidade Ideal de Atendentes (M): " + self.qtd_ideal_atd.get())
        print("Taxa de Atendimento Ideal (μ): " + self.taxa_ideal_atd.get()+"\n")
        
    def on_cancel(self):
        """Cancel and close the application."""
        self.quit()

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

    @staticmethod
    def str_result(tempo):
        result = ""
        if tempo < 0:
            result = "∞"
        else:
            horas = math.floor(tempo)
            minutos = math.floor((tempo-horas)*60)
            segundos = math.floor(((tempo-horas)*60-minutos)*60)
            result = str(horas)+"h "+str(minutos)+"min "+str(segundos)+"s"

        return (str(tempo), result)

if __name__ == "__main__":
    app = ttk.Window("Avaliação de Desempenho", "litera")
    DataEntryForm(app)
    app.mainloop()
