recip_pi = 0.318309886
recip_e = 0.367879441

# for positive c3-c4
print("Positive c3-c4 values for c1 upgrading")
lowest = 100
for p in range(2, 100):
    c3 = p ** recip_e

    c4, l = 0, 0
    while c3 - (l + 1) ** recip_pi > 0:
        l += 1
        c4 = l ** recip_pi
        
    val = c3 - c4
    if val < lowest:
        lowest = val
        print(f"{lowest:.8f}: c3={p}^(1/e), c4={l}^(1/pi)")

# output:
# 0.04358566: c3=2, c4=2
# 0.03888394: c3=5, c4=6
# 0.03340472: c3=7, c4=9
# 0.00367163: c3=8, c4=11
# 0.00166510: c3=19, c4=30
# 0.00105428: c3=28, c4=47
# 0.00081481: c3=40, c4=71
# 0.00005461: c3=79, c4=156

print()

# for negative c3-c4
print("Negative c3-c4 values for c2 upgrading")
lowest = -1
for p in range(2, 100):
    c3 = p ** recip_e

    c4, l = 0, 0
    while c3 - l ** recip_pi > 0:
        l += 1
        c4 = l ** recip_pi
    
    val = c3 - c4
    if val > lowest:
        lowest = val
        print(f"{lowest:.8f}: c3={p}, c4={l}")

# output:
# -0.12818604: c3=2, c4=3
# -0.05664334: c3=3, c4=4
# -0.00385257: c3=4, c4=5
# -0.00098118: c3=11, c4=16
# -0.00015865: c3=29, c4=49
# -0.00003444: c3=39, c4=69
