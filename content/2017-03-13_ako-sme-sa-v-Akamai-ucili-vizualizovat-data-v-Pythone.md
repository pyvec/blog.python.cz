Title: Ako sme sa v Akamai učili vizualizovať dáta v Pythone
Date: 2017-03-13 10:49:00
Author: Sveťa Margetová
Twitter: Mandragora258
Gravatar: richard.margeta@gmail.com
About: Programátorka v Pythone/vo Swifte. Vo voľnom čase rada behám a organizujem IT akcie, workshopy a rôzne druhy pretekov.

V piatok 3. 3. 2017 sa konal v [Akamai
Technologies](https://www.akamai.com/) workshop zameraný na vizualizáciu
dát v Pythone. Bežne v rámci PyLadies komunity pôsobím ako kouč, no v
tomto prípade som bola v roli opačnej a naozaj som sa tešila, že sa
môžem niečo nové z Pythonu a dátovej oblasti naučiť. Tešila som sa o to
viac, lebo s dátami denne pracujem na projektoch v rôznych oblastiach,
pracujem v [Pandas](http://pandas.pydata.org/) a
[Matplotlib](http://matplotlib.org/) je súčasťou každého môjho importu v
Jupyter notebookoch. No mala som pocit, že ho nevyužívam naplno a
celkovo sa vizualizácii dát nevenujem. Väčšina mojich grafov, ktoré som
si vykreslovala, boli určené iba mne, nehrala som sa s detailmi a
zobrazením a ak mal byť výstup prezentovateľný koncovému užívateľovi,
vždy som automaticky siahla po Reacte.

![Ukážka môjho bežného grafu]({static}/images/table.png)
Ukážka môjho bežného grafu

V Akamai nám lektori ukázali, ako však s dátami (vo forme JSONu)
pracovať a vizualizovať ich v podobe, v akej sú prínosné a jasne z nich
informácie zrozumiteľné. Po prvotných problémoch s rôznymi operačnými
systémami a verziami Pythonu sme sa hneď pustili do tvorby vizualizácií
zobrazovaných vo webovom prehliadači.

![Všichni z workshopu]({static}/images/94849416-0963-11e7-8616-ca8148e71dab.jpg)
Foto od Veroniky Gabrielovej

## Grafy, grafy, samé grafy

Prešli sme základnými typmi grafov, ktoré vidím takmer v každej
manažérskej a marketingovej prezentácii, ako napríklad:

1.  stĺpcový graf,
2.  koláčový graf,
3.  histogram.

Pri tvorbe grafov som zistila, že to môže byť naozaj aj zábava, je tam
priestor pre programovanie, matematiku, možnosti vlastného dizajnu a
podobne. Hneď ako som vykreslila jeden graf, som sa pustila do
modifikácie úlohy, kedy okrem maximálnej hodnoty som chcela pridať
minimálnu hodnotu a priemernú hodnotu. Páčilo sa mi v tomto prípade
použitie
[Counter()](https://docs.python.org/2/library/collections.html#collections.Counter)
- užitočná vec v Pythone. Síce moje grafické cítenie v tejto oblasti nie
je bohviečo, lebo keby mne niekto pošle ružovo-fialový graf so žltou
krikľavou čiarou v strede, asi dostanem z toho epileptický záchvat, na
jeho vykreslenie sme nepotrebovali ani veľa kódu a páčilo sa mi jeho
elegantné riešenie, kde bolo možné uplatiť napríklad:

-   list comprehensions

    ```python
    temp = enumerate([abs(j - avg) for j in n])
    ```

-   anonymnú funkciu lambda

    ```python
    mi = sorted(temp, key=lambda a : a[1])[0][0]
    ```

-   for cyklom prechádzať rôznymi agregačnými funkciami

    ```python
    for f in [min, max]:
        mi = list(n).index(f(n))
        patches[mi].set_color("#283891")
    ```

![Maximálna, minimálna, priemerná hodnota]({static}/images/rtt.png)
Maximálna, minimálna, priemerná hodnota

Následne sme si ukázali ďalšie typy grafov a okrem práce v Pythone sme
sa naučili aj niečo o
[RTT](http://searchnetworking.techtarget.com/definition/round-trip-time),
protokoloch a vzájomného prepojenia medzi oboma veličinami, aká je bežná
hodnota v realite a kde sa približne ukazovatele pohybujú.

![Závislosť rýchlosti na RTT pre protokol U - graf 1]({static}/images/rychlost.png)
Závislosť rýchlosti na RTT pre protokol U - graf 1

![Ukážka scatter grafu]({static}/images/rtt_scatter.png)
Ukážka scatter grafu

![Závislosť rýchlosti na RTT pre protokol U - graf 2]({static}/images/rychlost2.png)
Závislosť rýchlosti na RTT pre protokol U - graf 2

Okrem iného sme zistili aj to, že rovnaký graf, z rovnakých dát,
vykreslený rovnakým kódom môže vyzerať na dvoch počítačoch v závislosti
od operačného systému trochu inak.

![Foto od Veroniky Gabrielovej]({static}/images/img.jpg)
Foto od Veroniky Gabrielovej

![Darí sa!]({static}/images/94846086-0963-11e7-8268-a8d338c72990.jpg)
Foto od Veroniky Gabrielovej

## K čomu to celé bolo dobré?

Okrem toho, že som si obnovila opäť pozitívny vzťah k vizualizácii dát,
som si uvedomila, že nemusím vždy zaťažovať projekt vykresľovaním dát v
JavaScripte, ale môžem priamo dáta spracovať v Jupyteri, vizualizovať v
grafe, výstup si uložiť napríklad ako obrázok alebo celú HTML stránku a
tú následne vložiť do existujúcej HTML šablóny v Djangu, pričom dáta mám
real time aktualizované na základe zmien v databáze alebo vstupov
užívateľa nad filtrami a formulármi. Hneď na ďalší deň som si skúsila
nad reálnym projektom vykresliť top 10 krajín, v ktorých je najväčšie
zastúpenie produktov s najvyššou mierou popularity s jednoduchým
prevodom cez formát na percentá, alebo výpis príspevkov z RSS feedov v 5
jazykoch, indikujúci chýbajúce príspevky za daný deň a namiesto tabuľky
už posielam klientovi graf plný červeno-modrých stĺpcov.

![Koláčový graf]({static}/images/graf1.png)
Koláčový graf

Bola by som rada, ak by bolo pokračovanie, kde by nám ukázali chalani z
Akamai, ako sa z malej knižnice na prevod SQL príkazov cez Python do
grafov stal využívaný framework. A samozrejme, ako je v tejto dobe in,
real-time grafy. Dokým sa to nehýbe, nie je to až tak cool.

