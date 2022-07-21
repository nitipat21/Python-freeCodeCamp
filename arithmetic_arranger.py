def arithmetic_arranger(problems, isAnswer):
  if len(problems) > 5:
    raise ValueError('Error: Too many problems.')

  operator = '+-'
  line_1 = ""
  line_2 = ""
  line_3 = ""
  line_4 = ""
    
  for problem in problems:
    list = problem.split(' ')

    # check operator
    if not list[1] in operator:
      raise ValueError('Error: Operator must be '+' or '-'.')

    # check numbers are digit
    if not list[0].isdigit() or not list[2].isdigit():
      raise ValueError('Error: Numbers must only contain digits.')

    # check number length
    if len(list[0]) > 4 or len(list[2]) > 4:
      raise ValueError('Error: Numbers cannot be more than four digits.')

    longest_digit = 0
    answer = 0

    # save the longest length
    if len(list[0]) > len(list[2]):
      longest_digit = len(list[0])
    else:
      longest_digit = len(list[2])

    # calculate the answer
    if isAnswer:
        if list[1] == "+":
          answer = str(int(list[0]) + int(list[2]))
        else:
          answer = str(int(list[0]) - int(list[2]))

    tmp_1 = ""
    tmp_2 = list[1]
    tmp_3 = ""
    tmp_4 = ""

    
    for i in range(longest_digit + 2 - len(list[0])):
      tmp_1 += " "

    tmp_1 += list[0]

    
    for j in range(longest_digit + 2 - len(list[2]) - 1):
      tmp_2 += " "
      
    tmp_2 += list[2]

    
    for k in range(longest_digit + 2):
      tmp_3 += "-"
    
    if isAnswer:
      for i in range (longest_digit + 2 - len(answer)):
        tmp_4 += " "

      tmp_4 += answer
    
    line_1 += tmp_1 + "    "
    line_2 += tmp_2 + "    "
    line_3 += tmp_3 + "    "
    line_4 += tmp_4 + "    "

  print(line_1)
  print(line_2)
  print(line_3)
  print(line_4)
      
  
  
