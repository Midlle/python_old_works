def is_palindrome(num_list):
    reverse_list = num_list[::-1]
    if num_list == reverse_list:
        return True
    else:
        return False


nums = [1, 2, 3, 4, 5]
new_nums = []
answer = []

for i_nums in range(0, len(nums)):
    if is_palindrome(nums[i_nums:len(nums)]):
        answer = nums[:i_nums]
        answer.reverse()
        break

print(f'the original list {nums}')
print(f'Nums for palindrome {len(answer)}')
print(f'New list {answer}')
