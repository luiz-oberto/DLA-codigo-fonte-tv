'''
DESAFIO 01:
ordenação da playlist (por título da
música e por número de reproduções)

Chegou a hora de voltarmos na nossa playlist de
músicas do dia 16. Vamos incrementar aquilo que
nós já fizemos, deixando ainda mais robusto.

O desafio é utilizar os algoritmos que ensinamos
para ordenar a playlist pelo título da música e
também pelo número de reproduções. Faça a
ordenação por título usando o Bubble Sort e a de
reproduções com o Selection Sort , só para poder
praticar.

Dica: Crie 2 funções, uma para ordenar com título da
música e outra pelo número de reproduções.

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

        print(f'{music['name']} - {music['artist']} adicionado a sua playlist')

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
                print(f'{i[0]}. {i[1]['name']} - {i[1]['artist']} - {i[1]['reproductionTime']}')
                
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
    
# funções de ordenação das músicas
    # bubble sort
    def sort_by_title(self):
        print()
        need_to_order = True

        while need_to_order:
            for i in range(len(self.musics)):
                if i == len(self.musics)-1:
                    break

                musica_1 = self.musics[i]["name"]
                musica_2 = self.musics[i+1]["name"]

                # verificar qual possui a string maior
                nome_maior = musica_1 if len(musica_1) > len(musica_2) else nome_maior = musica_2
                
                # verificar se a primeira letra do nome é igual, se positivo, ordenar pela segunda letra
                if musica_1[0].upper() == musica_2[0].upper():
                    for i in range(len(nome_maior)):
                        if musica_1[i] < musica_2[i]:
                            ...
                        
                    # print('primeira letra dos nomes são iguais')

                if musica_1 > musica_2:
                    temp = self.musics[i+1]
                    self.musics[i+1] = self.musics[i]
                    self.musics[i] = temp
            
            for j in range(len(self.musics)):
                if j == len(self.musics)-1:
                    break
                
                if self.musics[j]['name'] < self.musics[j+1]['name']:
                    need_to_order = False

                else:
                    need_to_order = True
                    break
          
        for music in self.musics:
            print(music)

        
        return
    

    # Selection sort
    def sort_by_reproductions(self):

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

lista_linkin_park = Playlist('linkin park')

for music in album:
    lista_linkin_park.insert_music(music)

lista_linkin_park.show_playlist_musics('linkin park')

lista_linkin_park.sort_by_title()