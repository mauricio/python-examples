# -*- coding: utf-8 -*-
import pygtk
pygtk.require("2.0")

import gtk
import gobject
import threading
import lightblue

gtk.gdk.threads_init()

class Base:

    def __init__(self):
        self.window = gtk.Window( gtk.WINDOW_TOPLEVEL )
        self.window.set_title("My Window")
        self.window.connect( "destroy", self.destroy )

        self.table = gtk.Table(3, 3, True)

        self.devices = []

        self.select_label = gtk.Label("Selecione o dispositivo")

        self.table.attach( self.select_label, 0, 1, 0, 1 )
        self.select_label.show()

        self.select_button = gtk.Button( "Update devices list" )
        self.table.attach(self.select_button, 2, 3, 0, 1 )
        self.select_button.connect("clicked", self.update_devices_list)
        self.select_button.show()

        self.update_devices_list()

        self.mensagem_entry = gtk.Entry(50)
        self.table.attach( self.mensagem_entry, 0, 2, 1, 2 )
        self.mensagem_entry.show()

        self.mensagem_button = gtk.Button( "Enviar" )
        self.table.attach( self.mensagem_button, 2, 3, 1, 2 )
        self.mensagem_button.connect( "clicked", self.enviar_mensagem )
        self.mensagem_button.show()

        self.window.add( self.table )

        self.table.show()
        self.window.show()

    def update_devices_list(self, widget = None, data = None):
        self.find_devices()
        #lib em objectiive-c que fala com bluetooth no mac não é thread safe
        #threading.Thread( None, self.find_devices, "find-devices-thread" ).start()

    def find_devices(self):
        self.devices = lightblue.finddevices()
        print( self.devices )
        self.update_devices()

    def update_devices(self):
        self.select_combo = gtk.combo_box_new_text()

        for device in self.devices:
            print( "adding text %s" % device[1] )
            self.select_combo.append_text( device[1] )

        if len(self.devices) > 0:
            print("setting active item")
            self.select_combo.set_active(0)

        self.table.attach( self.select_combo, 1, 2, 0, 1 )
        self.select_combo.show()

    def enviar_mensagem( self, widget = None, data = None ):
        if len( self.devices ) > 0:
            device = self.devices[self.select_combo.get_active()]
            socket = lightblue.socket()
            socket.connect((device[0], device[2] ))
            socket.send( self.mensagem_entry.get_text() )
            socket.close()

    def main(self):
        gtk.main()

    def destroy(self, widget, data = None):
        gtk.main_quit()



base = Base()
base.main()