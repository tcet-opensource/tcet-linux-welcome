#!/usr/bin/env python
 
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from os import environ

# get install dir relative to $home
# we have to do this because when we start the program from terminal its executed in the ~/.local/share/tcet-linux-welcome
# when we auto start welcome.sh from the .desktop in ~/.config/autostart it is executed in the $HOME dir and our relative paths are broken
# so using the $HOME env variable get the path GTK more specifically set_from_file() / set_icon_from_file wont let you user ~/.local/share/tcet-linux-welcome

 
installDir = environ['HOME']+'/.local/share/tcet-linux-welcome'
 
class aboutWin(Gtk.Window):
 
    def __init__(self):
        super().__init__(title="About Us")
        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_left.set_homogeneous(True)
        self.set_default_geometry(400,100)
        self.set_border_width(10)
        # self.set_default_size(100, 20)
        self.set_resizable(False)
 
        frame2 = Gtk.Frame()
 
        grid2 = Gtk.Grid(row_spacing    = 10,
                         column_spacing = 10,
                         column_homogeneous = False)
 
        image1 = Gtk.Image()
        image1.set_from_file(f"{installDir}/assets/tcetlinux-logo.png")
 
        self.set_icon_from_file(f"{installDir}/assets/tcetlinux-logo.png")
        label1 = Gtk.Label(label="TCET - Linux" 
                           "\n"
                           "\n1.0"
                           "\n"
                           "\nTCET Linux is GNU/Linux distribution, based on Arch Linux built for enhancing college infrastructure and promoting Linux in software engineering education\n"
                           "\n"
                           "\n ©2020-2024 TCET-Opensource")
        label1.set_line_wrap(True)
        label1.set_justify(Gtk.Justification.CENTER)
        label1.set_max_width_chars(50)
        label1.set_margin_start(10)
        label1.set_margin_end(10)
 
        label1.set_hexpand(True)
 
        label2 = Gtk.Label()
        label2.set_markup("<a href ='https://linux.tcetmumbai.in//' title='Check out our website!'><b>Website</b></a>")
        label2.set_line_wrap(True)
        label2.set_max_width_chars(48)
        label2.set_justify(Gtk.Justification.CENTER)
        button21 = Gtk.Button(label="Back")
        # button21.set_hexpand(True)
        button21.connect("clicked", Gtk.main_quit)
        button21.set_property("width-request", 45)
        grid2.attach(button21, 2, 10, 2, 1)
        grid2.attach(image1,   0, 0, 4, 2)
        grid2.attach(label2,   0,3, 5, 2)
        grid2.attach(label1,   0, 2, 4, 2)
 
        self.add(frame2)
        frame2.add(grid2)
 
win5 = aboutWin()
 
win5.connect("destroy", Gtk.main_quit)
 
win5.show_all()
Gtk.main()
 