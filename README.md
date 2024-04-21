# Treenipäiväkirja

Sovelluksen avulla käyttäjä voi pitää kirjaa kuntosalitreeneistään ja seurata omaa kehitystään. Jokainen käyttäjä on joko peruskäyttäjä tai ylläpitäjä.

Sovelluksen suunniteltuja ominaisuuksia ovat:

* Käyttäjä voi luoda uuden tunnuksen sekä kirjautua sisään ja ulos.
* Käyttäjä voi kirjata sovellukseen, milloin on suorittanut treenin, mitä liikkeitä treeniin kuului, montako sarjaa sekä toistoa kussakin liikkeessä suoritettiin ja millä painoilla sarjat tehtiin.
* Käyttäjä voi halutessaan myös ilmoittaa kuinka raskaalta kukin sarja tuntui asteikolla 1-10.
* Käyttäjä voi jälkikäteen tarkastella ja muokata kirjaamiaan treenejä.
* Käyttäjä näkee kirjaamaansa tietoon pohjautuvia erilaisia tilastoja, esimerkiksi kuinka usein hän on treenannut, ja mikä on hänen arvioitu maksimikuormansa kussakin liikkeessä.
* Käyttäjän on myös mahdollista seurata miten hän vertautuu muihin sovelluksen käyttäjiin.
* Ylläpitäjä voi lisätä valittavissa olevia harjoitteluliikkeitä. Lisätessään treenin peruskäyttäjä siis valitsee valmiina olevalta listalta, mitä liikkeitä hän suoritti.

Tällä hetkellä sovelluksen ominaisuuksia ovat:

* Käyttäjä voi luoda uuden tunnuksen ja kirjautua sisään sekä ulos.
* Käyttäjä voi luoda uuden treenin sekä lisätä treeniin sarjoja yllä kuvatulla tavalla, kirjaukset tallentuvat tietokantaan. Huomaa, että käyttäjällä ei ole vielä mahdollisuutta tarkastella sovelluksessa kirjaamiaan treenejä.

Ohjeita sovelluksen käyttämiseen:

* Käyttääksesi sovellusta sinun on kloonattava repositorio omalle tietokoneellesi.
* Hakemistoon on lisättävä .env -tiedosto, jossa on määritelty tietokanta seuraavasti: DATABASE_URL=postgresql:///(lisää tietokannan nimi tähän) sekä salainen avain: SECRET_KEY=(lisää salainen avain tähän)
* Seuraavilla komennoilla aktivoit python-virtuaaliympäristön sekä asennat sovelluksen riippuvuudet:
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r ./requirements.txt
* Komennolla $ psql < schema.sql määrität sovelluksen vaatiman tietokannan
* Sovellus käynnistyy komennolla $ psql < schema.sql
