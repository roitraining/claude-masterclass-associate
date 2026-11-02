import csv
import sys
import time

T = 0
E = 0
R = {"CA": 0.0725, "TX": 0.0625, "NY": 0.08875, "OH": 0.0575}
C = {"C1": "Northwind Pottery", "C2": "Lakeside Books", "C3": "Fernhill Garden Supply", "C4": "Corner Bike Shop"}


def lk(c):
    time.sleep(0.05)
    return C.get(c, "UNKNOWN")


def tx(s, a):
    time.sleep(0.05)
    try:
        return a * R[s]
    except:
        return a * 0.05


def run(f="orders.csv", o="out.txt"):
    global T, E
    out = open(o, "w")
    for r in csv.DictReader(open(f)):
        try:
            n = lk(r["cust"])
            a = int(r["qty"]) * float(r["price"])
            if a > 500:
                a = a * 0.95
            t = tx(r["st"], a)
            tot = round(a + t, 2)
            if r["st"] == "NY":
                tot = tot + 12
            T = T + tot
            out.write("%s|%s|%s|%.2f\n" % (r["oid"], n, r["st"], tot))
        except:
            E = E + 1
            pass
    out.write("TOTAL %.2f ERR %d\n" % (T, E))
    out.close()
    print("done", T, E)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(sys.argv[1])
    else:
        run()
