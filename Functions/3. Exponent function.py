
def exponent(root , power) :

    """"
        17/07/2022
        this method making the same function of Exponent function
        2 ** 5 = 32
        2 * 2 * 2 * 2 * 2 = 32
    """
    temp = root # 2

    while power > 1 :   # 5
        power = power - 1
        root = temp * root # root = 2 * 2

    return root

print(exponent(3,10))