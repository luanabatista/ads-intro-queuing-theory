import math
from tkinter.ttk import Separator
from turtle import color
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class DataEntryForm(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # form variables
        self.taxa_chegada = ttk.DoubleVar(value=165)
        self.qtd_atendentes = ttk.DoubleVar(value=5)
        self.taxa_atendimento = ttk.DoubleVar(value=75)
        
        self.tempo_fila = ttk.DoubleVar(value=0)
        self.tempo_sistema = ttk.DoubleVar(value=0)
        self.qtd_ideal_atd = ttk.DoubleVar(value=0)
        self.taxa_ideal_atd = ttk.DoubleVar(value=0)

        # form header
        hdr_txt = "Por favor insira as informações de atendimento da empresa" 
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # form entries
        self.create_form_entry("Taxa Média de Chegada (λ):\n(em horas)", self.taxa_chegada)
        self.create_form_entry("Pontos de Atendimento (M):", self.qtd_atendentes)
        self.create_form_entry("Taxa Média de Atendimento (μ):\n(total em horas)", self.taxa_atendimento)
        self.create_buttonbox()

        

        
        


    def create_form_entry(self, label, variable):
        """Create a single form entry"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label, width=28)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable)
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
        """Print the contents to console and return the values."""
        
        if (self.taxa_chegada.get() > self.taxa_atendimento.get()):
          # form header
          hdr_txt = "Resultado" 
          hdr = ttk.Label(master=self, text=hdr_txt, width=50, bootstyle=DANGER)
          hdr.pack(fill=X, pady=(20,10))

        else:
          # form header
          hdr_txt = "Resultado" 
          hdr = ttk.Label(master=self, text=hdr_txt, width=50, bootstyle=SUCCESS)
          hdr.pack(fill=X, pady=(20,10))

        self.create_form_entry("Tempo Estimado de Espera\nna Fila:", self.tempo_fila)
        self.create_form_entry("Tempo Estimado de\nPermanência no Sistema:", self.tempo_sistema)

        self.tempo_fila.set(self.taxa_chegada.get()/(self.taxa_atendimento.get()*(self.taxa_atendimento.get()-self.taxa_chegada.get())))
        self.tempo_sistema.set(1/(self.taxa_atendimento.get()-self.taxa_chegada.get()))

        self.create_form_entry("Quantidade Ideal de\nAtendentes (M):", self.qtd_ideal_atd)
        self.create_form_entry("Taxa Média de Atendimento\nIdeal (μ):", self.taxa_ideal_atd)

        self.qtd_ideal_atd.set(math.ceil(self.taxa_chegada.get()/(self.taxa_atendimento.get()/self.qtd_atendentes.get())))
        self.taxa_ideal_atd.set(math.ceil(self.taxa_chegada.get()/self.qtd_atendentes.get()))
        return self.tempo_fila.get()
        
    def on_cancel(self):
        """Cancel and close the application."""
        self.quit()


if __name__ == "__main__":

    app = ttk.Window("Data Entry", "litera")
    DataEntryForm(app)
    app.mainloop()
