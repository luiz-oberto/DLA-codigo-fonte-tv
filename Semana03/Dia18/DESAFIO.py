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
        print(f'Música {music['name']} - {music['artist']} adicionado a sua playlist')
    
    def delete_music(self):
        print('\n# deseja deletar qual música?\n')
        
        for music in enumerate(self.musics, 1):
            print(f'{music[0]}. {music[1]["name"]} - {music[1]["artist"]}')
        
        index = input('\n$ Insira o índice-> ')
        
        try:

            select_to_int = int(index)
            select = input(f'excluir a música {self.musics[select_to_int-1]["name"]}? [Y/n] ').upper().strip()
            
            match select:
                case '':
                    musica_deletada = self.musics.pop(select_to_int-1)
                    print(f'A música {musica_deletada["name"]} foi excluída da playlist')
                
                case 'Y':
                    musica_deletada = self.musics.pop(select_to_int-1)
                    print(f'A música {musica_deletada["name"]} foi excluída da playlist')
                
                case 'N':
                    print(f'Exclusão cancelada.')
                
                case _:
                    print('Valor inválido \nExclusão cancelada.')

        except ValueError as e:
            raise e

    # Mostrar todas as músicas da playlist
    def show_playlist_musics(self, playlistName: str):

        if self.name == playlistName:
            print(f'\nExibindo músicas da playlist {playlistName}\n')
            for i in enumerate(self.musics, 1):
                print(f'{i[0]}. {i[1]['name']} - {i[1]['artist']} - {i[1]['reproductionTime']}')

    # Tocar playlist do inícion ao fim
    def play_playlist(self):
        print(f'\n# Tocando playlist {self.name} #')
        for music in self.musics:
            music.play()
    
    # tocar uma música
    def play_one_music(self, index: int):
        try:
            print(f"\nTocando {self.musics[index].name} de {self.musics[index].artist}")
        except:
            print('Índice inserido inválido')


    # trocar a ordem de uma música
    def change_order(self, music_index: int, new_order: int):
        list_musics = self.musics.copy()

        music_to_change = list_musics.pop(music_index)
        list_musics.insert(new_order, music_to_change)
        self.musics = list_musics

        print('\n# Ordem das músicas alterada com sucesso!')
        for i in self.musics:
            print(i.name)
 
# funções de ordenação das músicas
    # bubble sort
    def sort_by_title(self):
        print()
        need_to_order = True

        while need_to_order:

            for i in range(len(self.musics)-1):

                musica_1 = self.musics[i]
                musica_2 = self.musics[i+1]

                # verifica se a primeira letra do nome de cada música são iguais
                if musica_1["name"][0].upper() == musica_2["name"][0].upper():

                    # verificar qual possui a string menor
                    if len(musica_1["name"]) < len(musica_2["name"]) :
                        menor_nome = musica_1["name"] 
                    else:
                        menor_nome = musica_2["name"]

                    # verificar quem tem precedencia na ordem alfabética pelas letras que se seguem
                    for letra in range(1, len(menor_nome)-1):
                        if musica_1["name"][letra].upper() > musica_2["name"][letra].upper():
                            self.musics[i+1] = musica_1
                            self.musics[i] = musica_2
                            break

                        elif musica_1["name"][letra].upper() < musica_2["name"][letra].upper():
                            self.musics[i+1] = musica_2
                            self.musics[i] = musica_1
                            break

                        elif letra == len(menor_nome)-1:
                            break

                        else:
                            continue


                elif musica_1["name"] > musica_2["name"]:
                    temp = self.musics[i+1]
                    self.musics[i+1] = self.musics[i]
                    self.musics[i] = temp
            

            # Verifica se todas as músicas estão ordenadas
            for j in range(len(self.musics)):
                if j == len(self.musics)-1:
                    break

                if self.musics[j]['name'][0].upper() == self.musics[j+1]['name'][0].upper():
                    if self.musics[j]['name'][1].upper() < self.musics[j+1]['name'][1].upper():
                        need_to_order = False

                elif self.musics[j]['name'] < self.musics[j+1]['name']:
                    need_to_order = False

                else:
                    need_to_order = True
                    break
          
        for music in self.musics:
            print(music["name"])
    

    # Selection sort
    def sort_by_reproductions(self):
        try:
            musicas_nao_ordenadas = self.musics
            musicas_ordenadas = []
            while musicas_nao_ordenadas != []:
                menor_tempo = {}
                
                for music in musicas_nao_ordenadas:
                    if menor_tempo == {}:
                        menor_tempo = music
                    
                    if menor_tempo["reproductionTime"] > music["reproductionTime"]:
                        menor_tempo = music

                musicas_nao_ordenadas.remove(menor_tempo)
                musicas_ordenadas.append(menor_tempo)

        except ValueError as e:
            raise e


        return musicas_ordenadas
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
    },
    {
    "name": "Hands Held High",
    "artist": "Linkin Park",
    "reproductionTime": "3:55"
    },
    {
    "name": "No More Sorrow",
    "artist": "Linkin Park",
    "reproductionTime": "3:43"
    },
    {
    "name": "Valentine's Day",
    "artist": "Linkin Park",
    "reproductionTime": "3:18"
    },
    {
    "name": "In Between",
    "artist": "Linkin Park",
    "reproductionTime": "3:18"
    },
    {
    "name": "In Pieces",
    "artist": "Linkin Park",
    "reproductionTime": "3:38"
    },
    {
    "name": "The Little Things Give You Away",
    "artist": "Linkin Park",
    "reproductionTime": "6:25"
    },
]

lista_linkin_park = Playlist('linkin park')

for music in album:
    lista_linkin_park.insert_music(music)

# Ordenar por título
lista_linkin_park.sort_by_title()

# ordenar por tempo de reprodução
lista_ordenada = lista_linkin_park.sort_by_reproductions()

for musica in lista_ordenada:
    print(musica)