def validstate(k_bal, v_bal, k_jobb, v_jobb, c):
    "ellenőrzi, hogy az adott pillanatban az állapot érvényes-e"
    if k_bal < 0 or v_bal < 0 or k_jobb < 0 or v_jobb < 0:
        return False
    if (k_bal > v_bal + c and v_bal > 0) or (k_jobb > v_jobb + c and v_jobb > 0):
        return False
    return True

def getstates (state, c):
    """
    Generálja a lehetséges következő állapotokat egy adott állapotból.
    Figyelembe veszi, hogy a csónakban utazók a túlsó parton kiszállnak.
    """
    k_bal, v_bal, k_jobb, v_jobb, csonak = state
    allapot_valtozas = []
    if csonak == "bal":  # A csónak a bal parton van
        for k_in_csonak in range(3):  # kannibálok számának meghatározássa
            for v_in_csonak in range(3 - c_in_csonak):  # vegetáriánusok száma a kannibálokat figyelembe véve
                if k_in_csonak + v_in_csonak > 0 and k_in_csonak + v_in_csonak <= 2:  # A csónak kapacitása
                    new_k_bal = k_bal - k_in_csonak
                    new_v_bal = v_bal - v_in_csonak
                    new_k_jobb = k_jobb + k_in_csonak
                    new_v_jobb = v_jobb + v_in_csonak
                    if validstate(new_k_bal, new_v_bal, new_k_jobb, new_v_jobb, c):
                        allapot_valtozas.append((new_c_left, new_v_left, new_c_right, new_v_right, "right"))
    else:  # A csónak a jobb parton van
        for k_in_csonak in range(3):  # kannibálok számának meghatározása: 0, 1 vagy 2
            for v_in_csonak in range(3 - k_in_csonak):  # 0, 1, vagy 2 vegetáriánus
                if k_in_csonak + v_in_csonak > 0 and k_in_csonak + v_in_csonak <= 2:  # A csónak kapacitása
                    new_k_bal = k_bal + k_in_csonak
                    new_v_bal = v_bal + v_in_csonak
                    new_k_jobb = k_jobb - k_in_csonak
                    new_v_jobb = v_jobb - v_in_csonak
                    if is_valid_state(new_k_bal, new_v_bal, new_k_jobb, new_v_jobb, c):
                        allapot_valtozas.append((new_k_bal, new_v_bal, new_k_jobb, new_v_jobb, "bal"))
    return allapot_valtozas