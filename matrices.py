import os
import time
import numpy as np

from typing import Dict
from ascii import image

class Calculation():

    def __init__(self):
        self.A: np.ndarray = None
        self.length: int = 0
        self.count: int = 0

    def __repr__(self):
        return f"MATRICE: {self.B}; LENGHT: {self.length}"
    
    @staticmethod
    def counter():
        for i in range(5):
            time.sleep(1)
            print(f"\nGetting back in {i+1}...")

    def validate(self, key: int, value: int) -> bool:
        if value == self.length and key > 1:
            return True
        return False
    
    def calculate(self) -> np.ndarray:

        os.system("cls")
        print(image)
        print("MATRICE COMMON FACTOR\n")
        print("1. The matrice is supposed to be Rank 2-3.\n" \
              "2. Whole matrice can not be created of zeroes.\n" \
              "3. Each value is supposed to be an integer value and\n" \
              "   separated by a space.\n")
        data = input("Insert the values: ").split(" ")

        if not data or len(data) < 9:
            os.system("cls")
            print("You've insert wrong data, make sure it has 9 values separated by space.\n")
            self.counter()
            self.calculate()
            return None
        
        self.B = np.array([int(item) for item in data]).reshape(3, 3)
        removed = " ".join(data).replace("-", "").split(" ")
        self.A = np.array([int(item) for item in removed]).reshape(3, 3)

        numbers: np.ndarray = np.array([])
        formated: np.ndarray = np.array([])

        dictionary: Dict[int, int] = {}

        for i in range(3):
            for e in self.A[i]:
                numbers = np.arange(1, e+1)
                formated = np.append(formated, numbers[e % numbers == 0])
                self.length += 1
        self.length -= 1

        for i in formated:
            x = int(i)
            if not i in dictionary.keys():
                dictionary[x] = 1
            else:
                dictionary[x] = dictionary.get(x) + 1

        # so much attempts to reach these fucking numbers
        greatest: list[int] = [key for key, value in dictionary.items() if self.validate(key, value) == True]
        try:
            if greatest:
                new_array: np.ndarray = self.A * greatest[-1]
                text = f"{self.A}".split(" ")

                replaced = (" ".join(text)
                            .replace("[", " ")
                            .replace("]", " ")
                            .replace("\n", " ")
                            .split())
                
                string = ""
                start = 0
                end = 0
            
                for item in replaced:
                    self.count += 1
                    # Never liked the match case this much before
                    match self.count:
                        case 3:
                            if end == 2:
                                string += f"{item}*4]]\n "
                                end = 0
                            else:
                                string += f"{item}*4]\n "
                                end += 1
                            self.count = 0
                        case 1:
                            if start == 0:
                                string += f"[[{item}*4 "
                                start += 1
                            else:
                                string += f"[{item}*4 "
                        case _:
                            string += f"{item}*4 "
                string_splited = string.split(" ")
                new_string = " ".join(string_splited)
                os.system("cls")
                print(f"\nThe COMMON FACTOR is: {greatest[-1]}\n")
                print(f"Common Factor Applied:\n")
                print(f"{new_string}\n-----------------------------\n")
            print(f"Multiplied by Common Factor:\n")
            print(f"{new_array}")
        except UnboundLocalError:
            os.system("cls")
            print(f"\nThe COMMON FACTOR is NONE")
            print(f"The matrice leaved the same:\n")
            print(f"{self.B}")
            self.counter()
            self.calculate()

calculate = Calculation()

if __name__ == "__main__":
    try:
        calculate.calculate()
    except KeyboardInterrupt:
        pass