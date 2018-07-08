from collections import Counter
import math


def find_similarity_using_cosine(bag_a, bag_b):
    """
    Find the similarity between two list using cosine formula.
    wiki : https://en.wikipedia.org/wiki/Cosine_similarity
    """
    # Converting list into a dict
    fruits_in_bag_a = Counter(bag_a)
    fruits_in_bag_b = Counter(bag_b)

    # Finding the fruit combinations
    fruits = set(fruits_in_bag_a).union(fruits_in_bag_b)

    # Finding the cosine angle of two bags
    dot_product = sum(fruits_in_bag_a.get(fruit, 0) * fruits_in_bag_b.get(fruit, 0) for fruit in fruits)
    magnitude_of_bag_a = math.sqrt(sum(fruits_in_bag_a.get(k, 0) ** 2 for k in fruits))
    magnitude_of_bag_b = math.sqrt(sum(fruits_in_bag_b.get(k, 0) ** 2 for k in fruits))
    return dot_product / (magnitude_of_bag_a * magnitude_of_bag_b)


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
    # This was my initial solution to the problem
    initial_result = find_similarity(bag_a, bag_b, fruits_category)
    # I learnt about cosine similarity after going through some wikis
    final_result = find_similarity_using_cosine(bag_a, bag_b)
