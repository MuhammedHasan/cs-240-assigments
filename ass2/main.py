import thinkstats2
import pandas as pd
import thinkplot as tplot
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import stats
import random
import matplotlib.patches as mpatches


class PARTI:

    def __init__(self):
        self.df = df = pd.read_csv(
            'babyboom.dat', sep='\s+', header=None, skiprows=59,
            names=['time', 'sex', 'weight', 'minutes'])

    def exponential(self, x, y):
        return 1.0 - ((math.e) ** (-1 * float(y) * float(x)))

    def plot_random_exponential(self):
        ress = [self._random_exp_series() for i in range(3)]
        for x, alpha in ress:
            x.plot.line(label="alpha = %f" % alpha)
        plt.legend(loc=4)
        plt.show()

        for x, alpha in ress:
            pd.Series(1 - i for i in x).plot.line(label="alpha = %f" % alpha)
        plt.yscale('log')
        plt.legend(loc=1)
        plt.show()

    def inter_arrival_time_of_baby(self):
        cdf = thinkstats2.Cdf(self.df.minutes.diff())
        tplot.Cdf(cdf)
        tplot.Show()

        tplot.Cdf(cdf, complement=True)
        tplot.Show(yscale='log')

    def cdf_of_normal_distribution(self):
        m = self.df.weight.mean()
        s = self.df.weight.std()

        model = np.random.normal(m, s, 100000)
        cdf = thinkstats2.Cdf(self.df.weight)
        m_cdf = thinkstats2.Cdf(pd.Series(model))

        tplot.Cdf(m_cdf)
        tplot.Cdf(cdf)
        tplot.Show()
        tplot.Plot(cdf)

    def baby_scatter(self):
        plt.scatter(self.df.weight, self.df.minutes)
        plt.show()

    def _random_exp_series(self,  lower=1, upper=3):
        alpha = random.uniform(lower, upper)
        return (pd.Series(sorted(self.exponential(
            random.uniform(0, 3), alpha) for i in range(10000))), alpha)


print PARTI().baby_scatter()
