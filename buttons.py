import pygame, pygame.freetype
from utility import *
pygame.init()
defaultfont = pygame.freetype.SysFont('freesans', 12)
defaultfont.origin = True
class textButton(pygame.Rect):
  def __init__(self, x,y,width,height, text = ''):
    pygame.Rect.__init__(self, x,y,width,height)
    self._fontcolor = colors['black']
    self._color = colors['black']
    self.text= text
  #buttoncolor and fontcolor being properties just makes setting and getting them slightly easier and more convenient
  #allows values to be got and set just like normal variables (button.buttoncolor = ([color]))
  def _get_color(self):
    return self._color
  def _set_color(self, color):
    self._color = color
    return
  buttoncolor = property(_get_color,_set_color)
  def _get_font_color(self):
    return self._fontcolor
  def _set_font_color(self, color):
    self._fontcolor = color
  fontcolor = property(_get_font_color,_set_font_color)
  #called when the button is clicked
  #shift_caps is a effectively one variable but I needed it to have more scope than normal variables so it is a non-primitive type
  #tuple probably works here, but list works just fine
  #also adds the button's text to string [string] with the special cases called as needed, being the keys like space and enter that
  #aren't just as simple as adding their text to the rendered string
  #returns string back through so that it actually can update (primitive type)
  def click(self, string):
    if self.text in special_click_cases:
      return specialClickBehavior(string, self.text)
    upper = (shift_caps[1]+shift_caps[0])%2
    if shift_caps[0]:
      shift_caps[0] = False
    if upper:
      return string + self.text.upper()
    return string + self.text
  #draws the button on the pygame window
  #broken into 2 parts because I made them at different times, and for code clarity's sake
  #_drawButton draws the actual button part, and _drawText draws the text (shocking)
  #the "return" of the function is on the graphical window, with the button being rendered
  def draw(self, font = defaultfont, fcolor = None):
    if fcolor == None:
      fcolor = self._fontcolor
    self.window = pygame.display.get_surface()
    self._drawButton(self.window)
    self._drawText(self.window, font, fcolor)
  def _drawButton(self, window):
    pygame.draw.rect(window, self._color, self, 1)
  def _drawText(self,window, font=defaultfont, fontcolor = None):
    text_rect = font.get_rect(self.text)
    font.origin=True
    font.render_to(window, tupleSubtract(self.center, (text_rect.width/2, 0)), self.text, fontcolor)
class mineButton(pygame.Rect):
  def __init__(self, x, y, width, height):
    pygame.Rect.__init__(self, x,y,width,height)
    self._fontcolor = colors['black']
    self._color = colors['black']
  def _get_color(self):
    return self._color
  def _set_color(self, color):
    self._color = color
    return
  buttoncolor = property(_get_color,_set_color)
  def _get_font_color(self):
    return self._fontcolor
  def _set_font_color(self, color):
    self._fontcolor = color
  fontcolor = property(_get_font_color,_set_font_color)
  def draw(self):
    self.window = pygame.display.get_surface()
    self._drawButton()
    self._drawMine()
  def _drawButton(self):
    pygame.draw.rect(self.window, self._color, self, 1)
  def _drawMine(self):
    pygame.draw.circle(self.window, colors['black'], self.center, self.height/2)