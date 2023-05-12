import matplotlib.pyplot as plt
import random

# Function to generate the plot
def generate_plots(a,b,m,k,file,pic_name):
    
    # ticks on  the x-axis (0, 0.05, 0.10, .. , 1.00)
    arr = []
    val = 0
    for x in range(21):
        arr.append(val)
        val += 0.05

    # values of u
    u = []
    xi = k
    for x in range(100000):
        u.append(xi/m)    
        xi = (a*xi+b)%m
        
    values = "a = " + str(a) + ", x0 = " + str(k)

    numbers_bar = 20
    plt.xlabel('Value of ui')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.xticks(arr,rotation='vertical') 
    frequencies,bins,patches = plt.hist(u,numbers_bar,edgecolor = 'brown',label=values)
    plt.legend(loc='upper right')
    plt.savefig(pic_name)
    plt.clf()
    
    file.write(values)
    file.write("\n")
    file.write("Range, Frequency, ")
    file.write("\n")
    low = 0
    high = 0.05
    for i in range(20):
        file.write(str(round(low,2)) + " - " + str(round(high,2)) + ", ")
        file.write(str(frequencies[i]) + ", ")
        file.write("\n")
        low += 0.05
        high += 0.05


def main():
    m = 244944
    b = 10
    file = open("200123011_qus2_output.csv","a")
    img_Number = 1

    # generates 5 random (and distinct) values of x0 such that 0 <= x < m (assuming m >= 5)
    number = random.sample(range(m),5)

    # Part 1 ->  m = 244944, a = 1597, b = 3436
    a = 1597
    for k in number:
        pic_name = "200123011_qus2_fig "+str(img_Number)+".png"
        img_Number += 1 
        generate_plots(a,b,m,k,file,pic_name)
        file.write("\n")

    # Part 2 -> m = 244944, a = 51749, b = 3436
    a = 51749
    for k in number: 
        pic_name = "200123011_qus2_fig "+str(img_Number)+".png"
        img_Number += 1 
        generate_plots(a,b,m,k,file,pic_name)
        file.write("\n")

if __name__ == '__main__':
    main()
  