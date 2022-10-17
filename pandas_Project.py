import pandas as pd

class Pandas():
    def __init__(self):
        self.read()

    # Pandas ile read_csv komutunu kullanarak .CSV uzantılı dosyadaki verileri çekme
    def start_read(self):
        db = pd.read_csv("GBvideos.csv")
        return db
    
    def read(self):
        result = self.start_read()
        print(result)

Pandas()