import os

#CREO UN FILE ULTERIORE CHE ESTRAE LE INFO PIU SIGNIFICATIVE TRA DUE FILE E ALTRI DUE FILE
def moreIstruction(listaOggetti,listaOccorrenze,info,nomiFile):

    maxValue = 4 #FILTRO AI VALORI > 4
    positionCurrent = 0
    temp = 0
    line = ""
    titleFile = ""
    lineFileAfter = ""
    #CERCO IL VALORE MASSIMO E SCRIVO PER OGNI VALORE MAGGIORE L'OGGETTO DI QUELLA PROPRIETÀ
    for i in range(0,len(listaOccorrenze)):
        if listaOccorrenze[i] > maxValue: #TROVO IL MAX
            maxValue = listaOccorrenze[i] #SOVRASCRIVO IL MAX
            positionCurrent = i #SALVO LA POS

            print("Creazione nameFile.ini...")
            with open("nameFile.ini","w") as writeIni:
                writeIni.write("Filename=1=")
                writeIni.write("Filename=-1")

            with open("nameFile.ini","r") as ReadFileIni:
                lineFileAfter = ReadFileIni.read()

            #titoli nel file da mettere nel file di similarità
            with open("file.ini","r") as ReadFileIni:
                line = ReadFileIni.read()

            if line.split(":")[3] == "0" and lineFileAfter.split("=")[1] != "-1":
                titleFile = "Nome file: " + nomiFile[0] + "\n"
                with open("nameFile.ini","w") as writeIni:
                    writeIni.write("Filename=1=")
                    writeIni.write("Filename=-1")
            else:
                with open("nameFile.ini","w") as writeIni:
                    writeIni.write("Filename=1=")
                    writeIni.write("Filename=2")
                titleFile = "Nome file: " + nomiFile[1] + "\n"

            #lettura file nameFile.ini
            with open("nameFile.ini","r") as ReadFileIni:
                lineFile = ReadFileIni.read()

            #scrivo le info di similarità tra i 4 file letti
            with open("similarity.ini","a") as outfile:
                #if line.split(":")[3] != "1"
                if lineFile.split("=")[1] == "1" and line.split(":")[3] == "0":
                    with open("nameFile.ini","w") as writeIni:
                        writeIni.write("Filename=-1=")
                        writeIni.write("Filename=-1")
                    outfile.write(titleFile)
                elif lineFile.split("=")[3] == "2" and line.split(":")[3] == "1":
                    outfile.write(titleFile)
                    with open("nameFile.ini","w") as writeIni:
                        writeIni.write("Filename=-1=")
                        writeIni.write("Filename=-1")
                outfile.write(info + ": ") #SCRIVO LA PROPRIETÀ
                outfile.write(listaOggetti[positionCurrent]) #SCRIVO L'OGGETTO
                outfile.write(" ----> ")
                outfile.write(str(maxValue)) #SCRIVO IL VALORE MASSIMO PER QUELL'OGGETTO
                outfile.write("\n")
