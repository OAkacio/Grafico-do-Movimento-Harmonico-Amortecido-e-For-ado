import math
from matplotlib import pyplot as plt


def sqrt(x):
    r=(x)**(1/2)
    return r

def main():
    k=float(input("Escreva a constante 'k' (Constante de proporcionalidade) da mola trabalhada em (N/m): "))
    m=float(input("Escreva a massa do corpo oscilante no sistema massa mola em (kg): "))
    b=float(input("Escreva aqui a constante 'b' (Constante de Amortecimento) em (kg/s): "))
    gama=float(b/(2*m))
    w0=(k/m)**(1/2)
    f0=float(input("Escreva aqui a força 'Fo' aplicada distendendo a mola periódicamente em (N): "))
    Te=float(input("Escreva aqui o período 't' em que a força estará distendendo a mola em (s): "))
    we=float((2*math.pi)/(Te))
    A=float(((f0)/(m))/(sqrt(((((w0)**2)-((we)**2))**2)/((2*gama*we)**2))))
    fi=math.atan((2*gama*we)/(((w0)**2)-((we)**2)))
    delta=float(gama**2-w0**2)
    if w0<we:
        print("Infelizmente precisa-se que o período de aplicação da força no sistema precisa ser maior que o período de oscilação natural do sistema")
    if delta>0:
        s=1
    elif delta==0:
        s=2
    elif delta<0:
        s=3
    if s==1:
        c1=(((gama)*A)/(2*(delta**(1/2))))+(A/2)
        c2=(A/2)-((gama*A)/(2*(delta**(1/2))))
        def xh(t):
            x=c1*(math.e**(t*((delta**(1/2))-gama)))+c2*(math.e**(-t*(gama+(delta**(1/2)))))
            return xh
    elif s==2:
        c1=A
        c2=A*gama
        def xh(t):
            xh=(c1+t*c2)*math.e**(-gama*t)
            return xh
    elif s==3:
        w=(-delta)**(1/2)
        c1=(A*gama)/w
        c2=A
        def xh(t):
            xh=(math.e**(-gama*t))*(c1*math.sin(w*t)+c2*math.cos(w*t))
            return xh
    def x(t):
        x=float(xh(t)+A*math.cos(we*t-fi))
        return x
    TL=int(input("Escreva aqui o tempo máximo que deseja observar o movimento em (s): "))
    xp2=[i for i in range(0,TL)]
    yp2=[x(xp2) for xp2 in range(0,TL)]
    plt.plot(xp2,yp2)
    plt.show()
main()
