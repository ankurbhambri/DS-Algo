
- Common Backtracking Template

```

def backtrack(start, path):

    if is_goal_state(path):
        res.append(path[:])
        return

    for i in range(start, len(data)):
        if valid_choice(i, path):
            path.append(data[i])
            backtrack(i + step, path)
            path.pop()  # backtrack

```
