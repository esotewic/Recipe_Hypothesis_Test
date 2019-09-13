# Recipe Analysis
### Eric Wang

### Background and the Data

Cooking can be fun but challenging. Finding the right recipe is not always easy.<br> Epicurious.com is a popular website for all types of recipes. I want to see if the tags are reliable and if I can find any indicators by looking at their recipes.

One of the features is the tag function. By tagging recipes, recipe publishers can give a bit more insight into the culture or background of the recipe. I will be analyzing their usage and accuracy.

![png](/picture1.png)

# Work Flow
Recipe data is collected by using BeautifulSoup and MongoDB. It is then converted to Pandas Dataframe for EDA. Simple iteration functions were built for this. I then looked through the columns and extracted what I needed. Cleaned nan data where necessary.

#Plotting and Analysis
For each hypothesis, I would switch between filtering the recipe tags or ingredients. This involved simple pandas commands. To find my distributions, I would plot the density functions of the parameters I was checking. I noticed there were many outliers in the data so I had to clean the data.

![png](/picture1.png)
