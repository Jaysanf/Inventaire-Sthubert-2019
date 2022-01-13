class item:

    def __init__(self, name, nombre, inventaire, gamma, ecart):
        self.name = name
        self.nombre = nombre
        self.inventaire = inventaire
        self.gamma = gamma
        self.ecart = ecart

    def calculate_ecart(self):
        ecart = (self.inventaire - self.gamma)
        return ecart


inventaire_liste = ['Frites', 'Animaux', 'Filets', 'Poitrines Grillés Congelé', 'Brochettes Congelé',
                    'Côtes Levées Plaques Cuite', 'Poulets Broches', 'Côtes Levées Plaques Crues',
                    'Côtes Levées Caisses', 'Poitrines Grillés Dégelé', 'Brochettes Dégelé', 'Poulets Caisses']

inventaire_totale = []
counter = 0
for i in inventaire_liste:
    if i == 'Poitrines Grillés Dégelé':
        nb_ditem = int(input(f'Entrez le nombre de {i} en inventaire: '))
        inventaire_totale[3].inventaire += (nb_ditem * 5)

    elif i == 'Brochettes Dégelé':
        nb_ditem = int(input(f'Entrez le nombre de {i} en inventaire: '))
        inventaire_totale[4].inventaire += (nb_ditem * 5)

    elif i == 'Côtes Levées Plaques Cuite':
        nb_ditem = int(input(f'Entrez le nombre de {i} en inventaire: '))
        inventaire_totale.append(item('Côtes Levées', nb_ditem, (nb_ditem * 8), None, None))

    elif i == 'Côtes Levées Plaques Crues':
        nb_ditem = int(input(f'Entrez le nombre de {i} en inventaire: '))
        inventaire_totale[5].inventaire += (nb_ditem * 8)

    elif i == 'Côtes Levées Caisses':
        nb_ditem = int(input(f'Entrez le nombre de {i} en inventaire: '))
        inventaire_totale[5].inventaire += (nb_ditem * 48)


    elif i == 'Poulets Broches':
        nb_ditem1 = int(input(f'Entrez le nombre de {i} pré-cuites en inventaire: '))
        nb_ditem2 = int(input(f'Entrez le nombre de {i} crues en inventaire: '))
        nb_ditem = nb_ditem1 + nb_ditem2
        inventaire_totale.append(item(i, nb_ditem, (nb_ditem * 16), None, None))

    elif i == 'Frites':
        nb_ditem = int(input(f'Entrez le nombre de {i} en inventaire: '))
        inventaire_totale.append(item(i, nb_ditem, (nb_ditem * 6), None, None))

    elif i == 'Poulets Caisses':
        nb_ditem = int(input(f'Entrez le nombre de {i} en inventaire: '))
        inventaire_totale.append(item(i, nb_ditem, (nb_ditem * 60), None, None))
    else:
        nb_ditem = int(input(f'Entrez le nombre de {i} en inventaire: '))
        inventaire_totale.append(item(i, nb_ditem, (nb_ditem * 5), None, None))
broche = inventaire_totale.pop(6)
caisse = inventaire_totale.pop(6)
inventaire_totale.append(item('Cuisse', None, (broche.inventaire + caisse.inventaire) / 2, None, None))
inventaire_totale.append(item('Poitrine', None, (broche.inventaire + caisse.inventaire) / 2, None, None))

for i in range(len(inventaire_totale)):
    inventaire_totale[i].gamma = int(input(f'Entrez le Gamma de {inventaire_totale[i].name}: '))
    inventaire_totale[i].ecart = inventaire_totale[i].calculate_ecart()

for i in inventaire_totale:
    print(f'------ {i.name} ------')
    print(f'Inventaire : {i.inventaire}')
    print(f'Gamma : {i.gamma}')
    print(f'Ecart : {i.ecart}')
    if i.name == 'Cuisse':
        print(f'Broche: {broche.nombre} / {broche.inventaire}')
        print(f'Caisse: {caisse.nombre} / {caisse.inventaire}')