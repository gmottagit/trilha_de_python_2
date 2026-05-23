
def ataque(monstro1_nome, ataque, nome_defensor, hp_defensor):

  hp_defensor -= ataque
  print(f"{monstro1_nome} atacou {nome_defensor} causando {ataque} de dano")
  return hp_defensor

def exibe_placar(nome1, hp1, nome2, hp2):
  print(f"\n---PLACAR---\n{nome1} = {hp1}\n{nome2} = {hp2}\n")

#MAIN
monstro1_nome = input("Digite o nome do monstro 1: ")
monstro2_nome = input("Digite o nome do monstro 2: ")
monstro1_ataque = int(input("Digite o ataque do monstro 1: "))
monstro2_ataque = int(input("Digite o ataque do monstro 2: "))

if monstro1_ataque < 1 or monstro2_ataque < 1:
  print("Você não deve digitar um ponto de ataque menor do que 1")
  exit()

monstro1_HP = int(input("Digite o HP do monstro 1: "))
monstro2_HP = int(input("Digite o HP do monstro 2: "))
if monstro1_HP < 1 or monstro2_HP < 1:
  print("Você não deve digitar um ponto de vida menor do que 1")
  exit()

#Duelo:
print("\n---HORA DO DUELO---")
while True:

  monstro2_HP = ataque(monstro1_nome, monstro1_ataque, monstro2_nome, monstro2_HP)
  if monstro2_HP <= 0:
    monstro2_HP = 0
    print("O monstro 1 venceu")
    exibe_placar(monstro1_nome, monstro1_HP, monstro2_nome, monstro2_HP)
    break
  monstro1_HP = ataque(monstro2_nome, monstro2_ataque, monstro1_nome, monstro1_HP)
  if monstro1_HP <= 0:
    monstro1_HP = 0
    print("O monstro 2 venceu")
    exibe_placar(monstro1_nome, monstro1_HP, monstro2_nome, monstro2_HP)
    break
  exibe_placar(monstro1_nome, monstro1_HP, monstro2_nome, monstro2_HP)