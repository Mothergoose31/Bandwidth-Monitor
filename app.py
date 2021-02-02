import monitor
import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '200')
Config.set('graphics', 'resizable', False)

class InformationLabel(Label):
    def update(self,*args):
        self.text = monitor.Bandwidth()

class BandwidthApp(App):
    def __init__(self,**kwargs):
        self.title = "Bandwidth monitor"
        return super().__init__(**kwargs)
    def build(self):
        layout = BoxLayout(orientation = 'vertical')
        informationLabel = InformationLabel()
        Clock.schedule_interval(informationLabel.update,1)
        layout.add_widget(informationLabel)
        return layout

BandwidthApp().run()
        

