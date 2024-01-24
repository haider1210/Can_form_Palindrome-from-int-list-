def can_form_palindrome(nums):
    counter = [0] * 10  # Since the numbers are from 1 to 9
    odd_count = 0

    for num in nums:
        counter[num] += 1

    for count in counter:
        if count % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return False

    return True
