class Test:
    def __init__(self) -> None:
        pass

    def single_bits_test(self, random_binary: str, length: int) -> bool:
        number_of_zeros = 0
        number_of_ones = 0
        max_numbers = 10275
        for i in range(length):
            if random_binary[i] == "0":
                number_of_zeros += 1
                number_of_ones = 0
            else:
                number_of_ones += 1
                number_of_zeros = 0
            if number_of_zeros >= max_numbers or number_of_ones >= max_numbers:
                return False
        return True

    def series_test(self, random_binary: str, length: int) -> bool:
        current_zeros_series = 0
        current_ones_series = 0
        series_couter_zeros = [0, 0, 0, 0, 0, 0]
        series_couter_ones = [0, 0, 0, 0, 0, 0]
        series_ranges = [{"min": 2315, "max": 2685}, {"min": 1114, "max": 1386}, {"min": 527, "max": 723}, {"min": 240, "max": 384}, {"min": 103, "max": 209}, {"min": 103, "max": 209}]
        for i in range(length):
            if random_binary[i] == "0":
                current_zeros_series += 1
                if current_ones_series > 0:
                    if current_ones_series > 5:
                        series_couter_ones[5] += 1
                    else:
                        series_couter_ones[current_ones_series - 1] += 1
                    current_ones_series = 0
            else:
                current_ones_series += 1
                if current_zeros_series > 0:
                    if current_zeros_series > 6:
                        series_couter_zeros[5] += 1
                    else:
                        series_couter_zeros[current_zeros_series - 1] += 1
                    current_zeros_series = 0
        for i in range(6):
            print("Series zeros ", i + 1, " counter: ", series_couter_zeros[i])
            print("Series ones ", i + 1, " counter: ", series_couter_ones[i])
            if series_couter_zeros[i] < series_ranges[i]["min"] or series_couter_zeros[i] > series_ranges[i]["max"] or series_couter_ones[i] < series_ranges[i]["min"] or series_couter_ones[i] > series_ranges[i]["max"]:
                return False
        return True

    def long_series_test(self, random_binary: str, length: int) -> bool:
        current_zeros_series = 0
        current_ones_series = 0
        for i in range(length):
            if random_binary[i] == "0":
                current_zeros_series += 1
                current_ones_series = 0
            else:
                current_ones_series += 1
                current_zeros_series = 0
            if current_ones_series >= 26 or current_zeros_series >= 26:
                return False
        return True

    def poker_test(self, random_binary: str, length: int) -> bool:
        numbers = [0 for _ in range(16)]
        for i in range(0, length, 4):
            number = int(random_binary[i:i+4], 2)
            numbers[number] += 1
        X = 16/5000 * sum([number**2 for number in numbers]) - 5000
        print("X: ", X)
        return 2.16 < X < 46.17