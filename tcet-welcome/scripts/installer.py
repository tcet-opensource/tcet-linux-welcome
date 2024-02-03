#!/usr/bin/env python

import multiprocessing
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess
import time
import signal

package_map = {
  "NodeJS": "nodejs",
  "Google Chrome": "google-chrome",
  "VS Code": "visual-studio-code-bin",
  "Java": "jdk17-openjdk",
  "Libre Office": "libreoffice-still",
  "PyCharm (CE)":"pycharm-community-edition",
  "GitHub CLI":"github-cli",
  "Neovim":"neovim",
  "Intellij Idea (CE)":"intellij-idea-community-edition",
  "GoLang":"go"
}

installDir = '/usr/local/share/tcet-welcome'

class MyApp(Gtk.Window):
  def __init__(self):
    Gtk.Window.__init__(self, title="Application Installer (BETA)")
    self.set_border_width(10)
    self.set_default_size(500, 200)
    self.set_resizable(False)

    grid = Gtk.Grid()
    grid.set_column_spacing(10)
    grid.set_row_spacing(10)
    self.add(grid)

    # self.set_icon_from_file(f"{installDir}/assets/tcetlinux-logo.png")

    self.checkboxes = {}

    col = 0
    row = 0
    for i, displayed_name in enumerate(package_map):
      checkbox = Gtk.CheckButton(label=displayed_name)
      self.checkboxes[displayed_name] = checkbox
      if i % 5 == 0 and i > 0:
        col = 0
        row += 1

      grid.attach(checkbox, col, row, 1, 1)
      col += 1


    button = Gtk.Button(label="Install")
    button.set_property("height-request", 0)
    grid.set_column_homogeneous(True)
    grid.set_row_homogeneous(True)
    grid.attach(button, 2, 2, 1, 1)
    button.connect("clicked", self.on_install_clicked)

  def clear_checkboxes(self):
    for checkbox in self.checkboxes.values():
      checkbox.set_active(False)

  def on_install_clicked(self, widget):
    to_install = [v for k,v in package_map.items() if self.checkboxes[k].get_active()]
    installCMD = "yay -S --noconfirm"
    for package in to_install:
      installCMD = installCMD + " " + package
    result = os.popen('echo $XDG_CURRENT_DESKTOP').read().strip()
    match result:
      case "GNOME":
        p = subprocess.Popen(["kgx", "--", "bash", "-c", installCMD], preexec_fn=os.setpgrp)
        process = multiprocessing.Process(target = p)
        if not process.is_alive:
          #time.sleep(25)
          os.killpg(p.pid, signal.SIGINT)
      case "XFCE":
        p = subprocess.Popen(["xfce4-terminal", "--", "bash", "-c", installCMD], preexec_fn=os.setpgrp)
        process = multiprocessing.Process(target = p)
        if not process.is_alive:
          #time.sleep(25)
          os.killpg(p.pid, signal.SIGINT)
      case _:
        # yad --image="dialog-question" --title "Alert" --text "Can't recongnize desktop environment" --button="yad-ok:0"
        print("Cant Recognize DE")

    self.clear_checkboxes()

win = MyApp()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
