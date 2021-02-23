nb_rows = int(input("Entrez le nombre de lignes : "))
nb_cols = int(input("Entrez le nombre de colonnes : "))
matrice = []
for i in range(nb_rows):
    rows = []
    for j in range(nb_cols):
        x = int(input("Entrez l'élément [{}][{}] : ".format(i+1, j+1)))
        rows.append(x)
    matrice.append(rows)

for i in range(nb_rows):
    for j in range(nb_cols):
        print(matrice[i][j], end=" ")
    print("\n", end="")
