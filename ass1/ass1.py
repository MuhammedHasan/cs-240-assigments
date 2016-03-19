import thinkstats2
from thinkstats2 import pandas as ps


class PARTI:

    def __init__(self):
        self.df = PARTI._read_file()
        print self.df



    @staticmethod
    def _read_file():
        '''
            This static function readfiles and selects necessary rows.
            return: pandas dataframe
        '''
        table = list()
        for i in open('wine.txt'):
            row = i.split('\t')
            if len(row) > 2:
                table.append(row[1:])
            else:
                break
        header = table.pop()[1:]
        return ps.DataFrame(table, columns=header)

    def plotHistogram(self):
        open()

    def plotCategory(self, category, start_year, end_year):
        pass

    def findOutlier(self):
        pass

    def mean(self):
        pass

    def variance(self):
        pass


class PARTII:

    def generate():
        pass

    def PMF():
        pass

    def CDF():
        pass

    def findDefective():
        pass


PARTI()
