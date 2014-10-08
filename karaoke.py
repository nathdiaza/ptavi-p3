#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys

if __name__ == "__main__":

    try:
        fichero = sys.argv[1] 
    except IndexError:
        print "Usage: python karaoke.py file.smil"
        raise SystemExit    
    
    try:
        fich = open(fichero, 'r') 
        lista_fichero = fich.readlines()
    except IOError:
        print "Introduce un nombre correcto de fichero"
        raise SystemExit  
        
    fich.close()
    
    print lista_fichero
