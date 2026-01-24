from curtose_skewness import Vec

class Processing:
    def __init__(self, vec: Vec):
        self.vec = vec

    
    def cov_mat(self, *args: Vec):
        n = len(args)
        if n == 0:
            return []

        matrix = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            matrix[i][i] = args[i].var()
            for j in range(i + 1, n):
                c = self.cov(args[i], args[j])
                matrix[i][j] = c
                matrix[j][i] = c

        return matrix


    def cov(self, X: Vec, Y: Vec, ddof=1):
        if not X.data or not Y.data:
            return
        
        n = len(X.data)

        if len(X.data) != len(Y.data):
            return

        mean_x = X.mean()
        mean_y = Y.mean()

        sum_ = 0
        for xi, yi in zip(X.data, Y.data):
            sum_ += (xi - mean_x)*(yi - mean_y)

        return sum_ / (n-ddof)
