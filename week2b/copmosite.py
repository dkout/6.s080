def composite(f,g):
    def composition(x):
        return f(g(x))
    return composition 
