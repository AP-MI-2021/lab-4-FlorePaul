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


def palindrom(element):
    """
    Determina daca un numar este palindrom
    :param element: numarul pe care dorim sa il verificam daca este palindrom
    :return True, daca numarul este un palindrom, False, in caz contrar
    """
    n = len(element)
    for i in range(0, n/2):
        if element[i] != element[n-i-1]:
            return False
    return True


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


def 