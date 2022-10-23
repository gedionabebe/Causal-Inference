def jaccard_similarity_index(set1, set2):
        x = set(set1).intersection(set2)
        return round(len(x) / (len(set1) + len(set2) - len(x)), 3)