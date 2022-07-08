Machine learning is a field concerned with building machine learning algorithms for predictive analysis purposes. The algorithms apply to data to predict the outcomes. The famous machine learning algorithms are:

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


### Linear regression:

- Linear regression is a widely used algorithm. Linear models make a prediction using a linear function of the input features, which we will explain shortly.
- It is used when the predictor variable is continuous in nature. For regression, the general prediction formula for a linear model looks as follows: ŷ = w[0] * x[0] + w[1] * x[1] + ... + w[p] * x[p] + b
- Here, x[0] to x[p] are features. w and b are parameters of the model that are learned, and ŷ is the prediction the model makes. Above is the function of multi-linear regression with multiple features.
- If we simply see the equation
ŷ = w[0] * x[0] + b
- This equation sounds familiar as it is an equation of the line we learned in school.
- Python provides a library called scikit learn has the linear regression method. We can call that function from the library.

### Logistic regression:

-	When the dependent or output variable is categorical, it called a classification problem. Regression model can be used for classification problem. Usually, it is called logistic regression. The formula for logistic regression is:
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
