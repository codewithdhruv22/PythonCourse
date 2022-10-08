"""


Vishal has opened a new sports bar. On the very first day, he made the bar free for everyone.
There are various pool tables which most of the people are interested in and the pool tables are numbered from 1 to K.
 
Let's say there are N customers who visited the bar. Each has an entry and exit time. The customers are very specific with their pool table, if they get their requested table, then they are going to play, otherwise they will leave.
The customer will arrive at a table at his entry time and has to leave the table at his exit time. A customer will use only a table of his preference. If the customer doesn’t get the specific table of their choice, they won’t take any other table, even if it is available.
 
Vishal wants most of the customers to join his club, so that they visit again, and his business may flourish.
 
Given a list of N customer and K tables, along with their Entry (En[]) and Exit (Ex[]) time and table number T[], find the maximum number of customers that can be accommodated in the club.
 
Let us understand this with an example:
 
Let’s say N = 3 and K =3
Entry and Exit and Pool table is given in sequence for each customer.
Customer 1: 10 100 1 : Means entry time is 10, Exit time is 100, and the table which he prefers is 1
Customer 2: 10 50 1 : Means entry time is 10, Exit time is 50, and the table which prefers is 1.
Customer 3: 10 100 2 : Means entry time is 10, Exit time is 100, and the table which prefers is 2.
 
As Vishal wants more customers to be accommodated, he will prefer those customers who stay less, so that if anyone else comes, they can be easily accommodated.
So, here Customer 2, will be given Table 1.
For Table 2, there is no conflict, so customer 3 easily takes table 2.
 
In this way, we can accommodate a maximum of 2 customers.
Hence the answer is 2.
 
Example 1:
Input: 
3                             ->            Input integer, N
3                              ->            Input integer, K
1  3  1                    ->            Input integer, En[], Ex[], T[]
4  6  2                    ->            Input integer, En[], Ex[], T[]
7  10  3                 ->            Input integer, En[], Ex[], T[]
Output:
3              ->            Output
Explanation:    
Clearly in the above scenario, there is no conflict among the customers for pool tables, each customer is looking for different tables. Hence all the customers can be accommodated here.
So the answer is 3.
 
Example 2:
Input: 
4                             ->            Input integer, N
2                              ->            Input integer, K
10  100  1             ->            Input integer, En[], Ex[], T[]
100  200  1          ->            Input integer, En[], Ex[], T[]
150  500  2          ->            Input integer, En[], Ex[], T[]
200  300  2          ->            Input integer, En[], Ex[], T[]
Output:
3                              ->            Output
Explanation:
In the above scenario.
Table 1 can be easily used by both the customers 1 & 2, as their timings don’t overlap each other. Count = 2
Table 2 can be only be used by either customer 3 & 4, as their timings conflict. The table will be given to that who spends lesser time at the table. In this case it is customer 4. Count =1
 
So, the customer 1,2 & 4 can be accommodated.
So, the answer is 3.
 
Constraints:
1 <= N, K  <= 100
1 <= T < 100
1 <= En[] < Ex[] < 10000
All inputs are integers.
 
The input format for testing
First Input – Accept value of Integer, N.
Second Input – Accept value of Integer, K (Next Line).
Next ‘N’ Lines– Elements of integers, entry Time, Exit time, Table number  (Separated by SPACE)
The line number corresponding to the customer number.
 
The Output format for testing
The output is an integer as per above logic. (Check the output in Example 1, Example 2).
Additional messages in output will cause the failure of test cases.
 
Instructions:
System doesn’t allow any kind of hard coded input value/values.
Written program code by the candidate will be verified against the inputs which are supplied from the system.

          
Program EditorChoose programming Language* :  
C


Having issue with dropdown - Click here
1
class Sportsbar{
2
​
3
​
4
}
Compile CodeSave CodeFinal Submit
We understand few of the browsers / old browser versions do not support advanced scripting. We would recommend you to use latest Chrome (v80 and above) or Mozilla Firefox (v80 and above) browsers. In case, you are using older version of these browsers, or any other browser, they may not support the iON Advanced Coding Editor. You can switch to the recommended browsers & versions to get the best experience.
If you are not able to switch/upgrade for now, we have an option of a simple coding editor which will work on older Chrome/Mozilla versions, and various other browsers as well. You will not get some of the features of the iON Advanced coding editor (Like line numbers and keyword highlighting), but you will be able to type/submit code.



"""




#SOLUTION  -  

#  N K T En Ex


def sim_table(customer_details):
    dupes = [x for n, x in enumerate(customer_details) if x in customer_details[:n]]
    res = [*set(dupes)]
    return res


def time_diff_cal(assured_conflicted_customer):
    time_diff = []
    for customer in assured_conflicted_customer:
        calc_time = customer[1] - customer[0]
        time_diff.append(calc_time)
    return time_diff


num_of_cus = int(input("Enter the count of customers:- "))
num_of_tab = int(input("Enter the number of table available:- "))

num_of_assigned_cust = []


cust_dets = []
table_pref = []
for cus in range(num_of_cus):
    cust_det = []
    ent_time = int(input(f"Enter the entry time of customer no {cus+1} :- "))
    ext_time = int(input(f"Enter the exit time of customer no {cus+1}:- "))
    table_no = int(input(f"Enter the preferred table no. for customer no {cus+1}:- "))
    table_pref.append(table_no)

    cust_det.append(ent_time)
    cust_det.append(ext_time)
    cust_det.append(table_no)
    cust_dets.append(cust_det)

conflict_tab = sim_table(table_pref)

# [[1,2,3],[2,3,2] , [2,4,2]]
conflict_customer = []
for cusotmer in cust_dets:
     if cusotmer[2] in conflict_tab:
         conflict_customer.append(cusotmer)
print(conflict_customer)

assured_conflicted_customer = []

conflicted_program = False
for i in range(len(conflict_customer)):

    if(i>(len(conflict_customer) - 2)):
        break
    # print(i)
    # print(conflict_customer[i])
    # print(conflict_customer[i][1])
    # print(conflict_customer[i][1] <= conflict_customer[i + 1][0])
    elif conflict_customer[i][1] <= conflict_customer[i+1][0]:
        print(f"No Conflict Found between {conflict_customer[i][1]} and {conflict_customer[i+1][0]}")

    else:
        print(f"CONFLICT FOUND between {conflict_customer[i][1]} and {conflict_customer[i+1][0]}")
        assured_conflicted_customer.append(conflict_customer[i])
        assured_conflicted_customer.append(conflict_customer[i + 1])
        conflicted_program  = True


if conflicted_program:
    my_time_diff = list(time_diff_cal(assured_conflicted_customer))
    lowest_time_cust_details = assured_conflicted_customer[my_time_diff.index(min(my_time_diff))]

    print(cust_dets)
    print(assured_conflicted_customer)
    print(lowest_time_cust_details)


    noDupes_assured_conflicted_customer  = []

    for l in assured_conflicted_customer:
        if l not in noDupes_assured_conflicted_customer:
            noDupes_assured_conflicted_customer.append(l)

    for customer in noDupes_assured_conflicted_customer:
        cust_dets.remove(customer)
    cust_dets.append(lowest_time_cust_details)

print(f"A total of {len(cust_dets)} customers can be in sports bar and here are the details of the customers:- ")
print(cust_dets)





