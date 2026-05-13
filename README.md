# 05-NEDELA
### Izdevumu uzskaites projekts
Sākumā šis projekts likās kā viena liela putra ar visiem moduļiem un zariem, bet beigās izdevās uztaisīt reāli strādājošu rīku. Programma palīdz sekot līdzi tēriņiem, tos grupēt un pats galvenais - saglabāt visu tā, lai dati nekur nepazustu un būtu viegli analizējami.

### Uzstādīšana
Lai palaistu programmu savā datorā, terminālī jāizmanto šīs komandas:

Noklonē repozitoriju:
git clone https://github.com/dzilnamarta-coder/05-NEDELA.git

Ieej projekta mapē:
cd 05-NEDELA

Palaid programmu:
python3 expense_tracker/app.py

### Lietošana
Programmā viss notiek caur vienkāršu izvēlni, kur jāievada skaitļi no 1 līdz 7:

1) Pievienot izdevumu - Ievadi datus un programma tos saglabās json failā. Ja kļūdīsies formātā, programma liks ievadīt vēlreiz.

2) Parādīt visus - Apskati visu sarakstu un kopējo iztērēto summu formatētā veidā.

3) Filtrēt pēc mēneša - Atlasi datus tikai par konkrētu mēnesi, lai nav jāskatās viss garais saraksts.

4) Kopsavilkums pa kategorijām - Redzi, cik naudas kopā aiziet katrai grupai, piemēram, ēdienam vai mājoklim.

5) Dzēst izdevumu - Vari izņemt liekos ierakstus. Esmu iestrādājusi pārbaudi, lai nevarētu nejauši ierakstīt neeksistējošu numuru.

6) Eksportēt uz CSV - Saglabā visus datus failā, ko var ērti atvērt ar Excel (latviešu burti rādīsies pareizi).

7) Iziet - Droši pabeidz darbu un aizver programmu.

### Autors
Marta Dzilna