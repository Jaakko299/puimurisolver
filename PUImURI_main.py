
import sqlite3

from kivy.core.text import LabelBase

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.icon_definitions import md_icons

from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.list import IconLeftWidget, IconRightWidget

from kivymd.uix.button import MDFloatingActionButton



#new versio
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder

from kivymd.uix.list import MDList, TwoLineListItem
from kivymd.uix.textfield import MDTextField



# new version ends here exept kvlang and other?
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd




# feedback input class
# input class
class Input(BoxLayout):
    def __init__(self, label_text='', **kwargs):
        super().__init__(**kwargs)

        # Create a label for the input
        self.label = Label(text=label_text)

        # Create a text input widget
        self.input = TextInput(multiline=False)
        # if pressed enter
        self.input.bind(on_text_validate=self.on_enter)
        

        # Add the label and text input to the layout
        self.add_widget(self.label)
        self.add_widget(self.input)


    def on_enter(self, instance):
        # Get the text value of the input widget
        input_text = self.input.text

        # Insert the input value into the database
        con = sqlite3.connect('database_kivy_valipalautus.db')
        cur = con.cursor()
        cur.execute("INSERT INTO feedback_table (feedback) VALUES (?)", (input_text,))
        con.commit()



# input box class UNIT CONVERTER
class Input_equation(BoxLayout): # input class
    def __init__(self, **kwargs):
        super(Input_equation, self).__init__(**kwargs)
        self.text_input = TextInput(size_hint=(None, None), size=(200, 200), height=(100), multiline = False)# creates input
        self.add_widget(self.text_input) # makes created input widget appear
        

        
        self.text_input.bind(text=self.update_output_label)

        self.label = Label(text="", color=(0, 1, 0, 1), pos=(100, 100)) # output label
        self.add_widget(self.label) # output label added


    def update_output_label(self, instance, value): # updates from input
        
        if value == '':
            self.label.text = 'Enter a equation'

        elif value == 'U':
            self.label.text = 'U=RI'
        elif value == 'R':
            self.label.text = 'U/I=R'
            self.label.color = (0,1,0,1)  # color
        elif value == 'I':
            self.label.text = 'U/R=I'
            self.label.color = (0,1,0,1)  # color
        elif value == 'P':
            self.label.text = 'P=UI'
            self.label.color = (0,1,0,1)  # color
        
        

        else:
            self.label.text = f':Enter a equation!' # output label updated
            self.label.color = (0,1,0,1)  # color

        




Builder.load_string("""

<First_Screen>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            md_bg_color: 0.6, 0, 1, 1
            MDFloatLayout:
                #size: 50, 100
                size_hint: 0.5, 0.5





            MDFloatLayout:
                Image:
                    source: 'puimuri_teksti_kuva.png'
                    
                    size_hint: 0.5, None
                    pos_hint: {'x': 0, 'y': -2.3} 

        
            MDFloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    size_hint: 0.25, None
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                            
        MDLabel:


    FloatLayout:
        size: 100, 100
        size_hint: None, None
        canvas:
            Color:
                rgba: 0.6, 0, 1, 1
            Rectangle:
                pos: 0,0
                size: 2000, root.height / 9

                
    MDBoxLayout:
        
        pos_hint: {'x': 0, 'y': 0.4}
        MDList:

            OneLineAvatarIconListItem:
                text: 'POWER (P)'
                on_release: root.manager.current = 'P'
                IconLeftWidget: 
                    icon: 'power-plug'

            OneLineAvatarIconListItem:
                text: 'VOLTAGE (U)'
                on_release: root.manager.current = 'U'
                IconLeftWidget: 
                    icon: 'lightning-bolt'
            OneLineAvatarIconListItem:
                text: 'CURRENT (I)'
                on_release: root.manager.current = 'I'
                IconLeftWidget: 
                    icon: 'current-ac'
            OneLineAvatarIconListItem:
                text: 'RESISTANCE (R)'
                on_release: root.manager.current = 'R'
                IconLeftWidget: 
                    icon: 'omega'
                    
<P_Screen>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            md_bg_color: 0.6, 0, 1, 1
        
            

           
            MDFloatLayout:
                Image:
                    source: 'Power_kuva.png'
                    size_hint: 0.5, None
                    pos_hint: {'x': 0, 'y': -2.1} 
                    
            MDFloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    size_hint: 0.25, None
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                            
        MDLabel:


    MDFloatLayout:
        size: 100, 100
        size_hint: None, None
        canvas:
            Color:
                rgba: 0.6, 0, 1, 1
            Rectangle:
                pos: 0,0
                size: 2000, root.height / 9
    
    MDFloatingActionButton:
        pos_hint: {'center_x': .5, 'center_y': .18}
        elevation: 2.5
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'
        

            
# kaava kuvat
    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'P1m.png'
           # size: 200, 200
            size_hint: 0.5, None
            pos_hint: {'x': -0.5, 'y': 0}


    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'P2m.png'
            size_hint: 0.5, None
            pos_hint: {'x': -0.5, 'y': -0.2}

    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'P3m.png'
            size_hint: 0.5, None
            pos_hint: {'x': -0.5, 'y': -0.4}      

    MDFloatingActionButton:
        pos_hint: {'center_x': .7, 'center_y': .18}
        elevation: 2.5
        icon: 'information-variant'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'P_info'  
    
    MDFloatingActionButton:
        pos_hint: {'center_x': .6, 'center_y': .3}
        elevation: 2.5
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'P_guide'

    MDFloatingActionButton:
        pos_hint: {'center_x': .6, 'center_y': .5}
        elevation: 2.5
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'P'
                    
        
                    
<U_Screen>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            md_bg_color: 0.6, 0, 1, 1
        
            MDFloatLayout:
                Image:
                    source: 'Voltage_kuva.png'
                    size_hint: 0.5, None
                    pos_hint: {'x': -.07, 'y': -2.1} 
                    
            MDFloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    size_hint: 0.25, None
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                            

        MDLabel:

    # Bottom bar
    MDFloatLayout:
        size: 100, 100
        size_hint: None, None
        canvas:
            Color:
                rgba: 0.6, 0, 1, 1
            Rectangle:
                pos: 0,0
                size: 2000, root.height / 9




    MDFloatingActionButton:
        pos_hint: {'center_x': .5, 'center_y': .18}
        elevation: 2.5
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'



            
# kaava kuvat
    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'U1m.png'
            size_hint: 0.5, None
            pos_hint: {'x': -0.5, 'y': 0}


    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'U2m.png'
            size_hint: 0.5, None
            pos_hint: {'x': -0.5, 'y': -0.2}

    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'U3m.png'
            size_hint: 0.5, None
            pos_hint: {'x': -0.5, 'y': -0.4}   

    MDFloatingActionButton:
        pos_hint: {'center_x': .7, 'center_y': .18}
        elevation: 2.5
        icon: 'information-variant'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'U_info'         
<I_Screen>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            
            elevation: 2
            md_bg_color: 0.6, 0, 1, 1
        
            
            MDFloatLayout:
                Image:
                    source: 'current_kuva.png'
                    size_hint: 0.5, None
                    pos_hint: {'x': -.05, 'y': -2.1} 
                    
            MDFloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    size_hint: 0.25, None
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                            
        
                            
        MDLabel:

 # bottom bar
    MDFloatLayout:
        size: 100, 100
        size_hint: None, None
        canvas:
            Color:
                rgba: 0.6, 0, 1, 1
            Rectangle:
                pos: 0,0
                size: 2000, root.height / 9

    MDFloatingActionButton:
        pos_hint: {'center_x': .5, 'center_y': .18}
        elevation: 2.5
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1
        on_release:
            root.manager.current = 'first'


    MDFloatingActionButton:
        pos_hint: {'center_x': .7, 'center_y': .18}
        elevation: 2.5
        icon: 'information-variant'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'I_info'
                                      
# kaava kuvat
    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'I1m.png'
            size_hint: 0.5, None
            pos_hint: {'x': -0.5, 'y': 0}


    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'I2m.png'
            size_hint: 0.5, None
            pos_hint: {'x': -0.5, 'y': -0.2}

    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'I3m.png'
            size_hint: 0.5, None
            pos_hint: {'x': -0.5, 'y': -0.4}
                    
    MDFloatingActionButton:
        pos_hint: {'center_x': .7, 'center_y': .18}
        elevation: 2.5
        icon: 'information-variant'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'I_info'

            
           
<R_Screen>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            md_bg_color: 0.6, 0, 1, 1

            
            MDFloatLayout:
                Image:
                    source: 'Resistance_kuva.png'
                    size_hint: 0.5, None
                    pos_hint: {'x': -.01, 'y': -2.1} 
                    
            MDFloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    size_hint: 0.25, None
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                            
        MDLabel:

 # bottom bar
    MDFloatLayout:
        size: 100, 100
        size_hint: None, None
        canvas:
            Color:
                rgba: 0.6, 0, 1, 1
            Rectangle:
                pos: 0,0
                size: 2000, root.height / 9


    MDFloatingActionButton:
        pos_hint: {'center_x': .5, 'center_y': .18}
        elevation: 2.5
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'
# kaava kuvat
    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'R1m.png'
            size_hint: 0.5, None
            pos_hint: {'x': -0.5, 'y': 0}


    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'R2m.png'
            size_hint: 0.5, None
            pos_hint: {'x': -0.5, 'y': -0.2}

    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'R3m.png'
            size_hint: 0.5, None
            pos_hint: {'x': -0.5, 'y': -0.4}      

            
    MDFloatingActionButton:
        pos_hint: {'center_x': .7, 'center_y': .18}
        elevation: 2.5
        icon: 'information-variant'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'R_info'


<P_Info_Screen>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            md_bg_color: 0.6, 0, 1, 1

            
            MDFloatLayout:
                Image:
                    source: 'info_puimuri.png'
                    size_hint: 0.5, None
                    pos_hint: {'x': -0.1, 'y': -2} 
                    
            MDFloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    size_hint: 0.25, None
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                    
                            
        MDLabel:

    MDFloatingActionButton:
        pos_hint: {'center_x': .6, 'center_y': .18}
        elevation: 2.5
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'P'

    MDFloatingActionButton:
        pos_hint: {'center_x': .4, 'center_y': .18}
        elevation: 2.5
        icon: 'home'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'


<U_Info_Screen>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            md_bg_color: 0.6, 0, 1, 1

            
            MDFloatLayout:
                Image:
                    source: 'info_puimuri.png'
                    size_hint: 0.5, None
                    pos_hint: {'x': -0.1, 'y': -2} 
                    
            MDFloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    size_hint: 0.25, None
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                    
                            
        MDLabel:

        

    MDFloatingActionButton:
        pos_hint: {'center_x': .6, 'center_y': .18}
        elevation: 2.5
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'U'

    MDFloatingActionButton:
        pos_hint: {'center_x': .4, 'center_y': .18}
        elevation: 2.5
        icon: 'home'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'


<I_Info_Screen>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            md_bg_color: 0.6, 0, 1, 1

            
            MDFloatLayout:
                Image:
                    source: 'info_puimuri.png'
                    size_hint: 0.5, None
                    pos_hint: {'x': -0.1, 'y': -2} 
                    
            MDFloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    size_hint: 0.25, None
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                    
                            
        MDLabel:

    MDFloatingActionButton:
        pos_hint: {'center_x': .6, 'center_y': .18}
        elevation: 2.5
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'P'

    MDFloatingActionButton:
        pos_hint: {'center_x': .4, 'center_y': .18}
        elevation: 2.5
        icon: 'home'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'
<R_Info_Screen>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            md_bg_color: 0.6, 0, 1, 1

            
            MDFloatLayout:
                Image:
                    source: 'info_puimuri.png'
                    size_hint: 0.5, None
                    pos_hint: {'x': -0.1, 'y': -2} 
                    
            FloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    size_hint: 0.25, None
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                    
                            
        MDLabel:

    MDFloatingActionButton:
        pos_hint: {'center_x': .6, 'center_y': .18}
        elevation: 2.5
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'P'

    MDFloatingActionButton:
        pos_hint: {'center_x': .4, 'center_y': .18}
        elevation: 2.5
        icon: 'home'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'

""")








# first
class First_Screen(Screen):
    pass
# Power screens
class P_Screen(Screen):
    pass
class P_Info_Screen(Screen):
    pass
# Voltage Screen
class U_Screen(Screen):
    pass
class U_Info_Screen(Screen):
    pass
# Current Screens
class I_Screen(Screen):
    pass
class I_Info_Screen(Screen):
    pass

# Resistance screens
class R_Screen(Screen):
    pass

class R_Info_Screen(Screen):
    pass

# guide screens
class P_Guide_Screen_1(Screen):
    pass
class P_Guide_Screen_2(Screen):
    pass
class U_Guide_Screen(Screen):
    pass
class I_Guide_Screen(Screen):
    pass
class R_Guide_Screen(Screen):
    pass




class TestApp(MDApp):

    def build(self):

         # Set the window size and aspect ratio to match a phone screen
        Window.size = (350,600)
        Window.size_hint = (None, None)
        Window.aspect_ratio = 9/16
        
        # Create the screen manager

        sm = ScreenManager()
        # main screen
        sm.add_widget(First_Screen(name='first'))
        # P, U, I, R screens
        sm.add_widget(P_Screen(name='P'))
        sm.add_widget(U_Screen(name='U'))
        sm.add_widget(I_Screen(name='I'))
        sm.add_widget(R_Screen(name='R'))   

        # info screens
        sm.add_widget(U_Info_Screen(name='U_info'))
        sm.add_widget(P_Info_Screen(name='P_info'))
        sm.add_widget(I_Info_Screen(name='I_info'))
        sm.add_widget(R_Info_Screen(name='R_info'))

        # guide screens
        sm.add_widget(P_Guide_Screen_1(name='P_guide_1'))
        sm.add_widget(P_Guide_Screen_2(name='P_guide_2'))

        sm.add_widget(U_Guide_Screen(name='U_guide'))
        sm.add_widget(I_Guide_Screen(name='I_guide'))
        sm.add_widget(R_Guide_Screen(name='R_guide'))       

        return sm

if __name__ == '__main__':
    TestApp().run()















