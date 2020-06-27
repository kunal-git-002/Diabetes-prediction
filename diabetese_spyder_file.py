#diabetese 
#jay mataji
#temp file 0

import pandas as pd
from sklearn.externals import joblib
import seaborn as sns
import matplotlib.pyplot as plt


##diabetes df
dib=pd.read_csv(r"C:\Users\Kunnu\Desktop\full ml projects\csvs\diabetes\diabetes.csv")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split



x=dib.drop("op",axis=1)
y=dib["op"]

x_tr,x_te,y_tr,y_te=train_test_split(x,y,test_size=.10,random_state=21)

log_mod=LogisticRegression()
log_mod.fit(x_tr,y_tr)
#print(log_mod.score(x_te,y_te))
joblib.dump(log_mod,"diabetes_model_joblib")



