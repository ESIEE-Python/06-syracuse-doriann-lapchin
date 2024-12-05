"""
    Code

    """
# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """Fonction du prof
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({
        'layout': {
            'title': {'text': title},
            'xaxis': {'title': {'text': "x"}},
            'yaxis': {'title': {'text': "y"}},
        }
    })

    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color="blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
#######################

def syracuse_l(n):
    """Retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """
    l = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    return len(l)

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """
    n0 = l[0]
    count = 0
    for value in l:
        if value >= n0:
            count += 1
        else:
            break
    return count

def altitude_maximale(l):
    """Retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    return max(l)

#### Fonction principale ####

def main():
    """Main
    """
    # Vos appels à la fonction secondaire ici
    n_values = [3, 4, 5, 6, 15]
    for n in n_values:
        lsyr = syracuse_l(n)
        print(f"Suite de Syracuse pour n = {n} : {lsyr}")
        print(f"Temps de vol pour n = {n} : {temps_de_vol(lsyr)}")
        print(f"Temps de vol en altitude pour n = {n} : {temps_de_vol_en_altitude(lsyr)}")
        print(f"Altitude maximale pour n = {n} : {altitude_maximale(lsyr)}")
        print("-" * 50)
        # Pour visualiser le graphique, décommentez la ligne suivante :
        # syr_plot(lsyr)

if __name__ == "__main__":
    main()
