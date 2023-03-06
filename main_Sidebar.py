from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

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
                        
        MDNavigationDrawer:
            id: nav_drawer     
"""


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen


DemoApp().run()