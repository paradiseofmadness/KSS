from random import randint

'''0 bedeutet eine Straße nach unten,
1 bedeutet eine Straße nach rechts'''
def wege(n : int, m : int):
    # am unteren Rand (Street m) angekommen
    #   => einzig möglicher "Restweg" n-mal nach rechts
    if m == 0 and n != 0:
        return [[1]*n]
    
    # am rechten Rand (Avenue n) angekommen
    #   => einzig möglicher "Restweg" m-mal nach unten
    if n == 0:
        return [[0]*m]
    
    # erster Schritt nach unten => m -> m-1
    res1 = wege(n, m-1)
    # jedem Weg nach dem Schritt nach unten wird der
    #   besagte Schritt nach unten vorne hinzugefügt
    for i in res1:
        i.insert(0, 0)
    
    # erster Schritt nach rechts => n -> n-1
    res2 = wege(n-1, m)
    # jedem Weg nach dem Schritt nach rechts wird der
    #   besagte Schritt nach rechts vorne hinzugefügt
    for i in res2:
        i.insert(0, 1)
    
    # Wege mit dem ersten Schritt nach unten
    #   + Wege mit dem ersten Schritt nach rechts
    return res1+res2

for _ in range(10):
    n = randint(0, 3)
    m = randint(0, 3)
    print(f"{n+1}x{m+1}: {wege(n, m)}")