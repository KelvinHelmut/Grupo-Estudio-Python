#! /usr/bin/env python3.3
def main():
    xx = 0
    yy = 0
    for i in range(3):
        x = int( input( 'x' + str(i+1) + ': ' ) )
        y = int( input( 'y' + str(i+1) + ': ' ) )
        
        if (xx**2+yy**2) < (x**2+y**2):
            xx = x
            yy = y
    print( 'La coordena que esta mas lejos del centro es:', (xx,yy) )

main()
