__author__ = 'mauricio'

import pygtk
pygtk.require("2.0")

import gtk

class Base:

    def __init__(self):
        self.window = gtk.Window( gtk.WINDOW_TOPLEVEL )
        self.window.show()
        self.window.set_title("My Window")
        self.window.connect( "destroy", self.destroy )

        table = gtk.Table(5, 2, True)

        nome_label = gtk.Label()
        nome_label.set_text("Nome")
        self.nome_entry = gtk.Entry(50)

        table.attach( nome_label, 0, 1, 0, 1 )
        nome_label.show()

        table.attach( self.nome_entry, 1, 2, 0, 1 )
        self.nome_entry.show()

        idade_label = gtk.Label()
        idade_label.set_text("Idade")
        self.idade_entry = gtk.Entry(50)

        table.attach( idade_label, 0, 1, 1, 2 )
        idade_label.show()

        table.attach( self.idade_entry, 1, 2, 1, 2 )
        self.idade_entry.show()

        rua_label = gtk.Label()
        rua_label.set_text("Rua")
        self.rua_entry = gtk.Entry(50)

        table.attach( rua_label, 0, 1, 2, 3 )
        rua_label.show()

        table.attach( self.rua_entry, 1, 2, 2, 3 )
        self.rua_entry.show()

        cidade_label = gtk.Label()
        cidade_label.set_text("Cidade")
        self.cidade_entry = gtk.Entry(50)

        table.attach( cidade_label, 0, 1, 3, 4 )
        cidade_label.show()

        table.attach( self.cidade_entry, 1, 2, 3, 4 )
        self.cidade_entry.show()

        button = gtk.Button( "Salvar em arquivo" )
        button.connect("clicked", self.button_clicked)

        table.attach( button, 0, 2, 4, 5 )
        button.show()

        self.window.add(table)

        table.show()
        self.window.show()

    def button_clicked(self, component, data = None):
        self.file_selection = gtk.FileChooserDialog("Selecione o arquivo",
                                                    None,
                                                    gtk.FILE_CHOOSER_ACTION_SAVE, (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_SAVE, gtk.RESPONSE_OK) )

        self.file_selection.set_default_response(gtk.RESPONSE_OK)
        self.file_selection.set_do_overwrite_confirmation(False)

        response = self.file_selection.run()

        if response == gtk.RESPONSE_OK:
            self.selected_file()

        self.file_selection.destroy()

    def selected_file(self):
        with open(self.file_selection.get_filename(), "w") as file:
            file.write("%s,%s,%s,%s" % (self.nome_entry.get_text(), self.idade_entry.get_text(), self.rua_entry.get_text(), self.cidade_entry.get_text()))

    def main(self):
        gtk.main()

    def destroy(self, widget, data = None):
        gtk.main_quit()

base = Base()
base.main()