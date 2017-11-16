def get_largest_prime(N,n=2):
    if(N%n==0):
        if (n<N):
            N=N/n
            return get_largest_prime(N,n=n)
        if (n==N):
            return N
    else:
        if (n<=N and n>0):
          return get_largest_prime(N,n=(n+1))