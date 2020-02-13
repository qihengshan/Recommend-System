# --*-- coding: utf-8 --*--
import numpy as np
import pandas as pd


def create_ranked_df(movies, reviews):
    """
    INPUT
    movies - the movies dataframe
    reviews - the reviews dataframe

    OUTPUT
    ranked_movies - a dataframe with movies that are sorted by highest avg rating, more reviews,
                    then time, and must have more than 4 ratings
    """
    # movie_id分组 获取：[平均评分、评分量]
    movie_ratings = reviews.groupby('movie_id')['rating']
    avg_ratings = movie_ratings.mean()
    num_ratings = movie_ratings.count()

    # movie_id分组 获取：[最后评分时间]
    last_rating = pd.DataFrame(reviews.groupby('movie_id').max()['date'])
    last_rating.columns = ['last_rating']

    # 汇集统计数据
    rating_count_df = pd.DataFrame({'avg_rating': avg_ratings, 'num_ratings': num_ratings})
    rating_count_df = rating_count_df.join(last_rating)

    # rating_count_df 和 movies 根据movie_id融合, 增加三列 ['avg_rating', 'num_ratings', 'last_rating']
    movie_recs = movies.set_index('movie_id').join(rating_count_df)

    # 根据平均评分、评论数、最后评论时间排序
    ranked_movies = movie_recs.sort_values(['avg_rating', 'num_ratings', 'last_rating'], ascending=False)

    # 过滤评论数大于等于5条的数据
    ranked_movies = ranked_movies[ranked_movies['num_ratings'] > 4]

    return ranked_movies


def popular_recommendations(user_id, n_top, ranked_movies):
    """
    INPUT:
    user_id - the user_id (str) of the individual you are making recommendations for
    n_top - an integer of the number recommendations you want back
    ranked_movies - a pandas dataframe of the already ranked movies based on avg rating, count, and last rate time

    OUTPUT:
    top_movies - a list of the n_top recommended movies by movie title in order best to worst
    """
    # topN 电影列表
    top_movies = list(ranked_movies['movie'][:n_top])

    return top_movies  # a list of the n_top movies as recommended


def get_movie_names(movie_ids, movies_df):
    """
    INPUT
    movie_ids - a list of movie_ids
    movies_df - original movies dataframe
    OUTPUT
    movies - a list of movie names associated with the movie_ids
    """
    # 电影ID对应的电影名列表
    movie_lst = list(movies_df[movies_df['movie_id'].isin(movie_ids)]['movie'])

    return movie_lst


def find_similar_movies(movie_id, movies_df):
    """
    INPUT
    movie_id - a movie_id
    movies_df - original movies dataframe
    OUTPUT
    similar_movies - an array of the most similar movies by title
    """
    # dot product to get similar movies
    movie_content = np.array(movies_df.iloc[:, 4:])
    dot_prod_movies = movie_content.dot(np.transpose(movie_content))

    # find the row of each movie id
    movie_idx = np.where(movies_df['movie_id'] == movie_id)[0][0]

    # find the most similar movie indices - to start I said they need to be the same for all content
    similar_idxs = np.where(dot_prod_movies[movie_idx] == np.max(dot_prod_movies[movie_idx]))[0]

    # pull the movie titles based on the indices
    similar_movies = np.array(movies_df.iloc[similar_idxs, ]['movie'])

    return similar_movies

