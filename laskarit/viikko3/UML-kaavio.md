## Monopoli, alustava luokkakaavio

```mermaid

 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" --> "1" Aloitusruutu
    Monopolipeli "1" -- "1" Aloitusruutu
    Ruutu "1" --> "1" Vankila
    Ruutu "1" -->  "3"Sattuma
    Ruutu "1" --> "2" Yhteishyvä
    Ruutu --> "4" Asema
    Ruutu --> "2" Laitokset
    Ruutu --> "18" Normaalit_kadut
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Class Normaalit_kadut{
        +func build house
        +func build hotel
    }

```
