class Employee:
    def __init__(self, fun):
        self.employees = []
        self.fun = fun

        # Dynamic programming happens here.
        self.going = -1
        self.not_going = -1


def not_going(v: Employee):
    # Check for cached result.
    if v.not_going >= 0:
        return v.not_going

    v.not_going = 0

    for e in v.employees:
        v.not_going += going(e)

    return v.not_going


def going(v: Employee):
    # Check for cached result.
    if v.going >= 0:
        return v.going

    # Assume v goes to the party.
    result = v.fun

    for e in v.employees:
        result += not_going(e)

    # Make sure, it's better than
    # if v didn't go to the party.
    v.going = max(result, not_going(v))

    return v.going


if __name__ == "__main__":
    #       10
    #      /  \
    #     1    5
    #    / \
    #   2   1

    boss = Employee(10)
    emp1 = Employee(1)
    emp2 = Employee(5)
    emp3 = Employee(2)
    emp4 = Employee(1)

    boss.employees = [emp1, emp2]
    emp1.employees = [emp3, emp4]

    print(going(boss))
