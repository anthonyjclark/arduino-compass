'''
Jo Slayton 2020

Will calculate the direction of the sensor using a randomly generated x,y pair
A concept test for the arduino implementation
'''

import numpy as np

# idk what i'm doing
degrees = [360,355.5,351.0,346.5,342.0,337.5,333.0,328.5,324.0,319.5,315.0,310.5,306.0,301.5,
                   297.0,292.5,288.0,283.5,279.0,274.5,270.0,265.5,261.0,256.5,252.0,247.5,243.0,
                   238.5,234.0,229.5,225.0,220.5,216.0,211.5,207.0,202.5,198.0,193.5,189.0,184.5,
                   180.0,175.5,171.0,166.5,162.0,157.5,153.0,148.5,144.0,139.5,135.0,130.5,126.0,
                   121.5,117.0,112.5,108.0,103.5,99.0,94.5,90.0,85.5,81.0,76.5,72.0,67.5,63.0,58.5,
                   54.0,49.5,45.0,40.5,36.0,31.5,27.0,22.5,18.0,13.5,9.0,4.5]
                   
xavgs = [0.198,0.162,0.134,0.067,0.031,0.005,-0.048,-0.046,-0.063,-0.148,-0.229,-0.231,-0.266,
                 -0.305,-0.389,-0.54,-0.576,-0.638,-0.659,-0.738,-0.731,-0.848,-0.891,-0.889,-0.918,
                 -0.964,-0.922,-1.024,-1.005,-0.981,-0.986,-1.005,-0.961,-0.981,-0.971,-0.945,-0.91,
                 -0.912,-0.849,-0.818,-0.752,-0.709,-0.663,-0.672,-0.552,-0.542,-0.522,-0.393,-0.362,
                 -0.362,-0.231,-0.179,-0.108,-0.096,-0.003,0.023,0.034,0.127,0.107,0.146,0.163,0.232,
                 0.256,0.335,0.312,0.369,0.392,0.372,0.38,0.447,0.48,0.435,0.454,0.396,0.379,0.37,
                 0.354,0.306,0.244,0.261]
                 
yavgs = [-0.342,-0.388,-0.425,-0.458,-0.499,-0.501,-0.536,-0.513,-0.607,-0.57,-0.575,-0.572,
                 -0.551,-0.585,-0.57,-0.47,-0.479,-0.454,-0.434,-0.384,-0.419,-0.359,-0.201,-0.18,
                 -0.219,-0.104,-0.057,-0.06,-0.023,-0.003,0.012,0.093,0.151,0.177,0.3,0.305,0.386,
                 0.431,0.501,0.501,0.52,0.627,0.668,0.684,0.713,0.774,0.768,0.803,0.795,0.775,0.811,
                 0.859,0.824,0.79,0.775,0.766,0.754,0.67,0.683,0.711,0.622,0.576,0.55,0.516,0.412,
                 0.386,0.268,0.234,0.191,0.139,0.024,0.009,-0.035,-0.048,-0.106,-0.141,-0.257,-0.276,
                 -0.302,-0.367]

def main():
    # x accel sine = ((0.7)*sin(x+0.6492625))-0.3
    # y accel sine = ((0.7)*sin(x-0.6492625))+0.145
    # use the averages
    xsine = []
    ysine = []

    # this will be in a separate function but just keeping it in main for right now
    degrees.reverse()
    for i in degrees:
        xsine.append((0.7*np.sin(np.radians(i)+0.6492625)) - 0.3)
        ysine.append((0.7*np.sin(np.radians(i)-0.6492625)) + 0.145)
    #print(xsine)
    #print(ysine)

    #here is where I'm not super sure. I have my since curves, so I want to check where x and y are most similar
    # this will be in a separate function but just keeping it in main for right now
    x = xavgs[0]
    y = yavgs[0]
    temp = 1
    xdirection = 0
    ydirection = 0
    for i in range(len(xsine)):
        diff = abs(xsine[i]-x)
        if(diff < temp):
            temp = diff
            xdirection = degrees[i]
    
    for j in range(len(ysine)):
        diff = abs(ysine[j]-y)
        if(diff < temp):
            temp = diff
            ydirection = degrees[j]

    print(xdirection) # returns 234 w/o abs, 9 with
    print(ydirection) # returns 0 w/o abs, 261 with


if __name__ == "__main__":
    main()