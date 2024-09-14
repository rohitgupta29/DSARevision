

The Framework:

1. Look for the form of the problem! 

Eg. Level, choice, Check and Move 

2. Decide the state and meaning.

    [DP(_) = _ ]   # 2nd _ is return value

Eg. DP(level, constraint1,constraint2) -> expected return value 

3. Decide the transitions

Eg. DP[level, constain1,constraint2] 
    -1---> don't take: DP(level + 1, constraint1,constraint2)
    choice
    -2---> take: [we check condition] eg. x > 1, value_at_level + DP(level+1, constaint1 + constraint1[level], constraint2 + 1)


out of 1 and 2, we will take max. 

4. Check Time Complexity : Code the DP problems after checking TC. 

TC = (no. of states) * (1 + Avg. Tranition cost)

    or 

    = (no of states) * ( 1 + avg. no. of transitions per state)


How do we find states of a problem?

how many possibilities of state and time can be there?

N*K*X
N = level, 
K = constrain1 (0 to K)
X = constraint2 (o to X)


5. Code 

a. Pruning (to check if our value is getting out of max value)
b. Base Case 
c. Cache Check 
d. Transition 
e. Save and Return 

def rec(level, time_taken, item_taken):
    
    # pruning 

    # base case 
    if(level ==n):
        return 0
    # cache check 
    (usually array is the best cache we can use)
    dp = list() (with len = 1 + len(n))
    dp = [-1 for i in range(len(n) + 1)]
    
    if dp[level][time_taken][item_taken] != -1:
        return dp[level][time_taken][item_taken]



    # compute/ transition 
    ans = rec(level+1, time_taken,item_taken) 
    if (time_taken + t[level] <= x and item_taken + 1 <= k:
        ans = min(ans, s[level] + rec(level+1, time_taken + t[level], item_taken + 1)

    # save and return 
    return dp[level][time_taken][item_taken] = ans 