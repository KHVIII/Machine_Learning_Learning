def gradient_descent(learning_rate):
    w0 = 0
    w1 = 0
    for i in range(10):
        temp0 = w0 - learning_rate*(2*(w0+2*w1-4) + 2*(w0+3*w1-3))
        temp1 = w1 - learning_rate*(2*2*(w0+2*w1-4) + 2*3*(w0+3*w1+3))
        w0 = temp0
        w1 = temp1
        f = (w0+2*w1-4)**2 + (w0+3*w1-3)**2
        print("W0:{}, W1:{},f(w0,w1) = {}".format(w0,w1,f))

    return(w0,w1)

def main(learning_rate):
    w0, w1 = gradient_descent(learning_rate)
    print( "W0:{}, W1:{}".format(w0,w1))
