"""
Dans ce module on utlise 2 fonction une secondaire is palindrome qui va vrrifier si
la chaine de caractères passées en paramètres est un palindrome en tenant compte
des caractères alphanumériques et une main 
qui fait des appels et de test de ispalindrome 
"""
#### Fonction secondaire
def ispalindrome(p):
    """
    fonction ispalindrome, permet de déterminer si 
    un mot ou une chaine des caractères passé en argument est un palindrome
    renvoie vrai si oui sinon faux
    """
    accents = str.maketrans(
        "áàâäãåçéèêëíìîïñóòôöõúùûüýÿÁÀÂÄÃÅÇÉÈÊËÍÌÎÏÑÓÒÔÖÕÚÙÛÜÝ",
        "aaaaaaceeeeiiiinooooouuuuyyAAAAAACEEEEIIIINOOOOOUUUUY"
    )

    p = p.translate(accents).lower()

    p = ''.join(char.lower() for char in p if char.isalnum())

    return p == p[::-1]

#### Fonction principale
def main():
    """
    fonction main, permet de faire quelques test et appels de la fonction ispalindrome
    """
    ispalindrome("test")
    ispalindrome("anne")
    ispalindrome("anne anne")
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"] :
        print(s, ispalindrome(s))


if __name__ == "__main__" :
    main()
