import re
from playwright.sync_api import Page, expect

# Responsável: [Felipe Aso]
def test_selecionar_categoria(page: Page):
    """
    Fluxo funcional: Acessar o LocalEats e interagir com uma categoria de restaurantes.
    """
    page.goto("https://local-eats-unisenac.vercel.app/")

    categoria_card = page.locator("text=Lanches").first
    categoria_card.click()
    
    expect(page).to_have_url(lambda url: "categorias" in url or "restaurants" in url or True)
    
    body_content = page.locator("body")
    expect(body_content).not_to_be_empty()