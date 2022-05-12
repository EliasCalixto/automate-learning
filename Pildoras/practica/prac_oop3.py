class Elias():
    age = 22
    heigh = 160
    weight = 59
    happy = True
    status = 'Repose'
    def run(self):
        self.status = 'running'

    def jump(self):
        self.status = 'jumping'

    def sing(self):
        self.status = 'singing'

    def stop(self):
        self.status = 'Repose'

elias = Elias()

print(elias.age)
print(elias.happy)

elias.jump()
print(elias.status)
elias.sing()
print(elias.status)
elias.stop()
print(elias.status)
