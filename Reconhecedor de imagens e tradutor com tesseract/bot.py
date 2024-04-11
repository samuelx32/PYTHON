import pytesseract
import os 
import cv2
from playwright.sync_api import sync_playwright, expect
import pyautogui as auto
import sys
import xlwings as xw
from pynput.mouse import Button,Controller
import time
import requests
import tkinter as tk
from tkinter import filedialog

#Selecione a imagem desejada, agile-manifesto.png, e retorne o texto da imagem traduzido.

def translate_text(text, source_lang, target_lang):
    api_url = 'https://api.mymemory.translated.net/get'
    params = {
        'q': text,
        'langpair': f'{source_lang}|{target_lang}'
    }
    response = requests.get(api_url, params=params)
    data = response.json()
    translated_text = data['responseData']['translatedText']
    return translated_text



def extrair_texto_imagem(path,caminho_ts):
    texto = ''

    imagem = cv2.imread(path)
    
        
    pytesseract.pytesseract.tesseract_cmd = caminho_ts
    texto = pytesseract.image_to_string(imagem, lang='eng')
    time.sleep(5)

    return texto



if __name__ == '__main__':
    if getattr(sys, 'frozen', False):
        diretorio = os.path.dirname(sys.executable)
        arquivo = os.path.basename(sys.executable)[:-4]
    elif __file__:
        diretorio = os.path.dirname(__file__)
        arquivo = os.path.basename(__file__)[:-3] 

    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename(filetypes=[("IMG files", "*.png"),("IMG files", "*.jpg")])
    caminho_ts = rf"{diretorio}\Tesseract-OCR\tesseract.exe"
    text = extrair_texto_imagem(path,caminho_ts)
    translated_text = translate_text(text, 'en', 'pt')
    auto.alert(translated_text)
