import matplotlib.pyplot as plt

def drow():
    x1, y1 = [0.0, 0.0], [0.0, 2.0]
    i = 2
    stolX = [x1[0], y1[0]]
    stolY = [x1[1], y1[1]]
    while i < 5000:
        proba = 2
        vec1 = [y1[0] - x1[0], y1[1] - x1[1]]
        x2 = y1
        vec2 = [1, 0]
        vec2[1] = -vec2[0] * vec1[0]/vec1[1]
        y2 = [y1[0] + vec2[0], y1[1] + vec2[1]]
        if 4 != (y2[0] - y1[0])** 2 + (y2[1] - y1[1])** 2:
            proba = (4/(vec2[0]**2 + vec2[1]**2))** (0.5)
        vec2 = [vec2[0]*proba, vec2[1]*proba]
        vec2_invert = [-vec2[0], -vec2[1]]
        if y1[1] < 0:
            vec2 = vec2_invert
        y2 = [y1[0] + vec2[0], y1[1] + vec2[1]]
        #print (i)
        print(y2)
        stolX.append(y2[0])
        stolY.append(y2[1])
        i += 1
        y1 = y2
    plt.plot(stolX, stolY)
    plt.axis('equal')
    plt.show()
if __name__ == '__main__':
    drow()


