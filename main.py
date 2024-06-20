from lr_class import LinearRegressor

if __name__ == '__main__':
    # Import the data from CSV file
    linear_regressor = LinearRegressor('./data/car_price.csv')
    # Train the model and get the test set data
    linear_regressor.train_data()
    x_test, y_test = linear_regressor.get_test_dataset()
    # Visualize the training result using the test set data
    linear_regressor.plot_data(x_test, y_test)
