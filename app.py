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

class InformationLabel(label):
    def update(self,*args):
        self.text = monitor.Bandwidth()
        

