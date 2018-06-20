# def find_nearest_point(find_x,find_y,col,row,coord):
#     find_coord = (find_x,find_y)
#     dist_x,dist_y,diagonal_dist = [],[],[]
#     for i in range(col*row):
#         dist_x.append(abs(coord[i][0] - find_coord[0]))
#         dist_y.append(abs(coord[i][1] - find_coord[1]))
#         diagonal_dist.append(round(sqrt(dist_x[i]**2 + dist_y[i]**2),2))
#     min_dist_value = min(diagonal_dist)
#     min_dist_index = diagonal_dist.index(min_dist_value)
#     nearest_coord_x,nearest_coord_y = coord[min_dist_index][0],coord[min_dist_index][1]
#     nearest_coord = (nearest_coord_x,nearest_coord_y,min_dist_index)
#     return nearest_coord

# def remove_from_coord(index,coord,col,row):
#     x,y = coord[index][0],coord[index][1]
#     for i in range(col*row):
#         if coord[i][0] == x and coord[i][1] == y:
#             coord[i].pop()
#             coord[i].pop()
#     coord = filter(None,coord)            
#     return coord

    
# def find_points(x,y,index,coord,col,row):
#     print("x",x)
#     print("y",y)
#     print("Original coord",coord)

#     print("Updated coord",coord)
#     leftup,rightup,leftdown,rightdown = False,False,False,False
#     leftup_count,rightup_count,leftdown_count,rightdown_count = 0,0,0,0
#     leftup_array,rightup_array,leftdown_array,rightdown_array = [],[],[],[]
#     max_count = int(round(sqrt(row*col)/2,0))
#     dist_x,dist_y,diagonal_dist,numbers = [],[],[],[]
#     # points_removed = 1
#     for i in range(col*row-1):
#         dist_x.append(abs(coord[i][0] - x))
#         dist_y.append(abs(coord[i][1] - y))
#         diagonal_dist.append(round(sqrt(dist_x[i]**2 + dist_y[i]**2),2))
#     max_value = max(diagonal_dist)
#     print("A",diagonal_dist)
#     print("Maxcount",max_count)
#     loops = 0
#     while (leftup == False or rightup == False or leftdown == False or rightdown == False) and loops < (col*row*2):
#         temp_min = min(diagonal_dist)
#         print("tempmin",temp_min)
#         temp_min_index = diagonal_dist.index(temp_min)
#         print("tempminindex", temp_min_index)
#         if leftup_count < max_count:
#             if coord[temp_min_index][0] < x and coord[temp_min_index][1] < y:#to the left and up
#                 leftup = True
#                 leftup_count +=1
#                 print("leftup_count",leftup_count)
#                 leftup_array.append((coord[temp_min_index][0],coord[temp_min_index][1]))
#                 numbers.append(0)
#                 diagonal_dist.pop(temp_min_index)
#                 diagonal_dist.insert(temp_min_index,(max_value*1000))
#         if rightup_count < max_count:
#             if coord[temp_min_index][0] > x and coord[temp_min_index][1] < y:#to the left and up
#                 rightup = True
#                 rightup_count +=1
#                 print("rightup_count",rightup_count)
#                 rightup_array.append((coord[temp_min_index][0],coord[temp_min_index][1]))                
#                 numbers.append(1)
#                 diagonal_dist.pop(temp_min_index)   
#                 diagonal_dist.insert(temp_min_index,(max_value*1000))
#         if leftdown_count < max_count:
#             if coord[temp_min_index][0] < x and coord[temp_min_index][1] > y:#to the left and up
#                 leftdown = True
#                 leftdown_count +=1
#                 print("leftdown_count",leftdown_count)
#                 leftdown_array.append((coord[temp_min_index][0],coord[temp_min_index][1]))                
#                 numbers.append(2)
#                 diagonal_dist.pop(temp_min_index)
#                 diagonal_dist.insert(temp_min_index,(max_value*1000))
#         if rightdown_count < max_count:
#             if coord[temp_min_index][0] > x and coord[temp_min_index][1] > y:#to the left and up
#                 rightdown = True
#                 rightdown_count +=1
#                 print("rightdown_count",rightdown_count)
#                 rightdown_array.append((coord[temp_min_index][0],coord[temp_min_index][1]))                
#                 numbers.append(3)
#                 diagonal_dist.pop(temp_min_index)
#                 diagonal_dist.insert(temp_min_index,(max_value*1000))
#         loops += 1
#         print()
#         print("New",diagonal_dist)
#         print("Numbers",numbers, "loop",loops)
#         print("leftup_array ",leftup_array)
#         print("rightup_array ",rightup_array)
#         print("leftdown_array ",leftdown_array)
#         print("rightdown_array ",rightdown_array)
#     if len(leftup_array) == 0:
#         leftup_array = [()]
#     if len(rightup_array) == 0:
#         rightup_array = [()]
#     if len(leftdown_array) == 0:
#         leftdown_array = [()]
#     if len(rightdown_array) == 0:
#         rightdown_array = [()]
#     # all_arrays = (leftup_array + rightup_array + leftdown_array + rightdown_array)
#     print("all Arrays", all_arrays)

#     # return all_arrays
#     # global numbers,leftup_array,rightup_array,leftdown_array,rightdown_array    

    
    
# def drawLinesRandom(walk_num, step_num, col, row, len_th, begin, coord, Prightdown, Prightup, Pleftdown, Pleftup):
#     if begin == 1:#start at centre 
#         x = (displayWidth*0.5)

#     elif begin == 2:#start at left 
#         x = (displayWidth*0.5) - ((col*0.5)*len_th)
    
#     elif begin == 3: #start at right
#         x = (displayWidth*0.5) + ((col*0.5)*len_th)
        
#     xpos = x
#     y = (displayHeight*0.5)
#     ypos = y        
    
#     nearest_coord = find_nearest_point(xpos,y,col,row,coord)
#     stroke(255,0,0,100)
#     line(xpos,y,nearest_coord[0],nearest_coord[1])
#     x,y,index = nearest_coord[0],nearest_coord[1],nearest_coord[2]
#     # print(x,y,index)   
#     coord = remove_from_coord(index,coord,col,row)

#     xaverage_array = []
#     yaverage_array = []    
#     avg = []
        
#     for num in range(walk_num):
#         print("NEW WHOLE LOOP")
#         # result = find_points(x,y,index,coord,col,row)
#         x,y = nearest_coord[0],nearest_coord[1]
#         print("x",x)
#         print("y",y)
#         print("Original coord",coord)
    
#         print("Updated coord",coord)
#         leftup,rightup,leftdown,rightdown = False,False,False,False
#         leftup_count,rightup_count,leftdown_count,rightdown_count = 0,0,0,0
#         leftup_array,rightup_array,leftdown_array,rightdown_array = [],[],[],[]
#         max_count = int(round(sqrt(row*col)/2,0))
#         # max_count = 1
#         dist_x,dist_y,diagonal_dist,numbers = [],[],[],[]
#         # points_removed = 1
#         for i in range((col*row)-1):
#             dist_x.append(abs(coord[i][0] - x))
#             dist_y.append(abs(coord[i][1] - y))
#             diagonal_dist.append(round(sqrt(dist_x[i]**2 + dist_y[i]**2),2))
#         max_value = max(diagonal_dist)
#         print("A",diagonal_dist)
#         print("Maxcount",max_count)
#         loops = 0        
#         multiple_numbers = []
                                
#         for j in range(step_num):
            
#             prevx,prevy,prev_temp_min = x,y,0
            
            
#             while (leftup == False or rightup == False or leftdown == False or rightdown == False) and loops < (int((col*row))):
#                 print("new while loop")
#                 temp_min = min(diagonal_dist)
#                 if prev_temp_min == temp_min:
#                     temp_min_index = diagonal_dist.index(temp_min)
#                     diagonal_dist.pop(temp_min_index)
#                     diagonal_dist.insert(temp_min_index,(max_value*1000))
#                     temp_min = min(diagonal_dist)
#                 print("tempmin",temp_min)
#                 temp_min_index = diagonal_dist.index(temp_min)
#                 print("tempminindex", temp_min_index)
#                 print("tempminx",coord[temp_min_index][0],"tempminy",coord[temp_min_index][1])
#                 if coord[temp_min_index][0] < x and coord[temp_min_index][1] < y:#to the left and up
#                     if leftup_count < max_count:
#                         leftup = True
#                         leftup_count +=1
#                         print("leftup_count",leftup_count)
#                         leftup_array.append((coord[temp_min_index][0],coord[temp_min_index][1]))
#                         numbers.append(0)
#                         diagonal_dist.pop(temp_min_index)
#                         diagonal_dist.insert(temp_min_index,(max_value*1000))
#                 elif coord[temp_min_index][0] > x and coord[temp_min_index][1] < y:#to the left and up
#                     if rightup_count < max_count:
#                         rightup = True
#                         rightup_count +=1
#                         print("rightup_count",rightup_count)
#                         rightup_array.append((coord[temp_min_index][0],coord[temp_min_index][1]))                
#                         numbers.append(1)
#                         diagonal_dist.pop(temp_min_index)   
#                         diagonal_dist.insert(temp_min_index,(max_value*1000))
#                 elif coord[temp_min_index][0] < x and coord[temp_min_index][1] > y:#to the left and up
#                     if leftdown_count < max_count:
#                         leftdown = True
#                         leftdown_count +=1
#                         print("leftdown_count",leftdown_count)
#                         leftdown_array.append((coord[temp_min_index][0],coord[temp_min_index][1]))                
#                         numbers.append(2)
#                         diagonal_dist.pop(temp_min_index)
#                         diagonal_dist.insert(temp_min_index,(max_value*1000))
#                 elif coord[temp_min_index][0] > x and coord[temp_min_index][1] > y:#to the left and up
#                     if rightdown_count < max_count:
#                         rightdown = True
#                         rightdown_count +=1
#                         print("rightdown_count",rightdown_count)
#                         rightdown_array.append((coord[temp_min_index][0],coord[temp_min_index][1]))                
#                         numbers.append(3)
#                         diagonal_dist.pop(temp_min_index)
#                         diagonal_dist.insert(temp_min_index,(max_value*1000))
#                 prev_temp_min = temp_min
#                 loops += 1
#                 print()
#                 print("New",diagonal_dist)
#                 print("Numbers",numbers, "loop",loops)
#                 print("leftup_array ",leftup_array)
#                 print("rightup_array ",rightup_array)
#                 print("leftdown_array ",leftdown_array)
#                 print("rightdown_array ",rightdown_array)
#             print("While finish")
#             if len(leftup_array) == 0:
#                 leftup_array = [()]
#             if len(rightup_array) == 0:
#                 rightup_array = [()]
#             if len(leftdown_array) == 0:
#                 leftdown_array = [()]
#             if len(rightdown_array) == 0:
#                 rightdown_array = [()]
#             # all_arrays = (leftup_array + rightup_array + leftdown_array + rightdown_array)
#             # print("all Arrays", all_arrays)
        
#             # return all_arrays
#             # global numbers,leftup_array,rightup_array,leftdown_array,rightdown_array    
            
#             # leftup_array,rightup_array,leftdown_array,rightdown_array =  result[0],result[1],result[2],result[3]
#             print("leftup",leftup_array)
#             print("rightup",rightup_array)
#             print("leftdown",leftdown_array)
#             print("rightdown",rightdown_array)
            
#             for i in range(4):
#                 temp_count = numbers.count(i)
#                 print(i,"tempcount: ",temp_count)
#                 if temp_count > 1:
#                     for j in range(temp_count-1):
#                         multiple_numbers.append(i)
#                         print("multi numbers1",multiple_numbers)
#                         numbers.remove(i)
#                 print("NumBers", numbers)
#                 print("multi numbers2",multiple_numbers)
#             weights = [] 
            
#             for l in range(len(numbers)):
#                 if numbers[l] == 0:
#                     for k in range(int(Pleftup*100)):
#                         weights.append(0)
#                 if numbers[l] == 1:
#                     for k in range(int(Prightup*100)):
#                         weights.append(1)
#                 if numbers[l] == 2:
#                     for k in range(int(Pleftdown*100)):
#                         weights.append(2)
#                 if numbers[l] == 3:
#                     for k in range(int(Prightdown*100)):
#                         weights.append(3)
#             print("Wegihts: ",weights)    
            
#             number = random.choice(weights)#generates a random number
#             stroke(0,0,0,105)
#             strokeWeight(3)
#             print("Random number :", number)
#             print("The length of numbers",  len(numbers))
#             print("leftup",leftup_array)
#             print("rightup",rightup_array)
#             print("leftdown",leftdown_array)
#             print("rightdown",rightdown_array)
#             print("prevx",prevx)
#             print("prevy", prevy)
#             stroke(0,0,0,100)
#             if len(numbers) == 0:
#                 print("Exectued len numbers ==0")
#                 temp_amount_random_number = int(random.randint(0, col*row-1))
#                 line(prevx,prevy,coord[temp_amount_random_number][0],coord[temp_amount_random_number][1])
#             elif number == 0:#leftup
#                 print("Exectued numbers ==0")

#                 if multiple_numbers.count(0) == 0:
#                     print("Exectued numbers ==0 and multiple number count = 0")

#                     # print("AAAAAA",prevx,prevy,leftup_array[0],leftup_array[1])
#                     stroke(0,0,0,100)
#                     line(prevx,prevy,leftup_array[0][0],leftup_array[0][1])
#                     x,y = leftup_array[0][0],leftup_array[0][1]
#                 elif multiple_numbers.count(0) >= 1:
#                     temp_amount = multiple_numbers.count(0)
#                     temp_amount_random_number = int(random.randint(0, temp_amount))
#                     stroke(0,0,0,100)
#                     line(prevx,prevy,leftup_array[temp_amount_random_number][0],leftup_array[temp_amount_random_number][1])
#                     x,y = leftup_array[temp_amount_random_number][0],leftup_array[temp_amount_random_number][1]            
#             elif number == 1:#rightup
#                 print("Exectued numbers ==1")

#                 if multiple_numbers.count(1) == 0:
#                     print("Exectued numbers ==1 and multiple number count = 0")

#                     # print("BBBBBB",prevx,prevy,rightup_array[0],rightup_array[1])
#                     stroke(0,0,0,100)
#                     line(prevx,prevy,rightup_array[0][0],rightup_array[0][1])
#                     x,y = rightup_array[0][0],rightup_array[0][1]
#                 elif multiple_numbers.count(1) >= 1:
#                     temp_amount = multiple_numbers.count(1)
#                     temp_amount_random_number = int(random.randint(0, temp_amount))
#                     stroke(0,0,0,100)
#                     line(prevx,prevy,rightup_array[temp_amount_random_number][0],rightup_array[temp_amount_random_number][1])
#                     x,y = rightup_array[temp_amount_random_number][0],rightup_array[temp_amount_random_number][1] 
#             elif number == 2:#leftdown
#                 print("Exectued numbers ==2")

#                 if multiple_numbers.count(2) == 0:
#                     print("Exectued numbers ==2 and multiple number count = 0")

#                     # print("CCCCCC",prevx,prevy,leftdown_array[0],leftdown_array[1])
#                     stroke(0,0,0,100)
#                     line(prevx,prevy,leftdown_array[0][0],leftdown_array[0][1])
#                     x,y = leftdown_array[0][0],leftdown_array[0][1]
#                 elif multiple_numbers.count(2) >= 1:
#                     temp_amount = multiple_numbers.count(2)
#                     temp_amount_random_number = int(random.randint(0, temp_amount))
#                     stroke(0,0,0,100)
#                     line(prevx,prevy,leftdown_array[temp_amount_random_number][0],leftdown_array[temp_amount_random_number][1])
#                     x,y = leftdown_array[temp_amount_random_number][0],leftdown_array[temp_amount_random_number][1] 
#             elif number == 3:#rightdown
#                 print("Exectued numbers ==3")

#                 if multiple_numbers.count(3) == 0:
#                     print("Exectued numbers ==3 and multiple number count = 0")

#                     # print("DDDDDDDD", prevx,prevy,rightdown_array[0],rightdown_array[1])
#                     stroke(0,0,0,100)
#                     line(prevx,prevy,rightdown_array[0][0],rightdown_array[0][1])
#                     x,y = rightdown_array[0][0],rightdown_array[0][1]
#                 elif multiple_numbers.count(3) >= 1:
#                     temp_amount = multiple_numbers.count(3)
#                     temp_amount_random_number = int(random.randint(0, temp_amount))
#                     stroke(0,0,0,100)
#                     line(prevx,prevy,rightdown_array[temp_amount_random_number][0],rightdown_array[temp_amount_random_number][1])
#                     x,y = rightdown_array[temp_amount_random_number][0],rightdown_array[temp_amount_random_number][1] 
                     
#             avg.append([x,y])
#         fill(0,255,0)
#         textSize(14)
#         text(num+1,x,y)        
#         xaverage_array.append(x)
#         yaverage_array.append(y)

# #writes a number to link the line to the walk_num
#     averageline1(xaverage_array,yaverage_array,xpos,ypos)
#     averageline2(step_num,walk_num,avg,xpos,ypos)
