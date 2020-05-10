#opening sequence
print("BootUpSeq")
print("Initialize")
print("Dvorak 14.1.8")
print("Ready")
print(input("your name?"))
player_name =  input("your name?")
print("Your name is {}. You are an {}.".format(player_name, "insignificant human"))
print("I am Lambda, tasked to remove you from this place. To do this, I need you to solve a series of puzzles.")


class oneStepD:
  dialogue = ""
  def __init__(self, dialogue):
    de = ""
    self.dialogue = dialogue
    input(de)



test = oneStepD("Ok?")
print(test.dialogue)


class RPSGame:#rock paper scissors
  rps = 0
  NPC = 0
  def game():
    while rps == NPC:
      print("type a number between 1 to 3")
      print("1 = rock")
      print("2 = paper")
      print("3 = scissors")
      input(rps)
      NPC = random.choice([1,2,3])
      if (rps == 1 && NPC == 3) || (rps == 2 && NPC == 1) || (rps == 3 && NPC == 2):
        print("you win")
      else:
        print("you lost")
