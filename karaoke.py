#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler

try:
    fichero = sys.argv[1] 
except IndexError:
    print "Usage: python karaoke.py file.smil"
    raise SystemExit    
try:
    fich = open(fichero, 'r') 
    fich.close()
except IOError:
    print "Introduce un nombre correcto de fichero.smil"
    raise SystemExit  

parser = make_parser()
kHandler = SmallSMILHandler()
parser.setContentHandler(kHandler)
parser.parse(open(fichero))
    
for i in range(len(kHandler.lista)):
    linea = kHandler.lista[i]
    tag = linea['name']
    imprimir = tag
    for atributo in kHandler.atributos[tag]:
        if not linea[atributo] == "":
            imprimir = imprimir + "\\t" + atributo + '="' + linea[atributo] + '"'
    imprimir = imprimir + "\\n"
    print imprimir

