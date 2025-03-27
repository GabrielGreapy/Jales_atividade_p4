class Animal():
    def emitir_son(self):
        raise NotImplementedError("Subclasses devem implementar atributo.")
    
class Cachorro(Animal):
    def emitir_son(self):
        return 'auau'

class Gato(Animal):
    def emitir_son(self):
        return 'miau miau'
    
class Pato(Animal):
    def emitir_son(self):
        return 'queck queck'

pato1 = Pato()

def fazer_barulho(animal):
    som = animal.emitir_son()
    return som

print(fazer_barulho(pato1))