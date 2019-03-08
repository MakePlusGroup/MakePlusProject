from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput


class MakePlusApp(GridLayout):

    def __init__(self, **kwargs):
        super(MakePlusApp, self).__init__(**kwargs)
        self.cols = 1
        self.rows
        self.add_widget(Image(source='BCIT_LOGO.png'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class RunApp(App):

    def build(self):
        return MakePlusApp()


if __name__ == '__main__':
    RunApp().run()
