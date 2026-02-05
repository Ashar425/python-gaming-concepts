class car:
    def start(self,nn):
        print("To start the car press: ",nn)

    def speed(self,nm):
        print(nm, "increase the speed of the car")

    def stop(self,nm):
        print(nm, "stop the car")

ferrari=car()
toyota=car()
mini_cooper=car()

ferrari.start("start")
toyota.speed("toyota")
mini_cooper.stop("min_cooper")