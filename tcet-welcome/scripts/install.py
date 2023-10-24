#!/usr/bin/env python
 
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from os import environ

# get install dir relative to $home
# we have to do this because when we start the program from terminal its executed in the ~/.local/share/tcet-welcome
# when we auto start welcome.sh from the .desktop in ~/.config/autostart it is executed in the $HOME dir and our relative paths are broken
# so using the $HOME env variable get the path GTK more specifically set_from_file() / set_icon_from_file wont let you user ~/.local/share/tcet-welcome

 
installDir = environ['HOME']+'/.local/share/tcet-welcome'
 
# Create a list of apps to install
apps = ["firefox", "chromium", "libreoffice", "vlc", "gimp", "steam", "code", "discord"]
class installWin(Gtk.window):
    def __init__(self):
        super().__init__(title="Install Apps")
        self.set_default_Size(600, 400)
        self.set_border_width(10)
        self.set_resizable(False)

        # Create a grid to layout the window
        grid = Gtk.Grid(row_spacing=10, column_spacing=10)

        # Create a label for the app list
        label = Gtk.Label(label="Apps to install:")
        grid.attach(label, 0 , 0, 1, 1)

        # Create a scrollbar for the app list
        scrollbar = Gtk.Scrollbar()

        # Create a treeview to display the app list
        treeview = Gtk.TreeView()
        treeview.set_model(Gtk.ListStore(str))
        treeview.append_column(Gtk.TreeViewColumn(title="App", cell_renderer=Gtk.CellRendererText(), attribute="0"))
        treeview.set_vexpand(True)
        treeview.set_vadjustment(scrollbar.get_adjustment())

        # Add the treeview to the grid
        grid.attach(treeview, 0, 1, 1, 10)

        # Add the scrollbar to the grid
        grid.attach(scrollbar, 1, 1, 1, 10)

        # Add a button to install the selected apps
        button = Gtk.Button(label="Install")
        button.connect("clicked", self.on_install_clicked)
        grid.attach(button, 0, 11, 1, 1)

        # Populate the app list
        for app in apps:
            treeview.append([app])

        # Add the grid to the window
        self.add(grid)
    def on_install_clicked(self, button):
        # Get the selected apps
        selected_apps = []
        selection = self.get_child().get_selection()
        for model, iter in selection.selected_iterators():
            selected_apps.append(model.get_value(iter, 0))

        # Install the selected apps
        for app in selected_apps:
            os.system(f"sudo pacman -S {app}")

        # Close the window
        self.destroy()

win = installWin()

win.connect("destroy", Gtk.main_quit)

win.show_all()
Gtk.main()