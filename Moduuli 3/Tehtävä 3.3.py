sukupuoli = input("Anna sukupuolesi (nainen/mies): ").lower()
hb = int(input("Anna hemoglobiiniarvosi (g/l): "))
if sukupuoli == "nainen":
    if hb < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hb <= 175:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
if sukupuoli == "mies":
    if hb < 134:
        print("Hemoglobiinisi on alhainen.")
    elif hb <= 195:
        print("Hemoglobiinisi on normaali.")
    else:
        print("Hemoglobiinisi on korkea.")
else:
    print("Virheellinen sukupuoli.")