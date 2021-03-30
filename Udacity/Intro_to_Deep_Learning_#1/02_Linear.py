import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt



#read data
dataframe = pd.read_csv('data1.csv')
x_values = dataframe[['hours']]
y_values = dataframe[['result']]

#train model on data
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)


#visualize results
plt.scatter(x_values, y_values)
plt.plot(x_values, body_reg.predict(x_values))
plt.show()