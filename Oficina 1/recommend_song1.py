

# Filtragem colaborativa para recomendação de música

# Conjunto de dados de exemplo
#Temos um conjunto de dados com informações sobre usuários, músicas e classificações.
data = [{
  "user": "Alice",
  "song": "A",
  "rating": 5
}, {
  "user": "Bob",
  "song": "A",
  "rating": 3
}, {
  "user": "Charlie",
  "song": "A",
  "rating": 4
}, {
  "user": "Alice",
  "song": "B",
  "rating": 4
}, {
  "user": "Bob",
  "song": "B",
  "rating": 5
}, {
  "user": "Charlie",
  "song": "B",
  "rating": 3
}, {
  "user": "Alice",
  "song": "C",
  "rating": 2
}, {
  "user": "Bob",
  "song": "C",
  "rating": 2
}, {
  "user": "Charlie",
  "song": "C",
  "rating": 1
}, {
  "user": "Charlie",
  "song": "D",
  "rating": 5
}]


# Função para calcular a distância entre dois usuários
#Usamos a função calculate_distance para calcular a distância entre dois usuários baseado nas músicas que eles têm em comum e suas classificações. A métrica usada para calcular a distância entre dois usuários é a distância euclidiana. Ela é calculada como a raiz quadrada da soma das diferenças ao quadrado entre as classificações dos usuários para cada música em comum. Essa distância é usada para determinar a similaridade entre os usuários. Quanto menor a distância, maior a similaridade.
def calculate_distance(user1, user2):
  common_songs = []
  for d in data:
    if d["user"] == user1:
      for d2 in data:
        if d2["user"] == user2 and d["song"] == d2["song"]:
          common_songs.append(d["song"])
  distance = 0
  for song in common_songs:
    rating1 = 0
    rating2 = 0
    for d in data:
      if d["user"] == user1 and d["song"] == song:
        rating1 = d["rating"]
      if d["user"] == user2 and d["song"] == song:
        rating2 = d["rating"]
    distance  = (rating1 - rating2)**2
  return distance**0.5


# Função para encontrar os k vizinhos mais próximos
#Usamos a função find_neighbors para encontrar os k vizinhos mais próximos do usuário dado.
def find_neighbors(user, k):
  distances = []
  for d in data:
    if d["user"] != user:
      distances.append({
        "user": d["user"],
        "distance": calculate_distance(user, d["user"])
      })
  distances = sorted(distances, key=lambda x: x["distance"])
  return [d["user"] for d in distances][:k]


# Função para recomendar música para um usuário
#Usamos a função recommend_song para recomendar músicas para o usuário dado baseado nas classificações dos seus vizinhos mais próximos.
def recommend_song(user, k):
  neighbors = find_neighbors(user, k)
  songs = {}
  for d in data:
    if d["user"] in neighbors:
      if d["song"] not in songs:
        songs[d["song"]] = {"rating": 0, "votes": 0}
      songs[d["song"]]["rating"] += d["rating"]
      songs[d["song"]]["votes"] += 1
  for song in songs:
    songs[song]["rating"] = songs[song]["rating"] / songs[song]["votes"]
  songs = sorted(songs.items(), key=lambda x: x[1]["rating"], reverse=True)
  return songs


# Exemplo de uso
# No final, o exemplo de uso imprime se a musica é recomendada para o usuário ou não baseado no número de votos.
user = "Alice"
k = 2
rec_songs = recommend_song(user, k)
for song in rec_songs:
  if song[1]["votes"] >= k / 2:
    print(
      f'A musica {song[0]} é recomendada para o usuário {user} com uma classificação de {song[1]["rating"]}'
    )
  else:
    print(
      f'A musica {song[0]} não é recomendada para o usuário {user} pois não tem votos suficientes'
    )
