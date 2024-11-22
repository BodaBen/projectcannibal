def validstate(k_bal, v_bal, k_jobb, v_jobb, c):
    "ellenőrzi, hogy az adott pillanatban az állapot érvényes-e"
    if k_bal < 0 or v_bal < 0 or k_jobb < 0 or v_jobb < 0:
        return False
    if (k_bal > v_bal + c and v_bal > 0) or (k_jobb > v_jobb + c and v_jobb > 0):
        return False
    return True

def getstates (state, c):
    k_bal, v_bal, k_jobb, v_jobb, csonak = state
    allapot_valtozas = []
    if csonak == "bal":  # A csónak a bal parton van
        for k_in_csonak in range(3):  # kannibálok számának meghatározássa
            for v_in_csonak in range(3 - k_in_csonak):  # vegetáriánusok száma a kannibálokat figyelembe véve
                if k_in_csonak + v_in_csonak > 0 and k_in_csonak + v_in_csonak <= 2:  # A csónak kapacitása
                    new_k_bal = k_bal - k_in_csonak
                    new_v_bal = v_bal - v_in_csonak
                    new_k_jobb = k_jobb + k_in_csonak
                    new_v_jobb = v_jobb + v_in_csonak
                    if validstate(new_k_bal, new_v_bal, new_k_jobb, new_v_jobb, c):
                        allapot_valtozas.append((new_k_bal, new_v_bal, new_k_jobb, new_v_jobb, "jobb"))
    else:  # A csónak a jobb parton van
        for k_in_csonak in range(3):  # kannibálok számának meghatározása: 0, 1 vagy 2
            for v_in_csonak in range(3 - k_in_csonak):  # 0, 1, vagy 2 vegetáriánus
                if k_in_csonak + v_in_csonak > 0 and k_in_csonak + v_in_csonak <= 2:  # A csónak kapacitása
                    new_k_bal = k_bal + k_in_csonak
                    new_v_bal = v_bal + v_in_csonak
                    new_k_jobb = k_jobb - k_in_csonak
                    new_v_jobb = v_jobb - v_in_csonak
                    if validstate(new_k_bal, new_v_bal, new_k_jobb, new_v_jobb, c):
                        allapot_valtozas.append((new_k_bal, new_v_bal, new_k_jobb, new_v_jobb, "bal"))
    return allapot_valtozas


def kidolgozas (c=1):
    # A feladat megoldása, ha az erőfölény (C) = 1
    kezdo_allapot = (3, 3, 0, 0, "bal") 
    cel_allapot = (0, 0, 3, 3, "jobb") # Ez lenne a cél: 3 kannibál és 3 vegetáriánus a jobb parton 
    vizsgalt_utak = set() # Ez a tömb azért kell, hogy ne hajtsuk végre ugyanazt az utat kétszer
    queue = [(kezdo_allapot, [])]  # Lista mint sor: (jelenlegi állapot, útvonal)

    while queue:
        jelen_allapot, utvonal = queue.pop(0)  # Az első elemet vesszük ki (FIFO)
        if jelen_allapot in vizsgalt_utak:
            continue
        vizsgalt_utak.add(jelen_allapot)
        
        if jelen_allapot == cel_allapot:
            return utvonal + [jelen_allapot]
        
        for kov_allapot in getstates(jelen_allapot, c):
            queue.append((kov_allapot, utvonal + [jelen_allapot]))
    
    return None

megoldas = kidolgozas()
if megoldas:
    print("Megoldás lépései:")
    for i, step in enumerate(megoldas):
        print(f"Lépés {i}: Kannibálok (bal parton): {step[0]}, Vegetáriánusok (bal parton): {step[1]}, "
              f"Kannibálok (jobb parton): {step[2]}, Vegetáriánusok (jobb parton): {step[3]}, Csónak: {step[4]}")
else:
    print("Nincs megoldás.")

