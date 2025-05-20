class Music:
    # 7. ATRIBUTOS DA MÚSICA
    def __init__(self, name: str, artist: str, reproductionTime: str):
        self.name = name
        self.artist = artist
        self.reproductions = 0
        self.reproductionTime = reproductionTime

    def play(self):
        self.reproductions += 1
        print(f'Tocando {self.name} - {self.artist}')


class Playlist:
    def __init__(self, name):
        self.name = name
        self.musics = []

    # inserir música (sempre ao ínicio da lista)
    def insert_music(self, music: Music):
        self.musics.insert(0, music)
        print(f'Música {music.name} - {music.artist} adicionada à sua playlist')

    def delete_music(self):
        print('\n# Deseja deletar qual música?\n')
        for i, music in enumerate(self.musics, 1):
            print(f'{i}. {music.name} - {music.artist}')

        index = input('\n$ Insira o índice-> ')

        try:
            select_to_int = int(index)
            music = self.musics[select_to_int - 1]
            select = input(f'Excluir a música {music.name}? [Y/n] ').upper().strip()

            if select in ('', 'Y'):
                musica_deletada = self.musics.pop(select_to_int - 1)
                print(f'A música {musica_deletada.name} foi excluída da playlist')
            elif select == 'N':
                print('Exclusão cancelada.')
            else:
                print('Valor inválido. Exclusão cancelada.')

        except (ValueError, IndexError):
            print('Erro: Índice inválido')

    def show_playlist_musics(self, playlistName: str):
        if self.name == playlistName:
            print(f'\nExibindo músicas da playlist {playlistName}\n')
            for i, music in enumerate(self.musics, 1):
                print(f'{i}. {music.name} - {music.artist} - {music.reproductionTime}')

    def play_playlist(self):
        print(f'\n# Tocando playlist {self.name} #')
        for music in self.musics:
            music.play()

    def play_one_music(self, index: int):
        try:
            music = self.musics[index]
            music.play()
        except IndexError:
            print('Erro: Índice inserido inválido')

    def change_order(self, music_index: int, new_order: int):
        try:
            music_to_change = self.musics.pop(music_index)
            self.musics.insert(new_order, music_to_change)
            print('\n# Ordem das músicas alterada com sucesso!')
            for music in self.musics:
                print(music.name)
        except IndexError:
            print('Erro: Índice inválido')

    def sort_by_title(self):
        self.musics.sort(key=lambda m: m.name.lower())
        for music in self.musics:
            print(music.name)

    def sort_by_reproductions(self):
        sorted_musics = sorted(self.musics, key=lambda m: m.reproductionTime)
        for music in sorted_musics:
            print(f'{music.name} - {music.reproductionTime}')
        return sorted_musics
