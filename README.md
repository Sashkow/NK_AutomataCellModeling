NK_AutomataCellModeling
=======================

Life cell modeling using Kauffman`s NK Automata. The automata is used to model a living cell regulatory mechanics i.e. sequence of cell states. N stands for amount of genes a cell has. K represents amount of genes each gene behavior depends on. Gene is roughly a boolean variable which can be true or false (gene can be in to states: active or passive). States of all genes altogether at a particular discrete moment of time is a cell state.

The graphical interface includes:
- two sliders of N and K - parameters of the system
- go button - generates a random NK automata of specified parameters
- three image boxes:
  - graph representing behavior dependance links between genes
  - graph representing graph of all possible states the cell can reach
  - simplistic version of the second graph

Developed in Eclipse with PyDev and Qt

main file - mainGUI/main.py
