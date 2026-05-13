import storage
import logic
from datetime import date, datetime

def main():
    # Ielādējam datus startā
    expenses = storage.load_expenses()

    while True:
        print("\n--- IZVĒLNE ---")
        print("1) Pievienot izdevumu")
        print("2) Parādīt visus")
        print("3) Filtrēt pēc mēneša")
        print("4) Kopsavilkums pa kategorijām")
        print("5) Dzēst izdevumu")
        print("6) Iziet")
        
        choice = input("\nIzvēlies darbību: > ").strip()

        if choice == '1':
            # 1. DATUMA PĀRBAUDE
            today = date.today().strftime("%Y-%m-%d")
            while True:
                date_input = input(f"Datums (YYYY-MM-DD) [{today}]: > ").strip()
                final_date = date_input if date_input else today
                try:
                    datetime.strptime(final_date, "%Y-%m-%d")
                    break 
                except ValueError:
                    print(f"X Kļūda: '{final_date}' nav pareizs datums!")

            # 2. KATEGORIJAS PĀRBAUDE
            while True:
                print("Kategorijas: 1) Ēdiens 2) Transports 3) Izklaide 4) Apģērbs 5) Veselība 6) Mājoklis 7) Citi")
                cat_map = {"1": "Ēdiens", "2": "Transports", "3": "Izklaide", "4": "Apģērbs", "5": "Veselība", "6": "Mājoklis", "7": "Citi"}
                cat_choice = input("Izvēlies (1-7): > ").strip()
                if cat_choice in cat_map:
                    category = cat_map[cat_choice]
                    break 
                else:
                    print(f"X Kļūda: Izvēlies no 1 līdz 7!")

            # 3. SUMMAS PĀRBAUDE
            while True:
                try:
                    amount_input = input("Summa (EUR): > ").strip()
                    amount = float(amount_input)
                    if amount > 0:
                        break
                    else:
                        print("X Kļūda: Summai jābūt virs 0!")
                except ValueError:
                    print("X Kļūda: Ievadi skaitli!")

            # 4. APRAKSTS
            description = input("Apraksts: > ").strip()

            # SAGLABĀŠANA
            new_expense = logic.create_expense(final_date, category, amount, description)
            expenses.append(new_expense)
            storage.save_expenses(expenses)
            print(f"✓ Pievienots: {final_date} | {category} | {amount:.2f} EUR")

        elif choice == '2':
            if not expenses:
                print("\nSaraksts ir tukšs!")
            else:
                print("\n--- VISI IZDEVUMI ---")
                for e in expenses:
                    print(f"{e['date']} | {e['category']} | {e['amount']:.2f} EUR | {e['description']}")
                print(f"----------------------")
                print(f"KOPĀ: {logic.sum_total(expenses):.2f} EUR")

        elif choice == '3':
            # FILTRĒŠANA
            months = logic.get_available_months(expenses)
            if not months:
                print("\nNav datu, ko filtrēt!")
                continue
            
            print("\nPieejamie mēneši:")
            for i, m in enumerate(months, 1):
                print(f"  {i}) {m}")
            
            m_choice = input("Izvēlies mēnesi (numurs): > ").strip()
            if m_choice.isdigit() and 1 <= int(m_choice) <= len(months):
                selected = months[int(m_choice)-1]
                filtered = logic.filter_by_month(expenses, selected)
                print(f"\n--- {selected} IZDEVUMI ---")
                for f in filtered:
                    print(f"{f['date']} | {f['amount']:.2f} EUR | {f['category']}")
                print(f"Kopā: {logic.sum_total(filtered):.2f} EUR ({len(filtered)} ieraksti)")
            else:
                print("X Kļūda: Nepareizs numurs!")

        elif choice == '4':
            # KOPSAVILKUMS
            summary = logic.sum_by_category(expenses)
            if not summary:
                print("\nNav datu!")
            else:
                print("\n--- KOPSAVILKUMS PA KATEGORIJĀM ---")
                for cat, total in summary.items():
                    print(f"  {cat}: {total:.2f} EUR")

        elif choice == '5':
            # DZĒŠANA (ar uzlaboto ciklu)
            if not expenses:
                print("\nNav ko dzēst!")
                continue
            
            print("\nIzdevumi:")
            for i, e in enumerate(expenses, 1):
                print(f"{i}) {e['date']} | {e['amount']:.2f} EUR | {e['description']}")
            
            while True:
                try:
                    ievade = input("\nKuru dzēst? (numurs vai 0 lai atceltu): > ").strip()
                    d_choice = int(ievade)
                    
                    if d_choice == 0:
                        print("Dzēšana atcelta.")
                        break
                    
                    if 1 <= d_choice <= len(expenses):
                        removed = expenses.pop(d_choice - 1)
                        storage.save_expenses(expenses)
                        print(f"✓ Dzēsts: {removed['description']}")
                        break
                    else:
                        print(f"X Kļūda: Numurs {d_choice} nav sarakstā. Mēģini vēlreiz!")
                except ValueError:
                    print("X Kļūda: Lūdzu, ievadi skaitli!")

        elif choice == '6':
            print("Atā! Tiksimies nākamreiz.")
            break
        else:
            print("X Kļūda: Izvēlies 1-6!")

if __name__ == "__main__":
    main()