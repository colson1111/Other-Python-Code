#http://www.neural.cz/dataset-exploration-boston-house-pricing.html

import pandas as pd
from sklearn.datasets import load_boston

dataset = load_boston()
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
df['target'] = dataset.target

# get the shape of the data
instance_count, attr_count = df.shape

# summary statistics
df.describe()
df.info()


# missing values
pd.isnull(df).any()

# correlation
df.corr(method='pearson')

# predictivity:  correlation between predictors and target variable
pearson = df.corr(method='pearson')
corr_with_target = pearson.ix[-1][:-1]

pearson.ix[-1][:-1]
pearson.loc['target'][:-1]

predictivity = corr_with_target.sort_values(ascending=False, inplace=False)

# get strong negative correlations too
predictivity2 = corr_with_target[abs(corr_with_target).argsort()[::-1]]


# important correlations between input attributes
attrs = pearson.iloc[:-1,:-1]

threshold = 0.5 # consider it high correlation if it is higher than 0.5

important_corrs = (attrs[abs(attrs) > threshold][attrs != 1.0]).unstack().dropna().to_dict()

unique_important_corrs = pd.DataFrame( \
    list(set([(tuple(sorted(key)),important_corrs[key]) for key in important_corrs])),
    columns = ['attribute pair','correlation'])
    
# plotting
import seaborn as sns
import matplotlib.pyplot as plt

sns.corrplot(df)

sns.corrplot(df,annot=False,sig_stars=False,diag_names=False)

# matplotlib histogram
attr = df['AGE']
plt.hist(attr)
plt.hist(attr, bins=50)


# seaborn histogram
sns.distplot(attr)


# scatter plot
plt.scatter(df['AGE'], df['LSTAT'])

sns.jointplot(df['AGE'],df['LSTAT'], kind='scatter')

# matplotlib
x,y = df['AGE'],df['LSTAT']
plt.scatter(x,y,alpha=0.5)

# seaborn
sns.jointplot(x,y,kind='scatter',joint_kws={'alpha':0.5})

# hexagonal grid
sns.jointplot(x,y,kind='hex')
sns.jointplot(x,y,kind='kde')

