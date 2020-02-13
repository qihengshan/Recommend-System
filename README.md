```angular2html
In [1]: from recommender import Recommender

In [2]: rec = Recommender()

In [3]: rec.fit(reviews_pth='train_data.csv', movies_pth= 'movies_clean.csv', learning_rate=.01, iters=10)
Optimizaiton Statistics
Iterations | Mean Squared Error
1 		 12.104043
2 		 5.437694
3 		 3.239180
4 		 2.105978
5 		 1.428226
6 		 0.999180
7 		 0.718810
8 		 0.530387
9 		 0.400264
10 		 0.308054

In [4]: rec.predict_rating?
Signature: rec.predict_rating(user_id, movie_id)
Docstring:
INPUT:
user_id - the user_id from the reviews df
movie_id - the movie_id according the movies df

OUTPUT:
pred - the predicted rating for user_id-movie_id according to FunkSVD
File:      ~/py/Recommender-System/recommender.py
Type:      method

In [5]: rec.predict_rating(user_id=8, movie_id=2844)  # 预测用户8 对电影2844的评分
For user 8 we predict a 5.91 rating for the movie  Fantômas - À l'ombre de la guillotine (1913).
Out[5]: 5.911518928478018

In [6]: print(rec.make_recommendations(8, 'user'))  # 对用户8做出推荐
(array([1853728,  454876,   92965,  105695,  421715]), ['Empire of the Sun (1987)', 'Unforgiven (1992)', 'The Curious Case of Benjamin Button (2008)', 'Life of Pi (2012)', 'Django Unchained (2012)'])

In [7]: print(rec.make_recommendations(1853728))  # 相似电影
(None, ['Fahrenheit 451 (2018)', 'Death Wish (2018)', 'Den of Thieves (2018)', 'The Guernsey Literary and Potato Peel Pie Society (2018)', 'Tomb Raider (2018)'])

In [8]: print(rec.make_recommendations(1, 'user'))  # 基于排名的推荐
Because this user wasn't in our database, we are giving back the top movie recommendations for all users.
(None, ['Goodfellas (1990)', 'Step Brothers (2008)', 'American Beauty (1999)', 'There Will Be Blood (2007)', 'Gran Torino (2008)'])

In [9]: print(rec.make_recommendations(1))   # 电影不存与数据集中
That movie doesn't exist in our database.  Sorry, we don't have any recommendations for you.
(None, None)

```
