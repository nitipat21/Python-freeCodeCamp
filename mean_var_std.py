import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError('List must contain nine numbers.')

  # create container
  calculation = {}

  # create matrix 3*3
  np_list = np.array(list).reshape(3, 3)

  # calculate mean
  mean_list = []
  mean_list.append(np.mean(np_list, axis=0).tolist())
  mean_list.append(np.mean(np_list, axis=1).tolist())
  mean_list.append(np.mean(np_list).tolist())

  # calculate variance
  variance_list = []
  variance_list.append(np.var(np_list, axis=0).tolist())
  variance_list.append(np.var(np_list, axis=1).tolist())
  variance_list.append(np.var(np_list).tolist())

  # calculate standard deviation
  sd_list = []
  sd_list.append(np.std(np_list, axis=0).tolist())
  sd_list.append(np.std(np_list, axis=1).tolist())
  sd_list.append(np.std(np_list).tolist())

  # calculate max
  max_list = []
  max_list.append(np.max(np_list, axis=0).tolist())
  max_list.append(np.max(np_list, axis=1).tolist())
  max_list.append(np.max(np_list).tolist())

  # calculate max
  min_list = []
  min_list.append(np.min(np_list, axis=0).tolist())
  min_list.append(np.min(np_list, axis=1).tolist())
  min_list.append(np.min(np_list).tolist())

  # calculate sum
  sum_list = []
  sum_list.append(np.sum(np_list, axis=0).tolist())
  sum_list.append(np.sum(np_list, axis=1).tolist())
  sum_list.append(np.sum(np_list).tolist())
  
  # add value
  calculation['mean'] = mean_list
  calculation['variance'] = variance_list
  calculation['standard deviation'] = sd_list
  calculation['max'] = max_list
  calculation['min'] = min_list
  calculation['sum'] = sum_list

  return calculation
  
  
  

