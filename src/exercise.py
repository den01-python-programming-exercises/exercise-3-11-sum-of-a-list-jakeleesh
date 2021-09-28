def main():
    #write your code below this line
    nums = []
    while True:
        num = int(input())
        if (num == -1):
            break
        else:
            nums.append(num)
    sum = 0
    for number in nums:
        sum += number
    print("Sum: " + str(sum))

if __name__ == '__main__':
    main()
