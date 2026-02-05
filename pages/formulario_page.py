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

        # 🔥 SCROLL OBRIGATÓRIO (isso destrava o iframe no CI)
        self.page.mouse.wheel(0, 3000)

        # 🔥 Espera o iframe EXISTIR
        self.page.wait_for_selector(
            'iframe[src*="rdstation"]',
            timeout=20000
        )

        # 🔥 Só agora cria o frame_locator
        self.frame = self.page.frame_locator(
            'iframe[src*="rdstation"]'
        )

    @allure.step("Preencher nome")
    def preencher_nome(self, nome):
        self.frame.locator("#firstname").fill(nome)

    @allure.step("Preencher email")
    def preencher_email(self, email):
        self.frame.locator("#email").fill(email)

    @allure.step("Preencher telefone")
    def preencher_telefone(self, telefone):
        self.frame.locator("#phone").fill(telefone)

    @allure.step("Enviar formulário")
    def enviar(self):
        self.frame.locator("#_form_2475_submit").click()

    @allure.step("Validar sucesso")
    def validar_sucesso(self):
        expect(
            self.page.get_by_text("Conheça o Programa Completo")
        ).to_be_visible(timeout=15000)
