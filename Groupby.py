import pandas as pd
import csv

class Groupby:
	def __init__(self,myDataLoc,mySchema):	
		self.schema = pd.DataFrame.from_csv(mySchema,index_col=False);
		self.myData = pd.DataFrame.from_csv(myDataLoc,index_col=False,encoding = "ISO-8859-1");

	
	def create(self):
		idx = self.schema[self.schema.type=="cat"].index.tolist()
		z=[]
		for id in idx:
			u=[]
			x=pd.unique(self.myData.ix[:,id])
			v=[self.schema.ix[id,0]]*len(x)
			u = list(zip(v,x))
			z=z+u
		with open('groups.csv','w') as out:
			csv_out=csv.writer(out)
			csv_out.writerow(['col','value'])
			for row in z:
				csv_out.writerow(row)
		#print (z)


if __name__ == '__main__':	
	myDataLoc='/home/sachin/Documents/forever/ZENSUS.csv';
	mySchema = '/home/sachin/Documents/forever/schema.csv';
	gb = Groupby(myDataLoc,mySchema)
	gb.create()
