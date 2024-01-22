import requests
from bs4 import BeautifulSoup

def obter_odds_bet365():
    url_bet365 = "https://www.bet365.com/#/HO/"
    response = requests.get(url_bet365)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        odds_bet365 = soup.find_all("SPAN_COM_A_CLASSE_OU_TAG_DAS_ODDS_BLAZE")
        return odds_bet365
    else:
        print("Erro ao acessar bet365. Código de status:", response.status_code)

def obter_odds_esporte_da_sorte():
    url_esporte_da_sorte = "https://m.esportesdasorte.com/ptb/authentication/signup?click_id=oatrpwjhhhuepamprbzx&affid=70795&campaign_id=9078&utm_source=brand&gclid=Cj0KCQiAwbitBhDIARIsABfFYII8lRmDyDu89Rk__xstWdbQgkmlJ4IMgOJwF9UPbNW2sGcjRSCL8g0aAvglEALw_wcB"
    response = requests.get(url_esporte_da_sorte)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        odds_esporte_da_sorte = soup.find_all("SPAN_COM_A_CLASSE_OU_TAG_DAS_ODDS_ESPORTE_DA_SORTE")
        return odds_esporte_da_sorte
    else:
        print("Erro ao acessar Esporte da Sorte. Código de status:", response.status_code)

def main():
    odds_bet365 = obter_odds_bet365()
    odds_esporte_da_sorte = obter_odds_esporte_da_sorte()

    if odds_bet365 and odds_esporte_da_sorte:
        for odd_bet365, odd_esporte_da_sorte in zip(odds_bet365, odds_esporte_da_sorte):
            print("Blaze:", odd_bet365.text, "| Esporte da Sorte:", odd_esporte_da_sorte.text)
    else:
        print("Erro ao obter odds de uma das casas de apostas.")

if __name__ == "__main__":
    main()
