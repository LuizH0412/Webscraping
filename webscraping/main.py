import requests
from bs4 import BeautifulSoup



# Função feita para extrair os dados da tabela do site.
def extrair_dados(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    resposta = requests.get(url, headers=headers)

    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, 'html.parser')
        linhas = soup.find(id='tabelaResultado').find('tbody').find_all('tr')

        dados_fundo = []
        # Iterando sobre todas as informações e armazenando em um dicionário.
        for linha in linhas:
            dados_tabela = linha.find_all('td')
            dados_armazenar = {
                "Nome": dados_tabela[0].text.strip(),
                "Setor": dados_tabela[1].text.strip(),
                "Cotação": dados_tabela[2].text.strip(),
                "P/VP": dados_tabela[5].text.strip(),
                "DY %": dados_tabela[4].text.strip(),
            }
            dados_fundo.append(dados_armazenar)

        return dados_fundo
    else:
        print('Falha ao acessar a página')
        return None
    

# Função que mostra no terminal as informações que foram armazenadas anteriormente
def mostrar_dados_no_terminal(dados_fundo):
    if dados_fundo:
        for fundo in dados_fundo:
            print( 
                f"[{fundo['Nome']}]\n"
                f"\tSetor: {fundo['Setor']}\n"
                f"\tCotação: {fundo['Cotação']}\n"
                f"\tP/VP: {fundo['P/VP']}\n"
                f"\tDY %: {fundo['DY %']}\n"
            )


# Função principal que é executada quando o script é executado diretamente
if __name__ == "__main__":
    url = 'https://www.fundamentus.com.br/fii_resultado.php'
    dados_fundo = extrair_dados(url)
    if dados_fundo:
        mostrar_dados_no_terminal(dados_fundo)