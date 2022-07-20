def arithmetic_arranger(problems, isAnswer):
  if len(problems) > 5:
    raise ValueError('Error: Too many problems.')

  operator = '+-'
    
  for problem in problems:
    list = problem.split(' ')

    if not list[1] in operator:
      raise ValueError('Error: Operator must be '+' or '-'.')
    
    if not list[0].isdigit() or not list[2].isdigit():
      raise ValueError('Error: Numbers must only contain digits.')
    
    if len(list[0]) > 4 or len(list[2]) > 4:
      raise ValueError('Error: Numbers cannot be more than four digits.')

    if len(list[0])
    
    print(list)
  
  
