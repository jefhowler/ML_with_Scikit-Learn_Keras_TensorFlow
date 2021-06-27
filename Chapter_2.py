# Exercises
# 1. Try a Support Vector Machine regressor (sklearn.svm.SVR), with various hyperparameters such as kernel="linear"
# (with various values for the C hyperparameter) or kernel="rbf" (with various values for the C and gamma
# hyperparameters). Don't worry about what these hyperparameters mean for now. How does the best SVR predictor perform?
# Get the data
# Transform the data
# Figure out how to import his notebook
# Train and evaluate model using CV
#
# 2. Try replacing GridSearchCV with RandomizedSearchCV.
from scipy.stats import uniform
param_distributions = [
    {'kernel': ["linear"], 'C': uniform(loc=0, scale=1000)},
    {'kernel': ["rbf"], 'C': uniform(loc=0, scale=1000), 'gamma': uniform(loc=0, scale=1000)}
]
rscv = RandomisedSearchCV(
    svr, param_grid, n_iter=50, cv=5,
    scoring = 'neg_mean_squared_error',
    return_train_score = True
)
# 3. Try adding a transformer in the preparation pipeline to select only the most important attributes.
# Add a transformer to preparation pipeline:
    # How do I create a transformer?
    # How do I create a transformer which selects a subset of attributes?
        # How do I drop attributes?
from sklearn.base import BaseEstimator, TransformerMixin


class SelectRelevantAttributes(BaseEstimator, TransformerMixin):
    def __init__(self):
        return self
    def fit(self, X):
        return self
    def transform(self, X):
        X = X.drop("housing_median_age", axis = 1)
        # add further unimportant attributes to drop
        # paramterise attributes to drop
    # Decide which attributes are the most important
        # Which attributes correlate the most with house price
    # Hardcode those attributes into the Transformer
 # How do I add a transformer to the preperation pipeline?

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

filter_attribs = SelectRelevantAttributes()
housing_filtered_attribs = filter_attribs.transform(housing)
prep_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy="median")),
    ('attribs_adder', CombinedAttributesAdder()),
    ('std_scaler', StandardScaler()),
    ('filter_attribs', SelectRelevantAttributes()),
])

list_attribs = list(housing)

full_pipeline = ([
    ("filter", SelectRelevantAttributes(), list_attribs),
    ("num", num_pipeline, num_attribs),
    ("cat", OneHotEncoder(), cat_attribs),
])

# or
drop_attribs = ["median_house_age"]

full_pipeline = ([
    ("filter", "drop", drop_attribs),
    ("num", num_pipeline, num_attribs),
    ("cat", OneHotEncoder(), cat_attribs),
])
# 4. Try Creating a single pipeline that does the full data preperation and the final prediction

# 5.