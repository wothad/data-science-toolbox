import numpy


class preprocessor:
    def __init__(self):
        self.data=None

    def autoprocess(self,
                    data=None,
                    entryfil="mean",
                    outliers=True,
                    idcolumn=None
                    ):
        if(data is None):
            print("Please provide Data by setting data=<tabular-data>!")
            return

        self.data=data
        return(data)

    def fillMissingEntrys(self, mode="mean"):

