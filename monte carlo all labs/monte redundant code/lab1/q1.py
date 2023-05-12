def lin_Cong_Gen(a,b,m,st,numTerms,file):
    n = st
    for k in range(numTerms):
        file.write(str(n)+", ")
        xi = (a*n+b)%m
    file.write("\n")

def main():
    # Part 1 -> a = 6, b = 0, m = 11
    file = open("200123011_qus1_part_1st_output.csv","a")
    for k in range(100):
        file.write("x" + str(k) + ", ")
    file.write("\n")
    for i in range(0,11):
        lin_Cong_Gen(6,0,11,i,100,file)
    file.close()

    # Part 2 -> a = 3,b = 0,m = 11
    file = open("200123011_qus1_part_2nd_output.csv","a")
    for k in range(100):
        file.write("x" + str(k) + ", ")
    file.write("\n")
    for i in range(0,11):
        lin_Cong_Gen(3,0,11,i,100,file)
    file.close()

if __name__ == '__main__':
    main()
