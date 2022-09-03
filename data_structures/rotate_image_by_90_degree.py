#################################################################################
## Youtube Video Link: https://www.youtube.com/watch?v=IdZlsG6P17w&t=577s&ab_channel=NickWhite
## Rotate matrix by 90 degree without using any another matrix
## Step1: Transpose Matrix - it means that taking each columns and convert them to the rows
##   swap(array[i][j], array[j][i])
## Step2: Horizontal Flip
## swap(array[i][j], array[i][total_columns-1-j])
## INPUT Matrix:
## [ [1, 2, 3],
##   [4, 5, 6],
##   [7, 8, 9] ]
## OUTPUT Matix after 90 degree clock wise rotate:
## [ [7, 4, 1]
##   [8, 5, 2]
##   [9, 6, 3] ]
##
##
##
##
##
##
##
##################################################################################

custom_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
no_of_rows = len(custom_matrix)
no_of_columns = len(custom_matrix[0])
print("Main Matrix: ", custom_matrix)
for i in range(no_of_rows):
    for j in range(i, no_of_columns):
        custom_matrix[i][j], custom_matrix[j][i] = custom_matrix[j][i], custom_matrix[i][j]
print("Transpose Matrix: ", custom_matrix)

for i in range(no_of_rows):
    for j in range((no_of_columns//2)):
        custom_matrix[i][j], custom_matrix[i][no_of_columns-1-j] = custom_matrix[i][no_of_columns-1-j], custom_matrix[i][j]
print('Horizontal Flip (after 90 degree flip): ', custom_matrix)
