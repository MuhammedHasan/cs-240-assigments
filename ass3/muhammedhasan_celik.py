import thinkstats2
import pandas as pd
import thinkplot as tplot
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import stats
import random
import matplotlib.patches as mpatches
import math


class HypotesisTestingOnDifferenceInMean(thinkstats2.HypothesisTest):

    def TestStatistic(self, data):
        male, female = data
        return abs(male.mean() - female.mean())

    def MakeModel(self):
        male, female = self.data
        self.n, self.m = len(male), len(female)
        self.pool = np.hstack(self.data)

    def RunModel(self):
        np.random.shuffle(self.pool)
        return self.pool[:self.n], self.pool[self.n:]


class HypotesisTestingOnCorrelation(thinkstats2.HypothesisTest):

    def TestStatistic(self, data):
        x, time_spending = data
        return abs(thinkstats2.Corr(x, time_spending))

    def RunModel(self):
        x, time_spending = self.data
        x = np.random.permutation(x)
        return x, time_spending


class PARTI():

    def __init__(self):
        self.data = pd.read_csv('data.csv')

    def test_time_spending_GPA(self):
        testing_data = (self.data['GPA'].values,
                        self.data['Time Spend'].values)
        return HypotesisTestingOnCorrelation(testing_data).PValue()

    def test_time_spending_Age(self):
        testing_data = (self.data['Age'].values,
                        self.data['Time Spend'].values)
        return HypotesisTestingOnCorrelation(testing_data).PValue()

    def test_male_female(self):
        male = self.data[self.data['Gender'] == 'M']['Time Spend'].values
        female = self.data[self.data['Gender'] == 'F']['Time Spend'].values
        testing_data = (male, female)
        return HypotesisTestingOnDifferenceInMean(testing_data).PValue()


p = PARTI()
print p.test_time_spending_GPA()
print p.test_time_spending_Age()
print p.test_male_female()


class PART2():

    def __init__(self):
        self.data = pd.read_csv('data.csv')

    def plot_time_spending_GPA(self):
        GPA, time_spend = (self.data['GPA'].values,
                           self.data['Time Spend'].values)
        tplot.Scatter(time_spend, GPA)
        tplot.Show()
        inter, slope = thinkstats2.LeastSquares(time_spend, GPA)
        return inter, slope

    def plot_residuals(self):
        GPA, time_spend = (self.data['GPA'].values,
                           self.data['Time Spend'].values)

        inter, slope = thinkstats2.LeastSquares(time_spend, GPA)
        r = thinkstats2.Residuals(time_spend, GPA, inter, slope)

        tplot.Plot(sorted(time_spend), abs(r))
        tplot.Show()

    def GPA_Age(self):
        GPA, age = ([math.log10(i) for i in self.data['GPA'].values],
                    self.data['Age'].values)

        inter, slope = thinkstats2.LeastSquares(age, GPA)
        residuals = thinkstats2.Residuals(age, GPA, inter, slope)

        return thinkstats2.CoefDetermination(GPA, residuals)


p = PART2()
# print p.plot_time_spending_GPA()
# print p.plot_residuals()
print p.GPA_Age()
