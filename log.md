# 100 days of ML code
I have been working on Machine learning from last few weeks. And I came across the Siraj's Video to take up the pledge of 100 days of ML coding. I created this Reopository to mark my progress.

## Day 1
### (7th July 2018 IST 15:54)

***Today's progress*** :  Started with ML. Revised Python.<br>
***Thoughts*** : Today I started with the book "Data Science from scratch - first principles" by Joel Grus. I read first chapter which mostly gives introduction to data science. It also talks about some real time problem and their solutions. I also revised some python syntax and watched 10-12 videos of Sentdex Python Intermediate. I also got a video series on Machine learning by Andre NG. I will start the video series from tommorow.

## Day 2
### (8th July 2018 IST 21:29)

***Today's progress*** :  Started with Andrew NG. Started with gradient descent.<br>
***Thoughts*** : Today I started with my first algorithm for machine learning. I saw Siraj Raval's Video about Linear Regression using gradient descent. I typed code along with him. But, i dont know why, his output and my output differ on the same dataset. I must have done something wrong. Then, I saw videos from Andrew NG about linear regression. He explained it in a different manner. His notations and explaination was different. But after 2-3 videos i figured it out that it was the same as explained by siraj. I dont think i can say i understood gradient descent 100% but i will keep trying to study and understand how to minimize cost using it. Tomorrow i will continue watching Andrew NG's videos and read next chapter from the book "Data Science from scratch - first principles" by Joel Grus.<br>
***Link to work*** : [linear regression](https://github.com/DevashishPrasad/100_Days_of_ML_Code/tree/master/Linear-regression)

## Day 3
### (10th July 2018 IST 16:05)

***Today's progress*** : Fixed the error in linear regression<br>
***Thoughts*** : Today I fixed the error in my linear regression code. The error was very minute mistake in the formula of gradient descent. I also saw next videos in series of Andrew NG. He explained linear regression in other way. He also explained gradient descent. And now i can say that i have a better understanding of the algorithm. I need to focus and learn more about calculus to be perfect in gradient descent. Later in his video series he started with Linear algebra. I already knew about basics of it so watched a couple of videos in 1.75x speed. Tomorrow I will start will next chapter from book "Data Science from scratch - first principles" by Joel Grus.<br>
***Link to work*** : [linear regression error fixed](https://github.com/DevashishPrasad/100_Days_of_ML_Code/tree/master/Linear-regression)

## Day 4
### (11th July 2018 IST 16:20)
***Today's progress*** : Started with Linear Regression with multiple variables<br>
***Thoughts*** : Today I fininshed the basics linear algebra such as - Matrices and Vectors, Addition and Multiplication, Inverse and Transpose. I also started with Linear regression with multple variables or multiple features. Andrew NG explained the difference between both algorithms.<br>
We get our new function as - **h(x) = t0 + t1x1 + t2x2 + ..... + tnxn** (Where n us number of features). I also learnt about optimization of our new function. The new gradient descent algorithm which is derivative of cost function is repeated till the convergence for all values of ti (Where i is the index of a feature).<br>
Inorder to optimize the gradient descent for our algorithm we make sure that our features lie on the same scale. This is known as feature scaling. For eg - we have two features as  **x1 = size( 0 - 2000 ) feet** and **x2 = num_of_rooms (1 - 5)**. So, we can scale these features as **x1= size()/2000 therefore, 0 <= x1 <= 1 and x2 = num_of_rooms()/5 therefore, 0 <= x2 <= 1**. In this way, our gradient descent will converge faster.<br>
***Link to work*** : [linear regression with multiple variables](https://github.com/DevashishPrasad/100_Days_of_ML_Code/tree/master/Linear-Regression-with-multiple-variable)

## Day 5
### (12th July 2018 IST 16:20)
***Today's progress*** : Linear Regression with multiple variables<br>
***Thoughts*** : Today I continued watching Andrew NG. I learnt about the properties of gradient descent such as number of iterations required and learning rate. We should use a threshold such as 10^-3, if rate of change decreases this threshold value we stop iterating. Learning rate should be ideal. If Learning rate is too small then gradiemt descent will take longer to converge. If learning rate is large then it may overshoot. I also learned how to make new features from existing features inorder to simplify our algorithm. Instead of a straight line we can also fit a polynomial functions. I did not get enough time today but will cover huge amout of work this weekend. <br>
***Link to work*** : [linear regression with multiple variables](https://github.com/DevashishPrasad/100_Days_of_ML_Code/tree/master/Linear-Regression-with-multiple-variable)

## Day 6
### (16th July 2018 IST 22:50)
***Today's progress*** : An alternative for gradient descent<br>
***Thoughts*** : Today I continued watching Andrew NG. I learnt about the normal equation used to minimizde the weights or the theta in the hypothesis equation of linear regression. The equation is **t = (XT * X)^-1 * XT * y (where XT = X Transpose)**. This equation has some pros and some cons. Advntages of this equation are <br>1) It does not require any learning rate<br>2) It does not require iterations.<br> Disadvantages of this equation are - <br> 1) It is unsuitable for large dataset<br>2) It fails when XT * X is non-invertible<br>I also learnt about a new language recommended by Andrew NG for machine learning "Octave". I installed Octave on my computer and performed basic opertaions such as Arithmetic operations, Using Matrices and Vectors, initializing matrices and vectors using inbuilt functions.<br>

## Day 7
### (17th July 2018 IST 22:23)
***Today's progress*** : Octave, logistic regression and reinforcement learning<br>
***Thoughts*** : Today I continued watching Andrew NG. I have now finished watching 32 videos. I learnt about the octave language for ML. I learnt how to move data around like sizing, loading, saving and clearing data. I also learnt about slicing arrays and matrics in octave like we do in Numpy. Computing data is easier in octave. We can use functions like - abs(), max(), log(), exp(), sum(), floor(), ceil(), pinv() etc. We can also plot data in octave using some functions like - plot(), xlabel(), ylabel(), figure(), subplot() and axis(). I feel like octave is a bit complex and I am more familiar with Python. So from now onwards I am convinced that python is the best language for machine learning. Numpy is a great library for performing linear algebra calculations and Matplotlib is great for  visualizing data. So I am done with Octave.<br>
About Logistic regression I have an introductory knowlege. I learnt that this algorithm is used for classification. Andrew also proves that classification is possible using linear regression but it will fail often. So, best algorithm for classificatio is Logistic regression. Classification is chosen or practiced when we have data with y = 1 or 0. This can be Yes or No, True or False, Red or Blue and what not. We can also use Logistic regression for multi class classification where y can be {0 or 1 or 2 or ... n}. It is again, a type of supervised learning.<br>
Reinforcement Learning is a type of supervised learning with unlabelled dataset. It has 5 elements -<br>
1) Actor
2) Environment
3) Reward
4) State
5) Action<br>

Letz take an example of a self driving car. Here, Car is the actor and Road is environment. Whether the car is moving or still describes the state of the car. When depending on the state and environment car does an action i.e. if there is green light on the signal car moves, then this is known as action. Based on action of the car(actor) we give it a reward. A reward can be positive or negative. For eg. if car moves when light is red is a false action so it gets a negative reward and car moves when light is green is a positive reward.

## Day 8
### (18th July 2018 IST 23:35)
***Today's progress*** : Pandas and Matplotlib<br>
***Thoughts*** : Today I continued watching Andrew NG. I learnt more about logistic regression. I learnt that we need to use log functions as cost functions for logistic regression. I also learnt about the decision boundaries. Then I decided to practice my own linear regression fro scratch. I started searching for datasets and found the iris petal dataset perfect for simple linear regression. I downloaded it in the form of .xls file. I then used Pandas dataframe to fetch the data can convert it into the numpy arrays. I successfully did it. I aslo watched a tutorial on Pandas library. I learnt to fetch data from various formats such as csv, xml, dict, json etc. I was also able to now use the basic functions such as max(), min(), abs(), describe etc. <br>
Once i was able to successfully grab the data. I used matplotlib to visualize it. I used scatter plot to visualize it.

<img src="images/img1.png" alt="picture not available"/>

***Link to work*** : [simple linear regression or iris setosa sepals](https://github.com/DevashishPrasad/100_Days_of_ML_Code/tree/master/simple%20linear%20regression%20for%20iris%20petals)

## Day 9
### (19th July 2018 IST 23:57)
***Today's progress*** : Linear regression from scratch<br>
***Thoughts*** : Today I implemented linear-regression model for iris petal dataset from scratch using gradient descent. I took data from xls file through pandas dataframe. Then implemented gradient descent partial derivatives formulae and minized the values of m and c (b) of the equation y = mx + c. <br>
I finally plotted both the dataset and the line on a chart to visualize the results<br>
Encountered lot of errors... and solved each one of them
<br>
<img src="images/img2.png" alt="picture not available"/>

***Link to work*** : [simple linear regression or iris setosa sepals](https://github.com/DevashishPrasad/100_Days_of_ML_Code/blob/master/simple%20linear%20regression%20for%20iris%20petals/my_linear.py)

## Day 10
### (20th July 2018 IST 23:59)
***Today's progress*** : Multiple Linear regression from scratch<br>
***Thoughts*** : Today I read a couple of articles about multiple linear regression. I find it confusing and challenging. I also saw couple of videos which therotically explains how to implement it. I also gathered dataset to work upon. The dataset is systolic blood pressure prediction using age and weight of patient. Today i am successfull in taking data in python code from .xls file through pandas.<br> 
***Link to work*** : [multiple linear regression](https://github.com/DevashishPrasad/100_Days_of_ML_Code/tree/master/Linear-Regression-with-multiple-variable)

## Day 11
### (23th July 2018 IST 23:59)
***Today's progress*** : Multiple Linear regression from scratch<br>
***Thoughts*** : Today I visualized the data I gathered about systolic blood pressure in a 3d scatter plot. I checked for the collinearity of the dataset and found a strong one. I then started to implement linear regression with multiple variables from scratch. I am successful in bringing the data but i am facing an error in the gradient descent part. I need to study the algorithm more deeply and figure out what is the exact issue. Here is the visualizarion - <br>
<img src="images/check.png" alt="picture not available"/>

***Link to work*** : [multiple linear regression](https://github.com/DevashishPrasad/100_Days_of_ML_Code/tree/master/Linear-Regression-with-multiple-variable)

## Day 12
### (24th July 2018 IST 22:55)
***Today's progress*** : Multiple Linear regression from scratch error fixed<br>
***Thoughts*** : Today I solved the error from my code for multiple linear regression. It was mistake in the shapes of matrices while taking their dot product. The model predicted the systolic blood pressure when given age and weight as input with good enough accuracy. I successfully completed the algorithm from scratch using gradient descent. Now, I am on my way to implement logistic regression from scratch. I am clear with the concept and loss function. I just need to find a dataset and start working on it.<br>
***Link to work*** : [multiple linear regression done](https://github.com/DevashishPrasad/100_Days_of_ML_Code/blob/master/Linear-Regression-with-multiple-variable/regression.py)

## Day 13
### (27th July 2018 IST 22:55)
***Today's progress*** : Logistic regression<br>
***Thoughts*** : Today I again saw videos of Andrew NG about logistic regression and on the way to implement it from scratch. I am now clear with its cost function and gradient descent optimization. I also came across the multi-class logistic regression. It is just an enhanced version of simple logistic regression.<br>

## Day 14
### (28th July 2018 IST 22:55)
***Today's progress*** : Linear Algebra<br>
***Thoughts*** : Today I saw linear algebra videos from MIT open courseware from prof. Gilbert stang. I learnt about matrices, spaces, rank and other concepts. Nothing else today<br>

## Day 15
### (29th July 2018 IST 22:40)
***Today's progress*** : Logistic regression<br>
***Thoughts*** : Today I spent most of my time to draw a line in 3d graph in matplotlib. I want to fit the exact line of prediction in my multiple regression model. I was not successful at it. I learnt how to draw a 3d line but was not able to generate the line through the equation (hypothesis)<br>
I found a good data set for logistic regression. I will create a binary classifier from scratch with this dataset and then use the same for multi-class classification.<br>
***Link to work*** : [Logistic regression dataset](https://github.com/DevashishPrasad/100_Days_of_ML_Code/tree/master/logistic%20regression)

## Day 16
### (31th July 2018 IST 20:10)
***Today's progress*** : Logistic regression data analyzation<br>
***Thoughts*** : Today I started to find decision boundaries between my dataset of house satisfaction rates. I read data from raw file using pandas. Then I filtered and cleaned the data. I usied matplotlib to draw two scatter plots for two classes respectively. But I dont see any decision boundry I can work on. I get all blue(2nd class) dots which overlap the first class data. So its a bad idea and a bad dataset and need to find a good dataset.<br>
<img src="images/house.png"/><br>
***Link to work*** : [Logistic regression house dataset](https://github.com/DevashishPrasad/100_Days_of_ML_Code/tree/master/Logistic%20Regression)

## Day 17
### (1st August 2018 IST 20:20)
***Today's progress*** : Logistic regression data analyzation<br>
***Thoughts*** : Today I started the hour in a search of a good dataset. I thought I found a good dataset. Th dataset was about the calssification of breast cancer events. As usual I used pandas to read the data and matplotlib to visualize it. I randomly chose two features and used classified it in two classes. Then I plotted it on the scatter chart and still i did not find a good decision boundary. Here is the image of the dataset.<br>
<img src="images/cancer.png"/><br>
***Link to work*** : [Logistic regression breast cancer dataset](https://github.com/DevashishPrasad/100_Days_of_ML_Code/tree/master/Logistic%20regression%20for%20breast%20cancer)

## Day 18
### (2nd August 2018 IST 20:20)
***Today's progress*** : Logistic regression data visualization with Iris dataset<br>
***Thoughts*** : Today I worked on the same dataset to find a good classification problem. But it was again a failure. So I then found easiest datset for logistic regression of Iris petals from scikit learn library. I chose two classes (it has 50 records for each) with 100 records as a whole dataset. I used Matplotlib to visualize the dataset using scatter chart. And finally I successfully found a very good datsset. The decision boundary was clearly visible.<br>
<img src="images/iris_logistic.png"/><br>
***Link to work*** : [Logistic regression with Iris petal dataset](https://github.com/DevashishPrasad/100_Days_of_ML_Code/tree/master/Logistic%20regression%20Iris)

## Day 19
### (3rd August 2018 IST 23:25)
***Today's progress*** : Logistic regression implementation on Iris dataset<br>
***Thoughts*** : Today I worked on the same dataset and started the implementation of Logistic regression. I followed the formulae of Andrew NG and implemented them. Somehow, I have a calculation bug with weights in my program. I need to figure it out. Everything else like hypothesis function, cost function and gradient descent optimization formulae correctly. But still i will check everything once again.<br>
***Link to work*** : [Logistic regression with Iris petal dataset](https://github.com/DevashishPrasad/100_Days_of_ML_Code/blob/master/Logistic%20regression%20Iris/logistic.py)

## Day 20
### (4th August 2018 IST 23:25)
***Today's progress*** : Logistic regression finished<br>
***Thoughts*** : Today I finally figured out the bug. It was due to the bad shape of the array of outputs(Y). I used numpy reshape function to fix it. I trained the model for 30000 steps with learning rate 0.1. I also tested it on a sample value from the dataset and model predicts with a good accuracy.<br>
***Link to work*** : [Logistic regression with Iris petal finished](https://github.com/DevashishPrasad/100_Days_of_ML_Code/blob/master/Logistic%20regression%20Iris/logistic.py)

## Day 21
### (7th August 2018 IST 21:39)
***Today's progress*** : Multiclass Logistic regression<br>
***Thoughts*** : Today I started with multiclass logistic regression, I started the hour by watching siraj ravals logistic regression video. Then I saw Andrew NG's logistic regression video. I understood the algorithm theoretically. Then i searched a dataset for multi-class classification. I also visualized the iris dataset with 3 classes but the 3rd class was not clearly apart. So, to learn the algorithm i decided to use a good dataset. I found a dataset on UCI machine learning repositories with has 7 classes to classify type of glass. Tommorow i will start with the algorithm<br>
***Link to work*** : [Multiclass Logistic regression dataset](https://github.com/DevashishPrasad/100_Days_of_ML_Code/tree/master/Multi-class%20Logistic%20Regression)

## Day 22
### (8th August 2018 IST 21:19)
***Today's progress*** : Pickling<br>
***Thoughts*** : Today I read a couple of articles about Pickling. I learnt how to use pickle package in python to save the state of program. pickle.dump() and pickle.load() ar the main methods to use pickle. Not much ML today.

## Day 23
### (9th August 2018 IST 21:19)
***Today's progress*** : Softmax function<br>
***Thoughts*** : Today I started with multi-class logistic regression also known as multinomial or softmax regression. Here, we have more than 2 classes and our job is to find probability of each class over an event. Softmax function is used to achieve this. It gives us the probabilities of every class. Today I read some articles and studied the therotical parts of the model.<br>

## Day 24
### (24th October 2018 IST 19:00)
***Today's progress*** : Towards Neural Networks<br>
***Thoughts*** : Today I finally resumed my machine learning journey. Couple of months i was very busy in my under grad admission and new college life. I am now finally settled and back to my track. I am now trying to code my first neural network from scratch. I found 3 amazing articles written by Piotr Skalski on Medium.com (towards data science). The guy explained all about the neural networks very precisely. Here are the links - <br>
[PART I](https://towardsdatascience.com/https-medium-com-piotr-skalski92-deep-dive-into-deep-networks-math-17660bc376ba) <br>
[PART II](https://towardsdatascience.com/preventing-deep-neural-network-from-overfitting-953458db800a) <br>
[PART III](https://towardsdatascience.com/lets-code-a-neural-network-in-plain-numpy-ae7e74410795) <br>
I also made a python from his ipynb. I did not run it as I dont have confidence in my understanding of neural networks. I will be coding one from scratch. <br>
***Link to work*** : [First Neural Network](https://github.com/DevashishPrasad/100_Days_of_ML_Code/tree/master/First%20Neural%20Network)

## Day 25
### (25th October 2018 IST 22:00)
***Today's progress*** : Andrew NG neural networks<br>
***Thoughts*** : Today I started with Andrew NG Neural network series. He has many videos on neural networks. I completed 4-5 videos. I unterstood the basic working, conventions, idea and concept of mapping non linear function (complex) using neural networks.<br>

## Day 26
### (26th October 2018 IST 22:30)
***Today's progress*** : Continued Andrew NG neural networks<br>
***Thoughts*** : Today I continued Andrew NG Neural network series. He now started explaining the complex part of neral networks. I learnt how a neural network forward propagates. I also learnt about the Back propagation algorithm. I am not clear with back propagation yet but have a baasic understanding of what it is doing.<br>

