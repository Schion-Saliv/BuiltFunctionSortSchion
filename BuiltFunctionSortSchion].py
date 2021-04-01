from statistics import median

import time


def test_run():
    start = time.time()
    x = 1
    for i in range(0, 100000000):
        x *= 1.001
    end = time.time()
    print("The time taken is ", end - start, "seconds.")

def minmax(list):
    min = max = list[0] # assuming no-empty
    numMedian = median(list)

    for num in list:
        if (num > max):
            max = num
        if (num < min):
            min = num
    return (min,numMedian,max)


if __name__ == '__main__':

  import random
  numberList = []
  for k in range(int(random.random()*7+3)):
    numberList.append(int(random.random()*20-10))
  print(numberList)
print(minmax(numberList))

if __name__ == "__main__":
    test_run()

print(sorted(numberList))