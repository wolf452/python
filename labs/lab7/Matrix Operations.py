import numpy as np

num_of_arr1 = int(input("Enter the number of elements in the array: "))
num_of_arr2 = int(input("Enter the number of elements in the second array: "))

def rand_of_num1():
    return np.array(np.random.randint(0, num_of_arr1, size=num_of_arr1), ndmin=2)

def rand_of_num2():
    return np.array(np.random.randint(0, num_of_arr2, size=num_of_arr2), ndmin=2)

arr_1 = rand_of_num1()
arr_2 = rand_of_num2()


print("Sum arr_1:", np.sum(arr_1))
print("Mean arr_1:", np.mean(arr_1))
print("Transpose arr_1:", arr_1.T)


if num_of_arr1 == num_of_arr2:
    sum_of_arr = arr_1 + arr_2
    sub_of_arr = arr_1 - arr_2
    Multiplication = arr_1 * arr_2


    arr_2[arr_2 == 0] = 1
    Division = arr_1 / arr_2

    print("Sum:", sum_of_arr)
    print("Sub:", sub_of_arr)
    print("Multiplication:", Multiplication)
    print("Division:", Division)
else:
    print("Arrays must have the same size!")
