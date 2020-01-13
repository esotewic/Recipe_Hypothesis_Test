# Recipe Analysis
## Eric Wang

### Background and the Data

Cooking can be fun but challenging. Finding the right recipe is not always easy.<br> Epicurious.com is a popular website for all types of recipes. I want to see if the tags are reliable and if I can find any indicators by looking at their recipes.

One of the features is the tag function. By tagging recipes, recipe publishers can give a bit more insight into the culture or background of the recipe. I will be analyzing their usage and accuracy.

![png](/pics/cupcakecloud.png)

# Work Flow
Recipe data is collected by using BeautifulSoup and MongoDB. It is then converted to Pandas Dataframe for EDA. Simple iteration functions were built for this. I then looked through the columns and extracted what I needed. Cleaned nan data where necessary.

# Plotting and Analysis
For each hypothesis, I would switch between filtering the recipe tags or ingredients. This involved simple pandas commands. To find my distributions, I would plot the density functions of the parameters I was checking. I noticed there were many outliers in the data so I had to clean the data.

![png](/pics/cleanvsunclean.png)

# Hypothesis Test
After plotting the distribution we can see that it is not a normal distribution. Thus I used the U-test for my hypothesis tests.

Hypothesis Test 1: Trying to lose weight is common in the summer. I chose to look at data with summer and winter tags and compare the fat content. I performed a U-test on my hypothesis

H0: summer fat content is higher than winter.
H1: winter fat is higher.

P<.02, Reject the null hypothesis (0.000398)

![png](/pics/wintervssummer.png)

# Conclusion
Although some of the data needed to be wrangled, I believe my hypothesis tests shows that the tags can be a reliable source when determining what kind of meals you want to cook. Whether it is a fatty winter dessert or a healthy summer/vegetarian dish, Epicurious is a great resource for delicious meals.
