def arithmetic_arranger(problems, solution=False):
  
  #Check if num of problems is not more than 5
  if len(problems) > 5:
    return "Error: Too many problems."
  #Creaty empty lists for nums, operators and dashes
  num1 = []
  num2 = []
  sign = []
  dashes = []
  #Loop through problems
  for problem in problems:
    #Split problem so you can sort items into their lists
      item = problem.split()
      #Find the maximal number of digits and check if more than 4
      max_len = len(max(item, key=len))
      if max_len > 4:
        return "Error: Numbers cannot be more than four digits."
      #Create the dash line based on the max number of digits
      dash = "-"*(max_len+2)
      #Sort items into lists
      dashes.append(dash)
      num1.append(item[0])
      num2.append(item[2])
      sign.append(item[1])

  #Create empty string for each line of text  
  a=""
  b=""
  c=""
  d=""
  #Loop through the lists and format them using fstring
  for i in range(len(num1)):    
    #Right allign items based on the length of the dash line for each problem
    a += f"{num1[i]:>{len(dashes[i])}}    "
    b += f"{sign[i]}{num2[i]:>{len(dashes[i])-1}}    "
    c += f"{dashes[i]}    "

    #Check if items are digits    
    try:
      #Check which math operations to perform or return error if neither
      if sign[i] == "+":
        result = int(num1[i]) + int(num2[i])
      elif sign[i] == "-":
        result = int(num1[i]) - int(num2[i])
      else: return "Error: Operator must be '+' or '-'."
    except ValueError:
      return "Error: Numbers must only contain digits."
    
    #If optional arguement is True display solution  
    if solution:
      d += f"{result:>{len(dashes[i])}}    "
           
  #Solution formatting depending on the state of optional argument
  if solution:
    arranged_problems = f"{a.rstrip()}\n{b.rstrip()}\n{c.rstrip()}\n{d.rstrip()}" 
  else: arranged_problems = f"{a.rstrip()}\n{b.rstrip()}\n{c.rstrip()}"
    
  return arranged_problems
