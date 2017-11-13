def sum_from_list(range_num):
  return sum([x for x in range(1,range_num) if x % 3 == 0 or x % 5 == 0])