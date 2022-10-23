from causalnex.discretiser import Discretiser

def discretise(data):
    for column in data.columns:
        data[column] = Discretiser(method="uniform", num_buckets=10, numeric_split_points=[1, 10]).transform(data[column].values)
    return data