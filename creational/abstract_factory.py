from abc import ABCMeta
from abc import abstractmethod


class IFactory(metaclass=ABCMeta):
    

    @abstractmethod
    def createButton(self):
        # f = self.factory()
        # print("We have a loverly{}".format(f))
        # print("It says {}".format(f.speak()))
        pass

    @abstractmethod
    def createBorder(self):
        pass
class Factory(IFactory):
    def __init__(self, factory=None):
        self.factory = factory
        self.instance = self.factory()

    def createButton(self):
        self.instance.createButton()

    def createBorder(self):
        self.instance.createBorder()

class MacFactory(IFactory):
    def createButton(self):
        return MacButton()
    def createBorder(self):
        return MacBorder()

class WinFactory(IFactory):
    def createBorder(self):
        return WinBorder()
    def createButton(self):
        return WinButton()

class IButton(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass


class IBorder(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass


class MacButton(IButton):
    def __init__(self):
        print("mac button created")


class WinButton(IButton):
    def __init__(self):
        print("windows button created")


class MacBorder(IBorder):
    def __init__(self):
        print("mac border created")


class WinBorder(IBorder):
    def __init__(self):
        print("windows border created")

if __name__ == '__main__':
    l = [ MacFactory, WinFactory]
    for f in l:
        _factory = Factory(f)
        _factory.createButton()
        _factory.createBorder()
        print("="*20)
    

