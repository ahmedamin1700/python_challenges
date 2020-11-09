def print_first(problem_list: list) -> str:
    """
    Prints the first line of the arranger.
    :param problem_list: list of dicts.
    :return: str.
    """
    first = ""
    counter = 1
    for item in problem_list:
        first += "  "
        first += item["first"]
        if counter < len(problem_list):
            first += "    "
        counter += 1
    first += "\n"
    return first


def print_second(problem_list: list) -> str:
    """
    Prints the second line of the arranger.
    :param problem_list: list of dicts.
    :return: str.
    """
    second = ""
    counter = 1
    for item in problem_list:
        second += item["operator"] + " "
        second += item["second"]
        if counter < len(problem_list):
            second += "    "
        counter += 1
    second += "\n"
    return second


def print_dashes(problem_list: list) -> str:
    """
    Prints dashes.
    :param problem_list: list of dicts
    :return: str.
    """
    dashes = ""
    counter = 1
    for item in problem_list:
        dashes += "--"
        dashes += item["length"] * "-"
        if counter < len(problem_list):
            dashes += "    "
        counter += 1
    # dashes += "\n"
    return dashes


def calculate(problem_list: list) -> str:
    """
    Runs calculation of the problems and convert it to str.
    :param problem_list: list of dicts.
    :return: str.
    """
    result = "\n"
    counter = 1
    for item in problem_list:
        if item["operator"] == "+":
            res = int(item["first"]) + int(item["second"])
            item["result"] = "  " + str(res).rjust(item["length"])
        elif item["operator"] == "-":
            res = int(item["first"]) - int(item["second"])
            if res < 0:
                item["result"] = " " + str(res).rjust(item["length"])
            else:
                item["result"] = "  " + str(res).rjust(item["length"])
        result += item["result"]
        if counter < len(problem_list):
            result += "    "
        counter += 1
        # print(result, end="")
    return result


def print_all(problem_list: list, result: bool) -> str:
    """
    Prints all format.
    :param result: bool to calculate.
    :param problem_list: list of dicts.
    :return: str.
    """
    arranger = ""
    arranger += print_first(problem_list)
    arranger += print_second(problem_list)
    arranger += print_dashes(problem_list)
    if result:
        arranger += calculate(problem_list)

    return arranger


def rule_errors(problem_list: list) -> str:
    """
    Check for expected errors
    :param problem_list: list of dicts.
    :return: str.
    """
    for item in problem_list:
        if not (item["operator"] == "+" or item["operator"] == "-"):
            return "Error: Operator must be '+' or '-'."
        elif not (item["first"].isdigit() or item["second"].isdigit()):
            return "Error: Numbers must only contain digits."
        elif len(item["first"]) > 4 or len(item["second"]) > 4:
            return "Error: Numbers cannot be more than four digits."


def arithmetic_arranger(problems: list[str], result=False):
    """
    Arranger of the arithmetic problems.
    :param result: Calculate the arithmetic.
    :param problems: list of strings.
    :return: list of strings of errors.
    """
    problem_list = list()
    for problem in problems:
        new_problem = problem.split()

        if len(new_problem[0]) > len(new_problem[2]):
            largest_length = len(new_problem[0])
            new_problem[2] = (len(new_problem[0]) - len(new_problem[2])) * " " + new_problem[2]
        else:
            largest_length = len(new_problem[2])
            new_problem[0] = (len(new_problem[2]) - len(new_problem[0])) * " " + new_problem[0]

        pro_dict = {
            "first": new_problem[0],
            "second": new_problem[2],
            "operator": new_problem[1],
            "length": largest_length
        }

        problem_list.append(pro_dict)

    error = rule_errors(problem_list)
    if error:
        return error
    if len(problem_list) > 5:
        return "Error: Too many problems."
    else:
        print(print_all(problem_list, result))
        return print_all(problem_list, result)


# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
# arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
