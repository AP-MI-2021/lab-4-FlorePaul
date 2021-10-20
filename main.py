def citirelista():
    lista = []
    sircitit = imput("Dati lista, cu elementele separate prin virgula: ")
    numarinstring = sircitit.split(",")
    for x in numarinstring:
        lista.append(int(x))
        return lista


def numar_pare(lst):
    """
    Se determina numarul de numere pare dintr-o lista
    :param lst: lista initiala
    :return numarul de numere pare dintr-o lista
    """
    num = 0
    for i in lst:
        if i % 2 == 0:
            num += 1
    return num


def intersectie_liste(lst1, lst2):
    """
    Determinam intersectia intersectia dintre 2 liste
    :param lst1: prima lista de intregi
    :param lst2: a doua lista de intregi
    :return lst3: alta lista care reprezita intersectia dintre cele 2 liste
    """
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def palindrom(lst1 ,lst2 ):
    result = []
    l1 = len(lst1)
    l2 = len(lst2)
    p=0
    while p < l1 and p<l2:
        n_str=str(lst1[p])+str(lst2[p])
        n = int(n_str)
        if invers(n) == n:
            result.append(n)
        p = p + 1
    return result


def concatenare(num1, num2):
    """
    Concateneaza doi intregi, trasnformandu-i in str., si apoi rezultatul inapoi la intreg
    :param num1: primul intreg
    :param num2: al doilea strnig
    :return: intrgul format in urma concatenarii a celor 2 intregi
    """
    intconcatenat = int(str(num1) + str(num2))
    return intconcatenat


def list_concatenare(list1, list2):
    """
    Concateneaza 2 liste
    :param list1: prima lista de intregi
    :param list2: a doua lista de intregi
    :return listconcat: lista concatenata
    """
    listconcat = []
    if len(list1) > len(list2):
        maxim = len(list1)
    else:
        maxim = len(list2)
    for i in range(0, maxim):
        for j in range(0, maxim):
            if i == j:
                listconcat.append(concatenare(list1[i], list2[j]))
    return listconcat


def invers(numar):
    """
    Se realizeaza inversul unui intreg
    :param numar: intregul initial
    :return inv_numar: intregul inversat
    """
    inv_numar = 0
    while numar:
        cifre = numar % 10
        inv_numar = inv_numar * 10 + cifre
        numar /= 10
    return inv_numar


def div(list1, list2):
    """
    Inlocuim toate elementele cu oglinditul lor daca toate elementele sunt divizibile cu toate elemntele din lista a 3-a
    :param list1: prima lista
    :param list2: lista a 3-a
    :return list3: lista rezultata
    """
    list3 = []
    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if list1[i] % list2[j] == 0:
                list3.append(invers(list1[i]))
            else:
                list3.append(list1[i])
    return list3

if _main_ == '_main_':
    final = False
    while not final:
        print("1. Citire pentru 2 liste")
        print("2. Numarul de elemente pare")
        print("3. Intersectia listelor")
        print("4. Palindrom")
        print("5. Cerinta 5")
        print("x. Iesire din program")
        optiune = input("Dati obtiunea dorita: ")
        if optiune == '1':
            list1 = citirelista()
            list2 = citirelista()
        elif optiune == '2':
            list1 = citirelista()
            list2 = citirelista()
            if numar_pare(list1) == numar_pare(list2):
                print("Listele au numarul de elemente pare egal")
            else:
                print("Listele nu au numarul de elemente pare egal")
        elif optiune == '3':
            list1 = citirelista()
            list2 = citirelista()
            print("Intersectia celor doua liste este: ")
            print(intersectie_liste(list1, list2)
        elif optiune == '4':
            list1 = citirelista()
            list2 = citirelista()
            print(palindrom(list1, list2))
        elif option == 'x':
            finish = True
        else:
            print("Optiunea nu este valida")