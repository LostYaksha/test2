def update_dict_values(my_dict):
    modified_dict = my_dict.copy()  # Create a copy to avoid modifying the original
    keys = list(my_dict.keys())  # Get all keys to avoid iterating over changing dictionary

    for i, key in enumerate(keys):
        left_neighbor = keys[i - 1] if i > 0 else None
        right_neighbor = keys[i + 1] if i < len(keys) - 1 else None
        current_state = "alive" if my_dict[key] == 1 else "dead"


        if current_state == "alive":
            live_neighbors = 0
            if left_neighbor and my_dict[left_neighbor] == 1:
                live_neighbors += 1
            if right_neighbor and my_dict[right_neighbor] == 1:
                live_neighbors += 1
            modified_dict[key] = 0 if live_neighbors == 2 else 1
        elif current_state == "dead" and right_neighbor and my_dict[right_neighbor] == 1:
            modified_dict[key] = 1

    return modified_dict


my_dict = {
    "key1": 1,
    "key2": 1,
    "key3": 0,
    "key4": 0,
    "key5": 1,
    "key6": 0,
    "key7": 0,
    "key8": 1
}

for _ in range(5):
    my_dict = update_dict_values(my_dict.copy())
    print(my_dict)
