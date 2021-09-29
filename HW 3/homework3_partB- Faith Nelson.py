# To run code use Python IDLE or Pycharm

class Strategy():
    # This is my default class for the algorithms.
    def sort(self):
        print("This would be the bubble sort.\n")


class bubbleSort(Strategy):
    def sort(self):
        print("This would be the bubble sort.\n")


class mergeSort(Strategy):
    def sort(self):
        print("This would be the merge sort. \n")


class selectionSort(Strategy):
    def sort(self):
        print("This would be the selection sort. \n")


# ---------------------------------------------------------
class Inventory:
    # This creates a class that interfaces with the strategy classes above. It also creates a list
    # of objects. 
    def __init__(self, strategy: Strategy):
        self.object = []
        self.strategy = strategy

    # Here is where the interface methods are defined.
    def strategy(self) -> Strategy:
        return self.strategy

    def strategy(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def setObject(self, location, object):
        self.object.append(object)

    def getObject(self, location):
        return self.object[location]

    def inventoryInterface(self):
        self.Strategy.sort()


# -------------------------------------------------------

def main():
    # Creates two inventories
    inventory1 = Inventory(bubbleSort)
    for i in range(10):
        inventory1.setObject(i, i)

    inventory2 = Inventory(bubbleSort)
    for i in range(11):
        inventory2.setObject(i, i)

    inventory2.strategy()

    # Dynamically allows the user to change the sort type specifically of inventory1     
    userSort = input("Please enter sort wanted: ")

    while userSort != "end":
        userSort = input("Please enter sort wanted: ")
        if userSort == "selection":
            inventory1.strategy(selectionSort)
        elif userSort == "bubble":
            inventory1.strategy()
        elif userSort == "merge":
            inventory1.strategy(mergeSort)
        elif userSort == "end":
            break
        else:
            print("Sort type not recognized. Please try again")


main()
