#!/usr/bin/env python
#Script for creating a Tag Based Recommender Engine 

"""Metrics to assess performance on regression task
Functions named as ``*_score`` return a scalar value to maximize: the higher
the better
Function named as ``*_error`` or ``*_loss`` return a scalar value to minimize:
the lower the better
"""

import pandas as pd
import pdb
import json
from sklearn.feature_extraction.text import TfidfVectorizer
path ="D:\\Codes\\Project Repo\\Git Projects\\test_repo\\dictionary python\\ml-latest-small\\"



"""
Data Source


 
movies : 
		'movie-id' ,'title','genres'

links	:
		'movieId', 'imdbId', 'tmdbId' 

ratings	:
		'userId', 'movieId', 'rating', 'timestamp'
		
tags	:
		'userId', 'movieId', 'tag', 'timestamp'
		
		
		
"""
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

movies = pd.read_csv(path+'movies.csv')
links = pd.read_csv(path+'links.csv')
ratings = pd.read_csv(path+'ratings.csv')
tags = pd.read_csv(path+'tags.csv')
tags = ratings[['userId','movieId','rating']].set_index('userId').join(tags,on=['userId','movieId'],how ='left')
# tags =tags.join(.set_index('userId'), on =['userId','movieId']) 
# pdb.set_trace()


def user_profile_generation(tags):
	"""
	
	Description
	-----------
	
	Creating user profiles for the entire user based on the ratings they have given for each movie.
	
	Parameters 
	----------
	Tags file which contains the entire list of tags 
	tags	: Type - <DataFrame>
	<schema>
		'userId', 'movieId', 'tag', 'timestamp'
	
	
	
	
	
	Returns
    -------
	User Profile contains the entire user base - tag profile
	User Profile : Type - <DataFrame> 
	<schema>
		'userId', 'user_tags', 'number_of_tags', 'no_of_movies'
	
	
	
	
	
	
	"""
	user_profile_dict ={}
	user_df = pd.DataFrame()
	user_df['userId'] = tags['userId'].unique()
	tag_profile_dict = {}
	for id in user_df['userId']:
		tag_profile_counts = tags[tags['userId']==id]['tag'].value_counts()
		  = list(tag_profile_counts.index)
		tag_profile_dict = tag_profile_counts.to_dict()
		pdb.set_trace()
		
		print (id, " --- > ",tag_profile)
		# print (list(tag_profile))
		user_profile_dict[id] = tag_profile #list()
	
	keys = list(user_profile_dict.keys())
	values =list(user_profile_dict.values())

	user_profile = pd.DataFrame()
	user_profile['userId'] = keys
	user_profile['user_tags'] =values
	user_profile['number_of_tags'] =tags['userId'].value_counts().tolist()
	user_profile['no_of_movies'] = tags[['userId','movieId']].drop_duplicates().groupby('userId').count()['movieId'].tolist()
	# pdb.set_trace()
	

	"""

	Output
	------
	   userId                                          user_tags   number of tags	no_of_movies
	0       2  [funny, Highly quotable, will ferrell, Boxing ...            1507			   3
	1       7                                     [way too long]             432			   1
	2      18  [Al Pacino, gangster, mafia, Mafia, holocaust,...             370			   7
	3      21        [romantic comedy, wedding, painter, bloody]             323			   3
	4      49                  [black hole, sci-fi, time-travel]             280			   1



	"""


	
	
	
	
	
	return user_profile
	
	
	
def user_profile_transformation(user_profile):
	
	"""
	Description
	-----------
	Creating user profiles tag vectors using Tf-idf Vectorization.
	tag vectors - array of tag weights
	
	Parameters
	----------
	User_Profile :	Type - <DataFrame>
		<schema> 'userId', 'user_tags',  'number_of_tags', 'no_of_movies'

	
	Returns
    -------
	User_Profile_Transformation	:	Type - <DataFrame>
		<schema>  'userId', 'user_tag_vectors'
	
	"""
	user_profile
	print (user_profile)
	





	
	
user_profile = user_profile_generation(tags)
user_profile_transformation(user_profile)
print (user_profile.head())     
	
print (tags.head())