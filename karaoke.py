#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import os


class KaraokeLocal():

    def __init__(self, fichero):
        parser = make_parser()
        self.kHandler = SmallSMILHandler()
        parser.setContentHandler(self.kHandler)
        parser.parse(open(fichero))
        self.etiquetas = self.kHandler.get_tags()

    def __str__(self):
        for sublista in range(len(self.etiquetas)):
            linea = self.etiquetas[sublista]
            line = linea['name']
            for atrib in self.kHandler.atributos[linea['name']]:
                if not linea[atrib] == "":
                    line = line + "\\t" + atrib + '="' + linea[atrib] + '"'
            print line + "\\n"

    def do_local(self):
        for sublista in range(len(self.etiquetas)):
            linea = self.etiquetas[sublista]
            for atrib in self.kHandler.atributos[linea['name']]:
                if atrib == "src":
                    if linea[atrib][:7] == "http://":
                        os.system("wget -q " + linea[atrib])
                        linea[atrib] = linea[atrib].split('/')[-1]

if __name__ == "__main__":
    try:
        fichero = sys.argv[1]
    except IndexError:
        print "Usage: python karaoke.py file.smil"
        raise SystemExit

    kLocal = KaraokeLocal(fichero)
    kLocal.__str__()
    kLocal.do_local()
    kLocal.__str__()
