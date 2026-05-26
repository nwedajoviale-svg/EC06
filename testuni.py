# Fonction simple à tester
def additionner(a, b):
    return a + b

# Fonction simulant une gestion d'erreur / sécurité
def diviser(a, b):
    if b == 0:
        raise ValueError("Division par zero interdite !")
    return a / b