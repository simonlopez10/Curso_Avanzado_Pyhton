# def mayusculas(func):
#     def envoltura(texto):
#         return func(texto).upper()
#     return envoltura

# @mayusculas
# def mensaje(nombre):
#     return f'{nombre}, recibiste un mensaje'

# print(mensaje('simon'))

def no_necesito(func):
    def wrapped(team):
        print(f'No necesito que estes arriba para quererte glorisoso {team}')
    return wrapped

@no_necesito
def equipo(team):
    print (team) 

equipo('dim')

