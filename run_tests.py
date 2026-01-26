import subprocess

print("Executando testes...")
subprocess.run(
    "pytest --alluredir=allure-results",
    shell=True,
    check=True
)

print("Gerando relatório Allure...")
subprocess.run(
    "allure generate allure-results -o allure-report --clean",
    shell=True,
    check=True
)

print("Abrindo relatório...")
subprocess.run(
    "allure open allure-report",
    shell=True
)
