h, m = input().split()

h = int(h)
m = int(m)

if h >= 12:
    ampm = "PM"
    if h >= 13:
        h = h - 12
else:
    ampm = "AM"

print("%02d : %02d %s" % (h, m, ampm))
