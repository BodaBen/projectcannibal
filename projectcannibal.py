def validstate(k_bal, v_bal, k_jobb, v_jobb, c):
    "ellenőrzi, hogy az adott pillanatban az állapot érvényes-e"
    if k_bal < 0 or v_bal < 0 or k_jobb < 0 or v_jobb < 0:
        return False
    if (k_bal > v_bal + c and v_bal > 0) or (k_jobb > v_jobb + c and v_jobb > 0):
        return False
    return True

