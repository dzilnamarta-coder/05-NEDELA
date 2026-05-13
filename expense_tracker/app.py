import storage
import logic
from datetime import date, datetime

def main():
    expenses = storage.load_expenses()

    while True:
        print("\n1) Pievienot izdevumu")
        print("2) Parādīt izdevumus")
        print("3) Iziet")
        
        choice = input("\nIzvēlies: > ").strip()

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
                    print(f"X Kļūda: '{final_date}' nav pareizs datums! Raksti GGGG-MM-DD.")

            # 2. KATEGORIJAS PĀRBAUDE
            while True:
                print("Kategorija: 1) Ēdiens 2) Transports 3) Izklaide 4) Apģērbs 5) Veselība 6) Mājoklis 7) Citi")
                cat_map = {
                    "1": "Ēdiens", "2": "Transports", "3": "Izklaide", 
                    "4": "Apģērbs", "5": "Veselība", "6": "Mājoklis", "7": "Citi"
                }
                cat_choice = input("Izvēlies (1-7): > ").strip()
                if cat_choice in cat_map:
                    category = cat_map[cat_choice]
                    break 
                else:
                    print(f"X Kļūda: '{cat_choice}' nav sarakstā. Izvēlies 1-7!")

            # 3. SUMMAS IEVADE (Šis tev trūka!)
            while True:
                try:
                    amount_input = input("Summa (EUR): > ").strip()
                    amount = float(amount_input)
                    
                    if amount > 0:
                        break # Ja summa ir lielāka par 0, viss super, ejam tālāk!
                    else:
                        print("X Kļūda: Summai jābūt pozitīvai (virs 0)!")
                except ValueError:
                    print("X Kļūda: Ievadi skaitli (piemēram, 12.50)!")

            # 4. APRAKSTA IEVADE (Arī šis trūka!)
            description = input("Apraksts: > ").strip()

            # 5. SAGLABĀŠANA (Tagad Python zinās, kas ir amount un description)
            new_expense = logic.create_expense(final_date, category, amount, description)
            expenses.append(new_expense)
            storage.save_expenses(expenses)
            
            print(f"✓ Pievienots: {final_date} | {category} | {amount:.2f} EUR | {description}")

        elif choice == '2':
            if not expenses:
                print("\nSaraksts ir tukšs!")
            else:
                print("\n--- VISI IZDEVUMI ---")
                for e in expenses:
                    print(f"{e['date']} | {e['category']} | {e['amount']:.2f} EUR | {e['description']}")
                
                total = logic.sum_total(expenses)
                print(f"----------------------")
                print(f"KOPĀ: {total:.2f} EUR")

        elif choice == '3':
            print("Uz redzēšanos!")
            break
        else:
            print("X Kļūda: Izvēlies 1, 2 vai 3!")

if __name__ == "__main__":
    main()