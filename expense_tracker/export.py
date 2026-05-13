import csv

def export_to_csv(expenses, filename="izdevumi.csv"):
    # Eksportē izdevumu sarakstu uz CSV failu, izmantojot utf-8-sig kodējumu, lai Excel pareizi rādītu latviešu burtus.
  
    if not filename.endswith(".csv"):
        filename += ".csv"

    headers = ["Datums", "Kategorija", "Summa (EUR)", "Apraksts"]

    try:
        with open(filename, mode="w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            for e in expenses:
                writer.writerow([e['date'], e['category'], e['amount'], e['description']])
        return True
    except Exception as e:
        print(f"X Kļūda eksportējot: {e}")
        return False