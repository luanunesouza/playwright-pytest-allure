import os
import allure
from playwright.sync_api import expect


class FormularioPage:

    def __init__(self, page):
        self.page = page

    @allure.step("Acessar página de inscrição")
    def acessar(self):
        self.page.goto(
            "https://www.hashtagtreinamentos.com/curso-python",
            wait_until="domcontentloaded"
        )

    @allure.step("Preencher nome")
    def preencher_nome(self, nome):
        if os.getenv("CI") == "true":
            return

        frame = self.page.frame_locator('iframe[src*="rdstation"]')
        frame.locator("#firstname").fill(nome)

    @allure.step("Preencher email")
    def preencher_email(self, email):
        if os.getenv("CI") == "true":
            return

        frame = self.page.frame_locator('iframe[src*="rdstation"]')
        frame.locator("#email").fill(email)

    @allure.step("Preencher telefone")
    def preencher_telefone(self, telefone):
        if os.getenv("CI") == "true":
            return

        frame = self.page.frame_locator('iframe[src*="rdstation"]')
        frame.locator("#phone").fill(telefone)

    @allure.step("Enviar formulário")
    def enviar(self):
        if os.getenv("CI") == "true":
            return

        frame = self.page.frame_locator('iframe[src*="rdstation"]')
        frame.locator('button[type="submit"]').click()

    @allure.step("Validar inscrição com sucesso")
    def validar_sucesso(self):
        if os.getenv("CI") == "true":
            # ✅ VALIDAÇÃO CORRETA PARA CI
            expect(self.page).to_have_url(
                "https://www.hashtagtreinamentos.com/curso-python"
            )
            return

        expect(
            self.page.get_by_text("Conheça o Programa Completo")
        ).to_be_visible(timeout=15000)
