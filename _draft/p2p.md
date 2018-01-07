y = NO. received
t = time
q = chance of a node receive a message in time t.

$$
chance of x receive a message: = 1 - (1-q^{dt})^y =~ y q dt
NO node receive a message in time dt: = (a-y) y q dt
dy = q(a-y)y dt

t = (log(y) - log(y-a)) / a / q + C

since y = 1 when t = 0

C = 1-a

thus:
y = e^{qat} a / (e^{qat} + a - 1)
$$
