#### Language

```bash
Python >= 3.7
```

#### Library

```bash
Scikit learn
```

Machine learning is a field concerned with building machine learning algorithms for predictive analysis purposes. The algorithms apply to data to predict the outcomes. The famous machine learning algorithms are:

```bash
•	Linear regression

•	Logistic regression

•	Decision tree

•	SVM algorithm

•	Naive Bayes algorithm

•	KNN algorithm

•	K-means

•	Random forest algorithm

•	Dimensionality reduction algorithms

•	Gradient boosting algorithm and AdaBoosting algorithm
```

### Linear regression:

- Linear regression is a widely used algorithm. Linear models make a prediction using a linear function of the input features, which we will explain shortly.
- It is used when the predictor variable is continuous in nature. For regression, the general prediction formula for a linear model looks as follows: ŷ = w[0] * x[0] + w[1] * x[1] + ... + w[p] * x[p] + b
- Here, x[0] to x[p] are features. w and b are parameters of the model that are learned, and ŷ is the prediction the model makes. Above is the function of multi-linear regression with multiple features.
- If we simply see the equation
ŷ = w[0] * x[0] + b
- This equation sounds familiar as it is an equation of the line we learned in school.
- Python provides a library called scikit learn has the linear regression method. We can call that function from the library.

### Logistic regression:

-	When the dependent or output variable is categorical, it is called a classification problem. Regression model can be used for classification problem. Usually, it is called logistic regression. The formula for logistic regression is:
ŷ = w[0] * x[0] + w[1] * x[1] + ... + w[p] * x[p] + b > 0
-	It looks similar to linear regression, but instead of returning the weighted sum of features, we threshold the predicted value at zero. If the function is smaller than zero, we predict the class –1; if it is larger than zero, we predict the class +1.
- Outputs of logistic regression bounded by 0 and 1.
- Sigmoid function: The sigmoid function is used to predict values of probabilities into another value between 0 and 1.
- In Linear regression, predicted Y can exceed the 0 and 1 range, while in logistic regression, predicted Y lies within the 0 and 1 range. We get shape ‘S’ in logistic regression.

![image](https://user-images.githubusercontent.com/56231883/177996143-71b2ed17-e2f2-4f7c-aad6-efd78c6ae87b.png)

- The above function shows linear regression to predict some Y. The prediction Y can exceed. 

![image](https://user-images.githubusercontent.com/56231883/177996743-c7aa09d5-fff3-4a6b-93ce-47a60625de96.png)

- The above function shows the logistic regression to predict some Y. The prediction Y will always be between 0 and 1.

### Decision tree:

-	Decision trees are powerful way to solve classification and regression problems. Statistics

#### Basic Theory and Diagram
Here is a diagram of a basic decision tree. When you are doing regression, you may call this a 'regression tree'. There are MANY different flavors of tree-based models, and we'll learn about many of them in this class..

This image comes from [DataCamp](https://www.datacamp.com/community/tutorials/decision-trees-R) and is very well done.

<center>

![basic dt image](https://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1528907338/decision-tree_c2yyos.png)

</center>

Here's a breakdown of the terminology:

* **Root Node** represents the entire population or sample. It further gets divided into two or more homogeneous sets.

* **Splitting** is a process of dividing a node into two or more sub-nodes.

* When a sub-node splits into further *temporary or intermediate* sub-nodes, it is called a **Decision Node**.

* Nodes that do not split are called a **Terminal Node** or a Leaf.

* Is your model overfitting? You can control decision split criteria (like `min_samples_leaf` which says you can't split unless you end up with X samples in a leaf, and `max_depth` so that you limit the amount of interaction or depth of the tree), or you can remove sub-nodes of a decision node, which is called **Pruning**. The opposite of pruning is **Splitting**.

* A sub-section of an entire tree is called Branch.

* A node, which is divided into sub-nodes is called a **parent node** of the sub-nodes; whereas the sub-nodes are called the **child** of the parent node.

#### How to read a tree? `If/Then Statements`
A decision tree is simply a collection of if/then statements...

![if then statements](https://miro.medium.com/max/1648/0*J2l5dvJ2jqRwGDfG.png)

* IF the animal has feathers, and IF the animal can fly, THEN it is a hawk.
* If the animal does not have feathers, and IF the animal as fins, THEN it is a dolphin.

#### Pros and Cons
**Pros:** 
* the algorithm runs VERY fast and can quickly identify natural splits in the data.
* the algorithm is quite interpretable - you can literally read the rules that come from the tree.

**Cons:** 
* only makes one pass through the data - once data is partitioned, you can revisit rows and exploit their predictive power!
* might be too simple - unable to capture all of the nonlinearity that may be present.

### Support Vector Machines:

![image](https://user-images.githubusercontent.com/56231883/178104007-bf2ff90d-ffc3-4cdd-adfa-c7617cf35672.png)

- The above graph shows how some dots are placed on the line. Meaning it is unable to differentiate to which class these dots belong.
- To overcome this issue, a Support Vector Machine is used, which finds the hyperplane that maximizes the distance to the nearest point in each class.

### Naive Bayes:

- Naïve bayes classifier rely on bayes theorem. Naive Bayes uses for classification problems. It is an extremely fast and simple classification algorithm suitable for high-dimensional datasets.
- The model is called naïve since we do not expect the features to be independent or even conditional on the class label. If the assumption is not true, it still works great.
- The algorithm is efficient as they learn parameters by looking at each feature individually.

### K Nearest Neighbor:

- The KNN is an abbreviation of K Nearest Neighbor. There is no complex logic behind KNN. It is a simple model that does not require any complex mathematics. The only thing required in KNN is:

   •	Some notion of distance
   
   •	An assumption is that points that are close to one another are similar
   
- The ideology behind KNN is to predict the new data point. The algorithm finds the point in the training set that is closest to the new point. Then it assigns the label of this training point to the new data point.
- The K in Nearest Neighbor is instead of using only the closest neighbor, we can consider a fixed number k of neighbors in the training.


### K-Means:

- K-Means is a clustering algorithm. Clustering is an unsupervised technique where the labels of the data points are unknown.
- Clustering is the task of dividing a dataset into groups, called clusters.
- K-Means is the most commonly used clustering algorithm.
- It tries to find cluster centers that are representative of certain regions of the data. The algorithm alternates between two steps: assigning each data point to the closest cluster center and then setting each cluster center as the mean of the data points that are assigned to it. The algorithm is finished when the assignment of instances to clusters no longer changes.


### Random forest:

- Random forest is ensembled of decision trees. The drawback of the decision tree is it overfits the training data. Random forest addresses this problem.
- Random forest is a collection of decision trees where each tree is different from the others.

![RF diagram](https://miro.medium.com/max/851/1*Mb8awDiY9T6rsOjtNTRcIg.png)

-	A random forest simply fits many different decision trees and averages them together. Of course, what makes the random forest special are the components of randomness.

#### Why is it called a random forest?

Random Columns: this is shown in the documentation as `max_estimators` - so you are using a random subset of $n$ columns each time you build a tree - this is what makes the trees so different.

- You can also BOOTSTRAP and choose a random subset of rows! This is true by default and you can check the documentation for more details.
- Forest: this simply refers to the number of trees you select, this is known as `m_estimators` in the documentation.

**Pros:** RF will typically be your #1 or #2 model - it is robust to outliers and is a great, intuitive model!
 
**Cons:** can take some time to fit, categorical variables with many different values (especially rare ones) can be problematic, but this is true for most tree-based models.

###	Dimensionality reduction algorithms:

- In today's data world, a vast amount of data are being stored and analyzed. These data contain a lot of information, but the real challenge is identifying the useful variables.

- Dimensionality reduction algorithms like Decision Tree, Factor Analysis, Missing Value Ratio, and Random Forest can help you find relevant details.
