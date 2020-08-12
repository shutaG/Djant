 <center>  <h1>
      Djant
     </h1> </center>  

<center> Djant 是一款用vue和drf实现auth权限管理系统 </center>
<center> 基于ANTD PRO VUE 与 Django REST framework </center>

> 注意事项：
> 1. 使用pymysql需要修改以下内容
> ```python
    # site-packages\django\db\backends\mysql\operations.py 文件夹下边
    # 第146行，原为
    query = query.decode(errors='replace')
    # 修改为
    query = query.encode(errors='replace')
```
>
>
