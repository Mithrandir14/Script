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


class question:
  question = ""
  def __init__(self, something):
    self.question = something


question = question("")