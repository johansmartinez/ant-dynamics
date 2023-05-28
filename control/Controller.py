from model.Hormiguero import Hormiguero
from view.InterfazHormiguero import InterfazHormiguero

class Controller:
    def __init__(self):
        self.hormiguero={}
        self.io=InterfazHormiguero()