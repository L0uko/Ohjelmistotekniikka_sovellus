## Käyttöohjeet
Sovelluksen voi käynnistää suorittamalla 
```bash
poetry run invoke start
```
Lista muista komennoista.
```bash
poetry run invoke test
poetry run invoke lint
poetry run invoke coverage-report
```
Tetriksen peliohjeet ovat yksinkertaiset:
- Käytä nuolinäppäimiä liikuttaaksesi palikoita vasemmalle ja oikealle.
- Käytä ylös-nuolta kääntääksesi palikoita.
- Käytä alas-nuolta nopeuttaaksesi palikoiden putoamista.
- Käytä välilyöntiä pudottaaksesi palikan välittömästi alas.
- Täytä vaakarivit kokonaan saadaksesi pisteitä ja poistaaksesi rivin pelialueelta.
- Peli päättyy, kun palikat saavuttavat pelialueen yläreunan.
- Pelin jälkeen sovellus näyttää pistemääräsi ja sammuu sekunnin kuluttua.