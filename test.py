import pandas as pd

df = pd.read_csv("training_data.csv")

df.term=df.term.str.extract('([0-9]+)')
df.int_rate=df.int_rate.str.extract('([0.0-9]+)')
df.zip_code=df.zip_code.str.extract('([0.0-9]+)')
df.revol_util=df.revol_util.str.extract('([0.0-9]+)')
df.revol_util=df.revol_util.str.extract('([0.0-9]+)')
#置き換え
#df['emp_length'] =df['emp_length'].mask(df['amp_length']=='< 1 year’,’0’)
df['emp_length'] = df['emp_length'].mask(df['amp_length']=='< 1 year','0')
df['emp_length'] =df['emp_length'].mask(df['emp_length']=='10+ years','10')
df['emp_length']=df['emp_length'].mask(df['emp_length']=='n/a','0')
df.emp_length=df.emp_length.str.extract('([0-9]+)')
grades = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
df['grade'] = df['grade'].map(lambda x: grades.index(x))

df.to_csv('training_data.csv')
