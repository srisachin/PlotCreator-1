import PlotObj
import BarPlot
import ScatterPlot
import DensityPlot
import BarMean
import pandas as pd
import settings

class Genplots:

	def __init__(self,myDataLoc,myExp):	
		self.experiments = pd.DataFrame.from_csv(myExp,index_col=False);
		self.myData = pd.DataFrame.from_csv(myDataLoc,index_col=False,encoding = "ISO-8859-1");
		self.plotlist = []
	
	def myFactory(self,myStr,exp):
		for cls in PlotObj.PlotObj.__subclasses__():
#			print (cls)
			t = cls()
			if t.check(myStr):
				return t

	def generatePlots(self):		
		for exp in self.experiments.iterrows():
			myStr = exp[1]['plot']
			#print (myStr)
			p=self.myFactory(myStr,exp)
			p.plotExp(exp,self.myData)
#			if(exp[1]['plot'] =="bar"):
#				p=BarPlot.BarPlot(exp)
#			elif(exp[1]['plot'] =="scatter"):
#				p=ScatterPlot.ScatterPlot(exp)
#			elif(exp[1]['plot'] =="density"):
#				print("density")

#			self.plotlist.add(p)


#	def rankPlots():




if __name__ == '__main__':	
	myDataLoc='/home/sachin/Documents/forever/WINESEP.csv';
	myExp='/home/sachin/Documents/forever/experiment.csv';
	settings.initData()
	gen = Genplots(myDataLoc,myExp)
	gen.generatePlots()

# Input : data, experiments
# Output : list of plots

