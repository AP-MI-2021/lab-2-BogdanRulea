#problema 9: Transforma un numar din baza 2 in baza 16(numarul se da in baza 2)
def get_base_16_from_2(n : str):
    base_10 = 0
    base_2_length = int(len(n))
    #conversia din baza 2 in baza 10
    for i in range(base_2_length):
       base_10 += int(n[i])*(2**(base_2_length-i-1))

    #conversia din baza 10 in baza 16
    base_16 = ""
    while base_10!= 0:
        if base_10%16<10:
            base_16 += str(base_10%16)
        else:
            base_16 += str(chr(55+base_10%16))#convertesc din codul ASCII in literele corespunzatoare
        base_10//=16
    return base_16[::-1]#returnez in ordine inversa string-ul
    
def test_get_base_16_from_2():
    assert get_base_16_from_2("100111110001") == "9F1"
    assert get_base_16_from_2("100111110") == "13E"
    assert get_base_16_from_2("1011101011") == "2EB"
    assert get_base_16_from_2("1111100111011") == "1F3B"
    assert get_base_16_from_2("1010101111") == "2AF"

test_get_base_16_from_2()

#problema 10: Combinari de n luate cate k
def get_n_choose_k(n: int, k: int):
    comb = 1

    #formula combinari n! impartit la k!(n-k)!
    for i in range(1, n+1):
        comb *=i # n!

    for i in range(1,k+1):
        comb //= i # k!
    
    for i in range(1,n-k+1):
        comb //= i # (n-k)!
    
    return comb


def test_get_n_choose_k():
    assert get_n_choose_k(5,2) == 10
    assert get_n_choose_k(8,4) == 70
    assert get_n_choose_k(13,10) == 286
    assert get_n_choose_k(7,2) == 21
    assert get_n_choose_k(11,3) == 165
    assert get_n_choose_k(20,14) == 38760

test_get_n_choose_k()


def main():
    stillrunning = True
    while stillrunning:
        meniu = "Meniu de comenzi:\nProblema 1: Transforma un numar din baza 2 in baza 16(numarul se da in baza 2)\nProblema 2: Combinari de n luate cate k\nx : Program incheiat."
        print(meniu)
        problema = input("Scrie numarul problemei:\n")
        if problema == '1':
            print("Ai ales problema 1: Transforma un numar din baza 2 in baza 16(numarul se da in baza 2)")
            num_base_2 = input("Scrie numarul in baza 2:\n")
            print(f"Numarul {num_base_2} scris in baza 16 este: {get_base_16_from_2(num_base_2)}")
        elif problema == '2':
            print("Ai ales problema 2: Combinari de n luate cate k")
            n = int(input("Scrie n: "))
            k = int(input("Scrie k: "))
            print(f"Combinari de {n} luate cate {k} este egal cu {get_n_choose_k(n,k)} ")
        elif problema == 'x':
            stillrunning = False
        else:
            print("Ai ales o optiune inexistenta, incearca din nou!")

if __name__ == "__main__":
    main()