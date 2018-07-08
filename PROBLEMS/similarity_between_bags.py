
def find_similarity_score(difference, total_no_fruits):
    """
    Calculate the similarity score of the bags
    """
    total_no_of_dissimilar_fruits = sum(difference.values())
    return 1 - (total_no_of_dissimilar_fruits / total_no_fruits)


def find_similarity(bag_a, bag_b, fruits_category):
    """
    Calculates the similarity of the bag contents
    """
    # Convert both list into a dict
    fruits_in_bag_a = dict()
    fruits_in_bag_b = dict()
    for fruit in bag_a:
        fruits_in_bag_a[fruit] = fruits_in_bag_a.get(fruit, 0) + 1
    for fruit in bag_b:
        fruits_in_bag_b[fruit] = fruits_in_bag_b.get(fruit, 0) + 1
    # Find the number of fruits which can be removed from both the bags to make them similar
    difference = {fruit: abs(fruits_in_bag_b.get(fruit, 0) - fruits_in_bag_a.get(fruit, 0)) for fruit in fruits_category}
    return find_similarity_score(difference, len(bag_a)+len(bag_b))


if __name__ == '__main__':
    fruits_category = ['banana', 'apple', 'orange']
    # First convert the fruits in both the bags into a list
    bag_a = ['banana', 'apple', 'orange', 'apple', 'apple']
    bag_b = ['banana', 'banana', 'orange', 'apple', 'orange']
    result = find_similarity(bag_a, bag_b, fruits_category)
    print(result)

