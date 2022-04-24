# This file implements changing parameters when going to next day or upgrading
# Look at Parameters1.jpg, Parameters2.jpg and ChangingOrder.jpg
import ParametersDeclarer as data
import Printer as printer


def UpgradeE():  # Upgrade Energy storage
    if data.E < data.LvlUpE:
        return -1
    data.E -= data.LvlUpE
    data.LvlE += 1
    data.LvlUpE = round(data.LvlUpE*1.62)
    data.Emax = round(data.Emax*1.62)
    return 0


def UpgradeGen():  # Upgrade Generator
    if data.E < data.LvlUpGen:
        return -1
    data.E -= data.LvlUpGen
    data.LvlGen += 1
    data.LvlUpGen = round(data.LvlUpGen*1.62)
    data.Egen = round(data.Egen*2)
    return 0


def UpgradeGun():  # Upgrade Gun
    if data.E < data.LvlUpGun:
        return -1
    data.E -= data.LvlUpGun
    data.LvlGun += 1
    data.LvlUpGun = round(data.LvlUpGun*1.62)
    data.DpD = round(data.DpD*1.62)
    return 0


def UpgradeW():  # Upgrade Wall
    if data.E < data.LvlUpW:
        return -1
    data.E -= data.LvlUpW
    data.LvlW += 1
    data.LvlUpW = round(data.LvlUpW*1.62)
    data.HpmaxW = round(data.HpmaxW*1.62)
    data.HppD = round(data.HppD*1.2)
    return 0


def UpgradeEnemy():  # Upgrade Enemy
    if data.D % 3 == 0:
        data.Hpenemy += 1
        data.DpDenemy += 1
    data.NpDenemy *= 1.05
    data.NpDenemy = float('%.4f'%(data.NpDenemy))
    return 0


def PassDay():  # changing parameters when going to next day
    data.NpDenemy = float('%.4f'%(data.NpDenemy))    
    data.Nenemy = float('%.4f'%(data.Nenemy))  
    data.HpW = float('%.4f'%(data.HpW))
    
    data.D += 1
    data.E = min(data.Emax, data.E + data.Egen)
    data.E -= data.EtoLive
    if data.E < 0:
        printer.Die("E")
    data.HpW = min(data.HpmaxW, data.HpW + data.HppD) 
    data.HpW = float('%.4f'%(data.HpW))
    data.Nenemy = max(0, data.Nenemy - data.DpD/data.Hpenemy)
    data.Nenemy = float('%.4f'%(data.Nenemy))  
    data.HpW -= data.Nenemy*data.DpDenemy
    data.HpW = float('%.4f'%(data.HpW))
    if data.HpW < 0:
        printer.Die("Hp")
    data.Nenemy += data.NpDenemy
    data.Nenemy = float('%.4f'%(data.Nenemy))    
    data.EtoLive = round(data.EtoLive*1.05)
    UpgradeEnemy()
