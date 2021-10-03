class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        """Static access method."""
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """Virtually private constructor."""
        if Singleton.__instance != None:
            raise Exception(
                "This class is a singleton. You cannot initialize it more than once!"
            )
        else:
            Singleton.__instance = self

    def __repr__(self):
        return f"{self.__class__.__name__}"


s = Singleton.getInstance()

s2 = Singleton.getInstance()

# points to same reference
print(s is s2)
