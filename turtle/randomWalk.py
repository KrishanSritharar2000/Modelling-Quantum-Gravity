import Grid#imports the modules
import Lines

file_number = 1
Grid.grid(21)#calls the grid moudle to make a grid of size 21x21
for i in range(100):#repeats the drawing of the paths 100 times
    Lines.make_random_walk(30, 10, file_number)#calls the function with the required inputs
    file_number += 1
#30 because that is the size of one movement on the grid
#10 becuase there are 10 random walks
#file number is the title to each Results text file, so Results1.txt, Results2.txt. etc.
