#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio 
import subprocess

package_map = {
  "NodeJS": "nodejs",
  "Google Chrome": "google-chrome",
  "VS Code": "visual-studio-code-bin" ,
  "Java": "jdk17-openjdk",
  "Libre Office": "libreoffice-still",
  "PyCharm (CE)":"pycharm-community-edition",
  "GitHub CLI":"github-cli",
  "Neovim":"neovim",
  "Intellij Idea (CE)":"intellij-idea-community-edition",
  "GoLang":"go"
}

class MyApp(Gtk.Window):

  def __init__(self):
    Gtk.Window.__init__(self, title="Application Installer")
    self.set_border_width(10)
    self.set_default_size(500, 250)

    grid = Gtk.Grid()
    grid.set_column_spacing(10)
    grid.set_row_spacing(10)
    self.add(grid)

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

  def on_install_clicked(self):

    to_install = []
    for displayed_name, checkbox in self.checkboxes.items():
      if checkbox.get_active():
        package_name = package_map[displayed_name]
        to_install.append(package_name)

    for package in to_install:
      print(f"Installing {package}")
      subprocess.run(["pkexec","yay", "-S", package, "--noconfirm"])

win = MyApp() 
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()