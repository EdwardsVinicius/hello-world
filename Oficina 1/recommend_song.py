
#Nessa versão, a lógica é bem simples e direta, estamos pegando todas as músicas avaliadas por outros usuários e calculando a média das avaliações, se a média é maior ou igual a 4 a música é adicionada na lista de recomendação e o tamanho dessa lista é limitado pelo valor de k.

# Conjunto de dados de exemplo
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

# Função para recomendar música para um usuário baseado na média das avaliações


#A função, assim como a anterior, recebe o usuário e o número de K recomendações que deseja obter como entrada e retorna uma lista com as músicas recomendadas. Nessa versão, a recomendação é feita baseado na média das avaliações das músicas pelos outros usuários
def recommend_song(user, k):
  songs = {}
  for d in data:
    if d["user"] != user:
      if d["song"] not in songs:
        songs[d["song"]] = {"rating": 0, "votes": 0}
      songs[d["song"]]["rating"] += d["rating"]
      songs[d["song"]]["votes"]  += 1
  for song in songs:
    songs[song]["rating"] = songs[song]["rating"] / songs[song]["votes"]
  rec_songs = []
  for song in songs:
    if songs[song]["rating"] >= 4:
      rec_songs.append(song)
  return rec_songs[:k]


# exemplo de uso
user = "Charlie"
k = 3
rec_songs = recommend_song(user, k)
print(rec_songs)


