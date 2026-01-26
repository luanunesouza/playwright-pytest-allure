import pytest
import allure
from playwright.sync_api import sync_playwright


@pytest.fixture
def page(request):
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        yield page  # 🔥 TESTE RODA AQUI

        # 🔥 TEARDOWN – SEMPRE EXECUTA
        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            screenshot = page.screenshot(full_page=True)
            allure.attach(
                screenshot,
                name="Screenshot - Falha",
                attachment_type=allure.attachment_type.PNG
            )

        context.close()
        browser.close()


# Necessário para saber se o teste falhou
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


# Converte tags do Gherkin em pytest.mark
def pytest_bdd_apply_tag(tag, function):
    function.pytestmark = getattr(pytest.mark, tag)
