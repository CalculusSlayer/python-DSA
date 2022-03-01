def sum_of_array(A, n):
    if n == 1:
        return A[0]
    s = sum_of_array(A, n-1)
    s = s + A[n-1]
    return s

# n has to be greater than or equal to 0
def power_of_two(n):
    if n == 0:
        return 1
    else:
        power = 2 * power_of_two(n-1)
        return power


if __name__=='__main__':
    l1 = [2, 3, 4]
    l2 = [69, -14, 27]
    print("Sum of l1 is {}".format(sum_of_array(l1, len(l1))))
    print("Sum of l2 is {}".format(sum_of_array(l2, len(l2))))
    
    k = 19
    answer1 = 2**k
    product1 = power_of_two(k)
    print("2^{1} equals {0}".format(product1, k))
    assert answer1 == product1, "User defined power function is incorrect."

