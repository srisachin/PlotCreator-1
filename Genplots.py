# Copyright Sachin Srivastava
# Usage : python Genplots.py <data-filename> <experiment-filename>

import sys
import PlotSea.PlotObj
import pandas as pd
import settings
from PlotSea import *


class Genplots:

	def __init__(self,myDataLoc,myExp):	
		self.experiments = pd.DataFrame.from_csv(myExp,index_col=False);
		self.myData = pd.DataFrame.from_csv(myDataLoc,index_col=False,encoding = "ISO-8859-1");
		self.plotlist = []
	
	def myFactory(self,myStr,exp):
		for cls in PlotSea.PlotObj.PlotObj.__subclasses__():
			#__import__(cls.__name__)			
			t = cls()
			if t.check(myStr):
				return t

	def generatePlots(self):		
		for exp in self.experiments.iterrows():
			myStr = exp[1]['plot']
			p=self.myFactory(myStr,exp)
			p.plotExp(exp,self.myData)


def main(argv):	
	myDataLoc=argv[0]
	myExp=argv[1]
	settings.initData()
	gen = Genplots(myDataLoc,myExp)
	gen.generatePlots()


if __name__ == '__main__':	
	main(sys.argv[1:])

# Input : data, experiments
# Output : list of plots

