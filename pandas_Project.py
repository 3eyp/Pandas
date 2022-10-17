
import pandas as pd
import matplotlib.pyplot as plt

class Pandas():
    
    #  Pandas ile read_csv komutunu kullanarak .CSV uzantılı dosyadaki verileri çekme

    def __init__(self):
        self.read()

    def start_read(self):
        db = pd.read_csv("GBvideos.csv")
        return db
    
    def read(self):
        result = self.start_read()
        print(result)

Pandas()