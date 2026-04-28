import csv

def main():
    # 1. Otevři soubor
    with open("programování/data.csv", encoding="utf-8") as soubor:
        data = csv.DictReader(soubor)
        
        # 2. Procházej řádky
        for r in data:
            try:
                # 3. Udělej z textu čísla
                cena = int(r["cena_kus"])
                mnozstvi = int(r["mnozstvi"])
                
                # 4. Spočti to jen, když je zaplaceno
                if r["zaplaceno"] == "TRUE":
                    celkem = cena * mnozstvi
                    print(f"Zakaznik {r['zakaznik']} zaplatil {celkem}")
            except:
                continue # Když je v číslech chyba, jdi na další řádek

main()