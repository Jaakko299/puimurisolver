from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (350, 550)

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
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'

                Image:
                    source: 'PUImURI-logo2.png'

                MDLabel:
                    text: '   Kaavalista'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: '    Valitse haluttu kaava pyöritettäväksi.'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineListItem:
                            Image:
                                source: 'PUI.png'
                                pos: -65, 105

                        OneLineListItem:
                            Image:
                                source: 'URI.png'
                                pos: -65, 55
                                size: 55, 55
                                size_hint: None, None

                        OneLineListItem:
                            text: 'Kaava 2'

"""


class PuimuriApp(MDApp):

    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen


PuimuriApp().run()
