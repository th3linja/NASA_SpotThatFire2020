import numpy as np
from joblib import load
np.set_printoptions(suppress=True)


def prediction(model, data):
    regressor = load(model)
    p = regressor.predict(np.array(data).reshape(1, -1))
    return p


p = prediction('current.joblib', [100000, 400, 2])
print(float(p))