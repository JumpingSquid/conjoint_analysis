import random


def cluster(num_attr,
            num_attr_choice,
            pair_per_cluster,
            num_cluster):

    if isinstance(int, num_attr_choice):
        attrs_map = {i: {j: 0 for j in num_attr_choice} for i in range(num_attr)}
        total_choice = num_attr * num_attr_choice
    elif isinstance(list, num_attr_choice):
        assert len(num_attr_choice) == num_attr
        attrs_map = {i: {j: 0 for j in num_attr_choice[i]} for i in range(num_attr)}
        total_choice = sum(num_attr_choice)
    else:
        raise ValueError("num_attr_choice must be integer or list")

    quota_full = []
    cluster_list = {i: [] for i in range(num_cluster)}

    while len(quota_full) < total_choice:
        # select a starting attributes and attributes choice
        attrs_start = random.randint(0, num_attr)
        attrs_c_start = random.randint(0, len(attrs_map[attrs_start]))

        attrs_map[attrs_start][attrs_c_start] += 1

        # after selection,


    return