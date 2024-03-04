import tensorflow as tf
import numpy as np

class LogisticRegressionModel:
    def __init__(self, num_features):
        self.num_features = num_features
        self.model = self.build_model()

    def build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=(self.num_features,), name='input_layer'),
            tf.keras.layers.Dense(1, activation='sigmoid', name='output_layer')
        ])
        model.compile(optimizer='adam',
                      loss='binary_crossentropy',
                      metrics=['accuracy'])
        return model

    def train(self, X_train, y_train, epochs=10, batch_size=32):
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)

    def predict(self, X_test):
        return (self.model.predict(X_test) > 0.5).astype("int32")

if __name__ == "__main__":
    # Sample data
    X_train = np.array([[1, 2],
                        [2, 3],
                        [3, 4],
                        [4, 5],
                        [5, 6]])
    y_train = np.array([0, 0, 1, 1, 1])

    # Create and train the model
    model = LogisticRegressionModel(num_features=X_train.shape[1])
    model.train(X_train, y_train, epochs=100, batch_size=32)

    # Make predictions
    X_test = np.array([[6, 7],
                       [7, 8]])
    predictions = model.predict(X_test)

