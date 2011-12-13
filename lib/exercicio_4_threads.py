__author__ = 'mauricio'

import pygtk
pygtk.require("2.0")

import gtk
import gobject
import threading
import time

gtk.gdk.threads_init()

class Base:

    def __init__(self):
        self.window = gtk.Window( gtk.WINDOW_TOPLEVEL )
        self.window.set_title("My Window")
        self.window.connect( "destroy", self.destroy )

        self.update_timer = False

        table = gtk.Table(2, 2, True)

        self.watch_label = gtk.Label()

        self.update_watch()

        table.attach( self.watch_label, 0, 2, 0, 1 )

        self.watch_label.show()

        start_button = gtk.Button( "Start process" )
        start_button.connect( "clicked", self.start_update_timer )

        table.attach( start_button, 0, 1, 1, 2 )
        start_button.show()

        stop_button = gtk.Button("Stop button")
        stop_button.connect( "clicked", self.stop_update_timer )

        table.attach( stop_button, 1, 2, 1, 2 )
        stop_button.show()

        self.window.add( table )

        table.show()
        self.window.show()

        self.start_update_timer()


    def run_update_timer(self):
        while self.update_timer:
            gobject.idle_add(self.update_watch)
            time.sleep(0.5)

    def start_update_timer(self, widget = None, data = None):
        print "starting update timer"
        if self.update_timer == False:
            self.update_timer = True
            threading.Thread( None, self.run_update_timer, "update-timer-thread" ).start()

    def stop_update_timer( self, widget = None, data = None ):
        self.update_timer = False

    def update_watch(self, data = None):
        self.watch_label.set_text( time.strftime( "%d/%m/%y %H:%M:%S",  time.localtime() ) )

    def main(self):
        gtk.main()

    def destroy(self, widget, data = None):
        gtk.main_quit()

    

base = Base()
base.main()