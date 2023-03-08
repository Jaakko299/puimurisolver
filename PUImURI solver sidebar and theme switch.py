from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import BooleanProperty

#Window.size = (300, 300)

navigation_helper = """
Screen:
    size_hint: 1, 1
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'PUImURI Solver'
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        elevation:2
                        md_bg_color: 0.76, 0.03, 0.86

                    Widget:
                        # Add a theme switch button container
                        FloatLayout:
                            size_hint: None, None
                            size: dp(56), dp(24)
                            pos_hint: {'x': 0, 'y': 1}
                            MDSwitch:
                                pos_hint: {'center_x': 13.5, 'center_y': 23.5}
                                on_active: app.switch_theme(self.active)

        MDNavigationDrawer:
            id: nav_drawer     
"""
    
class DemoApp(MDApp):
    dark_theme = BooleanProperty(False)

    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen

    def switch_theme(self, switch_value):
        if switch_value:
            self.theme_cls.theme_style = 'Dark'
            self.dark_theme = True
        else:
            self.theme_cls.theme_style = 'Light'
            self.dark_theme = False

DemoApp().run()