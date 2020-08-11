 <center>  <h1>
      Djant
     </h1> </center>  

<center> Djant 是一款基于vue和drf的auth权限管理系统 </center>


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
