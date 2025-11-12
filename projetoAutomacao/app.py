import pyautogui
from time import sleep

pyautogui.click(536,516, duration=2)
pyautogui.write('jhonatan')

pyautogui.click(512,540, duration=2)
pyautogui.write('123456')

pyautogui.click(424,569, duration=2)

with open('produtos.txt', 'r') as arquivoLeitura:
    for linha in arquivoLeitura:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        pyautogui.click(340,521, duration=1)
        pyautogui.write(produto)
        pyautogui.click(328,551, duration=1)
        pyautogui.write(quantidade)
        pyautogui.click(298,574, duration=1)
        pyautogui.write(preco)
        pyautogui.click(208,736, duration=1)
        sleep(0.5)
    