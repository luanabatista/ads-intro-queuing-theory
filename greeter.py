from ctypes import alignment
import flet
from flet import ElevatedButton, Text, TextField, Row

'''def main(page):
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(Text(f"Hello, {name}!"))

    txt_name = TextField(label="Your name")

    page.add(txt_name, ElevatedButton("Say hello!", on_click=btn_click))

flet.app(target=main)'''

def main(page):
    page.title = "Flet counter example"
    page.vertical_alignment = "center"

    def btn_click(e):
        print(taxa_chegada.value)
        if not (taxa_chegada.value==0 and atendentes.value==0 and taxa_atendimento.value==0):

            taxa_chegada.error_text = None
            atendentes.error_text = None
            taxa_atendimento.error_text = None

            if not taxa_chegada.value==0:
                taxa_chegada.error_text = "Informe a taxa média de chegada"
                page.update()
            if not atendentes.value==0:
                atendentes.error_text = "Informe a quantidade de pontos de atendimento"
                page.update()
            if not taxa_atendimento.value==0:
                taxa_atendimento.error_text = "Informe a taxa média de atendimento"
                page.update()

        else:
            page.clean()
        

    taxa_chegada = TextField(label="Taxa média de chegada (λ)", value="165", width=250)
    atendentes = TextField(label="Pontos de atendimento", value="5", width=250)
    taxa_atendimento = TextField(label="Taxa média de atendimento (μ)", value="15*atendentes", width=250)

    page.add(
        Row(
            [   
                taxa_chegada, 
                atendentes, 
                taxa_atendimento
            ]
        ),
        Row(
            [   
                ElevatedButton("Enviar", on_click=btn_click),
            ]
        )
    )

flet.app(target=main)