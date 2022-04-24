# This is the main file of this game
from os import *
from msvcrt import *
import ParametersDeclarer as data
from Eventer import *
from ParametersChanger import *
from Printer import *

system("mode con: cols=85 lines=40")
system("title = Энергетический передоз")
Rules()
while True:
    system('cls')
    PrintParameters()
    getch()
    print("EVENT:")
    RunEvent()
    getch()
    LvlUpDiolog()
    getch()
    PassDay()
