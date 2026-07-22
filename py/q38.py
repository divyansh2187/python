prices = [7, 6, 1, 4, 3, 2, 9]

def sellBuy(arr):
    maxProfit = 0
    minPrice = float('inf')
    for i in range(0,len(arr)):
      minPrice =min(minPrice,arr[i])
      maxProfit = max(maxProfit , arr[i]-minPrice)
        
    return maxProfit 
print(sellBuy(prices))



# ------------brute force ---------------
# def buySEll(arr):
#     profit = float('-inf')
#     for i in range(0,len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]<arr[j]:
#               if arr[j]-arr[i]> profit:
#                 profit = arr[j]-arr[i]
#                 sell = arr[j]
#                 buy = arr[i]

#     return  buy , sell , profit
# print(buySEll(prices))


        