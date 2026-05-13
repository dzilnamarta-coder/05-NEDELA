import json # ielādējam JSON rīku
import os   # rīks failu meklēšanai

# atrodam, kur mēs vispār atrodamies datorā
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "expenses.json")

def load_expenses():
   #Šī funkcija nolasa vecos tēriņus no faila, ja tāds ir, un atgriež tos kā sarakstu. Ja nav, atgriež tukšu sarakstu.
    if not os.path.exists(FILE_PATH):
        return [] # ja faila nav, sāk ar tukšu lapu
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f) # dabūjam datus ārā
    except:
        return [] # ja kaut kas saiet grīstē, arī sākam no nulles

def save_expenses(expenses):
   #Šī funkcija visu smuki ieraksta failā, lai nekas nepazūd
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        # saglabājam tā, lai latviešu burti ir smuki un viss ir pārskatāms
        json.dump(expenses, f, indent=4, ensure_ascii=False)