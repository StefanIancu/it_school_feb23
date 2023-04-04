#return string and symbols on both left and right
# make_out_word('<<>>', 'Yay') → '<<Yay>>'

def make_word(out, word):
    return out[:2] + "word" + out[2:]


print(make_word("<<>>", "Yay"))

#return true if first and last index is 6 and len list >=1

def first_last(nums):
  if len(nums) >=1 and nums[0] == 6 and nums[-1] == 6:
    return True
  else:
    return False

first_last6 = [6]
first_last7 = [7, 7, 7]

print(first_last(first_last6))
print(first_last(first_last7))


#return 3, 1, 4

def make_pi():
  return [3, 1, 4]

print(make_pi())

#return true if both lists have the same first or last index with the length 1 or more

def common_end(a, b):
  return (len(a) and len(b) >= 1 and a[0] == b[0] or a[-1] == b[-1])


list1 = [1, 2, 3]
list2 = [1, 5, 4, 7, 3]

print(common_end(list1, list2))

#return sum of an array with 3 elements 

def sum3(numbers):
  return (len(numbers) == 3 and sum(numbers))

numbers = [1, 2, 3]

print(sum3(numbers))

#return swapped rotated left 

def rotate_left3(nums):
  nums[1], nums[2] = nums[2], nums[1]
  return nums[::-1]

nobrs = [1, 2, 3]

print(rotate_left3(nobrs))


numere = [1, 2, 3]
numere2 =  [7,7]

def get23(lista):
  if 2 or 3 in lista:
    return True 
  else:
    return False
  
print(get23(numere))
print(get23(numere2))



