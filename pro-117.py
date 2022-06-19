import pandas as pd
df = pd.read_csv("BankNote_Authentication.csv")
print("df.head")
from sklearn.model_library import train_test_split
independent = df["independent"]
dependent=df["target"]
independent_train,independent_test,dependent_train,dependent_test= train_test_split(independent,dependent,data=75%25%)
from sklearn.model_library import LogisticRegretion
import numpy as np
x=np.reshape(independent.ravel(),(len(independent_train),1))
y=np.reshape(dependent.ravel(),(len(dependent_train),1))
x_test=np.reshape(independent.ravel(),(len(independent_test),1))
x_test=np.reshape(dependent.ravel(),(len(dependent_test),1))
dependent_prediction=classify.predict(x_test)
predicted_values_1 = []
