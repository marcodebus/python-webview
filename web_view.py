import webview
import sys

pwd_file = 'pwd.txt'


class Api:
    password = '12345'
    app = None

    def __init__(self, password):
        self.password = password

    def verifyPassword(self, password):
        if self.password == str(password):
            print('password correct')
            self.app.destroy()
            sys.exit(0)

    def setApp(self, app):
        self.app = app


def read_pwd(input_file):
    with open(input_file) as opened_file:
        return opened_file.read().strip()


if __name__ == '__main__':
    pwd = read_pwd(pwd_file)
    api = Api(pwd)
    view = webview.create_window('Full-screen window', 'view.html', fullscreen=True, js_api=api)
    api.setApp(view)
    webview.start()
