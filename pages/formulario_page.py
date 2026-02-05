import allure
from playwright.sync_api import expect

class FormularioPage:

    def __init__(self, page):
        self.page = page

    @allure.step("Acessar página de inscrição")
    def acessar(self):
        self.page.goto("https://www.hashtagtreinamentos.com/curso-python")

    @allure.step("Preencher nome: {nome}")
    def preencher_nome(self, nome):
        frame = self.page.frame_locator("iframe")
        frame.locator("#firstname").fill(nome)

#    def preencher_nome(self, nome):
#        self.page.fill('xpath=//*[@id="firstname"]', nome)

    @allure.step("Preencher email: {email}")
    def preencher_email(self, email):
        frame = self.page.frame_locator("iframe")
        frame.locator("#email").fill(email)

    @allure.step("Preencher telefone: {telefone}")
    def preencher_telefone(self, telefone):
        frame = self.page.frame_locator("iframe")
        frame.locator("#phone").fill(telefone)

    @allure.step("Enviar formulário")
    def enviar(self):
        frame = self.page.frame_locator("iframe")
        frame.locator("#_form_2475_submit").click()

    @allure.step("Validar inscrição com sucesso")
    def validar_sucesso(self):
        # Aguarda a navegação finalizar
        self.page.wait_for_load_state("networkidle")

        # Aguarda o texto correto (SEM o "1")
        expect(
            self.page.get_by_text("Conheça o Programa Completo")
        ).to_be_visible(timeout=15_000)