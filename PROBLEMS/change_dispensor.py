import sys


class ChangeDispenser:
    """
    Class used for implementing the working of Change dispenser.
    """

    def __init__(self):
        """
        Constructor for ChangeDispenser.
        """
        self.result_set = []
        self.coin_count = sys.maxsize
        # Used to reduce the number of coins present in the solution.
        self.MAXIMUM_RESULTS = 5
        # Used to stop generating all possible solutions.

    def get_change(self,
                   amount_remaining,
                   coins_available,
                   result=[]):
        """
        Generate possible solutions for changes.
        """

        # Reducing the result set to only certain number of solutions.
        # This is helpful in situations where if coins are very large in number.
        # Then it may result in large number of possible solutions
        # which in turn leads to high run time complexity
        # resulting in making the user wait for a long period of time.
        if len(self.result_set) <= self.MAXIMUM_RESULTS:

            # If a possible solution is found
            if amount_remaining == 0:

                # If the number of coins in the current solution is equal
                # to the number of coins in the already accepted solution.
                if len(result) == self.coin_count:
                    # Sorting is done to avoid redundancies in result set.
                    result = sorted(result)

                    # If the current solution is not present in
                    # the previous accepted solution list.
                    if result not in self.result_set:
                        self.result_set.append(result)

                elif len(result) < self.coin_count:
                    # The current solution results in less number of coins
                    # than the previous accepted solution.
                    self.coin_count = len(result)
                    self.result_set = [sorted(result)]
            else:
                for coin, number_of_coins in coins_available.items():

                    # Recursively checking for all possible possible solutions.
                    if number_of_coins > 0:
                        if amount_remaining >= coin:

                            # Temporary variables are needed since recursion is used.
                            temp_coins_available = coins_available.copy()
                            temp_result = result.copy()
                            temp_coins_available[coin] = number_of_coins - 1
                            temp_result.append(coin)

                            # Recursive call.
                            self.get_change(amount_remaining-coin,
                                            temp_coins_available,
                                            temp_result)

    def __get_coin_preference_from_user(self):
        """
        Get the coin preference from the user.
        """
        print("Coins available in the result set :")
        print("Choose any one given below :")

        # if self.result_set is equal = [[2,3,5],[2,2,3,7]]
        # coins is equal to [2,3,5,7]
        coins = list(set(coin for result in self.result_set for coin in result))

        # Getting user preference.
        for index in range(0, len(coins)):
            print("{0} : {1} rupee coin.".format(index+1,
                                                 coins[index]))
        preference = int(input("Enter your preferences:"))
        print("You have chosen {} rupee coin as your preference."
              .format(coins[preference-1]))
        return coins[preference - 1]

    def __get_result(self, user_preferred_coin):
        """
        Get result containing maximum number of user preferred coin.
        """
        maximum = 0
        for result in self.result_set:
            if result.count(user_preferred_coin) > maximum:
                maximum = result.count(user_preferred_coin)
                solution = result
        return solution

    def obtain_solution(self):
        """
        Obtain solution from the result set
        """
        if len(self.result_set):
            # Print the result if there is only one possible solution.
            if len(self.result_set) == 1:
                return self.result_set[0]
            else:
                # User preferences is required since there are many solutions.
                user_preferred_coin = self.__get_coin_preference_from_user()
                return self.__get_result(user_preferred_coin)
        else:
            # When there is no solution possible.
            return "Change cannot be given"


if __name__ == '__main__':
    # Get the number of coins from the user.
    number_of_coins = int(input("Enter the number of coins :"))

    # Store the coins in a dictionary.
    # Eg: 2 five rupee coins will result in a dict equal to {5:2}
    coins_available = dict()
    for _ in range(0, number_of_coins):
        inp = int(input())
        coins_available[inp] = coins_available.get(inp, 0) + 1

    # Get the amount of Note for which the change should be provided.
    note = int(input("Enter your amount :"))

    # Get possible solutions of changes possible for a given note.
    obj = ChangeDispenser()
    obj.get_change(note, coins_available)
    result_set = obj.result_set

    # Obtain suitable change.
    result = obj.obtain_solution()

    print("RESULT :{}".format(result))
