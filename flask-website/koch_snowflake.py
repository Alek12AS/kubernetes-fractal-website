'''Contains functions which generate and display a koch snowflake.

Functions
----------
koch_snowflake
    Generates a koch snowflake of a given order.
draw_snowflake
    Saves the graph as a png.
'''
import numpy as np # pylint: disable=import-error
import matplotlib.pyplot as plt # pylint: disable=import-error

def koch_snowflake(order: int, scale=10):
    """
    Return two lists x, y of point coordinates of the Koch snowflake.

    Parameters
    ----------
    order : int
        The recursion depth.
    scale : float
        The extent of the snowflake (edge length of the base triangle).
    """
    def _koch_snowflake_complex(order: int):
        if order == 0:
            # initial triangle
            angles = np.array([0, 120, 240]) + 90
            return scale / np.sqrt(3) * np.exp(np.deg2rad(angles) * 1j)

        z_r = 0.5 - 0.5j * np.sqrt(3) / 3

        p_1 = _koch_snowflake_complex(order - 1)  # start points
        p_2 = np.roll(p_1, shift=-1)  # end points
        d_p = p_2 - p_1  # connection vectors_

        new_points = np.empty(len(p_1) * 4, dtype=np.complex128)
        new_points[::4] = p_1
        new_points[1::4] = p_1 + d_p / 3
        new_points[2::4] = p_1 + d_p *    z_r
        new_points[3::4] = p_1 + d_p / 3 * 2
        return new_points

    points = _koch_snowflake_complex(order)
    x, y = points.real, points.imag #pylint: disable=invalid-name
    return x, y

def draw_snowflake(order: int):
    '''Draw snowflake and save it as png.'''
    x,y = koch_snowflake(order) #pylint: disable=invalid-name
    plt.ioff()
    plt.figure(figsize=(8,8))
    plt.axis('equal')
    plt.fill(x,y,'g')

    plt.tick_params(axis='x', which='both', bottom=False,
                    top=False, labelbottom=False)
    plt.tick_params(axis='y', which='both', right=False,
                    left=False, labelleft=False)
    for pos in ['right', 'top', 'bottom', 'left']:
        plt.gca().spines[pos].set_visible(False)

    fname='static/koch_snowflake.png'
    fmt='png'
    plt.savefig(fname=fname,format=fmt,transparent=True)
