def slu4(y,x,x1):

    f = [i for i in range(0,10)]
    f[0] = (x[0]**2-x[1]**2)/(x[1]-x[0])
    f[1] = (x[0]**3-x[1]**3)/(x[1]-x[0])
    f[2] = f[0]*x[0]+x[0]**2
    f[9] = x[0]**3+f[1]*x[0]
    f[3] = f[0]*x[2]+x[2]**2-f[2]
    f[4] = f[1]*x[2]-f[9]+x[2]**3
    f[5] = f[4]/f[3]
    f[6] = f[2]*f[5]-f[9]
    f[7] = f[1]-f[0]*f[5]
    f[8] = f[6]+f[7]*x[3]-f[5]*x[3]**2+x[3]**3

    c = [i for i in range(0,8)]
    c[0] = y[0]
    c[1] = (y[1]-c[0])/(x[1]-x[0])
    c[2] = c[0]-c[1]*x[0]
    c[3] = c[2]+c[1]*x[2]
    c[4] = (y[2]-c[3])/f[3]
    c[5] = c[2]-f[2]*c[4]
    c[6] = c[1]+f[0]*c[4]
    c[7] = c[5]+c[6]*x[3]+c[4]*x[3]**2

    a = [i for i in range(0,4)]
    a[3] = (y[3]-c[7])/f[8]
    a[2] = c[4]-f[5]*a[3]
    a[1] = c[6]+f[7]*a[3]
    a[0] = c[5]+f[6]*a[3]

    y1 = a[0]+a[1]*x1+a[2]*x1**2+a[3]*x1**3
    return y1