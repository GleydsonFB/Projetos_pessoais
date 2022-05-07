def leiadinheiro(msg):
    v = False
    while not v:
        ent = str(input(msg)).replace(',', '.')
        if ent.isalpha():
            print(f'ERRO! "{ent}" são letras e não preços!')
        elif ent.isspace():
            print(f'ERRO: "{ent}" é um espaço e não um preço!')
        elif ent is '':
            print(f'ERRO: "{ent}" está vazio!')
        elif ent.isalnum():
            print(f'ERRO: "{ent}" contem letras além dos números!')
        else:
            v = True
            return float(ent)


