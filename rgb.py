#!/usr/bin/env python

import tkinter as tk
import random
import time


class RGBMatrix:
  def __init__(self, height, width):
    self.height = height
    self.width = width
    self.tiles = makeTiles(height, width)

  class Tile:
    def __init__(self, x, y, color):
      self.x = x
      self.y = y
      self.color = color


def makeRGBMatrix(height, width):
  rgbm = RGBMatrix(height, width)
  return rgbm


def makeTiles(height, width):
  # init tiles as black
  tiles = [[RGBMatrix.Tile(x, y, (0, 0, 0))
            for x in range(width)] for y in range(height)]
  return tiles


def rgb(color):
  color_html = "#%02x%02x%02x" % color
  return color_html


# create gui
width, height = 500, 500
gui = tk.Tk()
gui.title("RGB Matrix")
canvas = tk.Canvas(gui, width=width, height=height)
canvas = tk.Canvas(gui, width=width, height=height)


def show_led(colorMatrix):
  canvas.delete('all')
  rows, cols = len(colorMatrix), len(colorMatrix[0])
  rect_width, rect_height = width // rows, height // cols
  for y, row in enumerate(colorMatrix):
    for x, color in enumerate(row):
      x0, y0 = x * rect_width, y * rect_height
      x1, y1 = x0 + rect_width-1, y0 + rect_height-1
      canvas.create_rectangle(x0, y0, x1, y1, fill=rgb(color), width=0)
  canvas.pack()


# globals vars
i = None
passed = []
refresh_ms = 20


def task(refresh_ms):
  # init global vars
  global i
  global passed
  if i is None:
    i = 0
  # colors
  black = (0, 0, 0)
  blue = (0, 0, 255)
  cyan = (0, 255, 255)
  red = (255, 0, 0)

  # init colorMatrix with black tiles
  colorMatrix = [[black for x in range(10)] for y in range(10)]

  # assign correct matrix position
  if i in range(10):
    row = 0
    col = i
  elif i in range(10, 20):
    row = i - 10
    col = 9
  elif i in range(20, 30):
    row = 9
    col = 29 - i
  elif i in range(30, 40):
    row = 39 - i
    col = 0
  colorMatrix[row][col] = blue
  if [row, col] in passed:
    passed.remove([row, col])
  for tile in passed:
    colorMatrix[tile[0]][tile[1]] = cyan
  passed.append([row, col])

  # if i > 0:
  #   colorMatrix[row][col - 1] = cyan
  i += 1
  if i > 39:
    i = 0

  # for n in range(10):
  #   colorMatrix[0][n] = blue

  show_led(colorMatrix)
  gui.after(refresh_ms, task, refresh_ms)


def main():
  # run task
  gui.after(0, task, refresh_ms)
  gui.mainloop()


if __name__ == '__main__':
  main()
