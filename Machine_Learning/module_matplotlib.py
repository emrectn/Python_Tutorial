import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

DATA1 = [32528, 7788, 34028, 14489, 6692, 15040, 24565, 6989, 16845, 7975, 35550, 9980, 7895, 9538, 13295]
DATA2 = [[25261, 8477, 25261, 19372, 6005, 13664, 19359, 11268, 16625, 9377, 34476, 9587, 9607, 10110, 14699]]


def distribution_plot(RedFunction, BlueFunction, RedName, BlueName, Title):
    """ Bu fonksiyon dağılımı gösterir. Verilerin nasıl dağıldığını yoğunluğun nerede olduğunu görmemizi sağlar.
    """

    width = 12
    height = 10
    plt.figure(figsize=(width, height))

    # kde = False Dağılım çizgi grafiğini göstermez
    # hist = False Histogramların çizilmesini istemiyorsanız.
    ax1 = sns.distplot(RedFunction, hist=False, color="r", label=RedName)
    ax2 = sns.distplot(BlueFunction, hist=False, color="b", label=BlueName, ax=ax1)

    plt.title(Title)
    plt.xlabel('x_label')
    plt.ylabel('y_label')

    plt.show()
    plt.close()


def polly_plot(xtrain, xtest, y_train, y_test, lr, poly_transform):
    width = 12
    height = 10
    plt.figure(figsize=(width, height))

    # training data
    # testing data
    # lr:  linear regression object
    # poly_transform:  polynomial transformation object

    xmax = max([xtrain.values.max(), xtest.values.max()])

    xmin = min([xtrain.values.min(), xtest.values.min()])

    x = np.arange(xmin, xmax, 0.1)

    plt.plot(xtrain, y_train, 'ro', label='Training Data')
    plt.plot(xtest, y_test, 'go', label='Test Data')
    plt.plot(x, lr.predict(poly_transform.fit_transform(x.reshape(-1, 1))), label='Predicted Function')
    plt.ylim([-10000, 60000])
    plt.ylabel('Price')
    plt.legend()


def simple_plot(x, y, x_label, y_label, title, *argv):
    plt.plot(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    if argv:
        plt.text(argv[0], argv[1], argv[2])
    plt.show()

if __name__ == "__main__":
    " Distribution Plot"
    title = 'Graph Title'
    # distribution_plot([10,10,1,2], [33,33,4,3], "Red_LABEL", "Blue_LABEL", title)
    simple_plot([10,10,1,2], [33,33,4,3], "Red_LABEL", "Blue_LABEL", title)