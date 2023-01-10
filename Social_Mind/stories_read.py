class story_infor:
    stories = { "Học Tập":[],
                "Gia Đình":[],
                "Mối Quan Hệ Xã Hội":[],
                "Bản Thân Học Sinh":[]}
    def __init__(self) -> None:
        pass
    @staticmethod
    def add(topic, content):
        topic= topic[0:topic.index("\r")]
        story_infor.stories[topic].append(content)
    
f=open("Server/stories.txt","rb")
prev = f.readline().decode("utf-8")
content = ""
checked = 0
while True:
    current=f.readline().decode("utf-8")
    if current:
        if "#begin#" in current:  
            topic = prev
            checked = 1
        elif "#end#" in current: 
            story_infor.add(topic, content)
            content = ""
            checked = 0
        elif checked == 1: content+=current
    else: break
    prev = current
#for index in story_infor.stories:#
    #print(index, len(story_infor.stories[index]))