import shutil
import os
import pandas as pd

data = pd.read_excel('ABL_Test.xlsx')
df = pd.DataFrame(data, columns=['File Name'])
df = df['File Name'].values.tolist()
print(df)

dir_path = os.path.dirname(os.path.realpath(__file__))
os.mkdir('moved')
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if str(file) in df:
            # os.rename(root + '' + str(file),
            #           root + '/moved/' + str(file))
            shutil.copy(file, 'moved')
