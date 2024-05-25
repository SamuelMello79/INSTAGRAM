# Cria o objeto pessoa
class Pessoa:
    def __init__(self, nome, canal, perfil):
        self.nome = nome
        self.canalinscrito = canal
        self.perfilseguido = perfil

# Função para verificar se a pessoa consegue aprender python
def aprender_python(pessoa):
    if pessoa.canalinscrito == 'Samuel Mello' and pessoa.perfilseguido == 'Samuel Mello':
        return True
    else:
        return False

# Cria uma instancia pessoa
pessoa1 = Pessoa('Saimon', 'Samuel Mello', 'Samuel Mello')
resultado = aprender_python(pessoa1)

# Exibe o resultado
if resultado:
    print(f"{pessoa1.nome} está pronto para aprender Python! 🚀🐍")
else:
    print(f"{pessoa1.nome} precisa se inscrever no canal e seguir o perfil! ")

