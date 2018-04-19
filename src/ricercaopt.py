import json
import csv
import os
from similarity import *

def comparing(lista1,lista2,info,nomiFile):
    #print("FUNZIONE COMPARING")
    #SCRITTURA CARATTERE

    #### LISTE VUOTE ###########################################################
    supporting = list() #LISTA CONTENENTE SOLO VALORI CHE SONO PRESENTI SIA IN UN FILE CHE NELL'ALTRO
    contaOccLista = list() #LISTA CONTENENTE IL NUMERO DI VOLTE RIPETUTO PER OGNI VALORE
    ############################################################################
    lunghezzaLista1 = len(lista1)
    LunghezzaTot = len(lista1) + len(lista2)
    #CONTATENA LA LISTA1 CON LISTA2
    createListLength(lunghezzaLista1,LunghezzaTot,lista1,lista2)
    ############################################################################

    #RICERCA I VALORI SE NON PRESENTI LI INSERISCE SULLA LISTA ALTRIMENTI NO
    ############################################################################
    lung = len(lista1)
    for i in range(0,lung):
        if search(lista1[i],supporting) == False: #inseriscilo
            supporting.append(lista1[i])
    ############################################################################

    LunghezzaSupporting = len(supporting)
    for i in range(0,LunghezzaSupporting):
        contaOcc(supporting[i],lista1,contaOccLista)
    #print (supporting)


    #print(contaOccLista)
    #SCRITTURA SU FILE DELLE LISTE CON LE LORO OCCORRENZE
    print("Scrittura file in output...")
    scritturaFile(supporting,contaOccLista,info)

    #OTTENGO ALTRE STATISTICHE
    print("Scrittura file tra due output...")
    moreIstruction(supporting,contaOccLista,info,nomiFile)

    #SVUOTO LE LISTE
    cleanAll(supporting,contaOccLista)

################################################################################
################################################################################
#RIPULISCO TUTTO
def cleanAll(supporting,contaOccLista):
    supporting[:] = []
    contaOccLista[:] = []
################################################################################
################################################################################
#SCRITTURA SU FILE DELLE LISTE CON LE LORO OCCORRENZE
def scritturaFile(supporting,contaOcc,info):

    with open("file.ini","r") as readIni:
        line = readIni.readline().split(':')
    line = line[1]
    #print(line)
    if line == "1":
        with open("output1.json", "a") as outfile:
                 json.dump(info + ":",outfile)
                 json.dump(supporting,outfile)
                 #json.dump("-", outfile)
                 json.dump(contaOcc, outfile)
                 outfile.write("\n")
                 return
    else:
        with open("output.json", "a") as outfile:
            #writer = csv.writer(outfile)
            #writer.writerow((supporting,contaOcc))
            json.dump(info + ":",outfile)
            json.dump(supporting,outfile)
            #json.dump(outfile)
            json.dump(contaOcc, outfile)
            outfile.write("\n")
################################################################################

################################################################################
#CONTO LE OCCORRENZE DI OGNI VALORE PRESENTE NELLA LISTA
def contaOcc(elemento,lista1,contaOccLista):
    lung = len(lista1)
    sommatore = 0
    for i in range(0,lung):
        if elemento == lista1[i]:
            sommatore += 1
    contaOccLista.append(sommatore)
################################################################################

################################################################################
#CREO LA LISTA1 CON IL COLLEGAMENTO DELLA LISTA2 SULLA LISTA1
def createListLength(len1,len2,lista1,lista2):
    j = 0
    for i in range(len1,len2):
        lista1.append(lista2[j])
        j += 1
################################################################################

################################################################################
#RICERCO ELEMENTO PRENSETE NELLA LISTA CHE STO CREANDO
def search(elemento,supporting):
    lung = len(supporting)
    for i in range(0,lung):
        if elemento == supporting[i]:
            return True
    return False
################################################################################
