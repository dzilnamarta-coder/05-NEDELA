# Mans izdevumu izsekotāja plāns

## A. Kas šī ir par programmu
Tā ir vienkārša programma terminālī, kur es varu ierakstīt, kur un cik daudz naudas esmu iztērējusi. Programma man palīdzēs saglabāt šos tēriņus, sadalīt tos pa kategorijām (piemēram, ēdiens, rēķini) un beigās to visu varēs dabūt ārā kā CSV failu, lai apskatītos Excelī. Viss smuki saglabāsies `expenses.json` failā, lai nekas nepazūd, kad es aizveru VS Code.

## B. Kā izskatīsies mani dati
Es visus tēriņus glabāšu sarakstā, kur katrs ieraksts būs kā maza vārdnīciņa. Izskatīsies apmēram šādi:
[
  {
    "date": "2024-05-13",
    "amount": 5.50,
    "category": "Kafija",
    "description": "Rīta kafija benzīntankā"
  }
]

## C. Mani koda faili (Moduļi)
Lai viss nebūtu vienā lielā putrā, es sadalīšu kodu 4 failos:
1. `app.py` – Šī būs galvenā izvēlne ar cipariņiem 1, 2, 3... Šeit programma "runāsies" ar lietotāju (ar print un input).
2. `storage.py` – Šis fails atbildēs tikai par vienu lietu: paņemt datus no JSON faila un ierakstīt atpakaļ JSON failā.
3. `logic.py` – Šeit būs programmas "smadzenes". Te es rēķināšu summas un meklēšu tēriņus pa mēnešiem.
4. `export.py` – Šis fails pratīs maniem datiem uztaisīt CSV eksportu.

## D. Kā tas reāli strādās
1. **Ja viss sanāk:** Es gribu pievienot tēriņu. Programma man prasa datumu, summu, kategoriju. Es ievadu, viņa saglabā failā un pasaka "Tēriņš pievienots!".
2. **Ja es kļūdos:** Es netīšām summas vietā uzrakstu vārdu "pieci". Programma nenobruks, bet vienkārši pateiks "Lūdzu, ievadi normālu ciparu!" un prasīs vēlreiz.

## E. Kas notiks neparastās situācijās (Robežgadījumi)
1. **Nav faila:** Kad pirmo reizi atvēršu programmu, faila `expenses.json` vēl nebūs. Programma nesabīsies, bet vienkārši sāks darbu ar tukšu sarakstu `[]`.
2. **Nav ko rādīt:** Ja gribēšu apskatīt tēriņus, bet vēl neko neesmu pievienojusi, programma pateiks "Tavs saraksts pagaidām ir tukšs!".
3. **Nepareiza dzēšana:** Ja es gribēšu izdzēst 10. tēriņu, bet man ir tikai trīs, programma pateiks "Tāda tēriņa nemaz nav!".