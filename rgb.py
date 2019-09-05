#!/usr/bin/env python

import operator
import tkinter as tk
import random
import time


def rgb(color):
  color_html = "#%02x%02x%02x" % tuple(map(int, color))
  return(color_html)


class RGBMatrix(tk.Frame):

  def __init__(self, *args, **kw):
    tk.Frame.__init__(self, *args, **kw)

    width, height = 500, 500
    rows, cols = 10, 10

    # colors
    black = (0, 0, 0)

    self.led_ids = []
    self.canvas = tk.Canvas(self, width=width, height=height)

    # init colorMatrix with black tiles
    colorMatrix = [[black for x in range(cols)] for y in range(rows)]

    rect_width, rect_height = width // rows, height // cols

    for y, row in enumerate(colorMatrix):
      for x, color in enumerate(row):
        x0, y0 = x * rect_width, y * rect_height
        x1, y1 = x0 + rect_width-1, y0 + rect_height-1
        led = self.canvas.create_rectangle(
            x0, y0, x1, y1, fill=rgb(color), width=0)
        self.led_ids.append(led)

    self.canvas.pack()

  def get_led_ids(self):
    return(self.led_ids)

  def led_change_color(self, led_id, rgb_color):
    self.canvas.itemconfig(led_id, fill=rgb(rgb_color))


# working on a fade effect
# def smooth_transistion(w, led_id, rgb_start, rgb_end, duration_fade):
#   refresh_ms = 10
#   delta = tuple(map(operator.sub, rgb_end, rgb_start))
#   iters = duration_fade / refresh_ms
#   titers = (iters, iters, iters)
#   diff = tuple(map(operator.truediv, delta, titers))
#   rgb = rgb_start
#   for _ in range(1, int(iters)):
#     rgb = tuple(map(operator.add, rgb, diff))
#     w.after(refresh_ms, w.led_change_color, led_id, rgb)


def task(w):
  refresh_ms = 100

  leds_all = w.get_led_ids()
  leds_border = []
  # add top row
  for i in range(1, 10):
    leds_border.append(i)
  # right side
  for i in range(10, 100, 10):
    leds_border.append(i)
  # add bot row inverse
  for i in range(100, 90, -1):
    leds_border.append(i)
  # left side inverse
  for i in range(81, 1, -10):
    leds_border.append(i)
  for led in leds_border:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    w.led_change_color(led, (r, g, b))
  rled = random.randint(1, 36)
  smooth_transistion(w, rled, (255, 0, 50), (50, 0, 255), 5000)
  w.after(refresh_ms, task, w)


def main():
  # create app
  gui = tk.Tk()
  gui.title("RGB Matrix")
  # initialize gui
  w = RGBMatrix(gui)
  # show gui
  w.pack()
  # run task
  w.after(0, task, w)
  # mainloop
  w.mainloop()


if __name__ == '__main__':
  main()
