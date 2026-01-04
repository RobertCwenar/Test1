# Write a program that calculates the sum of all numbers from 1 to a given number n entered by the user.
# For example, for 5 the program should return 15 (1+2+3+4+5).

# Add library time
import time

# Function to calculate the sum from 1 to n
def sum_to_n(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

# Test 1 function using list comprehension
def test1_sum_to_n(n):
    return sum([n for n in range(1, n + 1)])

# Test 2 function using set comprehension
def test2_sum_to_n(n):
    return sum({n for n in range(1, n + 1)})

# Test 3 function using generator expression
def test3_sum_to_n(n):
    return sum((n for n in range(1, n + 1)))

# Test 4 function using the formula n(n + 1)/2
def test4_sum_to_n(n):
   return (1 + n)/ 2 * n

# Function to measure time taken by each function
def finish_timer(start):
    end = time.perf_counter()
    return end - start

def function_performance(func, arg):
    start= time.perf_counter()
    func(arg) # if you want to create a function you use () after the function name
    end =time.perf_counter()
    return end -start 

def show_message(message):
    print("Message from function.", message)

# Main program

print(function_performance(sum_to_n, 50000))
print(function_performance(test1_sum_to_n, 50000))
print(function_performance(test2_sum_to_n, 50000))
print(function_performance(test3_sum_to_n, 50000))  
print(function_performance(test4_sum_to_n, 50000))