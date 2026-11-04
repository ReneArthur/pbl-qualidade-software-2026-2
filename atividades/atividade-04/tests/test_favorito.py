import re
from playwright.sync_api import Page, expect

# Por: Rene Arthur Rocha de Souza
def test_favorito(page: Page) -> None:
    page.goto("https://local-eats-unisenac.vercel.app/static/login.html")
    page.get_by_role("textbox", name="teste@teste.com").click()
    page.get_by_role("textbox", name="teste@teste.com").fill("testerene@email.com")
    page.get_by_role("textbox", name="Sua senha secreta").click()
    page.get_by_role("textbox", name="Sua senha secreta").fill("1234")
    page.locator("#loginForm").get_by_role("button", name="Entrar").click()
    page.get_by_role("link", name="Restaurante Sabor 0").click()
    page.get_by_role("button", name=" Favoritar").click()
    page.get_by_role("link", name="Meus Favoritos").click()
    expect(page.locator("#favoritesGrid")).to_contain_text("Restaurante Sabor 0")
    page.get_by_role("button", name=" Remover Favorito").click()
    expect(page.locator("#favoritesGrid")).to_be_empty()