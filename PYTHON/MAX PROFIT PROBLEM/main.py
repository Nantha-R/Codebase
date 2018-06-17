from constants import *


class MaximumProfitProblem:
    """
    Class used for finding the maximum profit scenarios
    """
    def __init__(self):
        """Constructor for MaximumProfitProblem"""
        self.solution_list = []
        self.max_profit = 0

    def __get_current_profit(self, current_profit, remaining_units_of_time, profit_of_property, time_to_build):
        """Calculates the current profit"""
        return current_profit + profit_of_property * (remaining_units_of_time - time_to_build)

    def get_solution(self,
                     remaining_units_of_time,
                     no_of_casinos=0,
                     no_of_hotels=0,
                     no_of_apartments=0,
                     current_profit=0):
        """Calculates all possible scenarios of constructing the buildings"""

        # If the current profit is the maximum profit obtained so far
        if current_profit >= self.max_profit:

            # Creating a dict object for the results obtained
            solution = {'no_of_casinos': no_of_casinos,
                        'no_of_hotels': no_of_hotels,
                        'no_of_apartments': no_of_apartments}

            # If multiple solutions are present with the same maximum profit
            if current_profit == self.max_profit:
                self.solution_list.append(solution)
            else:
                self.max_profit = current_profit
                self.solution_list = [solution]

        # If the time remaining is enough to construct a Casino
        if remaining_units_of_time >= CasinoAttributes.TIME_TO_BUILD:
            self.get_solution(remaining_units_of_time - CasinoAttributes.TIME_TO_BUILD,
                              no_of_casinos + 1, no_of_hotels, no_of_apartments,
                              self.__get_current_profit(current_profit,
                                                        remaining_units_of_time,
                                                        CasinoAttributes.PROFIT_EARNED,
                                                        CasinoAttributes.TIME_TO_BUILD))

        # If the time remaining is enough to construct a Hotel
        if remaining_units_of_time >= HotelAttributes.TIME_TO_BUILD:
            self.get_solution(remaining_units_of_time - HotelAttributes.TIME_TO_BUILD,
                              no_of_casinos, no_of_hotels + 1, no_of_apartments,
                              self.__get_current_profit(current_profit,
                                                        remaining_units_of_time,
                                                        HotelAttributes.PROFIT_EARNED,
                                                        HotelAttributes.TIME_TO_BUILD))

        # If the time remaining is enough to construct a Apartment
        if remaining_units_of_time >= ApartmentAttributes.TIME_TO_BUILD:
            self.get_solution(remaining_units_of_time - ApartmentAttributes.TIME_TO_BUILD,
                              no_of_casinos, no_of_hotels, no_of_apartments + 1,
                              self.__get_current_profit(current_profit,
                                                        remaining_units_of_time,
                                                        ApartmentAttributes.PROFIT_EARNED,
                                                        ApartmentAttributes.TIME_TO_BUILD))


if __name__ == "__main__":
    # Get the value of time units from the user
    units_of_time = int(input("Time Unit:"))

    # Calculate the maximum profit scenarios
    obj = MaximumProfitProblem()
    obj.get_solution(units_of_time)

    # Print the results
    print("Earnings:{}".format(obj.max_profit))
    print("Solutions:")
    for index, solution in enumerate(obj.solution_list):
        print("{0}. C : {1} H : {2} A : {3}".format(index+1,
                                                    solution['no_of_casinos'],
                                                    solution['no_of_hotels'],
                                                    solution['no_of_apartments']))
