import storage
import logic
import export  
from datetime import date, datetime

# Šī ir galvenā programma, kas apvieno visu loģiku un datu glabāšanu. 
# Tā piedāvā vienkāršu teksta izvēlni, kur lietotājs var pievienot izdevumus, skatīt tos, 
# filtrēt pēc mēneša, redzēt kopsavilkumu pa kategorijām, dzēst ierakstus un eksportēt uz CSV failu. 
# Viss tiek glabāts lokāli, izmantojot storage.py funkcijas.
def main():
    expenses = storage.load_expenses()

    # Galvenā izvēlne, kas turpina darboties, līdz lietotājs izvēlas iziet.
    while True:
        print("\n--- IZVĒLNE ---")
        print("1) Pievienot izdevumu")
        print("2) Parādīt visus")
        print("3) Filtrēt pēc mēneša")
        print("4) Kopsavilkums pa kategorijām")
        print("5) Dzēst izdevumu")
        print("6) Eksportēt uz CSV")
        print("7) Iziet")
        # Iegūst lietotāja izvēli un apstrādā to, izsaucot atbilstošās funkcijas no logic.py un storage.py.
        choice = input("\nIzvēlies darbību: > ").strip()

        # Katrs if bloks atbilst vienai izvēlei, un tajā tiek apstrādāta lietotāja ievade, 
        # veikta nepieciešamā loģika un saglabāti dati.
        if choice == '1':
            
            today = date.today().strftime("%Y-%m-%d")
            while True:
                date_input = input(f"Datums (YYYY-MM-DD) [{today}]: > ").strip()
                final_date = date_input if date_input else today
                try:
                    datetime.strptime(final_date, "%Y-%m-%d")
                    break 
                except ValueError: print(f"X Kļūda: '{final_date}' nav pareizs datums!")
            # Kategoriju izvēle ar skaitļu karti, lai būtu vieglāk ievadīt. 
            # Validācija, lai izvēlētos tikai no piedāvātajām opcijām.
            while True:
                print("Kategorijas: 1) Ēdiens 2) Transports 3) Izklaide 4) Apģērbs 5) Veselība 6) Mājoklis 7) Citi")
                cat_map = {"1": "Ēdiens", "2": "Transports", "3": "Izklaide", "4": "Apģērbs", "5": "Veselība", "6": "Mājoklis", "7": "Citi"}
                cat_choice = input("Izvēlies (1-7): > ").strip()
                if cat_choice in cat_map:
                    category = cat_map[cat_choice]
                    break 
                else: print("X Izvēlies no 1 līdz 7!")
            # Summa tiek ievadīta kā teksts, bet tiek pārveidota par skaitli, lai varētu rēķināt.
            while True:
                try:
                    amount = float(input("Summa (EUR): > ").strip())
                    if amount > 0: break
                    else: print("X Jābūt virs 0!")
                except ValueError: print("X Ievadi skaitli!")
            # Apraksts ir brīvā formā, un ja tas nav norādīts, tiek piešķirts noklusējuma teksts.
            desc = input("Apraksts: > ").strip()
            expenses.append(logic.create_expense(final_date, category, amount, desc))
            storage.save_expenses(expenses)
            print("✓ Pievienots!")
        # Parāda visus izdevumus formatētā veidā, lai būtu vieglāk lasīt, un kopējo summu.
        elif choice == '2':
            if not expenses: print("\nSaraksts ir tukšs!")
            else:
                # Formatēta izvade 
                print(f"\n{'Datums':<12} {'Summa':>10} {'Kategorija':<15} {'Apraksts'}")
                print("-" * 60)
                for e in expenses:
                    print(f"{e['date']:<12} {e['amount']:>8.2f} EUR {e['category']:<15} {e['description']}")
                print(f"------------------------------------------------------------")
                print(f"KOPĀ: {logic.sum_total(expenses):.2f} EUR")
        # Filtrē izdevumus pēc izvēlētā mēneša, parādot tikai tos, kas atbilst GGGG-MM formātam, 
        # un kopējo summu šim mēnesim.
        elif choice == '3':
            months = logic.get_available_months(expenses)
            if not months: print("\nNav datu!")
            else:
                for i, m in enumerate(months, 1): print(f"  {i}) {m}")
                m_c = input("Izvēlies mēnesi (numurs): > ").strip()
                if m_c.isdigit() and 1 <= int(m_c) <= len(months):
                    sel = months[int(m_c)-1]
                    fil = logic.filter_by_month(expenses, sel)
                    print(f"\n--- {sel} IZDEVUMI ---")
                    for f in fil: print(f"{f['date']} | {f['amount']:.2f} EUR | {f['category']}")
                    print(f"Kopā: {logic.sum_total(fil):.2f} EUR ({len(fil)} ieraksti)")
        # Kopsavilkums pa kategorijām parāda, cik kopā iztērēts katrā kategorijā, un formatē to skaidri.
        elif choice == '4':
            summary = logic.sum_by_category(expenses)
            if not summary: print("\nNav datu!")
            else:
                print("\n--- KOPSAVILKUMS PA KATEGORIJĀM ---")
                for cat, total in summary.items(): print(f"  {cat}: {total:.2f} EUR")
        # Dzēst izdevumu ļauj lietotājam izvēlēties, kuru ierakstu dzēst pēc numura, un apstiprina dzēšanu.
        elif choice == '5':
            if not expenses: print("\nNav ko dzēst!"); continue
            for i, e in enumerate(expenses, 1): print(f"{i}) {e['date']} | {e['amount']:.2f} EUR | {e['description']}")
            while True:
                try:
                    d_c = int(input("\nKuru dzēst? (numurs vai 0 lai atceltu): > "))
                    if d_c == 0: break
                    if 1 <= d_c <= len(expenses):
                        removed = expenses.pop(d_c-1)
                        storage.save_expenses(expenses)
                        print(f"✓ Dzēsts: {removed['description']}"); break
                    else: print(f"X Nav tāda numura!")
                except ValueError: print("X Ievadi ciparu!")

        # Eksportēt uz CSV ļauj lietotājam norādīt faila nosaukumu, un tad tiek izsaukta export.py funkcija, 
        # lai saglabātu izdevumus CSV formātā, kas ir saderīgs ar Excel un citiem tabulu redaktoriem.
        elif choice == '6':
            
            f_name = input("\nFaila nosaukums [izdevumi.csv]: > ").strip()
            if not f_name: f_name = "izdevumi.csv"
            
            if export.export_to_csv(expenses, f_name):
                print(f"✓ Eksportēts: {len(expenses)} ieraksti -> {f_name}")
        # Iziet beidz programmu ar draudzīgu ziņu.
        elif choice == '7':
            print("Atā!"); break
        # Ja ievade nav derīga, tiek parādīts kļūdas paziņojums, un izvēlne tiek parādīta atkārtoti.
        else:
            print("X Izvēlies 1-7!")

if __name__ == "__main__":
    main()