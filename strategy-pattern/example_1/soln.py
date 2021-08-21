class Robot:
    def __init__(self, name, movement_stragety, display_strategy):
        self.name = name
        self.move = movement_stragety
        self.display = display_strategy


def walking_movement_strategy(coordinates):
    print("walking to ", coordinates)


def flying_movement_strategy(coordinates):
    print("flying to ", coordinates)


def text_display_strategy(data):
    print("displaying holographic data", data)


def threeD_display_strategy(data):
    print("displaying 3-d data", data)


if __name__ == "__main__":
    walking_robot = Robot(
        "walking robot 1", walking_movement_strategy, text_display_strategy
    )
    flying_robot = Robot(
        "flying robot 1", flying_movement_strategy, threeD_display_strategy
    )

    flying_robot.move({"x": 1, "y": 2})
