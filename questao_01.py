#Adicione os atributos tamanho e marca à classe Televisão. Crie dois objetos Televisão 
#e atribua tamanhos e marcas diferentes. Depois, imprima o valor desses atributos de forma a confirmar a 
#independência dos valores de cada instância (objeto).





class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 20
        self.marca = "Panasonic"


tv = Televisão()
tv.tamanho = 27
tv.marca = "CCE"
tv_sala = Televisão()
tv_sala.tamanho = 52
tv_sala.marca = "Samsug"

print(f"tv tamanho={tv.tamanho} marca={tv.marca}")
print(f"tv_sala tamanho={tv_sala.tamanho} marca={tv_sala.marca}")