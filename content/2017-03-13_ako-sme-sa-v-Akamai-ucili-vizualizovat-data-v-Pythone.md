Title: Ako sme sa v Akamai učili vizualizovať dáta v Pythone
Date: 2017-03-13 10:49:00
Author: Sveťa Margetová
Twitter: Mandragora258
Gravatar: richard.margeta@gmail.com
About: Programátorka v Pythone/vo Swifte. Vo voľnom čase rada behám a organizujem IT akcie, workshopy a rôzne druhy pretekov.

V piatok 3. 3. 2017 sa konal v <a href="https://www.akamai.com/">Akamai Technologies</a> workshop zameraný na vizualizáciu dát v Pythone. 
Bežne v rámci PyLadies komunity pôsobím ako kouč, no v tomto prípade som bola v roli opačnej a naozaj som sa tešila, že sa môžem niečo nové z Pythonu a dátovej oblasti naučiť. 

Tešila som sa o to viac, lebo s dátami denne pracujem na projektoch v rôznych oblastiach, pracujem v <a href="http://pandas.pydata.org/">Pandas</a> a <a href="http://matplotlib.org/">Matplotlib</a> je súčasťou každého môjho importu v Jupyter notebookoch. No mala som pocit, že ho nevyužívam naplno a celkovo sa vizualizácii dát nevenujem. Väčšina mojich grafov, ktoré som si vykreslovala, boli určené iba mne, nehrala som sa s detailmi a zobrazením a ak mal byť výstup prezentovateľný koncovému užívateľovi, vždy som automaticky siahla po Reacte.

<p align="center">
<img src="https://trello-attachments.s3.amazonaws.com/52589bca65b0b14e1d004d94/581efa2dafc1d1f2ca807a35/1e2fa40962b2c74b9017821ce00bf877/table.png" />
</p>
<p align="center">
<i>Ukážka môjho bežného grafu</i>
</p>

V Akamai nám lektori ukázali, ako však s dátami (vo forme JSONu) pracovať a vizualizovať ich v podobe, v akej sú prínosné a jasne z nich informácie zrozumiteľné. Po prvotných problémoch s rôznymi operačnými systémami a verziami Pythonu sme sa hneď pustili do tvorby vizualizácií zobrazovaných vo webovom prehliadači. 

<h2>Grafy, grafy, samé grafy</h2>

Prešli sme základnými typmi grafov, ktoré vidím takmer v každej manažérskej a marketingovej prezentácii, ako napríklad:
<ol>
    <li>stĺpcový graf,</li>
    <li>koláčový graf,</li>
    <li>histogram.</li>
</ol>

Pri tvorbe grafov som zistila, že to môže byť naozaj aj zábava, je tam priestor pre programovanie, matematiku, možnosti vlastného dizajnu a podobne. Hneď ako som vykreslila jeden graf, som sa pustila do modifikácie úlohy, kedy okrem maximálnej hodnoty som chcela pridať minimálnu hodnotu a priemernú hodnotu. 

Páčilo sa mi v tomto prípade použitie <a href="https://docs.python.org/2/library/collections.html#collections.Counter">Counter()</a> - užitočná vec v Pythone. Síce moje grafické cítenie v tejto oblasti nie je bohviečo, lebo keby mne niekto pošle ružovo-fialový graf so žltou krikľavou čiarou v strede, asi dostanem z toho epileptický záchvat, na jeho vykreslenie sme nepotrebovali ani veľa kódu a páčilo sa mi jeho elegantné riešenie, kde bolo možné uplatiť napríklad:

<ul>
    <li>list comprehensions</li>
        <ul>
            <li><code>temp = enumerate([abs(j - avg) for j in n])</code></li>
        </ul>
     <li>anonymnú funkciu lambda</li>
        <ul>
            <li><code>mi = sorted(temp, key=lambda a : a[1])[0][0]</code></li>
        </ul>
     <li>for cyklom prechádzať rôznymi agregačnými funkciami</li>
        <ul>
            <li><code>for f in [min, max]:
                        mi = list(n).index(f(n))
        			    patches[mi].set_color("#283891")</code></li>
       </ul>
</ul>

<p align="center">
    <img src="https://trello-attachments.s3.amazonaws.com/52589bca65b0b14e1d004d94/581efa2dafc1d1f2ca807a35/3441474aac63ae066f05edcccdaa6b6d/rtt.png" />
</p>
<p align="center">
    <i>Maximálna, minimálna, priemerná hodnota</i>
</p>

Následne sme si ukázali ďalšie typy grafov a okrem práce v Pythone sme sa naučili aj niečo o <a href="http://searchnetworking.techtarget.com/definition/round-trip-time">RTT</a>, protokoloch a vzájomného prepojenia medzi oboma veličinami, aká je bežná hodnota v realite a kde sa približne ukazovatele pohybujú.

<p align="center">
    <img src="https://trello-attachments.s3.amazonaws.com/52589bca65b0b14e1d004d94/581efa2dafc1d1f2ca807a35/f5ed4bdf1fcefe69bc01d0dc68c193d2/rychlost.png" />
</p>
<p align="center">
    <i>Závislosť rýchlosti na RTT pre protokol U - graf 1</i>
</p>

<p align="center">
    <img src="https://trello-attachments.s3.amazonaws.com/52589bca65b0b14e1d004d94/581efa2dafc1d1f2ca807a35/352dbde10cc026af5f962deda0c0a57a/rtt_scatter.png" />
</p>
<p align="center">
    <i>Ukážka scatter grafu </i>
</p>

<p align="center">
    <img src="https://trello-attachments.s3.amazonaws.com/52589bca65b0b14e1d004d94/581efa2dafc1d1f2ca807a35/bc8a4d88e90e85840c1d99035c42bf6d/rychlost2.png" />
</p>
<p align="center">
    <i>Závislosť rýchlosti na RTT pre protokol U - graf 2</i>
</p>

Okrem iného sme zistili aj to, že rovnaký graf, z rovnakých dát, vykreslený rovnakým kódom môže vyzerať na dvoch počítačoch v závislosti od operačného systému trochu inak.

<p align="center">
    <img src="https://trello-attachments.s3.amazonaws.com/52589bca65b0b14e1d004d94/581efa2dafc1d1f2ca807a35/11f1e7f463cf620d7e57d65f9ac23c22/img.jpg" />
</p>
<p align="center">
    <i>Foto od Veroniky Gabrielovej</i>
</p>

<h2>K čomu to celé bolo dobré?</h2>

Okrem toho, že som si obnovila opäť pozitívny vzťah k vizualizácii dát, som si uvedomila, že nemusím vždy zaťažovať projekt vykresľovaním dát v JavaScripte, ale môžem priamo dáta spracovať v Jupyteri, vizualizovať v grafe, výstup si uložiť napríklad ako obrázok alebo celú HTML stránku a tú následne vložiť do existujúcej HTML šablóny v Djangu, pričom dáta mám real time aktualizované na základe zmien v databáze alebo vstupov užívateľa nad filtrami a formulármi. 

Hneď na ďalší deň som si skúsila nad reálnym projektom vykresliť top 10 krajín, v ktorých je najväčšie zastúpenie produktov s najvyššou mierou popularity s jednoduchým prevodom cez formát na percentá, alebo výpis príspevkov z RSS feedov v 5 jazykoch, indikujúci chýbajúce príspevky za daný deň a namiesto tabuľky už posielam klientovi graf plný červeno-modrých stĺpcov.

<p align="center">
    <img src="https://trello-attachments.s3.amazonaws.com/52589bca65b0b14e1d004d94/581efa2dafc1d1f2ca807a35/96a7b6221362b0f48b6f5ca4f53b681c/graf1.png" />
</p>
<p align="center">
    <i>Koláčový graf</i>
</p>

Bola by som rada, ak by bolo pokračovanie, kde by nám ukázali chalani z Akamai, ako sa z malej knižnice na prevod SQL príkazov cez Python do grafov stal využívaný framework. A samozrejme, ako je v tejto dobe in, real-time grafy. Dokým sa to nehýbe, nie je to až tak cool. 
