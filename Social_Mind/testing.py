class process_content:
    def __init__(self,content,num):
        self.num=num
        self.content=' '+ content
    def process_content(self):
        pos_space=[index for index, chr in enumerate(self.content) if chr==" "]
        temp=''
        true_string=''
        for index in range(0,len(pos_space)-1):
            if (len(temp)+(pos_space[index+1] - pos_space[index]) < self.num):   
                if '\r' in self.content[pos_space[index]:pos_space[index+1]]:
                    tg= self.content[pos_space[index]:pos_space[index+1]]
                    true_string+=temp
                    temp=self.content[pos_space[index]+1:pos_space[index+1]]
                    #print("substring: ",tg)
                else: temp+=self.content[pos_space[index]:pos_space[index+1]]          
            else: 
                if temp[len(temp)-1]!="\n": temp+="\n"
                true_string+=temp
                temp=self.content[pos_space[index]:pos_space[index+1]]
        return true_string

