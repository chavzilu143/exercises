def sum_fibonacci_with_even(limit):
  previous, current = 0, 1
  total_sum = 0
  while True:
      previous, current = current, previous + current
      print("current ", current, ", previous ", previous )
      if current >= limit:
          break
      if current % 2 == 0:
          total_sum += current
  
  return total_sum