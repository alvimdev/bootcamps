def classfy(exp):
    if exp < 1000:
        return "Iron"
    elif exp >= 1000 and exp < 2000:
        return "Bronze"
    elif exp >= 2000 and exp < (5000 + 1000):
        return "Silver"
    elif exp >= 6000 and exp < 7000:
        return "Gold"
    elif exp >= 7000 and exp < 8000:
        return "Platinum"
    elif exp >= 8000 and exp < 9000:
        return "Ascendant"
    elif exp >= 9000 and exp < 10000:
        return "Imortal"
    elif exp >= 10000:
        return "Radiant"

hero_name = input("Digite o nome do herói: ")
hero_exp = int(input(f"Digite a quantidade de experiência de {hero_name}: "))

print(f"O herói {hero_name} está no nível {classfy(hero_exp)}")