from colors import color
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

#sqlite database 'strain_master.db'


#move category column to end
# df1 =master_df.pop('category')
# master_df['category']=df1

#combine all attributes into a bag of words
# master_df['combined'] = master_df[master_df.columns[1:]].apply(
    # lambda x: ', '.join(x), axis=1)


master_df = pd.read_csv('master_for_recs.csv')

# instantiating and generating the count matrix
count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(master_df['combined'])

# generating the cosine similarity matrix
cosine_sim = cosine_similarity(count_matrix, count_matrix)

# # creating a Series for the strains so they are associated to an ordered numerical
# # list I will use in the function to match the indexes
# indices = pd.Series(master_df.index)

#  defining the function that takes in strain
# as input and returns the top 5 recommended strains
def recommended_strains(strain, cosine_sim = cosine_sim):

    # initializing the empty list of recommended strains
    recommended_strain_index = []
    recommended_strains = []

    # gettin the index of the strain that matches the strain
    idx = master_df[master_df['strain']==strain].index[0]

    # creating a Series with the similarity scores in descending order
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)

    # getting the indexes of the 5 most similar strains
    top_5_indexes = list(score_series.iloc[1:6].index)

    # populating the list with the titles of the best 5 matching strains
    for i in top_5_indexes:
        recommended_strain_index.append(list(master_df.index)[i])

    for i in recommended_strain_index:
        recommended_strain = master_df.ix[i]['strain']
        recommended_strains.append(recommended_strain)
    return recommended_strains

# print(recommended_strains('old toby'))

# build table with inputted strain and 5 most similar

def build_comp_table_vec(df, strain):
    strain_0 = df[df['strain'] == strain]
    strain_1 = df[df['strain'] == recommended_strains(strain)[0]]
    strain_2 = df[df['strain'] == recommended_strains(strain)[1]]
    strain_3 = df[df['strain'] == recommended_strains(strain)[2]]
    strain_4 = df[df['strain'] == recommended_strains(strain)[3]]
    strain_5 = df[df['strain'] == recommended_strains(strain)[4]]

    to_append = [strain_1, strain_2, strain_3, strain_4, strain_5]
    table = strain_0.append(to_append)

    return table

# top_matches = build_comp_table_vec(master_df, 'old toby')
# top_matches = top_matches.iloc[:, :-1]
# top_matches.style.applymap(color)
