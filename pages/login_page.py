class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, usuario, password):
        self.page.goto("https://the-internet.herokuapp.com/login")
        self.page.fill("input[id='username']", usuario)
        self.page.fill("input[id='password']", password)
        self.page.click("button[type='submit']")

    def mensaje_exito(self):
        return self.page.get_by_text("You logged into a secure area!")

    def mensaje_error(self):
        return self.page.get_by_text("Your password is invalid!")