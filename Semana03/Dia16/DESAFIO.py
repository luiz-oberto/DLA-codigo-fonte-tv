'''
DESAFIO 01:
Playlist de Musicas em um App

Imagine que você está criando uma aplicação de
música, onde você pode ter uma playlist com
músicas escolhidas. Para começar o desafio a
playlist deve ter as seguintes funcionalidades:

# FEITO
1. Capacidade de adicionar músicas

# FEITO
1.1 Capacidade de remover músicas

# FEITO
2. Mostrar todas as músicas da playlist

# FEITO
3. Toda vez que uma música é adicionada, ela é
colocada no início da playlist

# FEITO
4. É possível mover a posição da música na playlist a
qualquer momento

# FEITO
5. Função para tocar toda a playlist do início ao fim

# FEITO
6. Capacidade para tocar apenas uma música da
playlist

# FEITO
7. As música devem ter os seguintes atributos: Nome
da música, nome do artista, Número de reproduções
e Tempo total da música

# FEITO
8. Cada vez que uma música é tocada é preciso
incrementar o número de reproduções

Esse é o primeiro desafio onde você terá as rédeas
de como solucionar, mas lembre-se que iremos voltar
nesse mesmo problema, porém com outras
funcionalidades.

Dica: Que tal utilizar um JSON para definir os
atributos das músicas.

# log de eventos do desenvolvimento
- pensei em criar um registro de músicas criadas ao longo da execução do programa, 
mas percebi que eu cresceria sem necessidade a complexidade do código, me fazendo 
desistir da idéia e deixa por isso mesmo.

'''
class Music:
    # 7. ATRIBUTOS DA MÚSICA
    def __init__(self, name: str, artist: str, reproductionTime: str):
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
    
    
    def delete_music(self):
        print('\n# deseja deletar qual música?\n')
        
        for music in enumerate(self.musics, 1):
            print(f'{music[0]}. {music[1].name} - {music[1].artist}')
        
        index = input('$ Insira o índice-> ')
        
        try:

            select_to_int = int(index)
            select = input(f'excluir a música {self.musics[select_to_int-1].name}? [Y/n] ')
            
            match select:
                case '':
                    musica_deletada = self.musics.pop(select_to_int-1)
                    print(f'A música {musica_deletada.name} foi excluída da playlist')
                
                case 'Y':
                    musica_deletada = self.musics.pop(select_to_int-1)
                    print(f'A música {musica_deletada.name} foi excluída da playlist')
                
                case 'y':
                    musica_deletada = self.musics.pop(select_to_int-1)
                    print(f'A música {musica_deletada.name} foi excluída da playlist')
                
                case 'n':
                    print(f'Exclusão cancelada.')
                
                case 'N':
                    print(f'Exclusão cancelada.')
                
                case _:
                    print('Valor inválido \nExclusão cancelada.')

        except:

            return print('\níndice inserido inválido!')
        
        return
     

    # Mostrar todas as músicas da playlist
    def show_playlist_musics(self, playlistName: str):

        if self.name == playlistName:

            print(f'\nExibindo músicas da playlist {playlistName}\n')

            for i in enumerate(self.musics, 1):
                print(f'{i[0]}. {i[1].name} - {i[1].artist} - {i[1].reproductionTime}')
                
        return


    # Tocar playlist do inícion ao fim
    def play_playlist(self):
        print(f'\n# Tocando playlist {self.name} #')
        for music in self.musics:
            music.play()
        return
    

    # tocar uma música
    def play_one_music(self, index: int):
        try:
            print(f"\nTocando {self.musics[index].name} de {self.musics[index].artist}")
        except:
            print('Índice inserido inválido')
        return


    # trocar a ordem de uma música
    def change_order(self, music_index: int, new_order: int):
        list_musics = self.musics.copy()

        music_to_change = list_musics.pop(music_index)
        list_musics.insert(new_order, music_to_change)
        self.musics = list_musics

        print('\n# Ordem das músicas alterada com sucesso!')
        for i in self.musics:
            print(i.name)

        return
    
###########################################################################################

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
musica = Music('Dia Lindo', 'O Rappa', '6:10')

# tocar música
musica.play()

# criar playlist
lista_1 = Playlist('lista_1')

# adicionando músicas a playlist de acordo com a lista passada acima
for i in album:
    music = Music(i["name"], i["artist"], i["reproductionTime"])
    lista_1.insert_music(music)

# mostrar playilst completa
lista_1.show_playlist_musics('lista_1')

# tocar playlist
lista_1.play_playlist()

# deletar música
lista_1.delete_music()

# tocar apenas uma música
lista_1.play_one_music(0)

# lista_1.show_playlist_musics('lista_1')

# mudar a ordem de uma música
lista_1.change_order(0,3)
