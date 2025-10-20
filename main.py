from utils.db_reader import carregar_dados
from utils.layout_loader import carregar_template
from utils.pdf_generator import gerar_pdf

def main():
    dados = carregar_dados("dados.db")
    print("DADOS------")
    print(dados)
    template = carregar_template("template.json")
    print("TEMPLATE")
    print(template)
    gerar_pdf(dados, template, output_path="folheto_final.pdf")

if __name__ == "__main__":
    main()