import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        widget = Widget()
        layout = BoxLayout(orientation='vertical')
        button = Button(text='Hello world', font_size=14)
        button2 = Button(text='Hello world2', font_size=14)
        button3 = Button(text='Hello world3', font_size=14)
        button4 = Button(text='Hello world4', font_size=14)
        button.bind(on_press=self.doStuff)
        button2.bind(on_press=self.doStuff)
        button3.bind(on_press=self.doStuff)
        button4.bind(on_press=self.doStuff)
        layout.add_widget(button)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        return layout
    def doStuff(self, event):
        print('bou')


if __name__ == '__main__':
    MyApp().run()
