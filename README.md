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
* Käyttäjä voi tarkastella treenin kirjaamista ja valita muutamasta valmiiksi asetetusta liikkeestä, mitä hän on suorittanut treenissään. Huomaa, että käyttäjä ei voi vielä kirjata treenejään.
* Siirtymällä sivulle /add_set, käyttäjä voi tarkastella alustavaa tapaa sarjojen lisäämiseen.

Ohjeita sovelluksen käyttämiseen:

* Käyttääksesi sovellusta sinun on kloonattava repositorio omalle tietokoneellesi.
* Tietokoneellasi tulee olla asennettuna PostreSQL-tietokanta ja sinne tulee olla lisättynä repositoriosta löytyvän schema.sql tiedoston mukainen users-taulu. Muita tauluja ei ole vielä tarvetta lisätä.
* Kloonatusta hakemistosta tulee löytyä Python virtuaaliympäristö sekä flask-kirjasto. Lisäksi on asennettava seuraavat kirjastot: flask-sqlalchemy ja psycopg2
* Hakemistoon on lisättävä .env -tiedosto, jossa on määritelty tietokanta seuraavasti: DATABASE_URL=postgresql:///(lisää tietokannan nimi) sekä salainen avain: SECRET_KEY=(lisää salainen avain)
