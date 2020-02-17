import matplotlib.pyplot as plt


def myplot(playerList):
    for name in playerList:
        plt.plot(Games[Pdict[name]], c='Black', ls='--', marker='s', ms=7, label=name)

    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.xticks(list(range(0, 10)), Seasons, rotation='vertical')
    plt.show()


myplot(['KobeBryant', 'JoeJohnson', 'LeBronJames', 'CarmeloAnthony', 'DwightHoward', 'ChrisBosh', 'ChrisPaul',
        'KevinDurant', 'DerrickRose', 'DwayneWade'])
