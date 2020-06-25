

ax1 = plt.figure(1)
plt.subplot(1,1,1)

## putting in larger values screws things up
# rotate 90, 30 by 

az1 = np.array(range(0,360,10))
hor1 = az1 * 0 + 50

rt = rotate_horizon(az1, hor1, 135, 15)

#hor1 = [0 if 90 <= x <= 270 else 90 for x in az1]
c1 = horiz_to_carte(az1, hor1)
b = rotate_towards(135, 80)
rotat = np.dot(b, c1)
C = carte_to_horiz(rotat[0], rotat[1], rotat[2])
C[1] = [x if x >= 0 else 0 for x in C[1]]  # no negative horizons

# get rid of doubles


plt.clf()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='northpolar')
ax.yaxis.set_visible(False)
ax.set_ylim(0, 1)
ax.plot(ra(az1), np.cos(ra(hor1)))
ax.plot(ra(C[0]), np.cos(ra(C[1])))
ax.plot(ra(C[0]), np.cos(ra(C[1])), 'g.')




###
c1 = horiz_to_carte(0, 80)
b = rotate_towards(0, 45)
rotat = np.dot(b, c1)
C = carte_to_horiz(rotat[0], rotat[1], rotat[2])


##############################################
## Workin#g Demo
az1 = np.array(range(0,360,10))
hor1 = az1 * 0 + 50
rt = rotate_horizon(az1, hor1, 120, 50)
obs = test_obscured(rt[0], rt[1], 5)

plt.clf()
 ## Plot cartesian
xx = np.append(rt[0], obs)
yy = np.append(rt[1], (obs * 0 + 90))
yy = yy[np.argsort(xx)]
xx = xx[np.argsort(xx)]
plt.plot(xx,yy)


# Plot sky

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='northpolar')
ax.yaxis.set_visible(False)
ax.set_ylim(0, 1)
ax.plot(ra(az1), np.cos(ra(hor1)))
ax.plot(ra(rt[0]), np.cos(ra(rt[1])))

# all pts
ax.plot(ra(rt[0]), np.cos(ra(rt[1])), 'g.')

# overhanging pts
ax.plot(ra(rt[0][rt[1] > 90]), np.cos(ra(rt[1][rt[1] > 90])), 'rx')

# skyview: 
    # Create spline equation to obtain hor(az) for any azimuth
    # add endpoints on either side of sequence so interpolation is good 
xx = np.concatenate((xx[-2:] - 360, xx, xx[:2] + 360)) 
yy = np.concatenate((yy[-2:], yy, yy[:2]))
FF = interp1d(x=xx, y=yy)
sky_view_factor(FF, 2)

#

############################################################v
## experimental Demo
az1 = np.array(range(0,360,10))
hor1 = az1 * 0 + 70
rt = rotate_horizon(az1, hor1, 120, 120)
obs= total_obscura(rt[0], rt[1], 5)

plt.clf()
 ## Plot cartesian
xx = np.append(rt[0], obs)
yy = np.append(rt[1], (obs * 0 + 90))
yy = yy[np.argsort(xx)]
xx = xx[np.argsort(xx)]
plt.plot(xx,yy)


# Plot sky

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='northpolar')
ax.yaxis.set_visible(False)
ax.set_ylim(0, 1)
ax.plot(ra(az1), np.cos(ra(hor1)))
ax.plot(ra(rt[0]), np.cos(ra(rt[1])))

# all pts
ax.plot(ra(rt[0]), np.cos(ra(rt[1])), 'g.')

# overhanging pts
ax.plot(ra(rt[0][rt[1] > 90]), np.cos(ra(rt[1][rt[1] > 90])), 'rx')

# skyview: 
    # Create spline equation to obtain hor(az) for any azimuth
    # add endpoints on either side of sequence so interpolation is good 
xx = np.concatenate((xx[-2:] - 360, xx, xx[:2] + 360)) 
yy = np.concatenate((yy[-2:], yy, yy[:2]))
FF = interp1d(x=xx, y=yy)
sky_view_factor(FF, 2)

#