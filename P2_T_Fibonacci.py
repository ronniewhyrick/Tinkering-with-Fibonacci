#Ron Whyrick
#Project 2: Fibonacci Sequence
#Description: Asks user to enter in a number greater than 100.
## this number is the number of iterations of fibbonacci we'll run through.
### the function will right out the sequence, give the sum of the sequence, and
#### give the sum of the subsequence of even numbers and odd numbers in that same iteration.

#Skills employed: List & Forloop manipulations, modulus, Golden Ratio, and string manipulaton

def main():
    
#Declare Local Variables
    i_0 = 0
    i_1 = 0
    n = 0
    
#Inputs
    print("Hello, How many iterations of fibonacci would you like to go through?")
    brkpnt = int(input())
    seq = []
    
#Execution
    #Raw Fib sequence iteration 
    for i in range(0,brkpnt+1):
        ans = i_0 + i_1
        seq.append(ans)
        i_0 = i_1
        if i < 2:
            i_1 = 1
            i_0 = 0
        else:
            i_1 = ans
    sum_seq = str(sum(seq))
    #Filtered Fib Sequence
    even_seq = []
    odd_seq = []
    for e in seq:
        if e % 2 == 0:
            even_seq.append(e)
        else:
            odd_seq.append(e)
    sum_even = str(sum(even_seq))
    sum_odd = str(sum(odd_seq))

#Outputs   
    #Raw Sequence Outputs 
    print("through is your fibonacci sequence")
    print(seq)
    print("The  sum of that sequence is " + sum_seq)
    #Filtered Sequence Outputs 
    print("This is the filtered sequence of all even values")
    print(even_seq)
    print("The sum of the even sequence is " + sum_even)
    print("This is the filtered sequence of all odd values")
    print(odd_seq)
    print("The sum of your odd sequence is " + sum_odd)
    
#Declarations 
if __name__=="__main__":
    main()
