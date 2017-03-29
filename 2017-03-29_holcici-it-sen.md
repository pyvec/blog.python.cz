Title: Holčičí IT sen
Date: 2017-03-29
Author: Tereza Jůzová
Gravatar: tereza.juzova1@gmail.com

About: Nedávno jsem se stala novým nadšencem Pythonu. Volné chvíle trávím na letišti a pozoruji svět z ptačí perspektivy nebo zůstávám při zemi při jízdě na longboardu.



**Jak vzniká takový holčičí IT sen?** Všechno to začalo před pár měsíci, kdy jsem objevila možnost, přihlásit se do Digitální Akademie od Czechitas. Nepřemýšlela jsem ani minutu a hned odesílala přihlášku. Nyní je konec března a celý první běh Digitální Akademie se blíží ke konci. Bude mi to celé hrozně chybět, protože jsem za ty 3 měsíce poznala skvělou partu holek, naučila se spoustu nových věcí, potkala se s úžasnými mentory a lektory a také s naší skvělou organizaci Czechitas, která pomáhá vytvářet holčičí IT sny 👸.

Můj závěrečný projekt výše zmíněného kurzu se jmenuje Czechitas wiki. Za obrovské pomoci mé skvělé mentorky Sveti, díky které jsem si zamilovala programovací jazyk **Python** a za to jí patří mé velké díky, se povedla za měsíc vytvořit první verze projektu, se kterou vás nyní seznámím.

Webová aplikace bude sloužit studentům a lektorům Czechitas jako interní wiki, pro sdílení materiálů z jednotlivých předmětů, kurzů, workshopů apod. Usnadnění komunikace a přehlednosti celého kurzu, všechny materiály budou na jednom místě. Studenti, pak mohou také sami tvořit wiki, mohou psát články o technologiích se kterými se během kurzů seznámili, další články by se mohly týkat závěrečných projektů studentů Digitální Akademie.

Uživatelé systému, jsou lektoři a studenti Czechitas. Lektor bude mít právo vytvářet jednotlivá vlákna týkající se oblastí, které vyučuje. Každé vlákno může mít několik dalších stránek a stránky pak několik dalších podstránek. Stránky a podstránky pak budou moci vytvářet jak lektoři, tak také studenti. Systém bude také propojený s kurzy na webu Czechitas a automaticky se v administraci vytvoří nové vlákno s názvem kurzu, pokud ještě vlákno neexistuje.

## Schéma postupu
![Schéma postupu]({filename}/images/schema.jpg)

## Krok za krokem
**1. Návrh datového modelu**


Základem pro tvorbu datového modelu jsou funkční požadavky aplikace (vytvořit vlákno, vložit stánku do vlákna, přihlášení, registrace, správa uživatelů, přidání souboru k předmětu, přidat komentář) a jednotlivá podstatná jména tvoří objekty a slovesa tvoří vazby mezi těmito objekty v datovém modelu.

![Datový model]({filename}/images/datovy_model.jpg)

** 2. Správa uživatelů**

* registrovaný uživatel - lektor a student
* neregistrovaný uživatel - veřejná vlákna
* admin - veškerá práva

** 3. User interface aplikace **

![UI]({filename}/images/UI-wiki.jpg)


** 4. Django ** 

Přicházíme k přípravě vývojového prostředí. V tomto kroku vytváříme projekt, superusera a nastartujeme projekt na localhostu. Dalším krokem je si otevřít projekt ve vývojovém prostředí, já jsem zvolila Atom. Pak už můžeme přejít k vytvoření modelových entit v Djangu, vycházíme z navrženého datového modelu výše. Nesmíme zapomenout se připojit k databázovému serveru, budeme pracovat s databází PostgreSQL. Je tedy potřeba mít nainstalovaný databázový server a pro správu databáze potřebujeme mít nainstalovaný pgAdmin. V pgAdmin registrujeme nový server a připojíme se k němu. Teď nám zbývá vymyslet, jak bude fungovat správa vláken a správa článků.

** 5. Úvodní dashboard **

Konečně se dostáváme k datové práci. Úvodní dashboard je rozdělen do třech částí. V první částí se nachází zobrazení celkového počtu vláken, dále pak celkový počet uživatelů a informace o přihlášeném uživateli, jeho jméno a poslední přihlášení.

Druhou částí dashboardu je tabulka s kalendářem akcí, které pořádají Czechitas. Každá akce je zároveň také nové vlákno wiki. Byla použita metoda scrapování dat z webu a zpracování dat v pandasu, na webu je vykreslený přímo pandas dataframe jako tabulka.

Třetí částí je propojení Czechitas wiki s fotkami z Instagramu, kde se ve spodní části dashboardu zobrazují fotografie, které měly nejvyšší počet likes.

## Podívejme se nyní, jak projekt vypadá :)
* Přihlášení uživatele

![Přihlášení uživatele]({filename}/images/okno_prihlaseni.jpg)
* Vlákna

![Vlákna]({filename}/images/vlakna.jpg)
* Články

![Články]({filename}/images/clanek.jpg)
* Dashboard

![Dashboard]({filename}/images/dashboard.jpg)

Tak to je ona první verze projektu po měsíci práce 🎉. Těším se na další pokračování a věřím, že z toho někdy bude plnohodnotná webová aplikace, která bude plnit svůj úkol. Jaký je tedy můj holčičí IT sen? Naučit se všechny ty super věci v Pythonu. 

