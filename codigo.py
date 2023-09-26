#pyautogui.click -> clicar com o mouse
#pyautogui.write -> escrever um texto
#pyautogui.press -> apertar 1 tecla
#pyautogui.hotkey -> atalho (combinação de teclas)

import time
import pyautogui

pyautogui.PAUSE = 0.5 #Intervalo entre comandos da automação

# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# esperar o site carregar
time.sleep(3)

# Fazer login
pyautogui.click(x=653, y=496)
pyautogui.write("francisvalcs@gmail.com")
pyautogui.press("tab")
pyautogui.write("1234")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep()



