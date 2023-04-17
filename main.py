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

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.list import MDList, TwoLineListItem
from kivymd.uix.textfield import MDTextField



# new version ends here exept kvlang and other?
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button









Builder.load_string("""

<First_Screen>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            elevation_normal: 0
            md_bg_color: 0.6, 0, 1, 1
            MDFloatLayout:
                #size: 50, 100
                size_hint: 0.5, 0.5


            MDFloatLayout:
                Image:
                    source: 'Puimuri_solver_neon.png'
                    allow_stretch: True                    
                    size_hint: 0.5, 5
                    pos_hint: {'x': 0, 'y': -2.3} 

        
            MDFloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    allow_stretch: True
                    size_hint: 0.25, 5
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                            
        MDLabel:

    MDFloatLayout:
        MDLabel:
            pos_hint: {'x': 0.02, 'y': .32}
            text: "Select the unknown factor:"
            font_size: "20sp"
        
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
            elevation_normal: 0
            md_bg_color: 0.6, 0, 1, 1
        
            

           
            MDFloatLayout:
                Image:
                    source: 'Power_kuva.png'
                    allow_stretch: True
                    size_hint: 0.5, 5
                    pos_hint: {'x': 0, 'y': -2.1} 
                    
            MDFloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    allow_stretch: True
                    size_hint: 0.25, 5
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
        pos_hint: {'center_x': .4, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'home'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'
        

            
# kaava kuvat
    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'P1m.png'
           # size: 200, 200
            allow_stretch: True
            size_hint: 0.4, 0.3
            pos_hint: {'x': -0.5, 'y': 0}

        Image:
            source: 'P2m.png'
            allow_stretch: True
            size_hint: 0.4, 0.3
            pos_hint: {'x': -0.5, 'y': -0.2}

        Image:
            source: 'P3m.png'
            allow_stretch: True
            size_hint: 0.35, 0.3
            pos_hint: {'x': -0.5, 'y': -0.4}   

        


  

    MDFloatingActionButton:
        pos_hint: {'center_x': .6, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'help'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'P_info'  

    MDFloatingActionButton:
        pos_hint: {'center_x': .85, 'center_y': .54}
        elevation: 2.5
        elevation_normal: 0
        icon: 'information-variant'
        md_bg_color: 0.46, 0.46, 0.46, 1
        size_hint: 0.12, 0.06

        on_release:
            root.manager.current = 'P_guide_1'  

    MDFloatingActionButton:
        pos_hint: {'center_x': .85, 'center_y': .35}
        elevation: 2.5
        elevation_normal: 0
        icon: 'information-variant'
        md_bg_color: 0.46, 0.46, 0.46, 1
        size_hint: 0.12, 0.06


        on_release:
            root.manager.current = 'P_guide_2'

                    
        
                    
<U_Screen>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            elevation_normal: 0
            md_bg_color: 0.6, 0, 1, 1
        
            MDFloatLayout:
                Image:
                    source: 'Voltage_kuva.png'
                    allow_stretch: True
                    size_hint: 0.5, 5
                    pos_hint: {'x': -.07, 'y': -2.1} 
                    
            MDFloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    allow_stretch: True
                    size_hint: 0.25, 5
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
        pos_hint: {'center_x': .4, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'home'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'

            
# kaava kuvat
    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'U1m.png'
            allow_stretch: True
            size_hint: 0.5, 0.3
            pos_hint: {'x': -0.5, 'y': 0}


    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'U2m.png'
            allow_stretch: True
            size_hint: 0.5, 0.3
            pos_hint: {'x': -0.5, 'y': -0.2}

    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'U3m.png'
            allow_stretch: True
            size_hint: 0.5, 0.3
            pos_hint: {'x': -0.5, 'y': -0.4}   

    MDFloatingActionButton:
        pos_hint: {'center_x': .6, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'help'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'U_info'       

    MDFloatingActionButton:
        pos_hint: {'center_x': .85, 'center_y': .55}
        elevation: 2.5
        elevation_normal: 0
        icon: 'information-variant'
        md_bg_color: 0.46, 0.46, 0.46, 1
        size_hint: 0.12, 0.06

        on_release:
            root.manager.current = 'U_guide_1'  

    MDFloatingActionButton:
        pos_hint: {'center_x': .85, 'center_y': .35}
        elevation: 2.5
        elevation_normal: 0
        icon: 'information-variant'
        md_bg_color: 0.46, 0.46, 0.46, 1
        size_hint: 0.12, 0.06

        on_release:
            root.manager.current = 'U_guide_2'

                   
<I_Screen>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            
            elevation: 2
            md_bg_color: 0.6, 0, 1, 1
        
            
            MDFloatLayout:
                Image:
                    source: 'current_kuva.png'
                    allow_stretch: True
                    size_hint: 0.5, 5
                    pos_hint: {'x': -.05, 'y': -2.1} 
                    
            MDFloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    allow_stretch: True
                    size_hint: 0.25, 5
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
        pos_hint: {'center_x': .4, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'home'
        md_bg_color: 0.6, 0, 1, 1
        on_release:
            root.manager.current = 'first'


                                      
# kaava kuvat
    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'I1m.png'
            allow_stretch: True
            size_hint: 0.5, 0.3
            pos_hint: {'x': -0.5, 'y': 0}

    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'I2m.png'
            allow_stretch: True
            size_hint: 0.5, 0.3
            pos_hint: {'x': -0.5, 'y': -0.2}

    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'I3m.png'
            allow_stretch: True
            size_hint: 0.5, 0.3
            pos_hint: {'x': -0.5, 'y': -0.4}

                    
    MDFloatingActionButton:
        pos_hint: {'center_x': .6, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'help'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'I_info'

# guide screen buttons
    MDFloatingActionButton:
        pos_hint: {'center_x': .85, 'center_y': .75}
        elevation: 2.5
        elevation_normal: 0
        icon: 'information-variant'
        md_bg_color: 0.46, 0.46, 0.46, 1
        size_hint: 0.12, 0.06


        on_release:
            root.manager.current = 'I_guide_1'  

    MDFloatingActionButton:
        pos_hint: {'center_x': .85, 'center_y': .55}
        elevation: 2.5
        elevation_normal: 0
        icon: 'information-variant'
        md_bg_color: 0.46, 0.46, 0.46, 1
        size_hint: 0.12, 0.06


        on_release:
            root.manager.current = 'I_guide_2'

    MDFloatingActionButton:
        pos_hint: {'center_x': .85, 'center_y': .35}
        elevation: 2.5
        elevation_normal: 0
        icon: 'information-variant'
        md_bg_color: 0.46, 0.46, 0.46, 1
        size_hint: 0.12, 0.06


        on_release:
            root.manager.current = 'I_guide_3'

            
           
<R_Screen>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            elevation_normal: 0
            md_bg_color: 0.6, 0, 1, 1

            
            MDFloatLayout:
                Image:
                    source: 'Resistance_kuva.png'
                    allow_stretch: True
                    size_hint: 0.5, 5
                    pos_hint: {'x': -.01, 'y': -2.1} 
                    
            MDFloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    allow_stretch: True
                    size_hint: 0.25, 5
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                            
        MDLabel:

    #bottom bar
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
        pos_hint: {'center_x': .4, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'home'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'


# kaava kuvat
    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'R1m.png'
            allow_stretch: True
            size_hint: 0.5, 0.3
            pos_hint: {'x': -0.5, 'y': 0}


    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'R2m.png'
            allow_stretch: True
            size_hint: 0.5, 0.3
            pos_hint: {'x': -0.5, 'y': -0.2}

    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'R3m.png'
            allow_stretch: True
            size_hint: 0.5, 0.3
            pos_hint: {'x': -0.5, 'y': -0.4}      

            
    MDFloatingActionButton:
        pos_hint: {'center_x': .6, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'help'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'R_info'

            

# guide screen buttons
    MDFloatingActionButton:
        pos_hint: {'center_x': .85, 'center_y': .75}
        elevation: 2.5
        elevation_normal: 0
        icon: 'information-variant'
        md_bg_color: 0.46, 0.46, 0.46, 1
        size_hint: 0.12, 0.06


        on_release:
            root.manager.current = 'R_guide_1'  

    MDFloatingActionButton:
        pos_hint: {'center_x': .85, 'center_y': .55}
        elevation: 2.5
        elevation_normal: 0
        icon: 'information-variant'
        md_bg_color: 0.46, 0.46, 0.46, 1
        size_hint: 0.12, 0.06


        on_release:
            root.manager.current = 'R_guide_2'

    MDFloatingActionButton:
        pos_hint: {'center_x': .85, 'center_y': .35}
        elevation: 2.5
        elevation_normal: 0
        icon: 'information-variant'
        md_bg_color: 0.46, 0.46, 0.46, 1
        size_hint: 0.12, 0.06


        on_release:
            root.manager.current = 'R_guide_3'

<P_Info_Screen>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            elevation_normal: 0
            md_bg_color: 0.6, 0, 1, 1

            
            MDFloatLayout:
                Image:
                    source: 'info_puimuri.png'
                    allow_stretch: True
                    size_hint: 0.5, 5
                    pos_hint: {'x': -0.1, 'y': -2} 
                    
            MDFloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    allow_stretch: True
                    size_hint: 0.25, 5
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                    
                            
        MDLabel:

    #bottom bar
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
        pos_hint: {'center_x': .6, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'P'

    MDFloatingActionButton:
        pos_hint: {'center_x': .4, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'home'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'

    MDFloatLayout:
        MDLabel:
            pos_hint: {'x': 0.005, 'y': 0.15} 
            text: "Electric power is the rate at which electrical energy is transferred or consumed. It is a measure of how much work can be done per unit time by an electrical system. The unit of electric power is the watt (W), which is defined as one joule of energy per second."
            font_size: "22sp"



<U_Info_Screen>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            elevation_normal: 0
            md_bg_color: 0.6, 0, 1, 1

            
            MDFloatLayout:
                Image:
                    source: 'info_puimuri.png'
                    allow_stretch: True
                    size_hint: 0.5, 5
                    pos_hint: {'x': -0.1, 'y': -2} 
                    
            MDFloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    allow_stretch: True
                    size_hint: 0.25, 5
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                    
                            
        MDLabel:

    #bottom bar
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
        pos_hint: {'center_x': .6, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'U'

    MDFloatingActionButton:
        pos_hint: {'center_x': .4, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'home'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'

    MDFloatLayout:
        MDLabel:
            pos_hint: {'x': 0.005, 'y': 0.15}
            text: "Voltage, also known as electric potential difference, is a measure of the amount of electric potential energy per unit charge in an electric circuit. It represents the force that drives the flow of electric charge through a circuit. Voltage is measured in volts (V), and it is a scalar quantity that can have both positive and negative values."
            font_size: "22sp"


<I_Info_Screen>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            elevation_normal: 0
            md_bg_color: 0.6, 0, 1, 1

            
            MDFloatLayout:
                Image:
                    source: 'info_puimuri.png'
                    allow_stretch: True
                    size_hint: 0.5, 5
                    pos_hint: {'x': -0.1, 'y': -2} 
                    
            MDFloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    allow_stretch: True
                    size_hint: 0.25, 5
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                    
                            
        MDLabel:

    #bottom bar
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
        pos_hint: {'center_x': .6, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'I'

    MDFloatingActionButton:
        pos_hint: {'center_x': .4, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'home'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'

    MDFloatLayout:
        MDLabel:
            pos_hint: {'x': 0.005, 'y': 0.15}
            text: "Electric current is the flow of electric charge through a conductor or an electric circuit. It is the rate at which electric charge flows past a given point in a circuit and is measured in amperes (A). Electric current is caused by the movement of free electrons in a conductor, which are pushed by an electric field."
            font_size: "22sp"
            
<R_Info_Screen>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            elevation_normal: 0
            md_bg_color: 0.6, 0, 1, 1

            
            MDFloatLayout:
                Image:
                    source: 'info_puimuri.png'
                    allow_stretch: True
                    size_hint: 0.5, 5
                    pos_hint: {'x': -0.1, 'y': -2} 
                    
            MDFloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    allow_stretch: True
                    size_hint: 0.25, None
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                    
                            
        MDLabel:

    #bottom bar
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
        pos_hint: {'center_x': .6, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'R'

    MDFloatingActionButton:
        pos_hint: {'center_x': .4, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'home'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'

    MDFloatLayout:
        MDLabel:
            pos_hint: {'x': 0.005, 'y': 0.15} 
            text: "Electrical resistance is a property of a material or a component that opposes the flow of electrical current through it. It is measured in ohms (Ω) and is represented by the symbol R. Resistance is a critical parameter in electrical circuits, as it determines the amount of current that flows through a circuit when a voltage is applied."
            font_size: "22sp"

<P_Guide_Screen_1>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            elevation_normal: 0
            md_bg_color: 0.6, 0, 1, 1

            
            MDFloatLayout:
                Image:
                    source: 'guide_puimuri.png'
                    allow_stretch: True
                    size_hint: 0.5, 5
                    pos_hint: {'x': -0.1, 'y': -2} 
                    
            MDFloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    allow_stretch: True
                    size_hint: 0.25, 5
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                    
                            
        MDLabel:

    #bottom bar
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
        pos_hint: {'center_x': .6, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'P'

    MDFloatingActionButton:
        pos_hint: {'center_x': .4, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'home'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'


# kaava kuvat
    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'P2pyor.png'
            allow_stretch: True
            #size_hint: 0.5, 0.4
            pos_hint: {'x': -0.5, 'y': -0.5}




<P_Guide_Screen_2>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            elevation_normal: 0
            md_bg_color: 0.6, 0, 1, 1

            
            MDFloatLayout:
                Image:
                    source: 'guide_puimuri.png'
                    allow_stretch: True
                    size_hint: 0.5, 5
                    pos_hint: {'x': -0.1, 'y': -2} 
                    
            FloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    allow_stretch: True
                    size_hint: 0.25, 5
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                    
                            
        MDLabel:

    #bottom bar
    MDFloatLayout:
        size: 100, 100
        size_hint: None, None
        canvas:
            Color:
                rgba: 0.6, 0, 1, 1
            Rectangle:
                pos: 0,0
                size: 2000, root.height / 9

# kaava kuvat
    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'P3pyor.png'
            allow_stretch: True
            pos_hint: {'x': -0.5, 'y': -0.6}


    MDFloatLayout:

    MDFloatingActionButton:
        pos_hint: {'center_x': .6, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'P'

    MDFloatingActionButton:
        pos_hint: {'center_x': .4, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'home'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'
        
            

<U_Guide_Screen_1>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            elevation_normal: 0
            md_bg_color: 0.6, 0, 1, 1

            
            MDFloatLayout:
                Image:
                    source: 'guide_puimuri.png'
                    allow_stretch: True
                    size_hint: 0.5, 5
                    pos_hint: {'x': -0.1, 'y': -2} 
                    
            FloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    allow_stretch: True
                    size_hint: 0.25, 5
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                    
                            
        MDLabel:

    #bottom bar
    MDFloatLayout:
        size: 100, 100
        size_hint: None, None
        canvas:
            Color:
                rgba: 0.6, 0, 1, 1
            Rectangle:
                pos: 0,0
                size: 2000, root.height / 9

# kaava kuva1
    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'U2pyor.png'
            allow_stretch: True
            pos_hint: {'x': -0.5, 'y': -0.6}


    MDFloatingActionButton:
        pos_hint: {'center_x': .6, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'U'

    MDFloatingActionButton:
        pos_hint: {'center_x': .4, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'home'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'

<U_Guide_Screen_2>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            elevation_normal: 0
            md_bg_color: 0.6, 0, 1, 1

            
            MDFloatLayout:
                Image:
                    source: 'guide_puimuri.png'
                    allow_stretch: True
                    size_hint: 0.5, 5
                    pos_hint: {'x': -0.1, 'y': -2} 
                    
            FloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    allow_stretch: True
                    size_hint: 0.25, 5
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                    
                            
        MDLabel:

    #bottom bar
    MDFloatLayout:
        size: 100, 100
        size_hint: None, None
        canvas:
            Color:
                rgba: 0.6, 0, 1, 1
            Rectangle:
                pos: 0,0
                size: 2000, root.height / 9

# kaava kuvat
    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'U3pyor.png'
            allow_stretch: True
            pos_hint: {'x': -0.5, 'y': -0.5}


    MDFloatingActionButton:
        pos_hint: {'center_x': .6, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'U'

    MDFloatingActionButton:
        pos_hint: {'center_x': .4, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'home'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'

<I_Guide_Screen_1>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            elevation_normal: 0
            md_bg_color: 0.6, 0, 1, 1

            
            MDFloatLayout:
                Image:
                    source: 'guide_puimuri.png'
                    allow_stretch: True
                    size_hint: 0.5, 5
                    pos_hint: {'x': -0.1, 'y': -2} 
                    
            FloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    allow_stretch: True
                    size_hint: 0.25, 5
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                    
                            
        MDLabel:

    #bottom bar
    MDFloatLayout:
        size: 100, 100
        size_hint: None, None
        canvas:
            Color:
                rgba: 0.6, 0, 1, 1
            Rectangle:
                pos: 0,0
                size: 2000, root.height / 9

# kaava kuvat
    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'I1pyor.png'
            allow_stretch: True
            pos_hint: {'x': -0.5, 'y': -0.5}



    MDFloatingActionButton:
        pos_hint: {'center_x': .6, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'I'

    MDFloatingActionButton:
        pos_hint: {'center_x': .4, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'home'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'

<I_Guide_Screen_2>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            elevation_normal: 0
            md_bg_color: 0.6, 0, 1, 1

            
            MDFloatLayout:
                Image:
                    source: 'guide_puimuri.png'
                    allow_stretch: True
                    size_hint: 0.5, 5
                    pos_hint: {'x': -0.1, 'y': -2} 
                    
            FloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    allow_stretch: True
                    size_hint: 0.25, 5
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                    
                            
        MDLabel:

    #bottom bar
    MDFloatLayout:
        size: 100, 100
        size_hint: None, None
        canvas:
            Color:
                rgba: 0.6, 0, 1, 1
            Rectangle:
                pos: 0,0
                size: 2000, root.height / 9

# kaava kuvat
    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'I2pyor.png'
            allow_stretch: True
            pos_hint: {'x': -0.5, 'y': -0.5}


    MDFloatingActionButton:
        pos_hint: {'center_x': .6, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'I'

    MDFloatingActionButton:
        pos_hint: {'center_x': .4, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'home'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'

<I_Guide_Screen_3>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            elevation_normal: 0
            md_bg_color: 0.6, 0, 1, 1

            
            MDFloatLayout:
                Image:
                    source: 'guide_puimuri.png'
                    allow_stretch: True
                    size_hint: 0.5, 5
                    pos_hint: {'x': -0.1, 'y': -2} 
                    
            FloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    allow_stretch: True
                    size_hint: 0.25, 5
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                    
                            
        MDLabel:

    #bottom bar
    MDFloatLayout:
        size: 100, 100
        size_hint: None, None
        canvas:
            Color:
                rgba: 0.6, 0, 1, 1
            Rectangle:
                pos: 0,0
                size: 2000, root.height / 9
        
# kaava kuvat
    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'I3pyor.png'
            allow_stretch: True
            pos_hint: {'x': -0.5, 'y': -0.5}


    MDFloatingActionButton:
        pos_hint: {'center_x': .6, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'I'

    MDFloatingActionButton:
        pos_hint: {'center_x': .4, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'home'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'


<R_Guide_Screen_1>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            elevation_normal: 0
            md_bg_color: 0.6, 0, 1, 1

            
            MDFloatLayout:
                Image:
                    source: 'guide_puimuri.png'
                    allow_stretch: True
                    size_hint: 0.5, 5
                    pos_hint: {'x': -0.1, 'y': -2} 
                    
            FloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    allow_stretch: True
                    size_hint: 0.25, 5
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                    
                            
        MDLabel:

    #bottom bar
    MDFloatLayout:
        size: 100, 100
        size_hint: None, None
        canvas:
            Color:
                rgba: 0.6, 0, 1, 1
            Rectangle:
                pos: 0,0
                size: 2000, root.height / 9

# kaava kuvat
    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'R1pyor.png'
            allow_stretch: True
            pos_hint: {'x': -0.5, 'y': -0.5}

    MDFloatingActionButton:
        pos_hint: {'center_x': .6, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'R'

    MDFloatingActionButton:
        pos_hint: {'center_x': .4, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'home'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'


<R_Guide_Screen_2>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            elevation_normal: 0
            md_bg_color: 0.6, 0, 1, 1

            
            MDFloatLayout:
                Image:
                    source: 'guide_puimuri.png'
                    allow_stretch: True
                    size_hint: 0.5, 5
                    pos_hint: {'x': -0.1, 'y': -2} 
                    
            FloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    allow_stretch: True
                    size_hint: 0.25, 5
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                    
                            
        MDLabel:

    #bottom bar
    MDFloatLayout:
        size: 100, 100
        size_hint: None, None
        canvas:
            Color:
                rgba: 0.6, 0, 1, 1
            Rectangle:
                pos: 0,0
                size: 2000, root.height / 9

# kaava kuvat
    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'R2pyor.png'
            allow_stretch: True
            pos_hint: {'x': -0.5, 'y': -0.5}

    MDFloatingActionButton:
        pos_hint: {'center_x': .6, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'R'

    MDFloatingActionButton:
        pos_hint: {'center_x': .4, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'home'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'first'

<R_Guide_Screen_3>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            elevation: 2
            elevation_normal: 0
            md_bg_color: 0.6, 0, 1, 1

            
            MDFloatLayout:
                Image:
                    source: 'guide_puimuri.png'
                    allow_stretch: True
                    size_hint: 0.5, 5
                    pos_hint: {'x': -0.1, 'y': -2}
                    
            FloatLayout:
                Image:
                    source: 'puimuri_transparent.png'
                    allow_stretch: True
                    size_hint: 0.25, 5
                    pos_hint: {'x': 0.75, 'y': -0.9}  
                    
                            
        MDLabel:

    #bottom bar
    MDFloatLayout:
        size: 100, 100
        size_hint: None, None
        canvas:
            Color:
                rgba: 0.6, 0, 1, 1
            Rectangle:
                pos: 0,0
                size: 2000, root.height / 9        

# kaava kuvat
    MDFloatLayout:
        pos_hint: {'x': 0.5, 'y': 0.6}

        Image:
            source: 'R3pyor.png'
            allow_stretch: True
            pos_hint: {'x': -0.5, 'y': -0.5}

    MDFloatingActionButton:
        pos_hint: {'center_x': .6, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
        icon: 'arrow-left-bold'
        md_bg_color: 0.6, 0, 1, 1


        on_release:
            root.manager.current = 'R'

    MDFloatingActionButton:
        pos_hint: {'center_x': .4, 'center_y': .18}
        elevation: 2.5
        elevation_normal: 0
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
# p guide screens
class P_Guide_Screen_1(Screen):
    pass
class P_Guide_Screen_2(Screen):
    pass

# U guide screens
class U_Guide_Screen_1(Screen):
    pass
class U_Guide_Screen_2(Screen):
    pass

# I guide screens
class I_Guide_Screen_1(Screen):
    pass
class I_Guide_Screen_2(Screen):
    pass
class I_Guide_Screen_3(Screen):
    pass

# R guide screens
class R_Guide_Screen_1(Screen):
    pass
class R_Guide_Screen_2(Screen):
    pass
class R_Guide_Screen_3(Screen):
    pass




class TestApp(MDApp):

    def build(self):

         # Set the window size hint to none
        Window.size_hint = (None, None)
        
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

        sm.add_widget(U_Guide_Screen_1(name='U_guide_1'))
        sm.add_widget(U_Guide_Screen_2(name='U_guide_2'))

        sm.add_widget(I_Guide_Screen_1(name='I_guide_1'))
        sm.add_widget(I_Guide_Screen_2(name='I_guide_2'))
        sm.add_widget(I_Guide_Screen_3(name='I_guide_3'))

        sm.add_widget(R_Guide_Screen_1(name='R_guide_1'))    
        sm.add_widget(R_Guide_Screen_2(name='R_guide_2'))
        sm.add_widget(R_Guide_Screen_3(name='R_guide_3'))   

        return sm

if __name__ == '__main__':
    TestApp().run()


