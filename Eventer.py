# This file uploads and runs events
import ParametersDeclarer as data
import ParametersChanger as change
from random import randint

# upload good events
GOOD_EVENTS = open("Events\GOOD_EVENTS.txt", "r").read().split("@")
# upload bad events
BAD_EVENTS = open("Events\BAD_EVENTS.txt", "r").read().split("@")


def RunGoodEvent():  # run random good event
    exec(GOOD_EVENTS[randint(0, len(GOOD_EVENTS) - 1)])


def RunBadEvent():  # run random bad event
    exec(BAD_EVENTS[randint(0, len(BAD_EVENTS) - 1)])


def RunEvent():  # run random event taking into account Luck
    try:
        if randint(1, 10000) <= data.Luck * 10000:
            RunGoodEvent()
        else:
            RunBadEvent()
    except:
        print("Эвент сломался, извените!")
