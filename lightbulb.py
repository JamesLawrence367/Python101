class Lightbulb:
    
    def __init__(self, id, state="off"):
        self.state = state
        self.id = id
    
    def __str__(self):
        return f"Lightbulb {self.id} is {self.state}"
    
    def toggle(self):
        if self.state == "on":
            self.state = "off"
        else:
            self.state = "on"

L1 = Lightbulb(1)
L2 = Lightbulb(2)
print(L1,L2, sep="\n")

L1 = Lightbulb(1)
L2 = Lightbulb(2)
L1.toggle()
print(L1,L2, sep="\n")
