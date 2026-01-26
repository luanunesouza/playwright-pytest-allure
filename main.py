print("ARQUIVO main.py ESTÁ SENDO EXECUTADO")


#abri um navegador
from playwright.sync_api import sync_playwright, expect
import time

with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)
    
    page = navegador.new_page()          # 👈 ISSO é o que faltava

    page.goto("https://www.hashtagtreinamentos.com/curso-python")   # 👈 força algo visível

    #page.locator('xpath=//*[@id="firstname"]').fill('Luan')

    page.fill('xpath=//*[@id="firstname"]', 'Luan')

    #page.locator('xpath=//*[@id="email"]').fill('luan@gmail.com')

    page.fill('xpath=//*[@id="email"]', 'luan@gmail.com')

    #page.locator('xpath=//*[@id="phone"]').fill("(11) 97377-7777")

    page.fill('xpath=//*[@id="phone"]', '(11) 97377-7777')
    
    #page.click('xpath=//*[@id="_form_2475_submit"]')

    page.locator('xpath=//*[@id="_form_2475_submit"]').click()
    
    time.sleep(10)

    expect(page.get_by_text("Conheça o Programa Completo")).to_be_visible()

    navegador.close()

    print("TESTE PASSOU")
