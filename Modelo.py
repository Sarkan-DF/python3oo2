class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def like(self):
        return self._like

    def dar_like(self):
        self._like += 1

    def __str__(self):
        return ("Nome: {} - Likes: {}".format(self.nome, self.like))

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return ("Nome: {} -- Duração {} Min -- Likes: {}".format(self.nome, self.duracao, self.like))

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return ("Nome: {} -- Duração {} Temporadas -- Likes: {}".format(self.nome, self.temporadas, self.like))

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 150)
poco = Filme('poço', 2020, 130)
lost = Serie('lost - perdidos', 2005, 6)
game_of_thrones = Serie('game of thrones', 2016, 5)

vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

poco.dar_like()
poco.dar_like()

game_of_thrones.dar_like()
game_of_thrones.dar_like()
game_of_thrones.dar_like()

lost.dar_like()
lost.dar_like()

listinha = [vingadores, lost, poco, game_of_thrones]
minha_playlist = Playlist('playlist_fim_de_semana', listinha)

for x in minha_playlist:
    print(x)

print(len(minha_playlist))