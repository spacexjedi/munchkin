# A card game 
class Munchikin: 
  def __init__(self, bonus, contra):
    self.bonus = bonus
    self.contra = contra
  
  def add_raca(self, raca):
    self.raca = raca
  

class Cultista(Munchikin):
  """This class bonus +2 for each cultista in the game """

class BatedorDeProfessor(Munchikin):
  """This class bonus +2 vs monsters level 10 or higher """


