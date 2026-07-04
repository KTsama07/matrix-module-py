class Matrix:
    def __init__(self,rows: int,cols: int, data: list[list[float]] | None = None):
        self.rows = rows
        self.cols = cols
        if data is not None:
            if len(data) != rows or any(len(rows) != cols for rows in data):
                raise ValueError("Injected data dimensions do not match rows/cols")
            self.data = data
        else:
            self.data = [[0 for _ in range(cols)] for _ in range(rows)]
    def set_value(self):
        for i in range(self.rows):
            for j in range(self.cols):
             self.data[i][j]= int(input(f"enter values for [{i},{j}]:"))
    def __str__(self):
        output = []
        for i in range(self.rows):
            row_str = " ".join(f"{self.data[i][j]:3}" for j in range(self.cols))
            output.append(row_str)
        return "\n".join(output)
    def __add__(self,other: 'Matrix') -> 'Matrix':
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimension must  be same")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j]= self.data[i][j] + other.data[i][j]
        return result
    def __sub__(self,other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimension must  be same")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j]= self.data[i][j] - other.data[i][j]
        return result
    def __mul__(self, other):
        if isinstance(other,(int, float)):
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
              for j in range(self.cols):
                result.data[i][j]= self.data[i][j]*other
            return result
        elif isinstance(other, Matrix): 
          if self.cols != other.rows:
            raise ValueError("dot product not possible between matices")
          result = Matrix(self.rows, other.cols)
          for i in range(self.rows):
            for j in range(other.cols):
                total=0
                for k in range(self.cols):
                    total += self.data[i][k] * other.data[k][j]
                result.data[i][j]= total
          return result
        else:
            raise TypeError("Unsupported operand type for Matrix multiplication.")
    def __truediv__(self,other):
        if not isinstance(other,(int,float)):
            raise ValueError("Divisor is not an integer")
        result = Matrix(self.rows,self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] /other
        return result
    def __eq__(self,other):
        if not isinstance(other, Matrix) or self.rows != other.rows or self.cols != other.cols:
            return False
        
        for i in range(self.rows):
               for j in range(self.cols):
                   if self.data[i][j] != other.data[i][j]:
                     return False
        return True      
    def __pow__(self,power):
        if not isinstance(power,int):
            raise ValueError("power must be an number")
        if self.rows != self.cols:
            raise ValueError("Not a square Matrix")
        if power==0:
            result = Matrix(self.rows,self.cols)
            for i in range(self.rows):
                result.data[i][i]=1
            return result
        base_matrix = self
        if power<0:
            result= self.inverse()
            power== abs(power)
        result = base_matrix
        for _ in range(power - 1):
            result = result * self
        return result

    def transpose(self):
        result= Matrix(self.cols, self.rows)
        for  i in range(self.cols):
            for j in range(self.rows):
                result.data[i][j]=self.data[j][i]
        return result
    def get_cfm(self,row,col):
        cfm = [[self.data[i][j] for j in range(self.cols) if j!=col]
               for i in range(self.rows) if i!=row]
        return cfm
    def det(self):
        if self.rows != self.cols:
            raise ValueError("Not a square Matrix")
        n = self.rows
        if n==1 :
            return self.data[0][0]
        if n==2:
            return self.data[0][0]*self.data[1][1]-self.data[1][0]*self.data[0][1]
        det =0
        for col in range(n):
            sign = (-1)**col
            cfm_mat = Matrix(n-1,n-1)
            cfm_mat.data = self.get_cfm(0,col)
            cfm_det = cfm_mat.det()
            det += sign * self.data[0][col] * cfm_det
        return det
    def trace(self):
        if self.rows != self.cols:
            raise ValueError("Not a square Matrix")
        trace = 0
        for i in range(self.rows):
            trace = trace + self.data[i][i]
        return trace
    def adj(self):
        if self.rows != self.cols:
            raise ValueError("Not a square Matrix")
        n = self.rows
        cfm_mat = Matrix(n,n)
        for i in range(n):
             for j in range(n):
                minor_mat = Matrix(n-1,n-1)
                minor_mat.data = self.get_cfm(i,j)
                cfm_mat.data[i][j] = (-1)**(i+j)*minor_mat.det()
        return  cfm_mat.transpose()

    def inverse(self):
          n = self.rows
          a = self.det()
          if a==0:
              return ValueError("Matrix is singular")
          return self.adj()/a
          
          
          
        
        
"""mat1 = Matrix(2,3)
mat1.data = [[1,2,3],[4,5,6]]
mat2 = Matrix(2,3)
mat2.data = [[7,8,9],[10,11,12]]   
mat3 = Matrix(3,2)
mat3.data = [[7,8],[9,10],[11,12]]
mat4 = Matrix(2,3)
mat4.data = [[1,2,3],[4,0,6]]
mat5 = Matrix(2,2)
mat5.data = [[1,2],[4,6]]
mat6 = Matrix(3,3)
mat6.data = [[7,8,9],[10,11,12],[13,14,15]]
mat7 = Matrix(3,3)
mat7.data = [[7,8,9],[12,11,19],[13,14,15]]
print(mat7**-2)""