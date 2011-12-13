__author__ = 'mauricio'

import pygtk
pygtk.require("2.0")

import gtk

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine("sqlite:///fatecjp.db", echo = True)

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key = True)
    nome = Column(String)
    email = Column(String)
    postagem = Column(String)

    def __init__(self, nome, email, postagem):
        self.nome = nome
        self.email = email
        self.postagem = postagem

    def __repr__(self):
        return "<Post('%s','%s', '%s')>" % (self.nome, self.email, self.postagem)

Base.metadata.create_all(engine)

Session = sessionmaker(engine)

class Application:

    def __init__(self):
        self.window = gtk.Window( gtk.WINDOW_TOPLEVEL )
        self.window.set_title("My Window")
        self.window.connect( "destroy", self.destroy )

        self.update_timer = False

        table = gtk.Table(4, 2, True)

        nome_label = gtk.Label( "Nome" )

        table.attach( nome_label, 0, 1, 0, 1 )
        nome_label.show()

        email_label = gtk.Label("Email")

        table.attach( email_label, 0, 1, 1, 2 )
        email_label.show()

        postagem_label = gtk.Label("Postagem")
        table.attach( postagem_label, 0, 1, 2, 3 )
        postagem_label.show()

        self.nome_entry = gtk.Entry()

        table.attach( self.nome_entry, 1, 2, 0, 1 )
        self.nome_entry.show()

        self.email_entry = gtk.Entry()
        table.attach( self.email_entry, 1, 2, 1, 2 )
        self.email_entry.show()

        self.postagem_entry = gtk.TextView()
        table.attach( self.postagem_entry, 1, 2, 2, 3 )
        self.postagem_entry.show()

        button = gtk.Button( "Save" )
        button.connect("clicked", self.save)
        table.attach( button, 0, 2, 3, 4 )
        button.show()

        self.window.add(table)

        table.show()
        self.window.show()


    def main(self):
        gtk.main()

    def destroy(self, widget, data = None):
        gtk.main_quit()

    def save(self, widget, data = None):
        session = Session()

        buffer = self.postagem_entry.get_buffer()

        post = Post(
            self.nome_entry.get_text(),
            self.email_entry.get_text(),
            buffer.get_text( buffer.get_start_iter(), buffer.get_end_iter() ) )
        session.add(post)
        session.commit()


app = Application()
app.main()
