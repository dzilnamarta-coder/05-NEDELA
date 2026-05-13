# Mana darba gaita

### Pirmie soļi 
Šodien man gāja raibi. Sākumā bija liela putra ar termināli un VS Code, nekas negribēja vērties vaļā, bet beigās izdevās visu savienot ar GitHub. Varbūt šis ir iemesls tam ka biju paņēmusi pauzi, un dažas detaļas " Izkrita no galvas" ;D

### Darba gaita
- Uzrakstīju projekta plānu, lai pati saprastu, ko gribu uztaisīt.
- Izveidoju mapju struktūru un pirmos failus.
- Sataisīju `storage.py`, lai dati tiešām saglabātos tajā JSON failā un nekur nepazustu.
- Uztaisīju `logic.py`, kur programma māk saskaitīt naudu un sataisīt smukus ierakstus.
- Dabūju gatavu `app.py` 
- Pārbaudiju visu, sanaca ievadit un izveidojas 'expenses.jason' fails, bet atradu kļūdu, ka ja ieraksta pie datuma ciparu 1 , programma to akceptē, jaizlabo šis 

### 1 KĻUDA

Izvēlies: > 1
Datums (YYYY-MM-DD) [2026-05-13]: > 1
X Kļūda: '1' nav pareizs datums! Raksti GGGG-MM-DD.
Datums (YYYY-MM-DD) [2026-05-13]: > 

- izlaboju kļūdu, papildināju app.py kodu ar speciālu pārbaudes ciklu, izmantojot datetime.strptime funkciju. Tagad programma strādā droši un neļauj turpināt darbu, kamēr lietotājs nav ievadījis datumu pareizā formātā (GGGG-MM-DD), kas nodrošina, ka manā expenses.json failā visi dati vienmēr būs kārtībā 

Izvēlies: > 1
Datums (YYYY-MM-DD) [2026-05-13]: > 1
X Kļūda: '1' nav pareizs datums! Raksti GGGG-MM-DD.
Datums (YYYY-MM-DD) [2026-05-13]: > 

### 2 KĻUDA - atklāju velvienu kļūdu 
Izvēlies: > 1
Datums (YYYY-MM-DD) [2026-05-13]: > 2026-05-01
Kategorija: 1) Ēdiens 2) Transports 3) Izklaide 4) Apģērbs 5) Veselība 6) Mājoklis 7) Citi
Izvēlies (1-7): > 10
Summa (EUR): > 

- izlaboju kļūdu - pamanīju, ka pie kategorijām varēju ierakstīt jebko, piemēram, skaitli 10, un programma neiebilda, tāpēc es pieliku vēl vienu while ciklu un speciālu pārbaudi pret savu kategoriju sarakstu. Tagad programma ir 'stūrgalvīga' un neļauj tikt tālāk pie summas ievades, kamēr neesmu ierakstījusi tieši kādu no cipariem no 1 līdz 7, kas nozīmē, ka manos datos vairs nebūs nekādu kļūdu un viss būs smuki sakārtots pa īstajām kategorijām

Izvēlies: > 1
Datums (YYYY-MM-DD) [2026-05-13]: > 2026-01-10
Kategorija: 1) Ēdiens 2) Transports 3) Izklaide 4) Apģērbs 5) Veselība 6) Mājoklis 7) Citi
Izvēlies (1-7): > 10
X Kļūda: '10' nav sarakstā. Izvēlies 1-7!
Kategorija: 1) Ēdiens 2) Transports 3) Izklaide 4) Apģērbs 5) Veselība 6) Mājoklis 7) Citi
Izvēlies (1-7): > 





### 3. velejos mainit funkciju - nepatika ja summa ir kļūdanaia viss jasak no jauna tapec nacas to labot

Izvēlies: > 1
Datums (YYYY-MM-DD) [2026-05-13]: > 2026-01-01
Kategorija: 1) Ēdiens 2) Transports 3) Izklaide 4) Apģērbs 5) Veselība 6) Mājoklis 7) Citi
Izvēlies (1-7): > 4
Summa (EUR): > -1.5
X Kļūda: Summai jābūt pozitīvai (virs 0)!
Summa (EUR): > 2.50
Apraksts: > Zeķes
✓ Pievienots: 2026-01-01 | Apģērbs | 2.50 EUR | Zeķes

atrisināju kļūdu, ieliekot summas prasīšanu vēl vienā while ciklā. Tagad, ja es ierakstu nepareizu summu, programma vienkārši paprasa to vēlreiz, bet neizdzēš to, ko es jau biju sarakstījusi iepriekšējos soļos.












### Darba gaita turpinājums
- Šajā posmā es pabeidzu 3.soli, pievienojot logic.py failam funkcijas, kas māk atlasīt pieejamos mēnešus, filtrēt tēriņus un sagrupēt tos pa kategorijām, savukārt app.py papildināju ar jaunu izvēlni, lai to visu varētu ērti apskatīt. 
- Pabeidzot 3. soli, es pamanīju kaitinošu kļūdu dzēšanas funkcijā — ja es nejauši ierakstīju numuru, kura nav sarakstā (piemēram, 7 vai 10), programma mani vienkārši izmeta atpakaļ uz galveno izvēlni un viss bija jāsāk no jauna. Lai to izlabotu, es izmainīju kodu un ieliku dzēšanu while ciklā, tāpēc tagad programma ir daudz gudrāka un kļūdas gadījumā nevis izslēdzas, bet gan parāda brīdinājumu un turpat uzreiz prasa ievadīt numuru vēlreiz. Tas padara lietošanu daudz ērtāku, jo es varu mēģināt, kamēr trāpu pareizo skaitli vai izvēlos 0, lai atceltu, nevis katru reizi skraidu cauri visai izvēlnei.

### Kļūda

--- IZVĒLNE ---
1) Pievienot izdevumu
2) Parādīt visus
3) Filtrēt pēc mēneša
4) Kopsavilkums pa kategorijām
5) Dzēst izdevumu
6) Iziet

Izvēlies: > 5
1) 2026-04-13 | 13.00 EUR | Internets
2) 2026-01-01 | 1.50 EUR | Bulciņa
3) 2026-01-01 | 2.50 EUR | Zeķes
4) 2026-05-13 | 16.00 EUR | Zāles kaklam

Kuru dzēst? (numurs vai 0 lai atceltu): > 7
X Nepareizs numurs!

--- IZVĒLNE ---
1) Pievienot izdevumu
2) Parādīt visus
3) Filtrēt pēc mēneša
4) Kopsavilkums pa kategorijām
5) Dzēst izdevumu
6) Iziet

Izvēlies darbību: > 5

Izdevumi:
1) 2026-04-13 | 13.00 EUR | Internets
2) 2026-01-01 | 1.50 EUR | Bulciņa
3) 2026-01-01 | 2.50 EUR | Zeķes
4) 2026-05-13 | 16.00 EUR | Zāles kaklam

Kuru dzēst? (numurs vai 0 lai atceltu): > 10
X Kļūda: Numurs 10 nav sarakstā. Mēģini vēlreiz!

 
### Grūtības:
Visgrūtāk gāja ar Git un zariem (branches). Pāris reizes faili nosvītrojās un pazuda, bet beigās iemācījos tos atdabūt un visu pareizi nosūtīt uz GitHub.

