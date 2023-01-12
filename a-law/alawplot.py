from numpy import arange,sign,log
from matplotlib.pyplot import plot,xlabel,ylabel,show,title,subplot

cx= [0.000000 ,0.000118 ,0.000766 ,0.002725 ,0.009479 ,0.196715 ,0.294132 ,0.333092 ,0.370320 ,0.408035 ,0.433538 ,0.525030]
str = ','.join([str(x) for x in cx])

for i in range (0,len(cx)):
  plot(cx)

title('compression law: a-law companding')
xlabel('Normalized |x|')
ylabel('normalized output |c(x)|')
show()