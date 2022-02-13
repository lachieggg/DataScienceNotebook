Data Science Notes
=

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
