#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):   
        self.lista_tag = []
     
        self.rootlayout = ""
        self.width = ""
        self.height = ""
        self.backgroundcolor = ""        
        
        self.region = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        
        self.img = ""
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""
        
        self.audio = ""
        self.src = ""
        self.begin = ""
        self.dur = ""
        
        self.textstream = ""
        self.src = ""
        self.region = ""
    
    def startElement(self, name, attrs):
    
        dic_atributos = {}
        
        if name == 'root-layout':
            self.width = attrs.get('width',"")
            self.height = attrs.get('height',"")
            self.backgroundcolor = attrs.get('background/color',"")
            
            dic_atributos['name'] = name
            dic_atributos['width'] = self.width
            dic_atributos['height'] = self.height
            dic_atributos['background/color'] = self.backgroundcolor
            
            self.lista_tag.append(dic_atributos)
            
        elif name == 'region':
            self.id = attrs.get('id',"")
            self.top = attrs.get('top',"")
            self.bottom = attrs.get('bottom',"")
            self.left = attrs.get('left',"")
            self.right = attrs.get('right',"")
            
            dic_atributos['id'] = self.id
            dic_atributos['top'] = self.top
            dic_atributos['bottom'] = self.bottom
            dic_atributos['left'] = self.left
            dic_atributos['right'] = self.right
            
            self.lista_tag.append(dic_atributos)

        elif name == 'img':
            self.src = attrs.get('src',"")
            self.region = attrs.get('region',"")
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"")
            
            dic_atributos['src'] = self.src
            dic_atributos['region'] = self.region
            dic_atributos['begin'] = self.begin
            dic_atributos['dur'] = self.dur
            
            self.lista_tag.append(dic_atributos)

        elif name == 'audio':
            self.src = attrs.get('src',"")
            self.region = attrs.get('region',"")
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"")
            
            dic_atributos['src'] = self.src
            dic_atributos['region'] = self.region
            dic_atributos['begin'] = self.begin
            dic_atributos['dur'] = self.dur
            
            self.lista_tag.append(dic_atributos)
            
        elif name == 'textstream':
            self.src = attrs.get('src',"")
            self.region = attrs.get('region',"")
            
            dic_atributos['src'] = self.src
            dic_atributos['region'] = self.region
            
            self.lista_tag.append(dic_atributos)       
          
    def get_tags(self):
       return self.lista_tag
    
if __name__ == "__main__":

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    print sHandler.get_tags()
