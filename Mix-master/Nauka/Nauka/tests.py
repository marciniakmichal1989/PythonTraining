def peak(arr):
    suma_z_prawej = []
    suma_z_lewej = []
    wynik = 0
    zmienna = 0
    print(len(arr))
    for x in arr:
        suma_z_prawej.append(x)
        zmienna += 1
        for y in arr.reverse():
            suma_z_lewej.append(y)
            if sum(suma_z_prawej) == sum(suma_z_lewej):
                wynik = zmienna
    return wynik
        






print(peak([1,2,3,5,3,2,1]))