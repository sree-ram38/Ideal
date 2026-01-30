# # Rectangle pattern
# n = int(input("Enter the range : "))
# for i in range(n):
#     for j in range(n):
#         print("*",end=' ')
#     print()    


# increasing triangle pattern
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=' ')
#     print()    

# decreasing triangle pattern
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=' ')
#     print()    

# right sided triangle *Decreasing space and increasing star
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(".",end='')
#     for j in range(i+1):
#         print('*',end='')
#     print()    


# right sided triangle increasing space and decreasing star
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end='')
#     for j in range(i,n):
#         print('*',end='')
#     print()    

# hill pattern decreasing space, increasing star, increasing star
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end='  ')
#     for j in range(i):
#         print('*',end='  ')
#     for j in range(i+1):
#         print('*',end='  ')
#     print()    

# Reverse hill pattern increasing space, Decreasing star, Decreasing star
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end='  ')
#     for j in range(i,n-1):
#         print('*',end='  ')
#     for j in range(i,n):
#         print('*',end='  ')
#     print()    





# Diamond pattern
# n = 5
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end='   ')
#     for j in range(i):
#         print('*',end='   ')
#     for j in range(i+1):
#         print('*',end='   ')
#     print()    
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end='   ')
#     for j in range(i,n-1):
#         print('*',end='   ')
#     for j in range(i,n):
#         print('*',end='   ')
#     print()    


# pyramid
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# n = 5
# for i in range(1, n+1):
#     print(" " * (n-i) + "* " * i)


# Right triangle
# *
# * *
# * * *
# * * * *
# * * * * *
# n = 5
# for i in range(1, n+1):
#     print("* " * i)


# left triangle
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# n = 5
# for i in range(1, n+1):
#     print(" " * (n-i) + "* " * i)


# right downward triangle
# * * * * *
# * * * *
# * * *
# * *
# *
# n = 5
# for i in range(n, 0, -1):
#     print("* " * i)


# Downward triangle
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# n = 5
# for i in range(n, 0, -1):
#     print(" " * (n-i) + "* " * i)


# # Double hill
#     *         *
#    * *       * *
#   * * *     * * *
#  * * * *   * * * *
# * * * * * * * * * *
# n = 5
# for i in range(1, n+1):
#     print(" "*(n-i) + "* "*i + " "*(2*(n-i)) + "* "*i)


# # Reversee pyramid
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# n = 5
# for i in range(n, 0, -1):
#     print(" "*(n-i) + "* " * i)


# # Butterfly pattern
# *       *
# * *   * *
# * * * * *
# * * * * *
# * *   * *
# *       *
n = 3
# Upper part
for i in range(1, n + 1):
    print("* " * i + "  " * (n - i) * 2 + "* " * i)
# Lower part
for i in range(n, 0, -1):
    print("* " * i + "  " * (n - i) * 2 + "* " * i)




# # Diamond
#     *
#    * *
#   * * *
#  * * * *
#   * * *
#    * *
#     *
# n = 4

# for i in range(1, n+1):
#     print(" "*(n-i) + "* "*i)

# for i in range(n-1, 0, -1):
#     print(" "*(n-i) + "* "*i)



# # Sandglass
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# n = 5
# for i in range(n, 0, -1):
#     print(" "*(n-i) + "* "*i)

# for i in range(2, n+1):
#     print(" "*(n-i) + "* "*i)



# # left pascal triangle
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *
# n = 4
# for i in range(1, n+1):
#     print("* "*i)

# for i in range(n-1, 0, -1):
#     print("* "*i)


# # # Right pascal triangle
#       *
#     * *
#   * * *
# * * * *
#   * * *
#     * *
#       *
# n = 4
# # Upper part
# for i in range(1, n + 1):
#     print("  " * (n - i) + "* " * i)

# # Lower part
# for i in range(n - 1, 0, -1):
#     print("  " * (n - i) + "* " * i)


