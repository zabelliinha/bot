from sqlite3 import Time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from datetime import datetime
import requests



assertividade = True
win = 0
porcentagem = win
loss = 0

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")
option.binary_location = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
driver.get('https://blaze.com/pt/games/double')
cores = []
padraoGeral = True
padrao1 = False
padrao2 = False
padrao3 = False
padrao4 = False
padrao5 = False
padrao6 = False


I_TOKEN = ""
I_CHAT_GRUPO = ""
MSG = "✅ ᴏ ʀᴏʙᴏᴢɪɴʜᴏ ᴍᴀɪs ʟᴇɢᴀʟ ᴅᴏ ᴘʟᴀɴᴇᴛᴀ!✅"
I_URL = "https://api.telegram.org/bot" + I_TOKEN + \
    "/sendMessage" + "?chat_id=" + I_CHAT_GRUPO + "&text=" + MSG
I_RESUL = requests.get(I_URL)


def sendMessage(text):
    token = ""
    chat_id = ""
    url_req = "https://api.telegram.org/bot" + token + \
        "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)


while True:
    time.sleep(1)
    resp = ""
    respresult = ""
    entrada = False
    resultado = False

#CALCULAR ASSSERTIVIDADE
    if assertividade == True:
        if loss >= 1:
         porcentagem = 100-(loss/win*100)
        else:
          assertividade = False
          

#LOSS E WINS
    if padrao1 == True:

        # RESULTADO LOSS PADRAO 1
        if cores[:3] == ['🔴', '🔴', '🔴']:
            loss += 1
            print("Loss")
            if loss >= 1:
                respresult = f"NÃO FOI DESSA VEZ ❌\n\n Placar | Win - {win} | Loss - {loss}| Acertos - {round(float(porcentagem))}%"
            if loss == 0:
                respresult = f"NÃO FOI DESSA VEZ ❌\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            if loss == 1:
                respresult = f"NÃO FOI DESSA VEZ ❌\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
                del cores[:]

            resultado = True
            padraoGeral = True
            padrao1 = False
            assertividade = True

      
      #RESULTADO WIN PADRÃO 1
        if cores[:1] == ['⚫️']:
            win += 1
            print("Win")
            if win >=1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - {round(float(porcentagem))}%"
            if loss == 0:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            if loss == 1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            del cores[:]

            resultado = True
            padrao1 = False
            padraoGeral = True
            assertividade = True
               
        if cores[:2] == ['🔴', '⚫️']:
            win += 1
            print("Win")
            if win >=1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - {round(float(porcentagem))}%"
            if loss == 0:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            if loss == 1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            del cores[:]

            resultado = True
            padrao1 = False
            padraoGeral = True
            assertividade = True
            
        if cores[:3] == ['🔴', '🔴', '⚫️']:
            win += 1
            print("Win")
            if win >=1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - {round(float(porcentagem))}%"
            if loss == 0:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            if loss == 1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            del cores[:]

            resultado = True
            padrao1 = False
            padraoGeral = True
            assertividade = True

      

    if padrao2 == True:

        # RESULTADO LOSS PADRAO 2
        if cores[:3] == ['⚫️', '⚫️', '⚫️']:
            loss += 1
            print("Loss")
            if loss >= 1:
                respresult = f"NÃO FOI DESSA VEZ ❌\n\n Placar | Win - {win} | Loss - {loss}| Acertos - {round(float(porcentagem))}%"
            if loss == 0:
                respresult = f"NÃO FOI DESSA VEZ ❌\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            if loss == 1:
                respresult = f"NÃO FOI DESSA VEZ ❌\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
                del cores[:]

            resultado = True
            padrao2 = False
            padraoGeral = True
            assertividade = True

          # RESULTADO WIN PADRAO 2
        if cores[:1] == ['🔴']:
            win += 1
            print("Win")
            if win >=1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - {round(float(porcentagem))}%"
            if loss == 0:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            if loss == 1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            del cores[:]

            resultado = True
            padrao2 = False
            padraoGeral = True
            assertividade = True

        if cores[:2] == ['⚫️', '🔴']:
            win += 1
            print("Win")
            if win >=1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - {round(float(porcentagem))}%"
            if loss == 0:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            if loss == 1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            del cores[:]

            resultado = True
            padrao2 = False
            padraoGeral = True
            assertividade = True

        if cores[:3] == ['⚫️', '⚫️', '🔴']:
            win += 1
            print("Win")
            if win >=1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - {round(float(porcentagem))}%"
            if loss == 0:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            if loss == 1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            del cores[:]

            resultado = True
            padrao2 = False
            padraoGeral = True
            assertividade = True

         
    if padrao3 == True:

        # RESULTADO LOSS PADRAO 3
        if cores[:3] == ['🔴', '🔴', '🔴']:
            loss += 1
            print("Loss")
            if loss >= 1:
                respresult = f"NÃO FOI DESSA VEZ ❌\n\n Placar | Win - {win} | Loss - {loss}| Acertos - {round(float(porcentagem))}%"
            if loss == 0:
                respresult = f"NÃO FOI DESSA VEZ ❌\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            if loss == 1:
                respresult = f"NÃO FOI DESSA VEZ ❌\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
                del cores[:]

            resultado = True
            padrao3 = False
            padraoGeral = True
            assertividade = True
          
          # RESULTADO WIN PADRAO 3
        if cores[:1] == ['⚫️']:
            win += 1
            print("Win")
            if win >=1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - {round(float(porcentagem))}%"
            if loss == 0:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            if loss == 1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            del cores[:]

            resultado = True
            padrao3 = False
            padraoGeral = True
            assertividade = True

        if cores[:2] == ['🔴', '⚫️']:
            win += 1
            print("Win")
            if win >=1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - {round(float(porcentagem))}%"
            if loss == 0:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            if loss == 1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            del cores[:]

            resultado = True
            padrao3 = False
            padraoGeral = True
            assertividade = True

        if cores[:3] == ['🔴', '🔴', '⚫️']:
            win += 1
            print("Win")
            if win >=1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - {round(float(porcentagem))}%"
            if loss == 0:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            if loss == 1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            del cores[:]

            resultado = True
            padrao3 = False
            padraoGeral = True
            assertividade = True



    if padrao4 == True:

        # RESULTADO LOSS PADRAO 4
        if cores[:3] == ['⚫️', '⚫️', '⚫️']:
            print("Loss")
            loss += 1
            if loss >= 1:
                respresult = f"NÃO FOI DESSA VEZ ❌\n\n Placar | Win - {win} | Loss - {loss}| Acertos - {round(float(porcentagem))}%"
            if loss == 0:
                respresult = f"NÃO FOI DESSA VEZ ❌\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            if loss == 1:
                respresult = f"NÃO FOI DESSA VEZ ❌\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            
                del cores[:]

            resultado = True
            padraoGeral = True
            padrao4 = False
            assertividade = True

          # RESULTADO WIN PADRAO 4
        if cores[:1] == ['🔴']:
            win += 1
            print("Win")
            if win >=1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - {round(float(porcentagem))}%"
            if loss == 0:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            if loss == 1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            del cores[:]

            resultado = True
            padraoGeral = True
            padrao4 = False
            assertividade = True

        if cores[:2] == ['⚫️', '🔴']:
            win += 1
            print("Win")
            if win >=1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - {round(float(porcentagem))}%"
            if loss == 0:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            if loss == 1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            del cores[:]

            resultado = True
            padraoGeral = True
            padrao4 = False
            assertividade = True

        if cores[:3] == ['⚫️', '⚫️', '🔴']:
            win += 1
            print("Win")
            if win >=1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - {round(float(porcentagem))}%"
            if loss == 0:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            if loss == 1:
                respresult = f"DEU NICE 💚💚💚\n\n Placar | Win - {win} | Loss - {loss}| Acertos - 'Calculando...'"
            del cores[:]

            resultado = True
            padraoGeral = True
            padrao4 = False
            assertividade = True

          

    if resultado == True:
        if respresult:
            sendMessage(respresult)
            print("Resultado Enviado")

    c = driver.page_source
    soup = BeautifulSoup(c, 'html.parser')
    dat = soup.find('div', class_="time-left")
    if 'Blaze Girou' in dat.getText():
        numero_cor = int(dat.getText().strip("Blaze Girou !"))
        if numero_cor == 0:
            cores.append('⚪️')

        elif numero_cor > 0 and numero_cor < 8:
            cores.append('🔴')
        else:
            cores.append('⚫️')
        print(cores)
        
        site = "https://blaze.com/pt/games/double"
        código_blaze = "https://blaze.com/pt/r/DqdyBx"

        if padraoGeral == True:
          
            if cores[:3] == ['⚫️', '🔴', '🔴']:
                resp = f"🐉 ENTRADA CONFIRMADA 🐉 \n \n APÓS O: {numero_cor}  \n \n 🍀ENTRAR NO : ⚫\n\n❗PROTEGER NO BRANCO\n\n🏆NÚMERO DE GALES: ATÉ DOIS GALES\n\nIr para blaze: {site}\n\nGanhe rodadas grátis: {código_blaze}"
                entrada = True
                del cores[:]
                padrao1 = True
                padraoGeral = False

            if cores[:3] == ['🔴', '⚫️', '⚫️']:
                resp = f"🐉 ENTRADA CONFIRMADA 🐉\n \n APÓS O: {numero_cor}  \n \n 🍀ENTRAR NO: 🔴\n\n❗PROTEGER NO BRANCO\n\n🏆NÚMERO DE GALES: ATÉ DOIS GALES\n\nIr para blaze: {site}\n\nGanhe rodadas grátis: {código_blaze}"
                entrada = True
                del cores[:]
                padrao2 = True
                padraoGeral = False

            if cores[:3] == ['🔴', '🔴', '⚫️']:
                resp = f"🐉 ENTRADA CONFIRMADA 🐉\n \n APÓS O: {numero_cor}  \n \n 🍀ENTRAR NO:  ⚫️\n\n❗PROTEGER NO BRANCO\n\n🏆NÚMERO DE GALES: ATÉ DOIS GALES\n\nIr para blaze: {site}\n\nGanhe rodadas grátis: {código_blaze}"
                entrada = True
                del cores[:]
                padrao3 = True
                padraoGeral = False

            if cores[:3] == ['⚫️', '⚫️', '🔴']:
                resp = f"🐉 ENTRADA CONFIRMADA 🐉\n \n APÓS O: {numero_cor}  \n \n 🍀ENTRAR NO: 🔴\n\n❗PROTEGER NO BRANCO\n\n🏆NÚMERO DE GALES: ATÉ DOIS GALES\n\nIr para blaze: {site}\n\nGanhe rodadas grátis: {código_blaze}"
                entrada = True
                del cores[:]
                padrao4 = True
                padraoGeral = False
            
        #deleta cores do terminal
             
        if cores[:4] == ['⚫️', '⚫️', '⚫️', '⚫️']:
            del cores[:]

        if cores[:4] == ['🔴', '🔴', '🔴', '🔴']:
            del cores[:]

        if cores[:3] == ['🔴', '⚫️', '🔴']:
            del cores[:]

        if cores[:3] == ['⚫️', '🔴', '⚫️']:
            del cores[:]

        if cores[:4] == ['🔴', '🔴', '🔴', '⚪️']:
            del cores[:]

        if cores[:4] == ['⚫️', '⚫️', '⚫️', '⚪️']:
            del cores[:]

        if cores[:4] == ['🔴', '🔴', '🔴', '⚫️']:
            del cores[:]

        if cores[:4] == ['⚫️', '⚫️', '⚫️', '🔴']:
            del cores[:]

        if cores[:3] == ['⚪️', '⚫️', '⚫️']:
            del cores[:]

        if cores[:3] == ['⚪️', '⚪️', '⚫️']:
            del cores[:]

        if cores[:3] == ['⚪️', '⚪️', '⚪️']:
            del cores[:]

        if cores[:3] == ['⚫️', '⚪️', '⚪️']:
            del cores[:]

        if padrao4 == False:
            if cores[:3] == ['⚫️', '⚫️', '⚪️']:
                del cores[:]

        if cores[:3] == ['⚫️', '⚪️', '⚫️']:
            del cores[:]

        if cores[:3] == ['⚪️', '🔴', '🔴']:
            del cores[:]

        if cores[:3] == ['⚪️', '⚫️', '🔴']:
            del cores[:]

        if cores[:3] == ['⚪️', '🔴', '⚫️']:
            del cores[:]

        if cores[:3] == ['⚪️', '⚪️', '🔴']:
            del cores[:]

        if cores[:3] == ['⚪️', '⚪️', '⚪️']:
            del cores[:]

        if cores[:3] == ['🔴', '⚪️', '⚪️']:
            del cores[:]

        if padrao3 == False:
            if cores[:3] == ['🔴', '🔴', '⚪️']:
                del cores[:]

        if cores[:3] == ['🔴', '⚪️', '🔴']:
            del cores[:]

        if cores[:3] == ['🔴', '⚪️', '⚫️']:
            del cores[:]

        if cores[:3] == ['⚫️', '⚪️', '🔴']:
            del cores[:]

        if cores[:3] == ['⚪️', '🔴', '⚪️']:
            del cores[:]

        if cores[:3] == ['⚪️', '⚫️', '⚪️']:
            del cores[:]

        if cores[:3] == ['⚫️', '🔴', '⚪️']:
            del cores[:]

        if cores[:3] == ['🔴', '⚫️', '⚪️']:
            del cores[:]

        if entrada == True:
            if resp:
                sendMessage(resp)
                print("Entrada Enviada")

    time.sleep(1.5)
    
    
