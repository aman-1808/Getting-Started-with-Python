# cook your dish here

# cook your dish here



for i in range(int(input())):



    u, p = map(int,input().split())

    cR = list(map(int,input().split()))

    sRank = list(map(int,input().split()))

    student=[]

    for i in range(p):

        c = list(map(int, input().split()))

        _c = sorted(c[1:], key=lambda u: cR[u-1])

        student.append([i, c[0], _c])

    sort_stu= sorted(student, key= lambda u: sRank[u[0]])

    

    cls_filed = [False] * u

    cho = 0

    for i in sort_stu:

        ch = 0

        for j in i[2]:

            if(cls_filed[j-1] == False):

                cls_filed[j-1] = True

                ch = j

                break

        if(i[0] == 0):

             cho = ch

             break

         

    print(cho)

