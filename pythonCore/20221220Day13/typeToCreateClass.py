def run(self):
    print(self)


Dog = type("Dog", (), {"number": 1, "run": run})
myDog = Dog()
myDog.run()
