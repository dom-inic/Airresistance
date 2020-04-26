import matplotlib.pyplot as plt
import numpy as np
# Model parameters
M = 1.0          # Mass of projectile in kg
g = 9.8          # Acceleration due to gravity (m/s^2)
V = 5          # Initial velocity in m/s
ang = 60.0       # Angle of initial velocity in degrees
Cd = 0.005       # Drag coefficient
dt = 0.5         # time step in s

# checking the variables by printing them out 
print (V, ang)
t = [0]      # t condition set to 0
# vx and vy conditions 
vx = [V*np.cos(ang/180*np.pi)]  
vy = [V*np.sin(ang/180*np.pi)]

# Drag force
drag = Cd*V**2                       

# defined lists 
ax = [-(drag*np.cos(ang/180*np.pi))/M]        
ay = [-g-(drag*np.sin(ang/180*np.pi)/M)]

# Print out some values to check
print (ax[0])
print (ay[0])
print (vx[0])
print (vy[0])
# Using the eulers method to update the variable 
counter = 0
while (counter < 10):
    t.append(t[counter]+dt)                # increment by dt and add to the list of time 
    vx.append(vx[counter]+dt*ax[counter])  # Update the velocity
    vy.append(vy[counter]+dt*ay[counter])  

    # With the new velocity calculate the drag force
    vel = np.sqrt(vx[counter+1]**2 + vy[counter+1]**2)   # magnitude of velocity
    drag = Cd*vel**2                                   # drag force 
    ax.append(-(drag*np.cos(ang/180*np.pi))/M)     
    ay.append(-g-(drag*np.sin(ang/180*np.pi)/M))
    
    # we Increment the counter by 1
    counter = counter +1

print ("t=", t)
print ("vx=", vx)

# Let's plot the velocity against time
plt.plot(t,vx)
plt.ylabel("x-velocity (m/s)")
plt.xlabel("time (s)")