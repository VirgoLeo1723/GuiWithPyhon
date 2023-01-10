import random
def setup():
    global new_word
    global kind
    global mean
    ques()

def ques():
    choice=input("Add new vocab or learn vocab (new/learn): ")
    if choice=="new": New()
    else: Learn()

def New():
    f1=open("Learn_Vocab/Vocab.txt","ab")
    word_list=[]
    check="y"
    while (check=="y"):
        new_word=input("New word: ")
        kind=input("n, n, adj: ")
        mean=input("Definition: ")
        group=(new_word, kind, mean)
        word_list.append(group)
        check=input("Another word (y,n): ")

    for word,kind,mean in word_list:
        print(f"{word} ({kind}): {mean}")
        st=(str(word)+":"+str(mean)+" ("+str(kind)+")\n").encode("utf8")
        f1.write(st)
    
    f1.close()

def Learn():
    word_list=[]
    vocab_dict={}
    f2=open("Learn_Vocab/Vocab.txt","rb")
    while True:
        st=f2.readline().decode("utf8")
        word_list.append(st)
        if not st: break
    random_ques=input("Bạn muốn kiểm tra bao nhiêu từ (all/x): ")
    if random_ques=="all": runner=len(word_list)
    else: runner=int(random_ques)
    
    
    print("Mình sẽ hiện nghĩa tiếng việt, còn bạn sẽ nhập từ đó nhaaaa")
    print("Mỗi từ bạn sẽ có 5 lần đoán, hoặc bạn có thể nhập \"pass\" để chuyển từ")
    
    for index in range(0,runner):
        word=random.choice(word_list)
        if word!="":
            group=(word.split(":"))
            group[1]=group[1][:len(group[1])-1]
            ans=input(group[1]+": ")
            temp_ans=ans
            time_each_word=0
    
            while temp_ans!=group[0] and (time_each_word<5) and temp_ans!="pass"  :
                print("Oh no, try agin !!!!!")
                temp_ans=input()
                time_each_word-=1

            print("Huray !!!!!!!!")

    f2.close()
setup()
