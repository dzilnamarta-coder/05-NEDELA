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

def get_available_months(expenses):
    """Atrod visus mēnešus (YYYY-MM), kuros ir ieraksti, un sakārto tos."""
    months = sorted(list(set(e['date'][:7] for e in expenses)))
    return months

def filter_by_month(expenses, year_month):
    #Atlasa tikai tos izdevumus, kas sākās ar konkrēto GGGG-MM.
    return [e for e in expenses if e['date'].startswith(year_month)]

def sum_by_category(expenses):
    #Saskaita, cik kopā iztērēts katrā kategorijā.
    summary = {}
    for e in expenses:
        cat = e['category']
        summary[cat] = summary.get(cat, 0) + e['amount']
    return summary