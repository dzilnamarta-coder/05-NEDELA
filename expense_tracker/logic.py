def sum_total(expenses):
    #Šī funkcija vienkārši saskaita visu naudu kopā
    total = 0
    for e in expenses:
        total += e['amount'] # ejam cauri sarakstam un pieskaitām katru summu
    return total

def create_expense(date, category, amount, description):
    #Šī funkcija paņem lietotāja teikto un uztaisa smuku vārdnīcu
    return {
        "date": date,
        "category": category,
        "amount": float(amount), # pārvēršam tekstu par skaitli, lai var rēķināt
        "description": description if description else "Nav apraksta"
    }