def word_count_aggregator():
    count = 0
    def aggr(word):
        nonlocal count
        count += len(word.split(" "))
        return count
    return aggr
