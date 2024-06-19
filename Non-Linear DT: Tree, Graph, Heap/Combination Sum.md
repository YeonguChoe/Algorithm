# Combination Sum

## Backtracking을 사용하지 않는 일반적인 DFS 방법
```python
def combinationSum(candidates, target):
    my_answer = []
    dfs(my_answer, [], candidates, target)
    result = set([tuple(element) for element in my_answer])
    result = [list(item) for item in result]
    return result


def dfs(answer, current_root, candidates, target):
    if sum(current_root) == target:
        answer.append(sorted(current_root.copy()))
        return
    else:
        for c in candidates:
            if sum(current_root) + c <= target:
                current_root.append(c)
                dfs(answer, current_root, candidates, target)
                current_root.pop()
    return
```
- 시간 복잡도: $O(\text{candidate의 개수}^{\frac{Target}{min(candidate)}})$
- 공간 복잡도: $O(\frac{Target}{min(candidate)})$

## Backtracking을 사용하는 방법
- 왼쪽은 include 하고 i 유지, 오른쪽은 exclude하고 i증가
```python
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
```
- 시간 복잡도: $O(2^{\frac{Target}{min(candidate)}})$
- 공간 복잡도: $O(\frac{Target}{min(candidate)})$
