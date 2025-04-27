import pandas as pd

tweets = pd.read_csv("archivos/02 vaccination_tweets.csv")

# print(tweets.head(5))
# print(tweets.info())

# ¿Cuántos tweets hay en total?
# print ("Hay en total:" ,tweets['retweets'].count())


# ¿Cuántos usuarios únicos han twitteado?
unicos = tweets['user_name'].unique()
# print(unicos.size)


# ¿Cuál es el tweet con más retweets?
retweets = tweets['retweets'].idxmax()
mayor = tweets.loc[retweets]
# print(mayor['retweets'])


# ¿Qué usuario escribió el tweet con más retweets?
# print(mayor['user_name'])


# ¿Cuál es el promedio de favoritos (likes) por tweet?
promedio = tweets['favorites'].mean()
# print("Promedio: ",promedio)

favoritos_positivos = tweets[tweets['favorites'] > 0]['favorites']
promedio = favoritos_positivos.mean()
# print("Promedio (sin contar ceros):", promedio)

# ¿Cuántos tweets tienen más de 500 favoritos?
mayor_quinientos = tweets ['favorites'] > 500
# print ("Tweets mayor a 500 likes: ", mayor_quinientos.sum())


# ¿Cuántos tweets contienen la palabra "Python"?
contiene = tweets ['text'].str.contains("and", case=False)
# print(contiene.sum())


# ¿Cuáles son los 5 usuarios con más tweets publicados?
usuarios = tweets.sort_values('retweets', ascending=False)
# print(usuarios.head(5))

# El promedio de retweets, sin considerar a aquellos usuarios que no tienen retweetts
promedio_retweets = tweets[tweets['retweets'] > 0]['retweets']
print( promedio_retweets.sum()) 
print( promedio_retweets.count()) 
print( promedio_retweets.mean()) 
print( promedio_retweets.sum() / promedio_retweets.count() )  


