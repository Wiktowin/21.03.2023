def is_sorted(my_list):
    if isinstance(my_list[0], str):
        sorted_list = sorted(my_list)
    else:
        sorted_list = sorted(my_list, key=int)
    return my_list == sorted_list

assert is_sorted([1, 3, 5]) == True
assert is_sorted([1, 5, 3, 8, 10]) == False
assert is_sorted(["apple", "blackberry", "cherry", "plum"]) == True
assert is_sorted(["mercedes", "mazda", "suzuki", "toyota"]) == False




def get_sublist(my_list, item):
    if item not in my_list:
        return "Error"
    elif my_list.index(item) == 0:
        return []
    else:
        return my_list[:my_list.index(item)]

assert get_sublist([1, 3, 5], 1) == []
assert get_sublist([1, 5, 3, 8, 10], 8) == [1, 5, 3]
assert get_sublist([], 8) == "Error"
assert get_sublist(["apple", "blackberry", "cherry", "plum"], "carrot") == "Error"
assert get_sublist(["mercedes", "mazda", "toyota", "suzuki"], "mazda") == ["mercedes"]




def city_rating(cities_dict):
    sum_points = sum(cities_dict.values())
    avg_points = sum_points / len(cities_dict)
    max_city = max(cities_dict, key=lambda x: cities_dict[x])
    return sum_points, avg_points, max_city

cities_dict = {
    "Munich": 74,
    "Berlin": 62,
    "Cologne": 51,
    "Hamburg": 68,
    "Dusseldorf": 59,
    "Kassel": 52
}
assert city_rating(cities_dict) == (366, 61.0, "Munich")




def not_busy_children(groups_dict):
    result_set = set()
    total_set = set()
    for group_set in groups_dict.values():
        total_set.update(group_set)
    for group_name, group_set in groups_dict.items():
        rest_groups_set = total_set - set([group_set])
        rest_set = set.union(*rest_groups_set)
        unique_set = set(group_set) - rest_set
        result_set.update(unique_set)
    return result_set

groups = {"swimming": ["Emma", "Albert", "Peter"],
          "chess": ["Caroline", "Albert", "Pam", "Harry"],
          "guitar": ["Harry", "Peter", "Sam"],}
assert not_busy_children(groups) == {"Emma", "Caroline", "Pam", "Sam"}


if __name__ == '__main__':
    test_is_sorted(my_list)
    test_get_sublist(my_list, item)