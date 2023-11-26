def calc_victories(w, l): return (w - l)
def classfy(z):
    if z < 10:
        return "Iron"
    elif z >= 10 and z < 20:
        return "Bronze"
    elif z >= 20 and z < 50:
        return "Silver"
    elif z >= 50 and z < 80:
        return "Gold"
    elif z >= 80 and z < 90:
        return "Diamond"
    elif z >= 90 and z < 100:
        return "Legend"
    elif z >= 100:
        return "Imortal"

qtd_wins = int(input("Ganhou quantas? "))
qtd_loses = int(input("Perdeu quantas? "))

print(f"O herói com saldo de vitórias {calc_victories(qtd_wins, qtd_loses)} está no nível {classfy(calc_victories(qtd_wins, qtd_loses))}")