kuha = float(input("Anna kuhan pituus senttimetreinä: "))
if kuha < 37:
    puuttuva = 37 
    print("Kuha on", puuttuva, "cm liian lyhyt, päästä se takaisin veteen.")
else:
    print("Kuha on tarpeeksi pitkä, voit pitää sen!")
