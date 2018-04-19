from ricercaopt import *

#TROVO LE SIMILITUDINI CHE CI SONO TRA I VARI DI FILE
def insertIntoLista(pos1,pos2,lista1,lista2,info,nomiFile):
    comparing(lista1["properties"][pos1].split(' '),lista2["properties"][pos2].split(' '),info,nomiFile)
