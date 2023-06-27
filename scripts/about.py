#!/usr/bin/env python

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class aboutWin(Gtk.Window):
    
    def __init__(self):
        super().__init__(title="About Us")
        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_left.set_homogeneous(True)
        self.set_default_geometry(400,100)
        self.set_border_width(10)
        # self.set_default_size(100, 20)
        self.set_resizable(False)

        frame2 = Gtk.Frame(label="TCET-Linux")

        grid2 = Gtk.Grid(row_spacing    = 10,
                         column_spacing = 10,
                         column_homogeneous = False)

        image1 = Gtk.Image()
        image1.set_from_file("assets/tcetlinux-logo.png")
    
        label1 = Gtk.Label(label="TCET Linux is GNU/Linux distribution, based on Arch Linux built for enhancing college infrastructure and promoting Linux in software engineering education. The primary goal of TCET Open Source is to provide other users with access to project documentation for all of their college projects.")
        label1.set_line_wrap(True)
        label1.set_justify(Gtk.Justification.CENTER)
        label1.set_max_width_chars(50)

        label1.set_hexpand(True)

        button21 = Gtk.Button(label="Back")
        # button21.set_hexpand(True)
        button21.connect("clicked", Gtk.main_quit)
        button21.set_property("width-request", 45)
        grid2.attach(button21, 2, 10, 2, 1)
        grid2.attach(image1,   0, 0, 4, 2)
        grid2.attach(label1,   0, 2, 4, 2)

        self.add(frame2)
        frame2.add(grid2)

win5 = aboutWin()

win5.connect("destroy", Gtk.main_quit)

win5.show_all()
Gtk.main()