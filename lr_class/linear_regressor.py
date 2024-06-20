import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class LinearRegressor:
    def __init__(self, data: str):
        self.regressor = LinearRegression()
        # Ingest the dataset
        self.dataset = pd.read_csv(data)
        x_data = self.dataset.iloc[:, :-1].values
        y_data = self.dataset.iloc[:, -1].values
        # Split the dataset into training set and test set
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            x_data, y_data, test_size=0.2, random_state=0
        )

    def train_data(self):
        # Perform linear regression on the training set
        self.regressor.fit(self.x_train, self.y_train)

    def plot_data(self, x_data, y_data):
        plt.title('car price vs car age')
        plt.xlabel('age (year)')
        plt.ylabel('price (dollar)')
        plt.scatter(x_data, y_data, color='red')
        plt.plot(x_data, self.regressor.predict(x_data), color='blue')
        plt.show()

    def get_training_dataset(self):
        return self.x_train, self.y_train

    def get_test_dataset(self):
        return self.x_test, self.y_test

    def get_full_dataset(self):
        return self.dataset

    def get_model(self):
        return self.regressor
