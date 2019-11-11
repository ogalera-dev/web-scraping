# web-scraping

##Descripció
Aquesta pràctica s'ha realitzat com a exercici per l'assignatura de *Tipologia i cicle de vida de les dades* del màster en *ciència de dades* per la *Universitat Oberta de Catalunya (UOC)*. 

##Membres de l'equip
Aquesta pràctica s'ha realitzat individualment per l'alumne Òscar Galera i Alfaro.


##Fitxers de codi.
###Scraping:
* **src/main.py**: Punt d'entra al programa, inicia el procés de *scraping* i que està configurat per descarregar totes les dades descrites a la memòria i guardar-les en el directori */data*.
* **src/NBAHistoryScraper.py**: Conté la lògica que s'encarrega de descarregar les dades (del web https://www.basketball-reference.com/) estadístiques i completes de tots els jugadors de la història de la NBA.
* **src/PlayersPageScraper.py**: Conté la lògica que s'encarrega de descarregar i processar la informació dels jugadors i demana al mòdul PlayerPageScraper que descarregui i processi les dades estadístiques de cada jugador.
* **src/PlayerPageScraper.py**: Conté la lògica que s'encarrega de descarregar i processar la informació estadística de cada jugador en cada temporada i de calcular els seus valors totals al llarg de la seva carrera professional.

###Preguntes i respostes:
* **usa-map/src/main.py**: Punt d'entrada als diferents testos de les dades.
* **usa-map/src/MapPinter.py**: Conté la lògica per dibuixar un mapa de calor dels estats units d'Amèrica a partir del nom dels equips de la NBA i un conjunt de valors.

##Bibliografia emprada:
Subirats, L., Calvo, M. (2018). Web Scraping. Editorial UOC.
Masip, D. EL lenguaje Python. Editorial UOC.
Lawson, R. (2015). Web Scraping with PYthon. Packt Publishing Lts. Chapter 2. Scraping the Data.