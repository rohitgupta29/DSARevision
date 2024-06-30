"""
Designing a browser history

-Browser class

- visit(url)


- back(steps)

-- forward (steps)


1. Always to set to call the constructor homepage.

2. visit(google.com) -> visit(instagram) -> visit(facebook) ->

3. go back by one step -> instagram -> go back by one step -> return google.com

4. forward(1) -> instagram -> visit(takeyouforward) -> facebook removed for visit

5. can i go two steps ahead? -> no, as we cannot go. so, we will be standing at takeyouforward.com

6.  back by 2 steps -> instagram, google.com

7. go back by 7 steps -> but at max i can go 1 step.



"""


