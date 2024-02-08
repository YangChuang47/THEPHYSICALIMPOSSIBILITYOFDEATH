import json
import jsonlines
import os

def cutbydate(filename):
    b=os.getcwd() + '\\'
    wd={}
    c=''
    with open(filename,encoding="utf-8") as jsdt:
        for line in jsdt:
            data=json.loads(line)
            wd={'created_at':data['created_at'],'content':data['content'],'user_name':data['user']['nick_name']}
            if '死'in wd['content']:
                date=wd['created_at'][:10]
                month=wd['created_at'][:7]
                path=b+month
                c=b+month+'\\'+date+'.jsonl'
                if not os.path.exists(path):
                    os.makedirs(path)
                with jsonlines.open(c,'a') as w:
                    w.write(wd)
                    w.close()
fname=input('输入文件名：')            
cutbydate(fname)
