import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def linear_regression(data: str):
    # Import the dataset from CSV file
    dataset = pd.read_csv(data)
    x_data = dataset.iloc[:, :-1].values
    y_data = dataset.iloc[:, -1].values

    # Split the dataset into training set and test set
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=0)

    # Perform linear regression on the training set
    linear_regressor = LinearRegression()
    linear_regressor.fit(x_train, y_train)

    return x_test, y_test, linear_regressor


def plot_data(x_data, y_data, regressor):
    plt.title('car price vs car age')
    plt.xlabel('age (year)')
    plt.ylabel('price (dollar)')
    plt.scatter(x_data, y_data, color='red')
    plt.plot(x_data, regressor.predict(x_data), color='blue')
    plt.show()


if __name__ == '__main__':
    # Get the test set data and the trained linear regression model
    x_test, y_test, linear_regressor = linear_regression('./data/car_price.csv')
    # Visualize the training result using the test set data
    plot_data(x_test, y_test, linear_regressor)
