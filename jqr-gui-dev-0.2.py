import sentry_sdk
sentry_sdk.init(
    dsn="https://80869325ff8a9333284966d4cdff7c66@o4506008195956736.ingest.sentry.io/4506120681029632",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)
import tkinter as tk
import requests
import json
import webbrowser
from tkinter import ttk
import requests#http请求
import json#json数据处理
from pygments import highlight#高亮
from pygments.lexers import JsonLexer#高亮
from pygments.formatters import TerminalFormatter#高亮
from colorama import Fore,Back, Style,init#高亮


v=0.1
u_date='2023/10/26'

def colorize_json(smg2,pcolor=''):
    json_data=smg2
    try:
        parsed_json = json.loads(json_data)  # 解析JSON数据
        formatted_json = json.dumps(parsed_json, indent=4)  # 格式化JSON数据

        # 使用Pygments库进行语法高亮
        colored_json = highlight(formatted_json, JsonLexer(), TerminalFormatter())

        print(colored_json)
    except json.JSONDecodeError as e:
        print(json_data)

def addmsg(msg, color="white"):
    if color == "white":
        print(msg)
    elif color == "red":
        print("\033[31m" + msg + "\033[39m")
    elif color == "yellow":
        print("\033[33m" + msg + "\033[39m")
    elif color == "green":
        print("\033[32m" + msg + "\033[39m")
    elif color == "aqua":
        print("\033[36m" + msg + "\033[39m")
init(autoreset=True)
def colorprint(smg2,pcolor):
    if pcolor=='red':
      print(Fore.RED + smg2)
    elif pcolor=='bandg':
      print(Back.GREEN + smg2)
    elif pcolor=='d':
      print(Style.DIM + smg2)
    # 如果未设置autoreset=True，需要使用如下代码重置终端颜色为初始设置
    #print(Fore.RESET + Back.RESET + Style.RESET_ALL)  autoreset=True

null=None

root = tk.Tk()
root.title("机器人控制器-GUI-DEV-"+str(v))

# 创建一个Notebook小部件
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10)

root.geometry("450x260")  # 设置窗口的大小为300x200
root.resizable(False, False)

token=''

def bclp():
    global token
    token=entry.get()
    additional_label.config(text='你已设置默认Token，可随时重设')
    entryt1.delete(0,tk.END)
    entryt1.insert(0,token)
    entryt.delete(0,tk.END)
    entryt.insert(0,token)

# 创建一个选项卡
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="设置默认Token")

# 在选项卡内创建一个Frame
frame1 = ttk.Frame(tab1)
frame1.pack()

# 创建一个标签
label = ttk.Label(frame1, text="Token:")
label.grid(row=0, column=0)

b1=ttk.Button(tab1, text="设为本次默认Token",command=bclp)
b1.pack(padx=6, pady=6)

# 添加另一个标签，仍然使用pack布局管理器
additional_label = tk.Label(tab1, text="此默认Token只会在本次用于自动填充，不会被保存")
additional_label.pack(padx=5, pady=5)

# 创建一个文本框
entry = ttk.Entry(frame1)
entry.grid(row=0, column=1)

entry.insert(0,token)

#选项卡2，发送消息
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="发送消息")

true=True

def get_userid(userid,fwqid,lpai):
    if len(userid)>16:
        return userid
    else:
        url='https://a1.fanbook.mobi/api/bot/'+lpai+'/searchGuildMemberByName'
        headers = {'content-type':"application/json;charset=utf-8"}
        #userid转array
        userid=userid.split()
        data = json.dumps({"guild_id":int(fwqid),"username":userid})
        user_cid=requests.post(url,headers=headers,data=data)
        print(user_cid.text)
        json.loads(user_cid.text)
        #{"ok":true,"result":[{"user":{"id":389320179948986368,"is_bot":false,"first_name":"◀王大哥▶","username":"4562997","avatar":"f"},"status":"member","oversea":false}]} 获取id
        print(json.loads(user_cid.text)['result'][0]['user']['id'])
        return json.loads(user_cid.text)['result'][0]['user']['id']

def fsxx():
    global token
    url='https://a1.fanbook.mobi/api/bot/'+entryt.get()+'/sendMessage'
    headers = {'content-type':"application/json;charset=utf-8"}
    jsonfile=json.dumps({
    "chat_id":int(entryf2.get()),
    "text": entryf3.get()
    })
    print(jsonfile)
    postreturn=requests.post(url,data=jsonfile,headers=headers)
    colorize_json(smg2=postreturn.text,pcolor='d')
    fhz=json.loads(postreturn.text)
    if fhz['ok']==true:
        l1.config(text='发送成功，详细信息请前往终端查看')
    else:
        l1.config(text='发送失败，详细信息请前往终端查看，错误代码解释请前往开放平台>错误码')
    
def get_private_channel():
    user_cid=get_userid(entry2.get(),entry3.get(),lpai=entryt1.get())
    url='https://a1.fanbook.mobi/api/bot/'+entryt1.get()+'/getPrivateChat'
    headers = {'content-type':"application/json;charset=utf-8"}
    jsonfile=json.dumps({"user_id":int(user_cid)})
    #post
    postreturn=requests.post(url,data=jsonfile,headers=headers)
    colorize_json(smg2=postreturn.text,pcolor='d')
    fhz=json.loads(postreturn.text)
    '''
    {
    "ok": true,
    "result": {
        "id": 510639729457618944,
        "guild_id": 0,
        "type": "private",
        "channel_type": 3
    }
}
    '''
    #获取id
    if fhz['ok']==true:
        entry4.delete(0,tk.END)
        entry4.insert(0,fhz['result']['id'])
        additional_label4.config(text='获取成功，可前往发送消息发送私信，频道id：')
        entry4.pack(padx=6, pady=6)
        
# 在选项卡内创建一个Frame
frame1 = ttk.Frame(tab2)
frame1.pack()
# 创建一个标签
label = ttk.Label(frame1, text="Token:")
label.grid(row=0, column=0)
label = ttk.Label(frame1, text="频道id:")
label.grid(row=1, column=0)
label = ttk.Label(frame1, text="文本消息内容:")
label.grid(row=2, column=0)

b1=ttk.Button(tab2, text="发送",command=fsxx)
b1.pack(padx=6, pady=6)

# 添加另一个标签，仍然使用pack布局管理器
additional_label1 = tk.Label(tab2, text="向频道发送消息")
additional_label1.pack(padx=5, pady=5)
l1 = tk.Label(tab2, text="")
l1.pack(padx=6, pady=5)
# 创建一个文本框
#token
entryt = ttk.Entry(frame1)
entryt.grid(row=0, column=1)
entryt.insert(0,token)
#频道id
entryf2 = ttk.Entry(frame1)
entryf2.grid(row=1, column=1)
#文本f
entryf3 = ttk.Entry(frame1)
entryf3.grid(row=2, column=1)

#选项卡，获取私聊频道
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text='获取私聊频道')

frame2 = ttk.Frame(tab4)
frame2.pack()

label2 = ttk.Label(frame2, text="Token:")
label2.grid(row=0, column=0)
label = ttk.Label(frame2, text="用户id:")
label.grid(row=1, column=0)
label = ttk.Label(frame2, text="服务器id:")
label.grid(row=2, column=0)


#token
entryt1 = ttk.Entry(frame2)
entryt1.grid(row=0, column=1)
entryt1.insert(0,token)
#用户id
entry2 = ttk.Entry(frame2)
entry2.grid(row=1, column=1)
entry2.insert(0,token)
#服务器id
entry3 = ttk.Entry(frame2)
entry3.grid(row=2, column=1)
entry3.insert(0,token)
#创建一个输入框，默认隐藏
entry4 = ttk.Entry(tab4)
#创建按钮，获取私聊频道
b3=ttk.Button(tab4, text="获取私聊频道",command=get_private_channel)
b3.pack(padx=6, pady=6)
additional_label4 = ttk.Label(tab4, text="获取私聊频道")
additional_label4.pack(padx=5, pady=5)

#最后一个选项卡，关于
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text='关于')
def open_fwq():
    webbrowser.open('https://fanbook.mobi/LmgLJF3N')
#创建一个按钮
b2 = ttk.Button(tab3, text="加入讨论服务器", command=open_fwq)
b2.pack(padx=6, pady=6)
#创建一个标签
additional_label2 = tk.Label(tab3, text="王大哥 机器人控制器-GUI-DEV-"+str(v))
additional_label2.pack(padx=5, pady=5)
#创建一个标签
additional_label3 = tk.Label(tab3, text="更新日期:"+str(u_date))
additional_label3.pack(padx=5, pady=5)
root.mainloop()