Time complexity: O(n) ?
Space complexity: O(1)
Executed in Leetcode: Yes
Challenges: No, as I had earlier learned in previous batch.
Comments: We use dynamic programming to calculate the minimum cost. For each value, we add the value to the minimum
value of colors different from the current color, belonging to the subsequent rows. This step step is performed for all 3 columns. 
Thereafter, the minimum from the first row is returned as the result.
            
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        # Boundary condition
        if len(costs) == 0:
            return 0
        
        for n in reversed(range(len(costs)-1)):
            
            # Total cost when nth house is painted red
            costs[n][0] += min(costs[n + 1][1], costs[n + 1][2])
            
            # Total cost when nth house is painted greem
            costs[n][1] += min(costs[n + 1][0], costs[n + 1][2])
            
            # Total cost when nth house is painted blue
            costs[n][2] += min(costs[n + 1][0], costs[n + 1][1])

        # Return the minimum value from the first row
        return min(costs[0]) 
        
