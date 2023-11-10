SIZE = 2
ITEM_CODE = [None] * SIZE
ITEM_DESCRIPTION = [None] * SIZE
ITEM_PRICE = [None] * SIZE
ITEM_QUANTITY = [None] * SIZE
ITEM_CATEGORY = [None] * SIZE
index = 0
while index < SIZE:

  choose = input("Push [1]\nAppend [2]\nPosition [3] ")

  # Push Item
  if choose == '1':
  
    # Shift the elements of the list one position to the right, starting from the last element and working backwards, until the element at index 0 is reached. The element at index 0 will not be shifted, as it will be replaced by the new element.
    i = SIZE - 1
    count = 0
    while i > 0 and count < SIZE - 1:
      ITEM_CODE[i] = ITEM_CODE[i-1]
      i -= 1
      count += 1
    ITEM_CODE[0] = input("Enter Item Code : ")
    
    ctr = 0
    while ctr < index:
      if ITEM_CODE[ctr] == ITEM_CODE[index]:
        print("Item Code Already Exist.")
        break
      else:
        ctr += 1
        
    if ctr == index:
    # Shift the elements of the list one position to the right, starting from the last element and working backwards, until the element at index 0 is reached. The element at index 0 will not be shifted, as it will be replaced by the new element.
      i = SIZE - 1
      count = 0
      while i > 0 and count < SIZE - 1:
        ITEM_DESCRIPTION[i] = ITEM_DESCRIPTION[i-1]
        ITEM_PRICE[i] = ITEM_PRICE[i-1]
        ITEM_QUANTITY[i] = ITEM_QUANTITY[i-1]
        ITEM_CATEGORY[i] = ITEM_CATEGORY[i-1]
        i -= 1
        count += 1
      ITEM_DESCRIPTION[0] = input("Enter Item Description : ")
      ITEM_PRICE[0] = float(input("Enter Item Price : "))
      ITEM_QUANTITY[0] = int(input("Enter Item Quantity : "))
      ITEM_CATEGORY[0] = input("Enter Item Category : ").upper()
      index += 1

  # Append Item
  elif choose == '2':
    ITEM_CODE[index] = input("Enter Item Code : ")
    ctr = 0
    while ctr < index:
      if ITEM_CODE[ctr] == ITEM_CODE[index]:
        print("Item Code Already Exist.")
        break
      else:
        ctr += 1
    if ctr == index:
      ITEM_DESCRIPTION[index] = input("Enter Item Description : ")
      ITEM_PRICE[index] = float(input("Enter Item Price : "))
      ITEM_QUANTITY[index] = int(input("Enter Item Quantity : "))
      ITEM_CATEGORY[index] = input("Enter Item Category : ").upper()
      index += 1

  # Insert at Specified Position
  elif choose == '3':
    position = int(input("Position: "))
    if position >= SIZE or position < 0:
      print("Index out of range. Please enter a valid position.")
      index -= 1
    else:
      # num = int(input("Enter number: "))
      # Shifts all the elements of the list starting from pos one position to the right in order to make room for the new value. It does this by assigning the value of each element to the element that comes after it.
      i = SIZE-1
      while i > position:
        ITEM_CODE[i] = ITEM_CODE[i-1]
        ITEM_DESCRIPTION[i] = ITEM_DESCRIPTION[i-1]
        ITEM_PRICE[i] = ITEM_PRICE[i-1]
        ITEM_QUANTITY[i] = ITEM_QUANTITY[i-1]
        ITEM_CATEGORY[i] = ITEM_CATEGORY[i-1]
        i -= 1

      ITEM_CODE[position] = input("Enter Item Code : ")
      ctr = 0
      while ctr < index:
        if ITEM_CODE[ctr] == ITEM_CODE[index]:
          print("Item Code Already Exist.")
          break
        else:
          ctr += 1
      if ctr == index:
        ITEM_DESCRIPTION[position] = input("Enter Item Description : ")
        ITEM_PRICE[position] = float(input("Enter Item Price : "))
        ITEM_QUANTITY[position] = int(input("Enter Item Quantity : "))
        ITEM_CATEGORY[position] = input("Enter Item Category : ").upper()
        index += 1
  
  # elif choose == '4':
  # elif choose == '5':
  # elif choose == '6':
  # elif choose == '7':
  # elif choose == '8':
  # elif choose == '9':
  # while True:
    #   flag = False
    #   j = 0
    #   while j < SIZE - 1:
    #     if ITEM_CODE[j] > ITEM_CODE[j + 1]:
    #       temp = ITEM_CODE[j]
    #       ITEM_CODE[j] = ITEM_CODE[j + 1]
    #       ITEM_CODE[j + 1] = temp

    #       #swap for description
    #       tempdesc = ITEM_DESCRIPTION[j]
    #       ITEM_DESCRIPTION[j] = ITEM_DESCRIPTION[j + 1]
    #       ITEM_DESCRIPTION[j + 1] = tempdesc

    #       #swap for price
    #       tempprice = ITEM_PRICE[j]
    #       ITEM_PRICE[j] = ITEM_PRICE[j + 1]
    #       ITEM_PRICE[j + 1] = tempprice

    #       #swap for quantity
    #       tempqnty = ITEM_QUANTITY[j]
    #       ITEM_QUANTITY[j] = ITEM_QUANTITY[j + 1]
    #       ITEM_QUANTITY[j + 1] = tempqnty

    #       #swap for Category
    #       tempcat = ITEM_CATEGORY[j]
    #       ITEM_CATEGORY[j] = ITEM_CATEGORY[j + 1]
    #       ITEM_CATEGORY[j + 1] = tempcat
    #       flag = True
    #     j += 1
    #   if not flag:
    #     break

    # ctrl = 0
    # while ctrl < SIZE:
    #   print(ITEM_CODE[ctrl], ITEM_DESCRIPTION[ctrl], ITEM_PRICE[ctrl],
    #         ITEM_QUANTITY[ctrl], ITEM_CATEGORY[ctrl])
    #   ctrl += 1
  # elif choose == '10':
    #   while True:
    #   flag = False
    #   j = 0
    #   while j < SIZE - 1:
    #     if ITEM_CODE[j] < ITEM_CODE[j + 1]:
    #       temp = ITEM_CODE[j]
    #       ITEM_CODE[j] = ITEM_CODE[j + 1]
    #       ITEM_CODE[j + 1] = temp

    #       #swap for description
    #       tempdesc = ITEM_DESCRIPTION[j]
    #       ITEM_DESCRIPTION[j] = ITEM_DESCRIPTION[j + 1]
    #       ITEM_DESCRIPTION[j + 1] = tempdesc

    #       #swap for price
    #       tempprice = ITEM_PRICE[j]
    #       ITEM_PRICE[j] = ITEM_PRICE[j + 1]
    #       ITEM_PRICE[j + 1] = tempprice

    #       #swap for quantity
    #       tempqnty = ITEM_QUANTITY[j]
    #       ITEM_QUANTITY[j] = ITEM_QUANTITY[j + 1]
    #       ITEM_QUANTITY[j + 1] = tempqnty

    #       #swap for Category
    #       tempcat = ITEM_CATEGORY[j]
    #       ITEM_CATEGORY[j] = ITEM_CATEGORY[j + 1]
    #       ITEM_CATEGORY[j + 1] = tempcat
    #       flag = True
    #     j += 1
    #   if not flag:
    #     break

    # ctrl = 0
    # while ctrl < SIZE:
    #   print(ITEM_CODE[ctrl], ITEM_DESCRIPTION[ctrl], ITEM_PRICE[ctrl],
    #         ITEM_QUANTITY[ctrl], ITEM_CATEGORY[ctrl])
    #   ctrl += 1
  # elif choose == '11':
  # elif choose == '12':
  # elif choose == '13':
  # elif choose == '14':
  # elif choose == '15':

# Result
print()
ctr1 = 0
while ctr1 < SIZE:
  print(ITEM_CODE[ctr1], ITEM_DESCRIPTION[ctr1], ITEM_PRICE[ctr1], ITEM_QUANTITY[ctr1], ITEM_CATEGORY[ctr1])
  ctr1 += 1
