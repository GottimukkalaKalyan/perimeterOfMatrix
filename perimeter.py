n,m = input().split()
n = int(n)
m = int(m)
list_a = []
for i in range(n):
    num = input().split()
    sub_list = []
    for j in num:
        sub_list.append(int(j))
    list_a.append(sub_list)
count = 0
for i in range(n):
    for j in range(m):
        if (i == 0) or (i == (n-1)):
            count += list_a[i][j]
        else:
            if (j == 0) or (j == (m-1)):
                count +=  list_a[i][j]
print(count)