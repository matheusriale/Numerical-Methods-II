# Initial Value Problems

In this section, i develop explicit Euler method, implicit Euler method and Runge-Kutta method for some pre-determined Initial Value Problems.
For the IVP-2 (Free fall problem), we got the following data: 
<code>

t0 = 0

v0 = 5 #m/s

y0 = 200 #m

k = 0.25 #kg/s

m = 2 #kg

g = 10 #m/s^2

deltaT = 0.1

</code>

And our initial value problem defined with state S = [v1,y1] and F = [-g-(k/m)*vs , vs]:
<code>

v1 = v0 + deltaT*(-g -(k/m)*v0)

y1 = y0 + deltaT*v0

</code>

<br>

Where <code>t0</code> is our initial time, <code>v0</code> our initial velocity,<code>y0</code> our initial height,<code>m</code> mass of our particle, 

<code>ImplicitExplicitEuler</code> i develop our initial value problem with explicit Euler method and implicit Euler method. We return the following data: delta t, maximum height of the particle, time to get to the maximum height, total time and our final velocity (velocity when the particle hits the ground, y0 = 0).
<br>

<code>Runge_Kutta</code>i develop our initial value problem with the Runge-Kutta method. Similarly with the Euler one, we return the following data: delta t, maximum height of the particle, time to get to the maximum height, total time and our final velocity (velocity when the particle hits the ground, y0 = 0).
<br>

