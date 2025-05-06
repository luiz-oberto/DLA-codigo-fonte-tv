'''
DESAFIO 01:
Playlist de Musicas em um App

Imagine que você está criando uma aplicação de
música, onde você pode ter uma playlist com
músicas escolhidas. Para começar o desafio a
playlist deve ter as seguintes funcionalidades:

# FEITO
1. Capacidade de adicionar músicas

# 
1.1 Capacidade de remover músicas

# FEITO
2. Mostrar todas as músicas da playlist

# FEITO
3. Toda vez que uma música é adicionada, ela é
colocada no início da playlist

# 
4. É possível mover a posição da música na playlist a
qualquer momento

# FEITO
5. Função para tocar toda a playlist do início ao fim

# 
6. Capacidade para tocar apenas uma música da
playlist

# FEITO
7. As música devem ter os seguintes atributos: Nome
da música, nome do artista, Número de reproduções
e Tempo total da música

# 
8. Cada vez que uma música é tocada é preciso
incrementar o número de reproduções

Esse é o primeiro desafio onde você terá as rédeas
de como solucionar, mas lembre-se que iremos voltar
nesse mesmo problema, porém com outras
funcionalidades.

Dica: Que tal utilizar um JSON para definir os
atributos das músicas.
'''
class Music:
    # 7. ATRIBUTOS DA MÚSICA
    def __init__(self, name: str, artist: str, reproductionTime):
        self.name = name
        self.artist = artist
        self.reproductions = 0
        self.reproductionTime = reproductionTime

    def play(self):
        self.reproductions+=1
        print(f'Tocando {self.name} - {self.artist}')


class Playlist:
    def __init__(self, name):
        self.name = name
        self.musics = []


    # inserir música (sempre ao ínicio da lista)
    def insert_music(self, music: Music):

        self.musics.insert(0, music)

        print(f'{music.name} - {music.artist} adicionado a sua playlist')

        return
     

    # Mostrar todas as músicas da playlist
    def show_playlist_musics(self, playlistName):

        if self.name == playlistName:

            print(f'\nExibindo músicas da playlist {playlistName}\n')

            for i in enumerate(self.musics, 1):
                print(f'{i[0]}. {i[1].name} - {i[1].artist} - {i[1].reproductionTime}')
                
        return


    # Tocar playlist do inícion ao fim
    def play_playlist(self):
        for music in self.musics:
            music.play()
        return
    

album = [
    {
    "name": "wake",
    "artist": "Linkin Park",
    "reproductionTime": "1:43"
    },
    {
    "name": "Given Up",
    "artist": "Linkin Park",
    "reproductionTime": "3:11"
    },
    {
    "name": "Leave Out All the Rest",
    "artist": "Linkin Park",
    "reproductionTime": "3:31"
    },
    {
    "name": "Bleed It Out",
    "artist": "Linkin Park",
    "reproductionTime": "2:46"
    },
    {
    "name": "Shadow of the Day",
    "artist": "Linkin Park",
    "reproductionTime": "4:52"
    },
    {
    "name": "What I've Done",
    "artist": "Linkin Park",
    "reproductionTime": "3:28"
    }
]


# criar música
# musica1 = Music('Given Up', 'Linkin Park', '3:11')

# tocar música
# musica1.play()

# criar playlist
lista_1 = Playlist('lista_1')

# lista_2 = Playlist('lista_2')
# lista_3 = Playlist('lista_3')
# lista_1.insert_music(musica1)

# adicionando músicas a playlist de acordo com a lista passada acima
for i in album:
    music = Music(i["name"], i["artist"], i["reproductionTime"])
    lista_1.insert_music(music)

# mostrar playilst completa
lista_1.show_playlist_musics('lista_1')

# tocar playlist
lista_1.play_playlist()
