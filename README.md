
 # Ohjelmistotekniikan Tetris projekti
Sovelluksella voidaan pelata klassista Tetristä. Sovellus on tehty Pythonilla ja tKinterillä

## Dokumentaatio
 - [Vaatimusmäärittely](application/dokumentaatio/maarittelydokumentti.md)
 - [Arkkitehtuurikuvaus](application/dokumentaatio/graph.md)
 - [Tuntikirjanpito](application/dokumentaatio/tuntikirjanpito.md)
 - [Changelog](application/dokumentaatio/changelog.md)

## Asennus
Sovellus asennetaan suorittamalla 
```bash
poetry install
```
## Käyttöohjeet
Sovelluksen voi käynnistää suorittamalla 
```bash
poetry run invoke start
```
Muut invoke komennot löytää komennolla
```bash
poetry run invoke list
```
Tetrominoja liikutetaan nuolinäppäimilä ja pyöritetään "nuoli ylös" näppäimellä. Kovaan pudotukseen painetaan välilyöntiä.

##Pytesteistä:
En löytänyt mitään tietoa miten tehdä unittestejä pygamella tehtyyn tickellä toimivaan peliin. 
Alkutilanteen voi tarkistaa, mutta siitä eteenpäin se on lähes mahdotonta. Pahoittelen testien puutetta ja toivon että se otetaan huomioon pisteytyksessä
