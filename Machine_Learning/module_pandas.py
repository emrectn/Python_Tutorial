import pandas as pd
import numpy as np

exmp_data = {'kept':['word','stop','4','soap','232.126.10.186'],'right':['exist','kids','70','block','131.195.7.119'],'colony':['fifteen','future','70','upward','16.39.69.149']}
csv_path = '../Datasets/cities.csv'
df = pd.read_csv(csv_path)
# df = pd.read_excel("excel_dosyasi_path")

# To get use numeric data
df_num = df._get_numeric_data()

# Data frame'in print edilmesi
print(df)

# Data frame ilk 5 satırının print edilmesi
print(df.head())

# Json datadan veriyi csv olarak almak
dfcsv = pd.DataFrame(exmp_data)
print(dfcsv)

print("Right Sutunun alınması")
x = dfcsv['right']
print(x)

print("kept ve right multiple sutun alınması")
x = dfcsv[['right', 'kept']]
print(x)


""" # Rows:
df.iloc[0] # first row of data frame (Aleshia Tomkiewicz) - Note a Series data type output.
df.iloc[1] # second row of data frame (Evan Zigomalas)
df.iloc[-1] # last row of data frame (Mi Richan)
# Columns:
df.iloc[:,0] # first column of data frame (first_name)
df.iloc[:,1] # second column of data frame (last_name)
df.iloc[:,-1] # last column of data frame (id)

# Multiple row and column selections using iloc and DataFrame
df.iloc[0:5] # first five rows of dataframe
df.iloc[:, 0:2] # first two columns of data frame with all rows
df.iloc[[0,3,6,24], [0,5,6]] # 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
df.iloc[0:5, 5:8] # first 5 rows and 5th, 6th, 7th columns of data frame (county -> phone1).

# select rows with id column between 100 and 200, and just return 'postal' and 'web' columns
df.loc[(data['id'] > 100) & (data['id'] <= 200), ['postal', 'web']]

# A lambda function that yields True/False values can also be used.
# Select rows where the company name has 4 words in it.
df.loc[data['company_name'].apply(lambda x: len(x.split(' ')) == 4)]

df[df['right']=='42']

# To save
df.to_csv('new_csv.csv')

# Datayı kategorilere ayırma - Kaç farklı kategori var tespit edilmesi
pd.Categorical([1,2,3,1,2,3])
# [1, 2, 3, 1, 2, 3]
# Categories (3, int64): [1, 2, 3]

# Kategorileri etiketleme
pd.Categorical([1,2,3,1,2,3]).codes
# array([0, 1, 2, 0, 1, 2], dtype=int8)
 """

# Predict model data #
new_input = np.arange(1, 101, 1).reshape(-1, 1)
print(new_input)
yhat = lm.predict(new_input)
print(yhat)
