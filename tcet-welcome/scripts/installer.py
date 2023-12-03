#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess

package_map = {
  "NodeJS": "nodejs",
  "Google Chrome": "google-chrome",
  "VS Code": "visual-studio-code-bin",
  "Java": "jdk17-openjdk",
  "Libre Office": "libreoffice-still",
  "PyCharm (CE)":"pycharm-community-edition",
  "GitHub CLI":"github-cli",
  "Neovim":"neovim-git",
  "Intellij Idea (CE)":"intellij-idea-community-edition",
  "GoLang":"go"
}

class MyApp(Gtk.Window):

  def __init__(self):
    Gtk.Window.__init__(self, title="Application Installer (BETA)")
    self.set_border_width(10)
    self.set_default_size(500, 200)

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

  def error_msg(self, package):
    dialog = Gtk.MessageDialog(transient_for=self,flags=0, message_type=Gtk.MessageType.ERROR,buttons=Gtk.ButtonsType.OK,text="Error installing "+package)
    dialog.format_secondary_text("Package "+package+" is not available. Please update the mirrorlist and try again.")
    dialog.run()
    dialog.destroy()
    Gtk.main_quit()

  def success_msg(self):
    dialog = Gtk.MessageDialog(transient_for=self,flags=0, message_type=Gtk.MessageType.ERROR,buttons=Gtk.ButtonsType.OK,text="Packages Installed ")
    dialog.format_secondary_text("Packages are installed successfully.")
    dialog.run()
    dialog.destroy()
    Gtk.main_quit()

  def on_install_clicked(self, widget):
    to_install = [v for k,v in package_map.items() if self.checkboxes[k].get_active()]
    error = False
    for package in to_install:
        subprocess.run(["pkexec", "yay", "-S", package, "--noconfirm"])
        try:
          subprocess.check_output(["pacman", "-Q", package]).decode().split("\n")
        except subprocess.CalledProcessError:
          self.error_msg(package)
          error = True

    if not error:
      self.success_msg()
    
win = MyApp()
win.connect("destroy", Gtk.main_quit) 
win.show_all()
Gtk.main()