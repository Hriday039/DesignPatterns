class Robot:
    def __init__(self, name):
        self.name = name

    def move(self, coordinates):
        print("moving to ", coordinates)

    def display(self, data):
        print(data)

    def morph(self):
        print("morphing...")


class Walking_robot(Robot):
    def __init__(self, name):
        super().__init__(name)

    def move(self, coordinates):
        print("walking to ", coordinates)

    def display(self, data):
        print("displaying text data", data)

    def morph(self):
        print("morphing into human...")


class Aerial_robot(Robot):
    def __init__(self, name):
        super().__init__(name)

    def move(self, coordinates):
        print("flying to ", coordinates)

    def display(self, data):
        print("displaying holographic data", data)

    def morph(self):
        print("morphing into vehicle...")


class Cleaner_robot(Robot):
    def __init__(self, name):
        super().__init__(name)

    def move(self, coordinates):
        print("Rolling to ", coordinates)

    def display(self, data):
        print("displaying text data", data)

    def morph(self):
        print("morphing into box...")
