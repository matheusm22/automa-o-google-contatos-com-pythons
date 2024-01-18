import pandas as pd

def filtrar_e_salvar_contatos(df, nome_filtro, nome_coluna='Name'):
    filtro = df[nome_coluna].str.contains(nome_filtro, case=False, na=False)
    contatos_filtrados = df[filtro].copy()

    if not contatos_filtrados.empty:
        nome_arquivo = f'contatos_{nome_filtro.lower()}.csv'
        contatos_filtrados.to_csv(nome_arquivo, index=False)
        print(f"Arquivo '{nome_arquivo}' salvo com os contatos de '{nome_filtro}'.")
    else:
        print(f"Não foram encontrados contatos de '{nome_filtro}'.")

def main():
    # Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo CSV
    arquivo_csv = 'contacts.csv'

    try:
        # Lê o arquivo CSV
        df = pd.read_csv(arquivo_csv)

        # Lista de nomes para filtrar
        nomes_filtro = ['junho', 'JUNHO']

        # Substitua 'Name' pelo nome real da coluna no seu arquivo CSV
        nome_coluna = 'Name'

        # Itera sobre os nomes de filtro
        for nome_filtro in nomes_filtro:
            filtrar_e_salvar_contatos(df, nome_filtro, nome_coluna)

        print("Processo concluído.")
    except FileNotFoundError:
        print(f"O arquivo '{arquivo_csv}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
