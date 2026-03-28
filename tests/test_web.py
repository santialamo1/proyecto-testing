from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_login_exitoso(page):
    login = LoginPage(page)
    login.login("tomsmith", "SuperSecretPassword!")
    expect(login.mensaje_exito()).to_be_visible()

def test_login_fallido(page):
    login = LoginPage(page)
    login.login("tomsmith", "password_malo")
    expect(login.mensaje_error()).to_be_visible()