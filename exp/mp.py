import multiprocessing
from datetime import datetime

def f(n):
  return [ n[0] ** n[1] ]

params = []

for i in range(0,100000):
  params.append([2,i])

start = datetime.now()
  
p = multiprocessing.Pool(multiprocessing.cpu_count())
res_list = p.map(f, params)

end = datetime.now()

print end - start