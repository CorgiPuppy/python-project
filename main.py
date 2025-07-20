from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression, Ridge, Lasso


housing = fetch_california_housing()

X = housing.data
y = housing.target

lr1 = LinearRegression()
lr1.fit(X, y)
print("Linear Regression")
for f, w in zip(housing.feature_names, lr1.coef_):
    print("{0:7s}: {1:6.2f}".format(f, w))
print("coef = {0:4.2f}".format(sum(lr1.coef_**2)))

lr2 = Ridge(alpha=10.0)
lr2.fit(X, y)
print("Ridge")
for f, w in zip(housing.feature_names, lr2.coef_):
    print("{0:7s}: {1:6.2f}".format(f, w))
print("coef = {0:4.2f}".format(sum(lr2.coef_**2)))

lr3 = Lasso(alpha=2.0)
lr3.fit(X, y)
print("Lasso")
for f, w in zip(housing.feature_names, lr3.coef_):
    print("{0:7s}: {1:6.2f}".format(f, w))
print("coef = {0:4.2f}".format(sum(lr3.coef_**2)))


