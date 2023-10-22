# Assignment 1: Data Cleaning
Since data cleaning is crucial before using any machine algorithm, kindly include a link to your Jupyter notebook that displays solutions and results for the following issues on a dataset:

- Missing values
- Outliers
- Duplicate records
- Data type issues
- Others (kindly include other issues regarding the dataset that you are using)


# Assignment 2: KNN
Using a cut down version of the Iris dataset, plot out the points on a 2D graph.

Here's the cut down version with 3 points per cluster:
```
petal_length, petal_width, cluster
1.7, 0.5, 0
1.4, 0.2, 0
1, 0.2, 0
4.7, 1.4, 1
4, 1.3, 1
4.5, 1.5, 1
5.6, 1.8, 2
5.1, 1.5, 2
5.3, 1.9, 2
```
Then, perform K-nearest neighbors with K = 3 to find the cluster of the following points:
```
(3, 1.1)
(1.8, 1.9)
(5, 1.75)
```
For each point, show how you selected the K other points (typically shown by closest distance) and show why the point should belong to a particular cluster.


# Assignment 3: Beyond Binary Classification
In this topic, we will dive deeper into what it means to have an imbalanced dataset and multiclass classifier by performing the following:

1. Create a notebook to show how to handle an Imbalanced dataset. Here is a reference for you to read:

https://www.justintodata.com/imbalanced-data-machine-learning-classification/#:~:text=Within%20it%2C%20we%20have%20imbalanced,is%20a%20highly%20imbalanced%20dataset.

Just pick two, perform them in your notebook, and write your discussion.

2. Choose a supervised ML that does multi-classification. Perform data cleaning, training, evaluation, and interpretation.


# Assignment 4: Gradient descent

Perform one step of gradient descent on the following unregularized objective using exponential loss:

L(w,b)=∑nexp[−yn(w⋅xn+b)]

With the following inputs:

$$X = \begin{bmatrix}1 & 1 & 1\\
2 & 2 & 1\\
1 & 2 & 3
\end{bmatrix}$$

$$Y = \begin{bmatrix}-1\\
1\\
1
\end{bmatrix}$$

$$w = \begin{bmatrix}0.64\\
0.5\\
0.85
\end{bmatrix}$$

$$ b = 1 $$

$$ n = 0.3 $$

Show the new weights, w
, and bias, b
, after one step and show your solution.

Submit the directory link of your notebook.

Reference book: http://ciml.info/dl/v0_99/ciml-v0_99-all.pdf

Go to pages 94 - 95 for the derivative of weights and bias


# Assignment 5: Kernel Methods
Kernel methods in machine learning

These are some of the many techniques of the kernel:

Support Vector Machine (SVM)
Adaptive Filter
Kernel Perception
Principle Component Analysis
Spectral Clustering
1. Choose 1 Kernel method that you want to explore.

2. Run a script to simulate its process.

3. Insert an explanation in between cells and give an introduction to the algorithm.


# Project 2: Perceptron
Here's a small diabetes data set.
```
glucose	bmi	bias	diabetic	w1	w2	wb
138	33.6	1	1	0.96	0.37	0.23
84	38.2	1	0	
125	28.9	1	1	
139	40.7	1	0	
145	44.2	1	1	
106	22.7	1	0	
```

1. Train a perceptron to predict whether an example presents a diabetic. Use 0.1 as your learning rate for those who haven't submitted yet.
2. Do only three epochs.
3. Create a video explaining the whole process. You may refer to the attached image to guide you in the simulation.


# Project 3: Neural Networks
Types of Algorithms used in Deep Learning
Here is the list of the top 10 most popular deep learning algorithms with their reference:

Convolutional Neural Networks (CNNs): https://www.analyticsvidhya.com/blog/2018/12/guide-convolutional-neural-network-cnn/
Long Short Term Memory Networks (LSTMs): https://medium.com/@aidangomez/let-s-do-this-f9b699de31d9
Recurrent Neural Networks (RNNs)
Generative Adversarial Networks (GANs)
Radial Basis Function Networks (RBFNs)
Multilayer Perceptrons (MLPs)
Self Organizing Maps (SOMs)
Deep Belief Networks (DBNs)
Restricted Boltzmann Machines( RBMs)
Autoencoders
1. Choose a deep learning algorithm that you want to implement.
2.  Perform manually two epochs of how to calculate the output. 
3. Create a python notebook to train the model.
4. Create a video discussing the concept, how the algorithm works, and the whole process. Include also its pros and cons.


# Practical Exam 1: Model Evaluation
We have several metrics for classification and regression problems. You can explore all the variables declared in each metric to see their values. The following are your tasks:

Choose 2 metrics from classification and regression where you will construct a graph to plot the result of the metric. You need to add a script to draw the plot,
Add a text or markdown cell to include the interpretation of each graph. You are expected to have 4 graphs all in all.
