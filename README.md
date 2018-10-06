# Modelling Quantum Gravity

A Gold CREST Award Project on "Developing Computational Methods of Modelling Quantum Gravity". Created a Monte Carlo simulation using Python and Processing (a graphical library) to model light travelling through deep space. A 7-month group project run from December 2017 to June 2018, with a presentation at the Blackett Laboratory, Imperial College London in September 2018. Throughout this project, we had the guidance of 2 mentors from Imperial College London.

Square, isometric and randomly generated grids were used to represent the deep space the light is travelling through. Experimented with different probabilities of the light moving in each direction. Generated, plotted and analysed the results to evaluate the models. Added gravitational models of planets to represent masses and experimented with how the direction of light is affected when travelling past them. As expected, the light bent towards the planet, with a stronger attraction depending on how close it gets to the planet.

To conclude, the project was a success. We built a working model of discrete space-time that is scalable and optimized. Through iterative development and transitioning to using Processing, the execution time of a long simulation at one point in the project was reduced from 11 minutes to 16 seconds. We had different types of grids, masses with denser gravitational fields, varying number of steps for light and different probabilities of it moving in each direction to reflect upon the true randomness. The results we collected at the end supported our hypothesis, with the average and moving average lines playing a key part in expressing this graphically. 

---

# How to run

To run the simulation yourself, use the latest version of the simulation in [Simulation.pyde](../main/Simulation.pyde). 
Simply clone the repository and open the file in Processing, which you can download [here](https://processing.org/download/)

Next, set the required parameters:
```
* column:           Number of columns
* row:              Number of rows
* space:            Pixels between columns/rows
* mode:             Either "square", "triangle" or "random"
* num_of_steps:     Number of steps to perform in each walk
* num_of_walks:     Number of walks to perform 
* begin:            Start position either: 1 -> Center, 2 -> Left, 3 -> Right
* planet:           True/False on whether to include planets
* planet_position:  Position of planet on grid (default 1)
* name:             Name of image screenshot taken of final simulation state
* Pdown:            Probability of going South      (square)
* Pup:              Probability of going North      (square)
* Pright:           Probability of going East       (square/triangle)
* Pleft:            Probability of going West       (square/triangle)
* Prightdown:       Probability of going South-East (triangle)
* Prightup:         Probability of going North-East (triangle)
* Pleftdown:        Probability of going South-West (triangle)
* Pleftup:          Probability of going North-West (triangle)
* startsearch:      Position to start average line
* searchX:          Steps to use in computing average line
```

Finally, simply run the code in Processing and you will be presented with a simulation. 

---

# Results from Simulation

Here are some videos showing the results from the simulation, each with a different set of parameters for investigating different objectives. 

## Square Grid, start at Center with Equal probability of all directions

<img src="https://user-images.githubusercontent.com/57354504/125507978-a979945e-5c6a-4cec-a47b-b4cba9e65830.gif" alt="Animation Sqaure Equal" height="270"/> <img src="https://user-images.githubusercontent.com/57354504/125507385-1a48a3f2-bff3-4fcd-ba78-f38e1f1e39ed.png" alt="standard deviation" height="270"/>

## Square Grid, start at Right With biased Right probability 

<img src="https://user-images.githubusercontent.com/57354504/125511614-511f5843-d278-4ddf-8c4b-901eda726c91.gif" alt="Animation Sqaure Right" height="270"/> <img src="https://user-images.githubusercontent.com/57354504/125511932-ec5ab649-0418-49d5-ad1b-91176ab6afa4.png" alt="mean distance" height="270"/>

## Isometric Grid, start at Center with Equal probability of all directions

<img src="https://user-images.githubusercontent.com/57354504/125526494-9098da7c-bd95-4193-a3ce-01300e1362bb.gif" alt="Animation Sqaure Right" height="260"/> <img src="https://user-images.githubusercontent.com/57354504/125525800-c9989102-71ac-48fc-b30d-5690c44e4d57.png" alt="log standard deviation" height="260"/>

## Random Grid

<img src="https://user-images.githubusercontent.com/57354504/125527276-3517f514-4828-41f4-b8cd-ffa2cba8b5e8.png" alt="random" height="270"/>

## Square Grid with Planet

<img src="https://user-images.githubusercontent.com/57354504/125527503-71c1b47f-ac93-435e-9489-b99112d4ae1b.gif" alt="Planet" height="270"/>

---

# Documentation

The project was presented to other participants and mentors at the Blackett Laboratory, Imperial College London in October 2018. The [presentation](../main/Developing%20Computational%20Methods%20of%20Modelling%20Quantum%20Gravity.pptx) used for this and the [poster](../main/Poster%20-%20Developing%20Computational%20Methods%20of%20Modelling%20Quantum%20Gravity.pdf) showing the outcome of the results can be found in the repository.  