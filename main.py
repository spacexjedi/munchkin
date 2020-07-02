from classes import BatedorDeProfessor, Cultista
from racas import Anao, Elfo
from itens import ArmaduraRechonchuda

# vou instanciar para virar objeto ^^^
player1 = BatedorDeProfessor(bonus =2, contra=-2)
player2 = Cultista(bonus=0, contra=None)

anao1 = Anao(itens=100, cartas=6, fuga=0)
player1.add_raca(anao1)