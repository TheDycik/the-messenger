from tests import nenada2

# nums = [1, 2, 6, 3, 23, 34, 12, 3, 2]
# print(max(nums))
# m = nums[0]
# for i in nums:
#   if i > m:
#     m = i

# print(m)

messages = [
    {'name': 'lox', 'time': 10, 'text': '12343'},
    {'name': 'lox', 'time': 20, 'text': '12452312'},
    {'name': 'lox', 'time': 30, 'text': '23413'},
    {'name': 'lox', 'time': 40, 'text': '4235'}
]

print(nenada2.max_for_dicts(messages, key='time'))

print(nenada2.filter_dicts(messages, key='time', min_value=30))
