import os

import gi

gi.require_version("Gtk", "3.0")

from gi.repository import GObject, Gtk, Gedit, PeasGtk, Gio


def preprocess(data):
    with open("file", "wb") as f:
        f.write(data.encode("utf-8"))

    os.system("black file")

    with open("file", "rb") as f:
        data = f.read()
    os.remove("file")
    return data.decode("utf-8")


class AdornAppActivatable(GObject.Object, Gedit.AppActivatable):
    app = GObject.property(type=Gedit.App)
    __gtype_name__ = "BableAppActivatable"

    def __init__(self):
        GObject.Object.__init__(self)
        self.menu_ext = None
        self.menu_item = None

    def do_activate(self):
        self._build_menu()

    def _build_menu(self):
        # Get the extension from tools menu
        self.menu_ext = self.extend_menu("tools-section")
        # This is the submenu which is added to a menu item and then inserted in tools menu.
        sub_menu = Gio.Menu()
        sub_menu_item = Gio.MenuItem.new("Adorn", "win.adorn")
        sub_menu.append_item(sub_menu_item)
        self.menu_item = Gio.MenuItem.new_submenu("Adorn", sub_menu)
        self.menu_ext.append_menu_item(self.menu_item)
        # Setting accelerators, now our action is called when Ctrl+Alt+1 is pressed.
        self.app.set_accels_for_action("win.adorn", ("<Primary><Alt>1", None))

    def do_deactivate(self):
        self._remove_menu()

    def _remove_menu(self):
        # removing accelerator and destroying menu items
        self.app.set_accels_for_action("win.dictonator_start", ())
        self.menu_ext = None
        self.menu_item = None


class AdornWindowActivatable(
    GObject.Object, Gedit.WindowActivatable, PeasGtk.Configurable
):
    window = GObject.property(type=Gedit.Window)
    __gtype_name__ = "BableWindowActivatable"

    def __init__(self):
        GObject.Object.__init__(self)

    # this is called every time the gui is updated
    def do_update_state(self):
        # if there is no document in sight, we disable the action, so we don't get NoneException
        if self.window.get_active_view() is not None:
            self.window.lookup_action("adorn").set_enabled("true")

    def do_activate(self):
        # Defining the action which was set earlier in AppActivatable.
        self._connect_menu()

    def _connect_menu(self):
        action = Gio.SimpleAction(name="adorn")
        action.connect("activate", self.action_cb)
        self.window.add_action(action)

    def action_cb(self, action, data):
        # On action get the document apply black code formatter and set new text to the document.
        doc = self.window.get_active_document()
        start, end = doc.get_bounds()
        data = start.get_slice(end)
        data1 = preprocess(data)
        doc.set_text(data1)

    def do_deactivate(self):
        pass
