# PROGETTO_STAGE Authorship Attribution (Italian Version)


<html>
  <head></head>
  <body>
    <h2> Descrizione tool </h2>
    <p>
    Il progetto in questione ha lo scopo di determinare, analizzando un codice malevolo, di determinare l'autore di quel codice. <br>
    Il tool cerca di analizzare un dataset didattico, realizzato con una traduzione MIST dal codice malevolo vero e proprio. <br>
    Il tool riceve in ingresso due nomi di file (situati nella cartella 'example') nel quale analizza questi file e crea un file contenente le similarità che riscontra in entrambi i file. A questo punto vengono creati alcuni file di configurazione (per avere la garanzia che il tool funzioni correttamente non toccare i file .ini), un file denominato "output.json" e un file similarity.ini contenente le similarità più particolari tra i diversi file. <br>
    Facendo partire un'altra volta il tool cambiando i nomi dei file in modo che venga creato un ulteriore file denominato "output1.json" nel quale come prima ci saranno le similarità tra questi ultimi due file. <br>
    </p>
    <h2> Come eseguire il tool: </h2><br>
    <p>
    <pre> $ ./python3 main.py nomefile1.json nomefile2.json </pre><br>
    </p>
    <h2> Cosa crea il tool: </h2> <br>
    <p>
    <ul>
      <li>
      <b>file.ini:</b> contiene delle impostazioni per creare senza dover modificare nulla due file ("output.json" e "output1.json")<br>
      </li>
      <li>
      <b>nameFile.ini:</b> contiene delle impostazioni per avere maggiore informazioni sul file similarity.ini <br>
      </li>
      <li>
      <b>similarity.ini:</b> contiene le similarità più particolari tra i file che vengono inseriti nel tool
      </li>
      <br>
      <blockquote><b>Nota: E' possibile aprire il file similarity.ini</b></blockquote>
    </ul>
    </p>
    <blockquote><b>A causa del dataset limitato non è possibile dire chi è l'autore dei malware analizzati</b></blockquote> <br>
  </body>
</html>
