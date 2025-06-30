##for visualization of data we have library called matplotlib(sub library/module=pyplot) and other is seaborn use pyplot
##seaborn is library which use matplotlib underneath of pyplot
#distplot= distribution curve(histogram)
#curve with histogram anf freq curve
from matplotlib import pyplot as ppt
import seaborn as ssb
x=ssb.distplot([1,2,3,4,5,6,7,8,9])                 ##distplot is old use displot it only gave histogram
ppt.show()

##curve only with histogram
from matplotlib import pyplot as ppt
import seaborn as ssb
x=ssb.displot([1,2,3,4,5,6,7,8,9])     
ppt.show()

##curve without histogram
from matplotlib import pyplot as ppt
import seaborn as ssb
x=ssb.distplot([1,2,3,4,5,6,7,8,9],hist=False)
ppt.show()   
