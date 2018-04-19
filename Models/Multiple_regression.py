# Required Python Machine learning Packages
import pandas as pd
import numpy as np
# For preprocessing the data
from matplotlib import pylab
from sklearn.preprocessing import Imputer
from sklearn import preprocessing
# To split the dataset into train and test datasets
from sklearn.cross_validation import train_test_split
# To model the Gaussian Navie Bayes classifier
from sklearn.naive_bayes import GaussianNB
# To calculate the accuracy score of the model
from sklearn.metrics import accuracy_score
from sklearn import linear_model
from sklearn.metrics import mean_squared_error,r2_score


adult_df = pd.read_csv('VSRR_Provisional_Drug_Overdose_Death_Counts.csv')


le = preprocessing.LabelEncoder()
State_cat = le.fit_transform(adult_df.State)
StateName_cat = le.fit_transform(adult_df.StateName)
Year_cat   = le.fit_transform(adult_df.Year)
Month_cat = le.fit_transform(adult_df.Month)
Period_cat = le.fit_transform(adult_df.Period)
Indicator_cat = le.fit_transform(adult_df.Indicator)
DataValue_cat = le.fit_transform(adult_df.DataValue)
PercentComplete_cat = le.fit_transform(adult_df.PercentComplete)
PercentPendingInvestigation_cat = le.fit_transform(adult_df.PercentPendingInvestigation)


#initialize the encoded categorical columns
adult_df['State_cat'] = State_cat
adult_df['StateName_cat'] = StateName_cat
adult_df['Year_cat'] = Year_cat
adult_df['Month_cat'] = Month_cat
adult_df['Period_cat'] = Period_cat
adult_df['Indicator_cat'] =Indicator_cat
adult_df['DataValue_cat'] = DataValue_cat
adult_df['PercentComplete_cat'] = PercentComplete_cat
adult_df['PercentPendingInvestigation_cat'] = PercentPendingInvestigation_cat


#drop the old categorical columns from dataframe
dummy_fields = ['State', 'StateName', 'Year',
                  'Month', 'Period', 'Indicator','DataValue',
                  'PercentComplete','PercentPendingInvestigation']
adult_df = adult_df.drop(dummy_fields, axis = 1)


adult_df= adult_df.reindex_axis(['State_cat', 'StateName_cat', 'Year_cat', 'Month_cat',
                                    'Period_cat', 'Indicator_cat','DataValue_cat',
                                    'PercentComplete_cat', 'PercentPendingInvestigation_cat', 'PercentPendingInvestigation_cat', 'Footnote_cat'], axis= 1)


num_features = ['State_cat', 'StateName_cat', 'Year_cat', 'Month_cat','Period_cat',
                                     'Indicator_cat','DataValue_cat']

scaled_features = {}
for each in num_features:
    mean, std = adult_df[each].mean(), adult_df[each].std()
    scaled_features[each] = [mean, std]
    adult_df.loc[:, each] = (adult_df[each] - mean)/std


print(adult_df['DataValue_cat'].values)

features = adult_df.values[:,:4]
target = adult_df.values[:,6]
features_train, features_test, target_train, target_test = train_test_split(features,
                                                                            target, test_size = 0.20, random_state=10)

print(features.shape)
print(target.shape)
# clf = GaussianNB()
# clf.fit(features_train, target_train)
# target_pred = clf.predict(features_test)
regr=linear_model.LinearRegression()
regr.fit(features_train,target_train)
target_pred=regr.predict(features_test)
print("Coefficient",regr.coef_)
print("MEan Square %.2f"% mean_squared_error(target_test,target_pred))
print("Variance %.2f" % r2_score(target_test, target_pred))

print("Score is %.2f"% regr.score(features_test,target_test))

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

plt.hist(target_pred,bins=40)

#label
plt.xlabel('features')
plt.ylabel('target')
plt.show()



# Using seabron to create a linear fit
sns.lmplot('Indicator_cat','DataValue_cat',data = adult_df)
sns.plt.show()
