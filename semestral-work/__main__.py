#!/usr/bin/env python3
from visual_screwdriver import *

vsd = VisualScrewdriver()
vsd.commandHelp()

while True:
    command = input()
    commandName = command.strip().split(' ', 1)[0]  # first world

    if commandName == 'exit':
        vsd.commandExit()
    elif commandName == 'help':
        vsd.commandHelp()
    elif commandName == 'save':
        vsd.commandSave()
    elif commandName == 'autosave':
        vsd.commandAutosave()
    elif commandName == 'new':
        vsd.commandNew()
    elif commandName == 'reset':
        vsd.commandReset()
    elif commandName == 'rotateR':
        vsd.commandRotateR()
    elif commandName == 'rotateL':
        vsd.commandRotateL()
    elif commandName == 'mirrorX':
        vsd.commandMirrorX()
    elif commandName == 'mirrorY':
        vsd.commandMirrorY()
    elif commandName == 'invert':
        vsd.commandInvert()
    elif commandName == 'dark':
        vsd.commandDark()
    elif commandName == 'light':
        vsd.commandLight()
    elif commandName == 'greyscale':
        vsd.commandGreyscale()
    elif commandName == 'highlight':
        vsd.commandHighlight()
    else:
        print("Command not found.")
        pass
