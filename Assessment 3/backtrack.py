def combinationSum(candidates, target):
    combinations = []
    
    def backtrack(start, path, target):
        if target == 0:
            combinations.append(path[:])  # Append a copy of the current combination
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                continue
            
            path.append(candidates[i])
            backtrack(i, path, target - candidates[i])
            path.pop()
    
    backtrack(0, [], target)
    
    return combinations

# Test case
candidates = [2, 3, 6, 7]
target = 7
result = combinationSum(candidates, target)
print(result)
