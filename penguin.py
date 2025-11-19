class Bird:
    def __init__(self):
        print("bird is ready")
    def whoisThis(self):
        print(Bird) 
    def swim(self):
        print("swim faster")
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("penguin is ready")
    def whoisThis(self):
        print("Penguin")
    def run(self):
        print("run faster")
peggy=Penguin()
peggy.whoisThis()            
peggy.swim()
peggy.run()