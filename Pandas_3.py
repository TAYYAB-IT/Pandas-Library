import pandas as pd
#data=pd.read_csv('dirtydata.csv')
#print(data.loc[7,'Duration'])
#for i in data.index:
#    if(data.loc[i,'Duration']>90):
#        data.drop(i,inplace=True)
#print(data.to_string())
#z=data.duplicated()  #Returns True for every row that is a duplicate, othwerwise False
#print(z)
#z=list(z)
#print('Duplicated Rows =',z.count(True))
####To remove Duplicated Rows ########
#data.drop_duplicates(inplace=True)
#print(data)
#######Give Correlation between Coloumns ######
#print(data.corr())
data=pd.read_excel('IT-19-A_(DCN)_Attendance.xlsx')
print(data.info())