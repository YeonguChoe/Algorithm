def combinationSum(candidates, target):
    result = []
    solution_variable = []
    backtrack(candidates, 0, result, solution_variable, target)
    return result


def backtrack(candidate, i, result, solution_variable, target):
    if sum(solution_variable) == target:
        result.append(solution_variable.copy())
        return
    if sum(solution_variable) > target or i >= len(candidate):
        return
    solution_variable.append(candidate[i])
    backtrack(candidate, i, result, solution_variable, target)
    solution_variable.pop()
    backtrack(candidate, i + 1, result, solution_variable, target)

print(combinationSum([2, 3, 5], 8))
