# Exercises
# 1. How would you define Machine Learning?
# A programme learns from experience (E) at task (T) if its performance (P) at task (T) improves with experience (E).
# 2. Can you name 4 types of Problem where it shines?
# - The existing solution requires lots of fine tuning or long lists of rules.
# - Getting insights from complex problems and large amounts of data.
# - Fluctuating environments: a Machine Learning System can adapt to new data.
# - Complex problems for which using a traditional approach yields no good solution:
#   ML techniques can sometimes find a solution.
# 3. What is a labelled training set?
# The data set points are labelled with the desired values that the model is predicting on e.g. a model predicting the
# probability that a patient has cancer trained on a training set that includes past patients diagnosis.
# 4. What are the two most common supervised tasks?
# - Classification
# - Predicting a target numeric value
# 5. Can you name 4 common unsupervised tasks?
# - Anomaly Detection
# - Clustering
# - Visualisation and Dimensionality reduction
# - Association rule learning
# 6. What type of machine learning algorithm would you use to allow a robot to walk in various unknown terrains?
# Reinforcement learning
# 7. What type of algorithm would you use to segment your customers into multiple groups?
# Clustering
# 8. Would you frame the problem of spam detection as an unsupervised learning task or a supervised one?
# Supervised
# 9. What is an online learning system?
# The system learns from data incrementally. It is fed data as mini-batches and learns from these batches quickly rather
# than needing to be trained on the whole data set whenever it is fed new data instances.
# 10. What is out of core learning?
# Using an online learning algorithm to train systems on datasets without needing to hold the whole dataset in memory.
# 11. Association learning model
# 12. What is the difference between a model parameter and a learning algorithm's hyperparameter?
# - Model parameter - parameters to the system model that are tweaked to fit it to the data.
# - Hyperparameter - parameter to the learning algorithm that is tweaked to constrain the model parameters to a range
#   of values.
# the difference - model paramteres are tweaked by the learning algorithm. A hyperparamter is not, it remains constant
# during training.
# 13. They search for patterns in the whole dataset by fitting the model to the training set. They make predictions by
# relating the input variable of the data point to the output variable.
# 15. - simplify the model
#     - enlarge training set
#     - reduce noise of training set
# 14. 4 of the main challenges of machine learning
#     - Poor training set data
#       - unrepresentative
#       - noisy feature set
#     - poor ML algorithm:
#       - underfits data
#       - overfits data
# 16. What is a test set and why would you want to use it?
#     To ensure that your model generalises to an acceptable standard.
# 17. Purpose of a validation set?
#     To select the most suitable model and hyperparamters.
# 18. What is a train dev set and when would you use it? How would you use it?
#     A dataset made up of data instances that you trained your model on that aren't as representative of the instances
#     being predicted on as the test set. You need it when the model performs poorly on validation and there is a
#     mismatch between training set and validation + test set. If model does well on train dev set then you need to
#     make training set more representative of data instances in production. If poorly then your model overfits the
#     training data.
# 19. What can go wrong if you tune hyperparamters using the test set?
# The learning model has a poorer generalisation error in production than on test set as it overfits the test set.

