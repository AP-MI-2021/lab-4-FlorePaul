def citirelista():
    l=[]
    sircitit = imput("Dati lista, cu elementele separate prin virgula: ")
    numarinstring = sircitit.split(",")
    for x in numarinstring:
        l.append(int(x))
        return l


def numar_pare (lst):
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


def intersectie_liste(lst1, lst2)
    """
    Determinam intersectia intersectia dintre 2 liste
    :param lis1: prima lista de intregi
    :param list2: a doua lista de intregi
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


def contatenare(num1, num2):
    """
    Concateneaza doi intregi, trasnformandu-i in str., si apoi rezultatul inapoi la intreg
    :param num1: primul intreg
    :param num2: al doilea strnig
    :return: intrgul format in urma concatenarii a celor 2 intregi
    """
    intconcatenat = int(str(num1) + str(num2))
    return intconcatenat

