

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

In summary, from the above, it is clear that the probability that an event $A$ occurs given an event $B$ has occurred is not the same as the converse, namely the probability that an event $B$ occurs given an event A has occurred. 

This can lead to very misleading results. In this case, the probability that a person is a user of a drug given that they tested positively for it is still only 22.8%. Phrased another way, this means that even if someone tests positively for the drug it is still more likely that they are not a user of that drug. 

We can see from this that the probabilities of $A |B$ and $B|A$ depend on the base probabilities. If the base probability of $B$ or $A$ is relatively low, this can impact the difference in the outcome of the probabilities of $A|B$ versus $B|A$ 

Linear Regression
=

Linear Regression is just fitting a line to a set of observations.

We can use this to predict unobserved values.

The name "linear regression" is misleading, it doesn't necessarily have anything to do with time or backtracking. **It is just fitting a line to a set of data points.**

Linear regression uses the least squares algorithm.

It is a model in which we minimize the sum of squared errors from a line. That is, we compute $m$ and $c$ in the equation $y = mx + c$, for which the sum of squared differences from the data points to $y$ is minimized.

It is also known as the "maximum likelihood estimation". 

**Measuring error with r-squared**

How well does the line computed by the linear regression fit the data?

R-squared will vary from 0 to 1.

0 means that no variance in the model is captured, 1 means all of the variance is captured.

Polynomial Regression
=

Important to note is that in polynomial regression, we want to avoid overfitting or underfitting to our data.

That is, we want to find a value of n, for which our polynomial is of degree n, that fits our data sufficiently but does not overvalue outliers in its shape.


Multiple Regression
=

When developing a model for predicting the price of a car, there are multiple variables that you would want to consider.

This is an instance in which we would use multiple regression, that is, regression across multiple variables.

Multiple regression is therefore when the outcome we are calculating depends on multiple input variables or independent variables.

For instance:

$price = \alpha + \beta_{1}*mileage + \beta_{2}*age + \beta_{3}*doors$





Multivariate Regression
=

Multivariate Regression is when we are predicting multiple outcomes, for instance, not just the price of a car, but perhaps estimate the time it will run for before needing a new engine.

In this case there could be several input variables as well as several output variables as well.

Articulated concisely, this is basically just having multiple dependent variables.

Multi-Level Models
=

From the lecture, some things happen at various different levels in a hierarchy.

Your health, is a function of how healthy the cells in your body are. The health of your cells is a function of how healthy the organs they are contained within are. The health of your organs are a function of how healthy your body is, which is in turn a function of the state of the society in which you live.

Predicting SAT scores for instance, might be based on the home environment of the child, how educated their parents are, how much money their parents were willing to invest in their education, whether they were available to tutor their kids in the course, amongst many other factors.

