import csv

def main():
    with open ("programování/data.csv", encoding="utf-8") as soubor:
        data = csv.DictReader(soubor)

        for r in data:
            try:     
                cena = int(r["cena_kus"])
                mnozstvi = int(r["mnozstvi"])
                if r["zaplaceno"] ==  "TRUE":
                    celkem = cena * mnozstvi
                    print(f"Zákaznik {r['zakaznik']} zaplatil {celkem}")
            except:
                continue
main()