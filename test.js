// 引入 request 组件 
const request = require('request')
 
// 发送 post 请求
request({
  url: 'http://192.168.1.247/a/submit.php',
  method: 'POST',
  json: true,
  headers: {
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
  },
  body: {
    policyid:'1',
    deviceid:'53657',//要注册的设备ID
    itemsid:'',
    processtime:'46',
    is_guest:'0',//是否游客登录
    roleid:'1',//注册类型
    user_name:'',//登陆者账号
    password:'',//登陆者密码
    auth_type:'User',//登陆者角色
    auth_type_server:'',
    is_auto_auth:'No',
    is_safecheck:'1',//安全检查是否通过
    isActive:'1',//是否激活
    repair:'',//是否修复问题
    reCheck:'',//是否修复后重新检查
    ControlPostion:'1',
    ChangeTime:'2023-06-13 13:43:18',
    CacheCheckItem:'',
    Res:'',
    LastAuthID:'',
    LastCheckTID:'',
    IsRoleChange:'',
    TradeRunTime:'',
    LastCheckTimestamp:'',
    LastCheckResult:'',
    AutoLogin:'',
    DevRegSubmitted:'',
    tokenkey:'',
  }
},(err,rep,body) => {
  if(err){
    console.log("request 请求post 出现错误 err : " , err );
    return false ;
  }
  // body表示返回的数据
  if(body){
    console.log("request 请求post成功!" ,rep);
    // 请求成功
  }
})
 