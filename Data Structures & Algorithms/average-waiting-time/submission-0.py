class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # customers[i] = arrival[i], time[i]
        # already sorted by arrival time
        # chef prepares one customer at a time
        # Return avg waiting time

        # Customers cannot be served until previous customer is finished
        # Start at arrival time
        # End when finished
        # 1, 2 means start at 1 finish at 3 (means 2 + 1 = 3) so time is 3-1 = 2
        
        prefix_sum = [customer[0]  + customer[1] for customer in customers]

        print("Sums: ", prefix_sum)
        start = customers[0][0]
        last_end = prefix_sum[0]
        sum = last_end - start

        print("SUM at 0: ", sum)
        for i in range(1, len(customers)):
            print()
            start = customers[i][0]
            end = customers[i][1]
    
            wait = last_end - start

            if wait < 0:
                last_end = end + start
                sum += end
                continue

            print(f"Last End: {last_end}")
            print(f"Arrived: {start} \tTime: {end} \tWait: {wait} ")
            sum += end + wait # When we ended + how long we waited

            last_end += end

            

            # We always end at prefix_sum_i + however long we waited
            # We want to store how long we waited
            # How long we waited
            # Whenever last element finished prefix_sum[i-1] + wait time

            # last_end = 3
            # start = 2
            # end = 5
            # last_end - start = 1 (waited 1)
            # sum = 7 + 1 (wait) - start
      

            
            print(f"SUM at {i}: {end + wait}")

        print("Final Sum: ", sum)
        return sum/len(customers)
        