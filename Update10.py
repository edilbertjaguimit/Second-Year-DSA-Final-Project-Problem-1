def menu():
  print("1. Insert Item at the Beginning")
  print("2. Insert Item at the End")
  print("3. Insert Item at Any Position")
  print("4. Delete Item at the Beginning")
  print("5. Delete Item at the End")
  print("6. Delete Item at Any Position")
  print("7. Delete Item by Item Code")
  print("8. Delete Item by Item Category")
  print("9. Sort Item by Item Code (Ascending)")
  print("10. Sort Item by Price (Descending)")
  print("11. Search Item by Code")
  print("12. Search Item by Type")
  print("13. Search Item by Quantity (from and to quantity)")
  print("14. Update Item by Code")
  print("15. Display")
  print("16. Exit")
  print()

menu()
SIZE = 5
ITEM_CODE = [None] * SIZE
ITEM_DESCRIPTION = [None] * SIZE
ITEM_PRICE = [None] * SIZE
ITEM_QUANTITY = [None] * SIZE
ITEM_CATEGORY = [None] * SIZE
index = 0
while index < SIZE:

  choose = input("Enter your Choice : ")
  print()
  
  # Insert Item at the Beginning
  if choose == '1':
    
    flag = False
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
      flag = True
      index += 1

    if flag:
      print("New Item Added.")
      
  # Insert Item at the End
  elif choose == '2':
    
    flag = False
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
      flag = True
      index += 1

    if flag:
      print("New Item Added.")

  # Insert Item at Any Position
  elif choose == '3':

    flag = False
    position = int(input("Position: "))
    if position >= SIZE or position < 0:
      print("Index out of range. Please enter a valid position.")
    else:
      i = index
      while i > position:
        ITEM_CODE[i] = ITEM_CODE[i-1]
        ITEM_DESCRIPTION[i] = ITEM_DESCRIPTION[i-1]
        ITEM_PRICE[i] = ITEM_PRICE[i-1]
        ITEM_QUANTITY[i] = ITEM_QUANTITY[i-1]
        ITEM_CATEGORY[i] = ITEM_CATEGORY[i-1]
        i -= 1

      if index == 0:
        position = 0
      if position < index+1:
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
          flag = True
          index += 1
      else:
        print("Index out of range. Please enter a valid position.")
    if flag:
      print("New Item Added.")

  # Delete Item at the Beginning
  elif choose == '4':
    if index == 0:
      print("List is Empty")
    else:
      found = False
      i = 0
      while i < SIZE:
        if i == 0:
          j = i
          while j < SIZE-1:
            ITEM_CODE[j] = ITEM_CODE[j+1]
            ITEM_DESCRIPTION[j] = ITEM_DESCRIPTION[j+1]
            ITEM_PRICE[j] = ITEM_PRICE[j+1]
            ITEM_QUANTITY[j] = ITEM_QUANTITY[j+1]
            ITEM_CATEGORY[j] = ITEM_CATEGORY[j+1]
            j += 1
          
          ITEM_CODE[index] = None
          ITEM_DESCRIPTION[index] = None
          ITEM_PRICE[index] = None
          ITEM_QUANTITY[index] = None
          ITEM_CATEGORY[index] = None
          found = True
          index -= 1
        i += 1
      if found:
        print("Item Deleted")
      else:
        print("Item Not Found")

  # Delete Item at the End
  elif choose == '5':
    if index == 0:
      print("List is Empty")
    else:
      found = False
      i = 0
      while i < SIZE:
        if i == SIZE-1:
          j = i
          while j < SIZE-1:
            ITEM_CODE[j] = ITEM_CODE[j+1]
            ITEM_DESCRIPTION[j] = ITEM_DESCRIPTION[j+1]
            ITEM_PRICE[j] = ITEM_PRICE[j+1]
            ITEM_QUANTITY[j] = ITEM_QUANTITY[j+1]
            ITEM_CATEGORY[j] = ITEM_CATEGORY[j+1]
            j += 1
          
          ITEM_CODE[index] = None
          ITEM_DESCRIPTION[index] = None
          ITEM_PRICE[index] = None
          ITEM_QUANTITY[index] = None
          ITEM_CATEGORY[index] = None
          found = True
          index -= 1
        i += 1
      if found:
        print("Item Deleted")
      else:
        print("Item Not Found")

  # Delete Item at Any Position
  elif choose == '6':
    if index == 0:
      print("List is Empty")
    else:
      deletePosition = int(input("Delete Postion : "))
      found = False
      i = 0
      while i < SIZE:
        if deletePosition == i:
          j = i
          while j < SIZE-1:
            ITEM_CODE[j] = ITEM_CODE[j+1]
            ITEM_DESCRIPTION[j] = ITEM_DESCRIPTION[j+1]
            ITEM_PRICE[j] = ITEM_PRICE[j+1]
            ITEM_QUANTITY[j] = ITEM_QUANTITY[j+1]
            ITEM_CATEGORY[j] = ITEM_CATEGORY[j+1]
            j += 1
          if i < index:
            ITEM_CODE[index] = None
            ITEM_DESCRIPTION[index] = None
            ITEM_PRICE[index] = None
            ITEM_QUANTITY[index] = None
            ITEM_CATEGORY[index] = None
            found = True
            index -= 1
        i += 1
      if found:
        print("Item Deleted")
      else:
        print("Item Not Found")

  # Delete Item by Code
  elif choose == '7':
    if index == 0:
      print("List is Empty")
    else:
      deleteItemCode = input("Delete Item by Code : ")
      found = False
      i = 0
      while i < SIZE:
        if deleteItemCode == ITEM_CODE[i]:
          j = i
          while j < SIZE-1:
            ITEM_CODE[j] = ITEM_CODE[j+1]
            ITEM_DESCRIPTION[j] = ITEM_DESCRIPTION[j+1]
            ITEM_PRICE[j] = ITEM_PRICE[j+1]
            ITEM_QUANTITY[j] = ITEM_QUANTITY[j+1]
            ITEM_CATEGORY[j] = ITEM_CATEGORY[j+1]
            j += 1
          
          ITEM_CODE[index] = None
          ITEM_DESCRIPTION[index] = None
          ITEM_PRICE[index] = None
          ITEM_QUANTITY[index] = None
          ITEM_CATEGORY[index] = None
          found = True
          index -= 1
        i += 1
      if found:
        print("Item Deleted")
      else:
        print("Item Not Found")

  # Delete Item by Category
  elif choose == '8':
    if index == 0:
      print("List is Empty")
    else:
      deleteItemCategory = input("Delete Item by Category : ").upper()
      found = False
      i = 0
      while i < SIZE:
        if deleteItemCategory == ITEM_CATEGORY[i]:
          j = i
          while j < SIZE-1:
            ITEM_CODE[j] = ITEM_CODE[j+1]
            ITEM_DESCRIPTION[j] = ITEM_DESCRIPTION[j+1]
            ITEM_PRICE[j] = ITEM_PRICE[j+1]
            ITEM_QUANTITY[j] = ITEM_QUANTITY[j+1]
            ITEM_CATEGORY[j] = ITEM_CATEGORY[j+1]
            j += 1
          
          ITEM_CODE[index] = None
          ITEM_DESCRIPTION[index] = None
          ITEM_PRICE[index] = None
          ITEM_QUANTITY[index] = None
          ITEM_CATEGORY[index] = None
          found = True
          index -= 1
        i += 1
      if found:
        print("Item Deleted")
      else:
        print("Item Not Found")
  
  # Sort Item by Code (Ascending)
  elif choose == '9':
    sorted = False
    while True:
      flag = False
      j = 0
      while j < index-1:
        if ITEM_CODE[j] > ITEM_CODE[j+1]:
          # Swap for Item Code
          tempItemCode = ITEM_CODE[j]
          ITEM_CODE[j] = ITEM_CODE[j+1]
          ITEM_CODE[j+1] = tempItemCode
  
          # Swap for Item Description
          tempItemDescription = ITEM_DESCRIPTION[j]
          ITEM_DESCRIPTION[j] = ITEM_DESCRIPTION[j+1]
          ITEM_DESCRIPTION[j+1] = tempItemDescription
  
          # Swap for Item Price
          tempItemPrice = ITEM_PRICE[j]
          ITEM_PRICE[j] = ITEM_PRICE[j+1]
          ITEM_PRICE[j+1] = tempItemPrice
  
          # Swap for Item Quantity
          tempItemQuantity = ITEM_QUANTITY[j]
          ITEM_QUANTITY[j] = ITEM_QUANTITY[j+1]
          ITEM_QUANTITY[j+1] = tempItemQuantity
  
          # Swap for Item Category
          tempItemCategory = ITEM_CATEGORY[j]
          ITEM_CATEGORY[j] = ITEM_CATEGORY[j+1]
          ITEM_CATEGORY[j+1] = tempItemCategory
          flag = True
          sorted = True
        j += 1
      if not flag:
        break
    if sorted:
      print("Item Code Sorted (Ascending)")
    else:
      print("Item Code is Already in Ascending Order.")

  # Sort Item by Price (Descending)
  elif choose == '10':
    sorted = False
    while True:
      flag = False
      j = 0
      while j < index-1:
        if ITEM_PRICE[j] < ITEM_PRICE[j+1]:
          # Swap for Item Code
          tempItemCode = ITEM_CODE[j]
          ITEM_CODE[j] = ITEM_CODE[j+1]
          ITEM_CODE[j+1] = tempItemCode

          # Swap for Item Description
          tempItemDescription = ITEM_DESCRIPTION[j]
          ITEM_DESCRIPTION[j] = ITEM_DESCRIPTION[j+1]
          ITEM_DESCRIPTION[j+1] = tempItemDescription

          # Swap for Item Price
          tempItemPrice = ITEM_PRICE[j]
          ITEM_PRICE[j] = ITEM_PRICE[j+1]
          ITEM_PRICE[j+1] = tempItemPrice

          # Swap for Item Quantity
          tempItemQuantity = ITEM_QUANTITY[j]
          ITEM_QUANTITY[j] = ITEM_QUANTITY[j+1]
          ITEM_QUANTITY[j+1] = tempItemQuantity

          # Swap for Item Category
          tempItemCategory = ITEM_CATEGORY[j]
          ITEM_CATEGORY[j] = ITEM_CATEGORY[j+1]
          ITEM_CATEGORY[j+1] = tempItemCategory
          flag = True
          sorted = True
        j += 1
      if not flag:
        break
    if sorted:
      print("Item Price Sorted (Descending)")
    else:
      print("Item Price is Already in Descending Order.")

  # Search Item by Code
  elif choose == '11':
    
    if index == 0:
      print("List is Empty")
    else:
      searchItemCode = input("Search Item by Code : ")
      found = True
      ctr = 0
      while ctr < index:
        if searchItemCode == ITEM_CODE[ctr]:
          print(ITEM_CODE[ctr], "\t", ITEM_DESCRIPTION[ctr], "\t\t", ITEM_PRICE[ctr], "\t\t", ITEM_QUANTITY[ctr])
          found = False
          break
        ctr += 1
      if found:
        print("Item Not Found.")

  # Search Item by Category
  elif choose == '12':
    if index == 0:
      print("List is Empty")
    else:
      searchItemType = input("Search Item by Category : ").upper()
      found = True
      ctr = 0
      while ctr < index:
        if searchItemType == ITEM_CATEGORY[ctr]:
          print(ITEM_CODE[ctr], "\t", ITEM_DESCRIPTION[ctr], "\t\t", ITEM_PRICE[ctr], "\t\t", ITEM_QUANTITY[ctr])
          found = False
          break
        ctr += 1
      if found:
        print("Item Not Found.")

  # Search Item by Quantity (from and to quantity)
  elif choose == '13':
    if index == 0:
      print("List is Empty")
    else:
      inputFrom = int(input("Search Item By Quantity (from) : "))
      inputQuantity = int(input("Search Item By Quantity (to quantity) : "))
      ctr = 0
      notFound = True
      while ctr < index:
        if inputFrom <= ITEM_QUANTITY[ctr] <= inputQuantity:
          print(ITEM_CODE[ctr], "\t", ITEM_DESCRIPTION[ctr], "\t\t", ITEM_PRICE[ctr], "\t\t", ITEM_QUANTITY[ctr])
          notFound = False
          break
        ctr += 1
      if notFound:
        print("Item Not Found.")
          
        
  # Update Item by Code
  elif choose == '14':
    if index == 0:
      print("List is Empty")
    else:
      itemCode = input("Enter Item Code to Update : ")
      found = False
      ctr = 0
      while ctr < index:
        if itemCode == ITEM_CODE[ctr]:
          ITEM_DESCRIPTION[ctr] = input("Enter New Description : ")
          ITEM_PRICE[ctr] = float(input("Enter New Price : "))
          ITEM_QUANTITY[ctr] = int(input("Enter New Quantity : "))
          ITEM_CATEGORY[ctr] = input("Enter New Category : ").upper()
          found = True
          break
        ctr += 1
      if found:
        print("Item Updated.")
      else:
        print("Item Code Not Found.")

  # Display All
  elif choose == '15':
    if index == 0:
      print("List is Empty")
    else:
      ctr = 0
      overAllTotal = 0
      print("Item Code | Item Description | Item Price | Item Quantity")
      while ctr < index:
        print("  ", ITEM_CODE[ctr], "\t\t\t ", ITEM_DESCRIPTION[ctr], "\t\t\t  ", ITEM_PRICE[ctr], "\t\t", ITEM_QUANTITY[ctr])
        overAllTotal = float(overAllTotal) + float(ITEM_PRICE[ctr])
        ctr += 1
      print("Total Line Items: ", index)
      print("Total Over All Items: ", overAllTotal)

  # Exit Section
  elif choose == '16':
    print("Program Terminated.")
    break

  else:
    print("Invalid Input.")
  print()
  
if index == SIZE:
  print("Item Storage is Full.")