import allure
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pages.formulario_page import FormularioPage

BASE_DIR = Path(__file__).parent
FEATURE_FILE = BASE_DIR.parent / "tests" / "test_inscricao.feature"

scenarios(str(FEATURE_FILE))


#### scenarios("../tests/test_inscricao.feature")

@given("que acesso a página de inscrição", target_fixture="formulario")
def acessar_pagina(page):
    formulario = FormularioPage(page)
    formulario.acessar()
    return formulario

@when("preencho o formulário")
def preencher_formulario(formulario):
    formulario.preencher_nome("Luan")
    formulario.preencher_email("luan@gmail.com")
    formulario.preencher_telefone("(11) 97377-7777")
    formulario.enviar()

@then("vejo a página de sucesso")
def validar_sucesso(formulario):
    formulario.validar_sucesso()