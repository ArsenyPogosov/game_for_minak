# This file visualize game parameters and some other things.
# For better understanding look at Parameters1.jpg and Parameters2.jpg
import ParametersDeclarer as data
import ParametersChanger as upgrade
from os import *
from msvcrt import *


def PrintParameters():
    print("D", data.D)
    print("EtoLive", data.EtoLive)
    # 22/18/16/12
    print("Энергохранилище(E)    Генератор(Gen)    Пушка(Gun)    Стена(W)      Вражины(Enemy)")
    print("LvlE {:<17}LvlGen {:<11}LvlGun {:<7}LvlW {:<9}Nenemy {}".format(data.LvlE, data.LvlGen, data.LvlGun, data.LvlW, data.Nenemy))
    print("LvlUpE {:<15}LvlUpGen {:<9}LvlUpGun {:<5}LvlUpW {:<7}Hpenemy {}".format(data.LvlUpE, data.LvlUpGen, data.LvlUpGun, data.LvlUpW, data.Hpenemy))
    print("Emax {:<17}Egen {:<13}DpD {:<10}HpmaxW {:<7}DpDenenmy {}".format(data.Emax, data.Egen, data.DpD, data.HpmaxW, data.DpDenemy))
    print("E {:<52}HpW {:<10}NpDenemy {}".format(data.E, data.HpW, data.NpDenemy))
    print("{:<54}HppD {}".format("", data.HppD))


def Die(s):
    system("cls")
    if s == "E":
        print("У тебя достаточно энергии? НЕТ!")
    elif s == "Hp":
        print("Вражины прорвали стену! О НЕТ!")
    print("Ты ПРОИГРАЛ!")
    input()
    exit()


def LvlUpDiolog():
    print("""Улучшить что-нибуть?
(0) Нет
(1) Энергохранилище
(2) Генератор
(3) Пушка
(4) Стена""")
    while True:
        try:
            ans = int(input())
        except:
            ans = -1
        if (ans == 0):
            break
        elif (ans == 1):
            if upgrade.UpgradeE() == -1:
                print("Нехватает Энерги!!!")
            else:
                print("Энергохранилище улучшено! Осталось энергии: {}".format(data.E))
        elif (ans == 2):
            if upgrade.UpgradeGen() == -1:
                print("Нехватает Энерги!!!")
            else:
                print("Генератор улучшен! Осталось энергии: {}".format(data.E))
        elif (ans == 3):
            if upgrade.UpgradeGun() == -1:
                print("Нехватает Энерги!!!")
            else:
                print("Пушка улучшена! Осталось энергии: {}".format(data.E))
        elif (ans == 4):
            if upgrade.UpgradeW() == -1:
                print("Нехватает Энерги!!!")
            else:
                print("Стена улучшена! Осталось энергии: {}".format(data.E))
        else:
            print("Такого в списке нет.")
        print("Ещё чего-нибудь?")


def Rules():
    print("В 2228 году мир охватила ядерная война. Большенство людишек погибло, а их остатки были оттеснены сверхразумными мегароботами...")
    getch()
    print("Вы -- маленький сверхинтелект решивший покорить всю планету.")
    getch()
    system('cls')
    print("Любому сверхразумному мегазладею нужна мегабаза, подумали вы и преступили к сторительству")
    getch()
    print("Что же у Вас есть? Энергохраниище, генератор, пушка, стена и ...")
    getch()
    print("ВРАЖИНЫ!!!")
    getch()
    print("Кажется оставшиеся людишки прознали про вас и пытаются помешать! Боже, они продолжают набегать!")
    getch()
    system('cls')
    print("Итак, пройдёмся по плану.")
    getch()
    print("Генератор будет генерировать для нас ЭНЕРГИЮ -- ультимативную валюту современного мира.")
    getch()
    print("Энергию мы будем запасать в энергохранилище.")
    getch()
    print("[Никита] Мне кажется им не интересно это читать.")
    getch()
    print("[Арсений] Минак сказал нужно запилить правила.")
    getch()
    print("[Никита] Тогда, может уберём ту часть про ядерную войну?")
    getch()
    print("[Тёма] Да пофиг!")
    getch()
    print("Искусственому инетлекту самому нужна энергия, причём с каждым днём всё больше и больше. По этому после доставки энергии придётся немножко забрать.")
    getch()
    print("[Никита] А что будет если энергии не хватит?")
    getch()
    print("[Арсений] Тогда вот тут появится надпись типа: \"кирдык тебе!\", или что-то такое.")
    getch()
    print("[Тёма] Можно написать [нецензурная шутка].")
    getch()
    print("[Арсений] Давайте дальше.")
    getch()
    print("К концу дня в нашу обитель смерти будет прибывать новая порция вражин, причём каждый раз их будет чуть-чуть больше.")
    getch()
    print("В результате генных модификаций вызванных радиацией их число может быть не целым! Полторы вражины у стены -- нормальная ситуация!")
    getch()
    print("Так же радиация улучшает строение вражин, увеличивает их здоровье и атаку.")
    getch()
    print("Однако ещё до отрпавки новой порции вражин произойдёт небольшое сражение:")
    getch()
    print("Мы приготовимся к нему починв немного стену.")
    getch()
    print("Затем выстрелим по вражинам из пушки, сильно проредив их ряды.")
    getch()
    print("Потом толпа разгневанных вражин потыкается немного в нашу стену и возможно поцарапает её.")
    getch()
    print("Но это всё прозойдёт ночью. А днём вам придётся принимать несколько важных решений, а так же возможно улучшать Ваши постройки.")
    getch()
    print("Это собственно весь план...")
    getch()
    system('cls')
    print("Теперь поговорим о некоторых внутриигровых характеристиках.")
    getch()
    print()
    print("D (day) -- номер текщего дня")
    getch()
    print("EtoLive (energy to live) -- энергия которая вам понадобится в этот день")
    getch()
    print()
    print("ЭНЕРГОХРАНИЛИЩЕ")
    print("LvlE (level energy storage) -- уровень энергохранилища")
    getch()
    print("LvlUpE (levelup energy storage) -- цена улучшения энергохранилища")
    getch()
    print("Emax (energy maximal) -- максимальный возможный запас энергии")
    getch()
    print("E (energy) -- запас энергии")
    getch()
    print()
    print("ГЕНЕРАТОР")
    print("LvlGen (level generator) -- уровень генератора")
    getch()
    print("LvlUpGen (levelup generator) -- цена улучшения генератора")
    getch()
    print("Egen (energy generation) -- кол-во энергии, генерируещееся за день")
    getch()
    print()
    print("ПУШКА")
    print("LvlGun (level gun) -- уровень пушки")
    getch()
    print("LvlUpGun (levelup gun) -- цена улучшения пушки")
    getch()
    print("DpD (damege per day) -- урон, который пушка нанесёт за день")
    getch()
    print()
    print("СТЕНА")
    print("LvlW (level wall) -- уровень стеный")
    getch()
    print("LvlUpW (levelup wall) -- цена улучшения стены")
    getch()
    print("HpmaxW (hp maximal wall) -- максимальное hp стены")
    getch()
    print("HpW (hp wall) -- текущее hp стены")
    getch()
    print("HppD (hp per day) -- на сколько Вы почините стену перед атакой")
    getch()
    print()
    print("ВРАЖИНЫ")
    print("Nenemy -- кол-во вражин")
    getch()
    print("Hpenemy -- hp одной вражины")
    getch()
    print("DpDenemy -- урон одной вражины")
    getch()
    print("NpDenemy -- число вражин, прибегущих после сражения")
    getch()
    system('cls')
    print("Удачной недоигры!")
    getch()
    
    
