executar codegen do playwright
python -m playwright codegen --target python-pytest https://local-eats-unisenac.vercel.app/

comando para gerar arquivo com relatório de teste para Linux
python -m pytest -v | tee relatorio-pytest.txt