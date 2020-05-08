#opening sequence
def hi():
  print("test")
  hi()
print("BootUpSeq")
print("Initialize")
print("Dvorak 14.1.8")
print("Ready")
print(input("your name?"))
player_name =  input("your name? >")
print("Your name is {}. You are an {}.".format(player_name, "insignificant human"))
print("I am Lambda, tasked to remove you from this place. To do this, I need you to solve a series of puzzles.")

class question:
  question = ""
  def __init__(self, question):
    self.question = question


question = question("test")
print(question.question)