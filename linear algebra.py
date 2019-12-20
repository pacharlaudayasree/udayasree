import numpy as np
print("operations on linear algebra")
x=input("enter 3*3 matrix whos det is not equal to zero\n [[a,b,c],[e,f,g],[h,i,j]]\n")
one=np.array(x)
m=np.array([[1,2,3],[4,3,5],[9,2,5]])
n=np.array([[1,2,9],[1,2,1],[9,6,8]])
d=np.dot(m,n)
print "1.dot product\n",d
print "2.dot product of multiple equations\n",np.linalg.multi_dot([one,m,n])
print "3.linalg.vdot returns dot product=\n",np.vdot(m,n)
print "4.mul of two matrix=\n",np.matmul(m,n)
print "5.power or square of a matrix=\n",np.linalg.matrix_power(one,2)
print "6.eigen values and eigen vector=\n",np.linalg.eig(one)
print "7.eigen values and eigen vectors of real symmetry=\n",np.linalg.eigh(one)
print "8.eigen values of a general matrix=",np.linalg.eigvals(one)
print "9.eigenvalues of a real symmetric matrix=",np.linalg.eigvalsh(one)
print "10.determinant of a matrix=",np.linalg.det(one)
print "11.sign and logithm values of determinant of matrix=", np.linalg.slogdet(one)
print "12.rank of a matrix=",np.linalg.matrix_rank(one)
print "13.trace=",np.trace(one)
print "14.diagonal elements of a matrix=",np.diagonal(one)
print "15.upper triangle of a matrix=\n",np.triu(one)
print "16.lower triangle of a matrix=\n",np.tril(one)
print "17.inverse of a matrix=\n",np.linalg.inv(one)
print "18.leaner solution=\n",np.linalg.solve(m,n)
print "19.cross product of vectors=\n",np.cross(m,n)
print "20.addition of two vectors=\n",m+n
print '21.subtraction of two vectors=\n',m-n
print "22.multiplication of vectors=\n",m*n
print "23.division of vector=\n",m/2
print "24.transpose of a matrix=\n",np.transpose(one)

