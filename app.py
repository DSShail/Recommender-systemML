import streamlit as st
import pickle

movies=pickle.load(open('movies.pkl', 'rb'))
similarities=pickle.load(open('similarities.pkl','rb'))

def recommend(movie):
    index=movies[movies['title'] == movie].index[0]
    distances=list(enumerate(similarities[index]))
    movie_list=sorted(distances,reverse=True,key= lambda x:x[1])[1:6]
    recommend_movies_list=[]
    for i in movie_list:
        movie_id=i[0]
        #fetch poster from api
        recommend_movies_list.append(movies.iloc[i[0]].title)
    return  recommend_movies_list

st.title('Movie Recommender System')
selected_movie=st.selectbox('please select a movie', movies['title'].values)
if st.button('Recommend'):
    recommended_movie=recommend(selected_movie)
    for i in recommended_movie:
        st.write(i)
