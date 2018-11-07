# BeerPersonalization
The goal of this project is to create a beer recommendation system using personalization algorithms such as collaborative filtering and matrix factorization. We hope build a model that can suggest users new beers to try based on their preferences

For this exercise, we used data from the popular beer review website BeerAdvocate.com (available at https://snap.stanford.edu/data/web-BeerAdvocate.html).
During the first phase, we focused on implementing two brute-force collabrative filterings to predict the user ratings for certain beers: neighborhood-based (including user-based and item-based) and model-based (specifically matrix factorization). We tested and compared the result of collaborative filtering approaches (both item and user based) and matrix factorization. Both models were developed using only the overall beer ratings (from 1 to 5), but we plan to expand the number of features in future iterations.

For the first phase, we focused our initial analysis on a subset of top 2,000 users and top 200 beers by number of reviews. Our initial findings shows that the user based collaborative filtering approach achieves the lowest RMSE and MAE for unobserved beer ratings (0.529 and 0.4 respectively), compared to SVD and NMF which achieved RMSE of 0.54 and 0.55 respectively. 
