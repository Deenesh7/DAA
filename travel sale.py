e = [[0,1,3],[1,2,5],[1,3,2],[2,3,1]]
threshold =4
def find_near_city(e,threshold):
    min_dis = float('inf')
    city=-1
    for e in e:
        if e[0]==1 and e[2] <= threshold and e[2] < min_dis:
            min_dis=e[2]
            city = e[1]
        elif e[1]== 1 and e[2]<=threshold and e[2]< min_dis:
            min_dis=e[2]
            city=e[0]
    return city
result = find_near_city(e,threshold)
print(result)