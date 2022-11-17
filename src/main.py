"""
Module Docstring
"""
import matplotlib.pyplot as plt
import koch_snowflake as koch

def main():
    x,y = koch.koch_snowflake(5)
    plt.figure(figsize=(8,8))
    plt.axis('equal')
    plt.fill(x,y,'g')
    
    fname='../artifacts/koch-snowflake.png'
    format='png'
    plt.savefig(fname=fname,format=format)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()