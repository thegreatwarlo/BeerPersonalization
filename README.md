# BeerPersonalization

##### Background
For this project, we pretend to be an online craft beer retailer. Our goal is to develop an algorithm that generates purchase recommendations for our customers when they visit our website. The recommendations should take into account the customer’s taste and preferences while helping them discover new beers they have not tried before. For each user, we provide up to 10 beer recommendations each time they visit our website.

##### Challenges
Our project focuses on tackling the following challenges:
1. How can we build recommendations that take into account user preferences and taste?
2. How do we ensure that there is enough variety among the set of beers that are recommended during each user session?
3. How do we encourage users to explore beers/styles that they have not tried before - either because they are newly released items (not many reviews) or because they are a different type than the one usually consumed by the user? (serendipitous recommendations/novelty items)
4. How do we provide recommendations for users that just joined the service? (cold start problem)

##### Project in Abstract
1. Exploratory Data Analysis of BeerAdvocate dataset
2. Implementation and training of different algorithms (SVD , NMF, KNN and NLP Content based model(CBM)) across user subgroups.
3. Model Evaluation based on accuracy
4. Variety and Serendipity evaluation
5. Tackling the Cold Start Problem

##### Approach
Our recommendations are based off a number of different approaches, each of them targeting to one of more business challenges:
- Collaborative filtering/model based methods (targeting challenge #1)
- Popular items (#3, #4)
- Item based features (#2, #3)
- User Preferences (#4)

##### Data Source
For this exercise, we used data from the popular beer review website BeerAdvocate.com (available at https://snap.stanford.edu/data/web-BeerAdvocate.html).

#### Description
During the first phase, we focused on implementing two brute-force collabrative filterings to predict the user ratings for certain beers: neighborhood-based (including user-based and item-based) and model-based (specifically matrix factorization). We tested and compared the result of collaborative filtering approaches (both item and user based) and matrix factorization. Both models were developed using only the overall beer ratings (from 1 to 5), but we plan to expand the number of features in future iterations.

For the first phase, we focused our initial analysis on a subset of top 1,000 users and top 100 beers by number of reviews. We initially implemented item-based collaborative filtering using pandas dataframes, but due to performance issues we ultimately opted for a different implementation of collaborative filtering which leverages numpy arrays. Our initial findings shows that the user based collaborative filtering approach achieves the lowest RMSE and MAE for unobserved beer ratings (0.529 and 0.4 respectively), compared to SVD and NMF which achieved RMSE of 0.54 and 0.55 respectively. We suspects these results are in part due to the way we constructed our initial review subset, so we plan to test the performance of these approaches for larger and sparser datasets in the near future.

The "Final_Report" folder includes two jupyter notebooks which show how we trained and tested our final collaborative filtering and matrix factorization approaches respectively. The "Dataset" folder contains the subset of the dataset that we used for this initial phase. The "Others" folder includes obsolete files, including our initial item-based collaborative filtering implementation.

Collaborators:
- Ameya Karnad (ak4251)
- Carlo Provinciali (cp2984)
- Yilin Sun (ys2780)



