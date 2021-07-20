recip_pi = 0.318309886
recip_e = 0.367879441
lowest = 100

for p in range(2, 100):
    c3 = p ** recip_pi

    c4, l = 0, 0
    while c3 - (l + 1) ** recip_e > 0:
        l += 1
        c4 = l ** recip_e
        
    val = c3 - c4
    if val < lowest:
        print(f"{lowest}: c3={p}, c4 = {l}")
        lowest = val


# output:
# 0.24686898874179475: c3=3, c4 = 2
# 0.1281860407548756: c3=4, c4 = 3
# 0.05664334225524592: c3=5, c4 = 4
# 0.0038525691934716555: c3=16, c4 = 11
# 0.0009811844364824296: c3=49, c4 = 29
# 0.00015865359786859656: c3=69, c4 = 39