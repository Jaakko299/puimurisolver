from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button

class Screen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='This is Screen 1'))
        switch_button = Button(text='Go to Screen 2', size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        switch_button.bind(on_press=self.switch_to_screen2)
        self.add_widget(switch_button)

    def switch_to_screen2(self, instance):
        self.manager.current = 'screen2'

class Screen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='This is Screen 2'))
        switch_button = Button(text='Go to Screen 1', size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        switch_button.bind(on_press=self.switch_to_screen1)
        self.add_widget(switch_button)

    def switch_to_screen1(self, instance):
        self.manager.current = 'screen1'

class ScreenManagerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen1(name='screen1'))
        sm.add_widget(Screen2(name='screen2'))
        return sm

if __name__ == '__main__':
    ScreenManagerApp().run()
