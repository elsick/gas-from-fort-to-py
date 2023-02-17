from slu4 import slu4
def fg(x1,x,dx,n,y):
    z = [i for i in range(0,4)]
    f = [i for i in range(0,4)]
    if x1+dx*2 <= x: #p
        if x1+dx*(n-3)>= x: #s
            k = int((x-x1)/dx)
            z[0] = x1+dx*(k-1)
            z[1] = z[0]+dx
            z[2] = z[1]+dx
            z[3] = z[2]+dx
            f[0] = y[k-1]
            f[1] = y[k]
            f[2] = y[k+1]
            f[3] = y[k+2]
        else:
            z[0] = x1+dx*(n-3)
            z[1] = x1+dx*(n-2)
            z[2] = x1+dx*(n-1)
            z[3] = x1+dx(n)
    else:
        z[0] = x1
        z[1] = x1+dx
        z[2] = x1+dx*2
        z[3] = x1+dx*3
        f[0] = y[0]
        f[1] = y[1]
        f[2] = y[2]
        f[3] = y[3]
    y1 = slu4(f,z,x)

    return y1

