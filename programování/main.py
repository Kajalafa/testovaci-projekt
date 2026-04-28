import csv  # Nahraje knihovnu pro práci s tabulkami (.csv soubory)

def main():  # Definice hlavní funkce (krabice, kde je tvůj kód)
    # Otevře soubor; "utf-8" zajistí, že české znaky (ěščřž) nebudou rozsypaný čaj
    with open("programování/data.csv", encoding="utf-8") as soubor:
        
        # Udělá z tabulky seznam slovníků (můžeš používat názvy sloupců v závorkách)
        data = csv.DictReader(soubor)
        
        for r in data:  # Prochází řádek po řádku celou tabulku (r = aktuální řádek)
            try:  # "Zkus tohle" -> pokud se něco nepovede, program nespadne
                
                # Vytáhne text ze sloupce a změní ho na celé číslo (aby se s ním dalo počítat)
                cena = int(r["cena_kus"])
                mnozstvi = int(r["mnozstvi"])
                
                # Podmínka: Spočítá a vypíše to jen tehdy, pokud je ve sloupci 'zaplaceno' text TRUE
                if r["zaplaceno"] == "TRUE":
                    celkem = cena * mnozstvi  # Klasické násobení
                    
                    # f-string: vypíše text, do kterého vloží hodnoty z proměnných v závorkách {}
                    print(f"Zakaznik {r['zakaznik']} zaplatil {celkem}")
            
            except:  # Pokud řádek obsahuje chybu (třeba chybějící číslo), skočí sem
                continue  # Přeskočí chybný řádek a jde hned na další

main()  # Spustí celý program (bez tohoto řádku by se nic nestalo)