import webview
import sys
from threading import *
import time
# ----------------------------

pwd_file = 'pwd.txt'
# ----------------------------


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
        else:
            print('password does not match...')

    def setApp(self, app):
        self.app = app


def read_pwd(input_file):
    with open(input_file) as opened_file:
        return opened_file.read().strip()


# -------------------Thread - close_app--------------------------------------

def close_app(handle):
    time.sleep(5)
    print('checking password now...')
    val = str(input("Enter Password: "))
    handle.verifyPassword(val)
# ------------------------------------------------------------------------


if __name__ == '__main__':

    pwd = read_pwd(pwd_file)
    print(pwd)
    api = Api(pwd)
    t1 = Thread(target=close_app, args=(api,),)
    t1.daemon = True
    t1.start()
    view = webview.create_window('Full-screen window', 'view.html', fullscreen=False, js_api=api)
    api.setApp(view)
    webview.start()
    print('END')
