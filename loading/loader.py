import re
import pandas as pd

class loader:

    def __init__(self, filedir=None):
        if filedir is None:
            print("Please provide filedir='path-to-file'!")
            return

        ending=re.split("\.", filedir)[-1]
        if ending == "csv":
            separators=[";", " ", ","]
            self.data = pd.read_csv(filedir)

    def getData(self):
        return(self.data)
