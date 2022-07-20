# Solving Sudoku Using Interger Linear Programming (ILP)

## Introduction

Some intro blah blah



![Example Sudoku board - Generating & Solving Sudoku Puzzles | by Daniel Sasse | Medium](README.assets/example-board.png)

## Interger Linear Program Formulation

To solve Sudoku puzzle as a linear program, there is no need to find a optimum maximum/minimum of some objective function.

Objective function:

$$
\min Z = 0\\
$$

Now we require the feasibility of each square being a an interger value in $[1,9]$ with the constraints being each cell value must be unique to that row, column and box (sub $3\times 3$ boards). For a $9\times 9$ board $M$ indexed by two integers $i,j\in [1,9]$ for every cell in $M$ and possible values $v\in [1,9]$ and we create decision variables $x$ which is denoted as $x_{ijv}$ that represents whether a value $v$ is chosen corresponding to its cell $i,j$ thus $x$ is either $1$ or $0$. 

Thus the constraints are **Subject to**:

$$
\begin{cases}
    & \sum^{9}_{v = 1} x_{ijv} = 1,& \text{for } i,j \in [1, 9], \text{one } v \text{ per cell} \\
    & \sum^{9}_{i = 1} x_{ijv} = 1,& \text{for } j,v \in [1, 9],\text{one } v \text{ per row} \\
    & \sum^{9}_{j = 1} x_{ijv} = 1,& \text{for } i,v \in [1, 9],\text{one } v \text{ per column} \\
    & \sum^{3p}_{j=3p-2} \sum^{3q}_{i=3q-2} x_{ijv} = 1,& \text{for } v \in [1, 9],p,q \in [1,3],\text{one }v \text{ per } 3\times 3 \text{ sub-board}\\
    & x_{ijv} = 1,& \text{for } x_{ijv} > 0 \in M_{ij} \text{ already assigned cells}\\
    & \forall x \in [0,1] & \text{decision variables}
\end{cases}
$$

## [Implementation of Sudoku ILP solver in Gurobi Python](solver.py)


## Empirical analysis of Sudoku solving for randomly generated $9\times 9$ boards

### [Generating random boards](generate_board.py)

Generate a $9\times 9$ board with some probability $p$ of having a number assigned which is a random value chosen uniformly in $[1,9]$, otherwise indicate as $0$ as it is not assigned.

