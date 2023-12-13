import requests
import time 
# import warnings
# from requests.packages import urllib3
# urllib3.disable_warnings()
# warnings.filterwarnings("ignore")
def add(id):
    re=object()
    headers = {
        "Host": "192.168.1.247",
        "Connection": "keep-alive",
        "Content-Length": "391",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "http://192.168.1.247",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.0.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }

    # post请求
    url2 = "http://192.168.1.247/a/submit.php"
    param2 = {
        "policyid": "1",
        "deviceid": id,  # 要注册的设备ID：53657
        "itemsid": "",
        "processtime": "46",
        "is_guest": "0",  # 是否游客登录
        "roleid": "1",  # 注册类型
        "user_name": "",  # 登陆者账号
        "password": "",  # 登陆者密码
        "auth_type": "User",  # 登陆者角色
        "auth_type_server": "",
        "is_auto_auth": "No",
        "is_safecheck": "1",  # 安全检查是否通过
        "isActive": "1",  # 是否激活
        "repair": "",  # 是否修复问题
        "reCheck": "",  # 是否修复后重新检查
        "ControlPostion": "1",
        "ChangeTime": "2023-06-13 13:43:18",
        "CacheCheckItem": "",
        "Res": "",
        "LastAuthID": "",
        "LastCheckTID": "",
        "IsRoleChange": "",
        "TradeRunTime": "",
        "LastCheckTimestamp": "",
        "LastCheckResult": "",
        "AutoLogin": "",
        "DevRegSubmitted": "",
        "tokenkey": "",
    }
    try:
        re = requests.post(url2, data=param2,timeout=1.0, headers=headers, verify=False)
        print("当前时间是：",time.asctime(time.localtime()))
        print("上网请求已发送,状态码是：",re.status_code)
        print("你现在可以上网了，10分钟后，会再次检测连接状态，放心")
    except: #requests.exceptions.ConnectionError
        return

def detect():
    url="http://192.168.102.7/users/sign_in"
    re=object()
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.0.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    try:
        print("正在检测连接状态...")
        re = requests.get(url,timeout=1.0, headers=headers, verify=False,allow_redirects=False)
    except: #requests.exceptions.ConnectionError
        print("网络连接错误，已停止...")
        return ''
    if re.status_code==200:
        print("当前时间是：",time.asctime(time.localtime()))
        print("状态码是：",re.status_code,"目前可以上网")
    else:
        print("当前时间是：",time.asctime(time.localtime()))
        print("状态码是：",re.status_code,"不能上网")
    return re.status_code

if __name__ == '__main__':
   
    id =input("请输入你要上内网的设备ID：")
    status=detect()
    if status==200:
        print("你发送过一次上网请求，现在不清楚还有多长时间结束，我会循环检测你的状态")
        while True:
            status=detect()
            if status==302:
                print("断网了，正在重连中...")
                break
            time.sleep(10)      
    if status==302:
        while True:
            add(id)
            time.sleep(600)
            while True:
                status=detect()
                if status==302:
                    print("断网了，正在重连中...")
                    break
                time.sleep(5)
    if status=='':
        print("根本没有状态码，应该是公司服务器挂了，请你检查下")
    else:
        print("状态码是：",status)
        print("既不是200也不是302，应该服务器升级了请求过滤，请退出程序进行排查")