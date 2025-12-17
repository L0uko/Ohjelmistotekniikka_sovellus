## Arkkitehtuurikuvaus

### Rakenne

Koodi on jaettu kolmeen tiedostoon:
-  main.py, mikä suorittaa sovelluksen käynnistämisen ja ei sisällä logiikkaa, vaan määrittelee tärkeitä muuttujia ja kutsuu sovelluslogiikan ja käyttöliittymän.
- gameloop.py hoitaa pelisilmukan ja ajastuksen.
- map.py hoitaa kartan ylläpidon ja luo kartta-olion
- tetromino.py hoitaa putoavan tetromino-olion luomisen ja hallinnoimisen.
- game.py hoitaa loput sekalaiset toiminnot.
- userinterface.py hoitaa kentän ja palikoiden piirtämisen.


### Luokkakaavio

```mermaid
classDiagram
Loop --> Game: 
Game --> Map: 
Game --> UI: 
Game --> Tetromino: 
Tetromino --> Map: 

```

