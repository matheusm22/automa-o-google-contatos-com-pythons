import pandas as pd

def mesclar_contatos_por_telefone(df):
    # Substitua 'Phone 1 - Value' pelo nome real da coluna de número de telefone no seu arquivo CSV
    coluna_telefone = 'Phone 1 - Value'

    # Convertendo todos os valores para string, tratando valores nulos
    df = df.applymap(lambda x: str(x) if pd.notna(x) else '')

    # Mescla os contatos com base no número de telefone
    contatos_mesclados = df.groupby(coluna_telefone, as_index=False).agg(lambda x: ', '.join(x.unique()))

    return contatos_mesclados

def main():
    # Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo CSV
    arquivo_csv = 'contacts2.csv'

    try:
        # Lê o arquivo CSV
        df = pd.read_csv(arquivo_csv, low_memory=False)

        # Mescla os contatos por número de telefone
        contatos_mesclados = mesclar_contatos_por_telefone(df)

        # Substitua 'contatos_mesclados.csv' pelo nome desejado para o arquivo de contatos mesclados
        arquivo_mesclado = 'mesclados.csv'
        contatos_mesclados.to_csv(arquivo_mesclado, index=False)

        print(f"Contatos mesclados salvos no arquivo '{arquivo_mesclado}'.")
    except FileNotFoundError:
        print(f"O arquivo '{arquivo_csv}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
