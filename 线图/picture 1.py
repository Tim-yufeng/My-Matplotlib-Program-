import matplotlib.pyplot as plt
import numpy as np
# import math
x=np.linspace(0,9,50)
y=3-x/3


plt.figure('How you flunk out in SJTU')
plt.plot(x,y,color='purple')

plt.ylabel(r'$Your\ GPA$')
plt.xlabel('$Semester$')
plt.xticks([0,3,6,9],
           ['$Fall,Not\ bad$','$Spring,trash!$','$Summer,Flunked!$','$Fall,High\ school\ again!$'])

plt.show()



