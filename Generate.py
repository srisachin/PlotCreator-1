import xml.etree.ElementTree as ET
import pandas as pd
class Generate:
	def __init__(self,mySchema,myPrototype):
		self.schema = pd.DataFrame.from_csv(mySchema,index_col=False);		
		self.prototype = pd.DataFrame.from_csv(myPrototype,index_col=False);
	def generateExperiments(self):
		exp1 = pd.merge(self.prototype, self.schema, left_on='xaxis', right_on='type', how='inner');
		exp1['xaxis']=exp1['name'];
		exp1 = exp1[['xaxis','yaxis', 'plot']]
		idx = exp1['yaxis'].isin(['cat', 'num'])
		
		exp2 = pd.merge(exp1[idx], self.schema, left_on='yaxis', right_on='type', how='inner')
		exp2['yaxis']=exp2['name']
		exp2 = exp2[['xaxis','yaxis', 'plot']]
		exp=pd.concat([exp1[~idx], exp2])
		exp.to_csv('/home/sachin/Documents/forever/experiment.csv')

if __name__ == '__main__':
	mySchema = '/home/sachin/Documents/forever/schemaZ.csv'
	myPrototype = '/home/sachin/Documents/forever/prototype.csv'
	gen = Generate(mySchema,myPrototype)
	gen.generateExperiments()


# Input : Schema, Plot Prototype
# Output : Experiments
#Experiment 1
#x=variableName1
#y=variableName2
#plotFuction bar

#
#Experiment 2
#x=variableName3
#y=variableName4
#plotFunction correlation

#
#Experiment 3
#x=variableName2
#y=variableName4
#Groupby=variableName5
#plotFunction correlation


	
