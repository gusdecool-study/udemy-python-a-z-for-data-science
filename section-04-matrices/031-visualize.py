import matplotlib
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = 8, 4
plt.plot(Salary[0], c='Black', ls='--', marker='s', ms=7, label=Players[0])
plt.plot(Salary[1], c='Red', ls='--', marker='o', ms=7, label=Players[1])
plt.plot(Salary[2], c='Green', ls='--', marker='^', ms=7, label=Players[2])
plt.plot(Salary[3], c='Blue', ls='--', marker='s', ms=7, label=Players[3])
plt.plot(Salary[4], c='Magenta', ls='--', marker='s', ms=7, label=Players[4])
plt.plot(Salary[5], c='Black', ls='--', marker='o', ms=7, label=Players[5])
plt.plot(Salary[6], c='Red', ls='--', marker='^', ms=7, label=Players[6])
plt.plot(Salary[7], c='Green', ls='--', marker='D', ms=7, label=Players[7])
plt.plot(Salary[8], c='Blue', ls='--', marker='s', ms=7, label=Players[8])
plt.plot(Salary[9], c='Magenta', ls='--', marker='o', ms=7, label=Players[9])
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks(list(range(0, 10)), Seasons, rotation='vertical')
plt.show()

plt.rcParams['figure.figsize'] = 8, 4
plt.plot(Games[0], c='Black', ls='--', marker='s', ms=7, label=Players[0])
plt.plot(Games[1], c='Red', ls='--', marker='o', ms=7, label=Players[1])
plt.plot(Games[2], c='Green', ls='--', marker='^', ms=7, label=Players[2])
plt.plot(Games[3], c='Blue', ls='--', marker='s', ms=7, label=Players[3])
plt.plot(Games[4], c='Magenta', ls='--', marker='s', ms=7, label=Players[4])
plt.plot(Games[5], c='Black', ls='--', marker='o', ms=7, label=Players[5])
plt.plot(Games[6], c='Red', ls='--', marker='^', ms=7, label=Players[6])
plt.plot(Games[7], c='Green', ls='--', marker='D', ms=7, label=Players[7])
plt.plot(Games[8], c='Blue', ls='--', marker='s', ms=7, label=Players[8])
plt.plot(Games[9], c='Magenta', ls='--', marker='o', ms=7, label=Players[9])
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks(list(range(0, 10)), Seasons, rotation='vertical')
plt.show()
