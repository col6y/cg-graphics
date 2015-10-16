"""
This is a simple interactive graphics and animation library for Python.
Author: Andrew Merrill
Contributor: Colby Skeggs
Version: 4.0 (last updated October, 2015)

This code is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike license
see http://creativecommons.org/licenses/by-nc-sa/3.0/ for details
"""

print "using graphics.py library version 4.0"

import pygame, colors, keys, joysticks, fps, display, audio, gmath, image, keyboard, events, mouse, timers


class World:
    pass


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GameLibInfo:
    def __init__(self):
        self.world = None
        self.display = display.Display()
        self.joyinfo = joysticks.JoysticksInfo()
        self.keys = keyboard.Keys()
        self.timers = timers.Timers()
        self.fps = fps.GameClock()
        self.eventloop = events.EventLoop()

        self.graphicsInited = False
        self.eventListeners = {}
        self.nextEventType = pygame.USEREVENT

    def initGraphics(self):
        if not self.graphicsInited:
            self.display.initialize()
            self.joyinfo.initialize()
            self.keys.initialize()
            events.handler(pygame.QUIT, self.eventloop.stop)
            events.handler(pygame.KEYDOWN, self.check_quit_key)
            self.graphicsInited = True

    def check_quit_key(self, event, world):
        if event.key == pygame.K_ESCAPE:
            self.eventloop.stop()

    def startGame(self):
        self.world = World()
        self.fps.start()
        self.eventloop.start()

    def getWorld(self):
        return self.world

    # use animate for non-interactive animations
    def animate(self, drawFunction, timeLimit, repeat=False):
        def startAnimation(world):
            pass

        def timeExpired(world):
            if getElapsedTime() >= timeLimit:
                if repeat:
                    resetTime()
                else:
                    _GLI.eventloop.stop()

        def drawAnimationFrame(world):
            drawFunction(float(getElapsedTime()))

        self.runGraphics(startAnimation, timeExpired, drawAnimationFrame)

    # use runGraphics for interactive programs like games
    def runGraphics(self, startFunction, updateFunction, drawFunction):
        self.startGame()
        startFunction(self.world)

        def loopFunction():
            updateFunction(self.world)
            self.display.renderWithFunction(lambda: drawFunction(self.world))
            self.fps.tick()

        self.eventloop.runloop(self.world, loopFunction)


_GLI = GameLibInfo()

animate = _GLI.animate
runGraphics = _GLI.runGraphics


def makeGraphicsWindow(width, height, fullscreen=False):
    _GLI.initGraphics()
    setGraphicsMode(width, height, fullscreen)


def getScreenSize():
    _GLI.initGraphics()
    return _GLI.display.getScreenSize()


def getAllScreenSizes():
    _GLI.initGraphics()
    return _GLI.display.getAllScreenSizes()


getActualFrameRate = _GLI.fps.getActualFPS
displayFPS = _GLI.fps.display

setBackground = _GLI.display.setBackground
setForeground = _GLI.display.setForeground

setGraphicsMode = _GLI.display.setGraphicsMode
getWindowWidth = _GLI.display.getWindowWidth
getWindowHeight = _GLI.display.getWindowHeight
setWindowTitle = _GLI.display.setWindowTitle

saveScreen = _GLI.display.saveScreen
getScreenPixel = _GLI.display.getScreenPixel

lookupColor = colors.lookupColor
getColorsList = colors.getColorsList

drawPixel = _GLI.display.drawPixel
drawLine = _GLI.display.drawLine
drawCircle = _GLI.display.drawCircle
fillCircle = _GLI.display.fillCircle
drawEllipse = _GLI.display.drawEllipse
fillEllipse = _GLI.display.fillEllipse
drawRectangle = _GLI.display.drawRectangle
fillRectangle = _GLI.display.fillRectangle
drawPolygon = _GLI.display.drawPolygon
fillPolygon = _GLI.display.fillPolygon
sizeString = _GLI.display.sizeString
drawString = _GLI.display.drawString
getFontList = _GLI.display.getFontList

loadImage = image.loadImage
saveImage = image.saveImage
getImageWidth = image.getImageWidth
getImageHeight = image.getImageHeight
getImagePixel = image.getImagePixel
getImageRegion = image.getImageRegion

loadSound = audio.loadSound
playSound = audio.playSound
stopSound = audio.stopSound
loadMusic = audio.loadMusic
playMusic = audio.playMusic
stopMusic = audio.stopMusic

onKeyPress = keyboard.onKeyPress
onAnyKeyPress = keyboard.onAnyKeyPress
onKeyRelease = keyboard.onKeyRelease
onAnyKeyRelease = keyboard.onAnyKeyRelease

onMousePress = mouse.onMousePress
onMouseRelease = mouse.onMouseRelease
onWheelForward = mouse.onWheelForward
onWheelBackward = mouse.onWheelBackward
onMouseMotion = mouse.onMouseMotion

onGameControllerStick = _GLI.joyinfo.onGameControllerStick
onGameControllerDPad = _GLI.joyinfo.onGameControllerDPad
onGameControllerButtonPress = _GLI.joyinfo.onGameControllerButtonPress
onGameControllerButtonRelease = _GLI.joyinfo.onGameControllerButtonRelease

onTimer = _GLI.timers.onTimer

getMousePosition = keyboard.getMousePosition
getMouseButton = keyboard.getMouseButton
hideMouse = keyboard.hideMouse
showMouse = keyboard.showMouse
moveMouse = keyboard.moveMouse

isKeyPressed = _GLI.keys.isKeyPressed

getKeyName = keys.getKeyName
getKeyCode = keys.getKeyCode
sameKeys = keys.sameKeys

numGameControllers = _GLI.joyinfo.getJoystickCount
gameControllerSetDeadZone = _GLI.joyinfo.setDeadzone

gameControllerNumStickAxes = _GLI.joyinfo.getAxisCount
gameControllerGetStickAxesNames = _GLI.joyinfo.getAxisNames
gameControllerSetStickAxesNames = _GLI.joyinfo.setAxisNames
gameControllerStickAxis = _GLI.joyinfo.getAxis

gameControllerNumButtons = _GLI.joyinfo.getButtonCount
gameControllerButton = _GLI.joyinfo.getButton

gameControllerNumDPads = _GLI.joyinfo.getDPadCount
gameControllerDPadX = _GLI.joyinfo.getDPadX
gameControllerDPadY = _GLI.joyinfo.getDPadY

polarToCartesian = gmath.polarToCartesian
cartesianToPolarAngle = gmath.cartesianToPolarAngle
pointInPolygon = gmath.pointInPolygon

endGraphics = _GLI.eventloop.stop

getWorld = _GLI.getWorld

getElapsedTime = _GLI.fps.getElapsedTime
resetTime = _GLI.fps.resetTime
setFrameRate = _GLI.fps.setTargetFPS
