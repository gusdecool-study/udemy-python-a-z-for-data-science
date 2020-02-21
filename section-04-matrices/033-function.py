import matplotlib.pyplot as plt


# Run the code in 027-matrices.py first
def myplot(data, playerList = Players):
    color = {'KobeBryant': 'Black', 'JoeJohnson': 'Red', 'LeBronJames': 'Green', 'CarmeloAnthony': 'Blue',
             'DwightHoward': 'Magenta', 'ChrisBosh': 'Black', 'ChrisPaul': 'Red', 'KevinDurant': 'Green',
             'DerrickRose': 'Blue', 'DwayneWade': 'Magenta'}

    marker = {'KobeBryant': 's', 'JoeJohnson': 'o', 'LeBronJames': '^', 'CarmeloAnthony': 's',
              'DwightHoward': 's', 'ChrisBosh': 'o', 'ChrisPaul': '^', 'KevinDurant': 'D',
              'DerrickRose': 's', 'DwayneWade': 'o'}

    for name in playerList:
        plt.plot(data[Pdict[name]], c=color[name], ls='--', marker=marker[name], ms=7, label=name)

    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.xticks(list(range(0, 10)), Seasons, rotation='vertical')
    plt.show()


myplot(MinutesPlayed)
