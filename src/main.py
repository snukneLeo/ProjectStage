import json
import sys
import xml.etree.ElementTree as ET
import os

name1 = ""
name2 = ""

#INSERIMENTO FILE DA RIGA DI COMANDO
while(1):
    if len(sys.argv) != 3:
        print("Error! <syntax>: main.py nomefile1.json nomefile2.json")
        exit()
    else:
        break

name1 = sys.argv[1]
name2 = sys.argv[2]


nomiTransfer = list()
nomiTransfer.append(name1)
nomiTransfer.append(name2)

#LEGGO I FILE DA RIGA DI COMANDO
with open(name1, "r") as jsonFile:
    data1 = json.load(jsonFile)

##LEGGO I FILE DA RIGA DI COMANDO
with open(name2, "r") as otherFile:
    data2 = json.load(otherFile)

#creo il file.ini per creare un ulteriore file nel caso il primo fosse
#già stato creato

line = ""

print("Creazione file.ini....")
with open("file.ini","w") as writeIni:
    if os.path.isfile("output.json"): #se esiste il file
        print("File output.json esiste...")
        writeIni.write("exists:1:") #setto a 1
        writeIni.write("title:1")
    else:
        print("File output.json esiste...")
        writeIni.write("exists:0:") #setto a 0
        writeIni.write("title:0")

#carico la struttura del file per leggere le similitudini che ci sono tra i due file
from insertList import *

for i in data1["properties"]:

    for j in data2["properties"]:

        if i == "label" and j == "label":
            insertIntoLista(i,j,data1,data2,"label",nomiTransfer)

        elif i == "file_access" and j == "file_access":
            insertIntoLista(i,j,data1,data2,"file_access",nomiTransfer)

        elif i == "file_delete" and j == "file_delete":
            insertIntoLista(i,j,data1,data2,"file_delete",nomiTransfer)

        elif i == "pe_imports" and j == "pe_imports":
            insertIntoLista(i,j,data1,data2,"pe_imports",nomiTransfer)

        elif i == "reg_read" and j == "reg_read":
            insertIntoLista(i,j,data1,data2,"reg_read",nomiTransfer)

        elif i == "reg_write" and j == "reg_write":
            insertIntoLista(i,j,data1,data2,"reg_write",nomiTransfer)

        elif i == "pe_sec_character" and j == "pe_sec_character":
            insertIntoLista(i,j,data1,data2,"pe_sec_character",nomiTransfer)

        elif i == "cmd_exec" and j == "cmd_exec":
            insertIntoLista(i,j,data1,data2,"cmd_exec",nomiTransfer)

        elif i == "api_resolv" and j == "api_resolv":
            insertIntoLista(i,j,data1,data2,"api_resolv",nomiTransfer)

        elif i == "sig_deletes_self" and j == "sig_deletes_self":
            insertIntoLista(i,j,data1,data2,"sig_deletes_self",nomiTransfer)

        elif i == "file_write" and j == "file_write":
            insertIntoLista(i,j,data1,data2,"file_write",nomiTransfer)

        elif i == "pe_sec_entropy" and j == "pe_sec_entropy":
            insertIntoLista(i,j,data1,data2,"pe_sec_entropy",nomiTransfer)

        elif i == "pe_sec_name" and j == "pe_sec_name":
            insertIntoLista(i,j,data1,data2,"pe_sec_name",nomiTransfer)

        elif i == "sig_persistence_autorun" and j == "sig_persistence_autorun":
            insertIntoLista(i,j,data1,data2,"sig_persistence_autorun",nomiTransfer)

        elif i == "sig_packer_entropy" and j == "sig_packer_entropy":
            insertIntoLista(i,j,data1,data2,"sig_packer_entropy",nomiTransfer)

        elif i == "mutex_access" and j == "mutex_access":
            insertIntoLista(i,j,data1,data2,"mutex_access",nomiTransfer)

        elif i == "sig_injection_rwx" and j == "sig_injection_rwx":
            insertIntoLista(i,j,data1,data2,"sig_injection_rwx",nomiTransfer)

        elif i == "file_read" and j == "file_read":
            insertIntoLista(i,j,data1,data2,"file_read",nomiTransfer)

        elif i == "reg_access" and j == "reg_access":
            insertIntoLista(i,j,data1,data2,"reg_access",nomiTransfer)

        elif i == "sig_copies_self" and j == "sig_copies_self":
            insertIntoLista(i,j,data1,data2,"sig_copies_self",nomiTransfer)

        elif i == "sig_dropper" and j == "sig_dropper":
            insertIntoLista(i,j,data1,data2,"sig_dropper",nomiTransfer)

        elif i == "file_drop" and j == "file_drop":
            insertIntoLista(i,j,data1,data2,"file_drop",nomiTransfer)

        elif i == "sig_stealth_file" and j == "sig_stealth_file":
            insertIntoLista(i,j,data1,data2,"sig_stealth_file",nomiTransfer)

        elif i == "str" and j == "str":
            insertIntoLista(i,j,data1,data2,"str",nomiTransfer)
