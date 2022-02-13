# Data Science Notebook

Python data science code and notes for the [Data Science and Machine Learning course](https://www.udemy.com/course/data-science-and-machine-learning-with-python-hands-on/) on Udemy.

This repository is mainly for my own safekeeping.

- Almost all of the code comments are written by me
- Some code is modified by me from source code provided in the course
- Other sections, namely the exercise solutions were written from scratch by myself.
- Most of the code here was written by the [course author](https://www.udemy.com/user/frank-kane-2/).
- The notes markdown file is comprised of partially my own notes and partially notes from the lecture slides

Setup
=
```
cd MLCourseData
conda activate
jupyter notebook
```


Pandas
=
Pandas is a Python library for importing data from files and cleaning it up and manipulating it.

To learn about Pandas, open up:

```PandasTutorial.ipynb```


Statistics
=

**Mean** - the average, the sum of the possible outcomes divided by the number of outcomes

**Median** - the middle number, where 50% of the values are above and 50% below

**Mode** - the most common number

Probability
=

**Probability density function** - for continuous data, take the integral to find the probability of a random outcome being between two values.

**Probability mass function** - for discrete data.


Moments
=
Moments are ways to measure the shape of the distribution

The first moment is the *mean*.

The second moment is the *variance*.

The third moment is how lopsided the distribution is. It is called *skew*. 

The fourth moment is about how accentuated the peak of the distribution is. This value is known as *kurtosis*.

Covariance
=

Covariance measures how two variables vary together from their means.

Measuring covariance is done by first converting the data into two variables as high dimensional vectors.

Small covariance, close to 0, means that there isn't much correlation between the two variables.

Large covariance, that is, the absolute difference from 0 is large, indicates that there is a correlation. But what is "large"?

Correlation
=

Correlation is the covariance divided by the product of the standard deviations of the variables. This standardizes the covariance and gives us a more accurate picture of how the two variables behave. 

Correlation of 0, means that there is no relationship between the two variables.

A correlation of 1 is a perfect correlation, and -1 is a perfect inverse correlation. 

Correlation does not imply causation.

You cannot say anything about causation without running an experiment, but correlation will tell you what kind of experiments you might want to run.


Variables
=

In an experiment, there are the independent and dependent variables. The independent variables are the variables that you are varying. The dependent variable is the variable that you are measuring.

For instance, consider an experiment measuring the relationship between maths scores and room temperature.

The maths score would be the dependent variable, the room temperature is the independent variable or the variable that is being modified and allowed to vary. 

Conditional Probability
=

$Pr(B|A) = \dfrac{Pr(A,B)}{Pr(A)}$

$Pr(A,B) = Pr(B|A)*Pr(A)$

This is intuitive, since if $A$ has already occurred, the sample space is limited to situations where $A$ occurs. Therefore we should divide by the probability that $A$ occurs which *increases* the value of the fraction.

$Pr(A,B) = P(A)*P(B) \Longleftrightarrow A$ and $B$ are independent.

$Pr(A|B) = Pr(A)$ if $A$ and $B$ are independent

**Derivation**

$Pr(A|B) = \dfrac{Pr(A,B)}{Pr(B)}$

$=> Pr(A|B) = \dfrac{Pr(A)*Pr(B)}{Pr(B)}$ when $A$ and $B$ are independent

$=> Pr(A|B) = Pr(A)$

Another probability law:

$P(A|B) + P(¬A|B) = 1$

Bayes Theorem
=

$Pr(A|B) = \dfrac{Pr(A)Pr(B|A)}{Pr(B)}$

Event $A$ $->$ Person $X$ is a user of a drug $Y$

Event $B$ $->$ Person $X$ tests positive to drug $Y$

$P(B|A) = 0.99$

$P(¬B|¬A) = 0.99$

$P(A) = 0.003$

$P(B) = P(B,A) + P(B, ¬A)$

$= P(B|A)*P(A) + P(B|¬A)*P(¬A)$

$= 0.99 * 0.003 + P(B|¬A)*0.097$

$= 0.99 * 0.003 + (1-P(¬B|¬A))*0.097$

$= 0.99 * 0.003 + 0.01 * 0.097$

$= 0.013$

**Applying Bayes theorem**: 

$P(A|B) = \dfrac{P(A)*P(B|A)}{P(B)}$

$=\dfrac{0.003*0.99}{0.013}$

$= 0.228 $






