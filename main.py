import pyautogui


pyautogui.PAUSE = 0.5

nome = "Francisval Cavalcante de Sousa"
pyautogui.press("win")
pyautogui.write("Bloco de notas")
pyautogui.press("PgDn")
pyautogui.press("PgUp")
pyautogui.press("enter")
pyautogui.write(nome)
