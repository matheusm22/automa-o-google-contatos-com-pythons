import pandas as pd

def renomear_contato(nome):
    nomes_nao_renomear = ['inativo', 'inativos' , 'INATIVOS', 'INATIVO', 'maury', 'MAURY', 'jannis', 'JANNIS', 'dani', 'DANI',
                           'contabilidade', 'CONTABILIDADE', 'adv', 'ADV', 'passivas', 'passiva', 'PASSIVAS','PASSIVA', 'rodizio', 'RODIZIO', 'fiscal','FISCAL']
    
    if pd.isna(nome) or nome.lower() in nomes_nao_renomear:
        return nome
    else:
        # Supondo que o DDD esteja no início do nome entre colchetes, ex: [81] João
        ddd = None
        if '[' in nome and ']' in nome:
            ddd = nome.split('[')[1].split(']')[0]
        else:
            # Se não houver colchetes, tentar encontrar DDD em qualquer lugar no nome
            for token in nome.split():
                if token.isdigit() and len(token) == 2:
                    ddd = token
                    break
        
        estado = obter_estado_por_ddd(ddd)
        
        return f'Contato {estado}' if estado else nome

def obter_estado_por_ddd(ddd):
    # Mapear DDD para Estado (adicione mais conforme necessário)
    ddd_estado = {
        '11': 'SP', '12': 'SP', '13': 'SP', '14': 'SP', '15': 'SP', '16': 'SP', '17': 'SP', '18': 'SP', '19': 'SP',
        '21': 'RJ', '22': 'RJ', '24': 'RJ',
        '27': 'ES', '28': 'ES',
        '31': 'MG', '32': 'MG', '33': 'MG', '34': 'MG', '35': 'MG', '37': 'MG', '38': 'MG', '39': 'MG',
        '41': 'PR', '42': 'PR', '43': 'PR', '44': 'PR', '45': 'PR', '46': 'PR',
        '47': 'SC', '48': 'SC', '49': 'SC',
        '51': 'RS', '53': 'RS', '54': 'RS', '55': 'RS',
        '61': 'DF',
        '62': 'GO', '64': 'GO',
        '63': 'TO',
        '65': 'MT', '66': 'MT',
        '67': 'MS',
        '68': 'AC',
        '69': 'RO',
        '71': 'BA', '73': 'BA', '74': 'BA', '75': 'BA', '77': 'BA',
        '79': 'SE',
        '81': 'PE', '82': 'AL', '83': 'PB', '84': 'RN',
        '85': 'CE', '86': 'PI', '87': 'PE', '88': 'CE', '89': 'PI',
        '91': 'PA', '92': 'AM', '93': 'PA', '94': 'PA', '95': 'RR', '96': 'AP', '97': 'AM', '98': 'MA', '99': 'MA',
    }
    
    return ddd_estado.get(ddd, None)

def salvar_arquivo_por_estado(df, estado):
    if not df.empty:
        nome_arquivo = f'arquivo_{estado}.csv'
        df.to_csv(nome_arquivo, index=False)
        print(f"Arquivo '{nome_arquivo}' salvo.")
    else:
        print(f"O estado '{estado}' não possui contatos.")

def main():
    # Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo CSV
    arquivo_csv = 'contacts.csv'
    
    try:
        # Lê o arquivo CSV
        df = pd.read_csv(arquivo_csv)
        
        # Substitua 'Name' pelo nome real da coluna no seu arquivo CSV
        nome_coluna = 'Name'
        df[nome_coluna] = df[nome_coluna].apply(renomear_contato)
        
        # Filtra linhas com estados válidos e diferentes de NaN
        df_valido = df[df[nome_coluna].notna() & df[nome_coluna].str.startswith('Contato')]
        
        # Cria uma série de booleanos indicando se o estado é SP, RJ ou MG
        estados = ['SP', 'RJ', 'MG', 'ES', 'PR', 'SC', 'RS', 'DF', 'GO', 'TO', 'MT', 'MS', 'AC', 'RO', 'BA', 'SE', 'PE', 'AL', 'PB', 'RN', 'CE', 'PI', 'PA', 'AM', 'RR', 'AP', 'MA']
        
        for estado in estados:
            estado_filtrado = df_valido[nome_coluna].str.startswith(f'Contato {estado}')
            df_estado = df_valido[estado_filtrado].copy()
            salvar_arquivo_por_estado(df_estado, estado)
        
        print("Processo concluído.")
    except FileNotFoundError:
        print(f"O arquivo '{arquivo_csv}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
