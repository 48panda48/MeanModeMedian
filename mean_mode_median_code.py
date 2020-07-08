import itertools
config = {"max_num":20,"print total":True,"print_all_solutions":False,"plot_number_freq_data":False,"export_solutions_as_csv":False,"csv_export_name":"solutions.csv","plot_number_freq_data_grid":False}
def get_mean(a,b,c,d,e):
    return (a+b+c+d+e)/5
def get_range(a,b,c,d,e):
    return e-a # e is the biggest, a is the smallest
def get_median(a,b,c,d,e):
    return c
total_correct=0
a_={i:0 for i in range(1,config["max_num"]+1)}
b_={i:0 for i in range(1,config["max_num"]+1)}
c_={i:0 for i in range(1,config["max_num"]+1)}
d_={i:0 for i in range(1,config["max_num"]+1)}
e_={i:0 for i in range(1,config["max_num"]+1)}
csv=""
solutions=[]
abc=0
for a in range(1,config["max_num"]+1):
    for b in range(a,config["max_num"]+1):
        for c in range(b,config["max_num"]+1):
            for d in range(c,config["max_num"]+1):
                for e in range(d,config["max_num"]+1):
                    isSolution=False
                    if get_mean(a,b,c,d,e) == get_range(a,b,c,d,e): # from all my testing, this is the test that failed the most so this order of checking is the most time efficient!
                        if get_range(a,b,c,d,e) == get_median(a,b,c,d,e):
                            total_correct +=1
                            csv+=f"{a},{b},{c},{d},{e}\n"
                            solutions.append((a,b,c,d,e))
                            if config["print_all_solutions"]:
                                print(f"{a},{b},{c},{d},{e}")
                            a_[a]+=1
                            b_[b]+=1
                            c_[c]+=1
                            d_[d]+=1
                            e_[e]+=1
                            isSolution=True
                    if not isSolution and (a+b+c+d+e)%5==0 and (a+b+d+e)%4==0 and b+d == 3*c+2*a:
                        abc+=1
                        print(abc)
if config["export_solutions_as_csv"]:
    with open(config["csv_export_name"],"w+") as f:
        f.write(csv)
if config["print total"]:
    print(total_correct)
if config["plot_number_freq_data"]:
    import matplotlib.pyplot as plt
    def autolabel(rects,pos1,pos2):
        for rect in rects:
            height = rect.get_height()
            ax[pos1][pos2].text(rect.get_x() + rect.get_width()/2., 1*height,
                    str(height),
            ha='center', va='bottom')
    def plot(list_data, pos1,pos2,label):
        labels = [str(i) for i in range(1,config["max_num"]+1) if list(list_data.values())[i-1] != 0]
        x=[i for i in range(1,config["max_num"]+1) if list(list_data.values())[i-1] != 0]
        sizes = [i for i in list_data.values() if i != 0]
        b=ax[pos1][pos2].bar(x=x,height=sizes)
        ax[pos1][pos2].set_title(label)
        ax[pos1][pos2].set_xticks(x)
        ax[pos1][pos2].set_aspect('auto')
        ax[pos1][pos2].set_yticks([])
        ax[pos1][pos2].set_ylim(ymin=0,ymax=int(max(sizes)+2))
        ax[pos1][pos2].set_xticklabels(labels)
        autolabel(b,pos1,pos2)

    fig,ax=plt.subplots(2,3)
    plot(a_,0,0,"smallest number")
    plot(b_,0,1,"2nd smallest number")
    plot(c_,0,2,"3rd largest number")
    plot(d_,1,0,"2nd largest number")
    plot(e_,1,1,"largest number")
    ax[1][2].axis("off")

    plt.show()
if config["plot_number_freq_data_grid"]:
    import matplotlib.pyplot as plt
    def autolabel(rects,pos1,pos2):
        for rect in rects:
            height = rect.get_height()
            ax[pos1][pos2].text(rect.get_x() + rect.get_width()/2., 1.05*height-0.8,
                    str(height),
            ha='center', va='bottom')
    def plot(list_data, pos1,pos2,label):
        labels = [str(i) for i in range(1,config["max_num"]+1) if list(list_data.values())[i-1] != 0]
        x=[i for i in range(1,config["max_num"]+1) if list(list_data.values())[i-1] != 0]
        sizes = [i for i in list_data.values() if i != 0]
        b=ax[pos1][pos2].bar(x=x,height=sizes)
        ax[pos1][pos2].set_title(label)
        ax[pos1][pos2].set_xticks(x)
        ax[pos1][pos2].set_aspect('auto')
        ax[pos1][pos2].set_yticks([])
        ax[pos1][pos2].set_ylim(ymin=0,ymax=int(max(sizes)+2))
        ax[pos1][pos2].set_xticklabels(labels)
        autolabel(b,pos1,pos2)
    fig,ax=plt.subplots(5,5)
    labels=["smallest number","2nd smallest number","3rd largest number","2nd largest number","largest number"]
    def plot_scatter(x,y):
        x_dat=[]
        y_dat=[]
        c_dat=[]
        colorfromnumber=["k","m","r","y","g","c","b","w"]
        for i in range(1,21):
            for j in range(1,21):
                count=0
                for k in solutions:
                    if k[x]==j and k[y]==i:
                        count+=1
                x_dat.append(i)
                y_dat.append(j)
                c_dat.append(colorfromnumber[count])
                ax[x][y].scatter(x_dat,y_dat,c=c_dat,s=7)
    for i in range(5): # label rows and columns
        ax[i][0].set_ylabel(labels[i])
        ax[0][i].set_xlabel(labels[i])
        ax[0][i].xaxis.set_label_position('top')
        for j in range(5):#disable x and y ticks and set x and ylims
            ax[i][j].set_xticks([])
            ax[i][j].set_yticks([])
            ax[i][j].set_xlim((0,21))
            ax[i][j].set_ylim((0,21))
            ax[i][j].set(adjustable='box', aspect='equal')
    for i in range(5):
        for j in range(5):
            print(f"{i}:{j}")
            if i!=j:
                plot_scatter(i,j)
            else:
                plot([a_,b_,c_,d_,e_][i],i,i,"")
    plt.show()
#sum is 0 mod 5
# if the average  is a and the sum is s, the average is s/5 so s=5a which means s is a multiple of 5
#s=5a is equvalent to s-a=4a and s-2a = 3a so 
