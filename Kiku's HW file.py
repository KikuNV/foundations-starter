"""Important your modules here:"""

#import sympy in the line below:
import sympy as sp
import numpy as np

#from sympy.vector import coords3d in the line below
from sympy.vector import CoordSys3D
N = CoordSys3D('N')

from sympy import *
x, y, z = symbols('x y z')


###########################################################################################
def theProblem():
#     x=sp.pi/2
#     #insert y in the line below
     vector_y = N.i + sp.sin(x)*N.j
#     
#     f = (sp.E)*N.i
#     print(f)
#     #what does this function need to return? write it below
#     return y
def main():
     print(theProblem())
#     

if __name__ == "__main__":
    main()