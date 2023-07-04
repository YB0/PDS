class artigo:
    
    def __init__ (self, autor, titulo):
        
        self.autor = autor
        self.titulo = titulo
    
    def get_art (self):
    
        return "Titulo do Artigo:" + self.titulo + "\nAutor do Artigo:" + self.autor + "\n-----------------------"

class edicao:
    
    def __init__ (self, numero, volume, data):
        
        self.numero = numero
        self.volume = volume
        self.data = data
        self.artigos = []
    
    def novo_art (self, artigo):
    
        self.artigos.append(artigo)

    def delete_art (self, titulo):

        for artigo in self.artigos:

            if artigo.titulo == titulo:

                del self.artigos[self.artigos.index(artigo)]
                return "Artigo deletado com sucesso!"
    
    def ver_ed (self):
    
        return "Número da Edição:" + str(self.numero) + "\nVolume da Edição:" + str(self. volume) + "\n-----------------------"
    
    def ver_arts (self):
        
        data = ""
        
        for artigo in self.artigos:
            
            print(artigo.get_art())
    
    def num_artigos (self):
    
        return len(self.artigos)

class revista_cientifica:
    
    def __init__ (self, titulo, issn, periodicidade):
        
        self.titulo = titulo
        self.issn = issn
        self.periodicidade = periodicidade
        self.edicoes = []
    
    def nova_ed (self, edicao):
        
        num_artigos = edicao.num_artigos()
        
        if (num_artigos >= 10 and num_artigos <= 15):
        
            self.edicoes.append(edicao)
            return "Publicação de Edição realizada com sucesso!"

        elif (num_artigos < 10):

            return "Uma edição precisa ter entre 10 e 15 artigos para ser publicada. \nEsta edição possui " + str(num_artigos) + " artigos. Adicione " + str(10 - num_artigos) + " artigos e tente novamente."

        elif (num_artigos > 15):

            return "Uma edição precisa ter entre 10 e 15 artigos para ser publicada. \nEsta edição possui " + str(num_artigos) + " artigos. Exclua " + str(num_artigos - 15) + " artigos e tente novamente."

    def delete_ed (self, numero):

        for edicao in self.edicoes:

            if edicao.numero == numero:

                del self.edicoes[self.edicoes.index(edicao)]
                return "Edição deletada com sucesso!"

    def ver_eds (self):
    
        data = ""
        
        for edicao in self.edicoes:
        
            print(edicao.ver_ed())