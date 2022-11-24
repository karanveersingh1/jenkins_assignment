def angle_inside(x,y,z):
  if(x>y):
    if(z>x and z<=360):
      return True
    if(z<y and z>=0):
      return True
  else:
    if(z>x and z<y):
      return True
  return False