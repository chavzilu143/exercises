def sum_from_list():
  list_num=[x for x in range(1,1000) if x % 3 == 0 or x % 5 == 0]
  return sum(list_num)