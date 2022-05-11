from collections.abc import Sized

class Lista(Sized):
    def __init__(self, descricao = "Igor"):
        self.descricao = descricao

    def __str__(self):
        return self.descricao

    def __len__(self):
        return len(self.descricao)

lista1 = Lista()

print(lista1)
print(len(lista1))