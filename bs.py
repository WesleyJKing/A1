import pickle
pickle_file_path = 'naive_bayes_res/embed_naive_bayes_res.pkl'

with open(pickle_file_path, 'rb') as file:
    pickle.load(file)

