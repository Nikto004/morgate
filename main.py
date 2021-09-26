from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import webbrowser


Window.size=(480, 853)

from kivy.config import Config
Config.set('kivy', 'keybord_mode', 'sistemanddock')



class LoginScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('login.kv')
    def logger(self):
        if len(self.root.ids.user.text) > 10 and len(self.root.ids.password.text) > 7:
            self.root.ids.Welcome_label.text = f'Успешно'
        else:
            self.root.ids.Welcome_label.text = f'Повторите ввод'
            self.root.ids.user.text = ""
            self.root.ids.password.text = ""
    # def register(self):
    #     return register()




if __name__ == "__main__":
    MyApp().run()