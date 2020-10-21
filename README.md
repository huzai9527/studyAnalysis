# 东南大学无锡分校青年大学习统计

## 运行截图
![image.png](https://i.loli.net/2020/10/21/l7APkWE1cm9yTvS.png)
## 环境安装
- 你可以按照下面的方式下载代码到本地
 ```bash
 git clone --depth 1 https://github.com/huzai9527/studyAnalysis.git SUSmember-dev
 ```
- 本项目在**python 3** 下运行,并且依赖**pands**,你可以在终端运行以下命令进行安装
```bash
pip install pandas
```
## 所需要的文件以及格式
- 本院总名单,按照如下格式,首行为班级名称,首列为索引号(excel自带),将班级同学名字替换即可
![image.png](https://i.loli.net/2020/10/21/jMKtVx8bW1lAL9H.png)
- 班级累计分数:首行为列名第一列列名空,第二列列名累计分数
- 第一列为填班级名,第二列为保存的班级名
![image.png](https://i.loli.net/2020/10/21/Lh3eE9PY6QZqMzA.png)
- 最后是大学习的统计情况,此文件是上级下发的,只要移到此目录即可
![image.png](https://i.loli.net/2020/10/21/5hxkHRVJbCaXBpQ.png)
- **注:** 总名单以及班级累计分数可以在下载好的文件中直接修改
## 安装好环境以及准备好相应文件后,在终端运行(文件目录路径下)
```bash
python SUSmember.py 无锡分校-东南-第十一期
```
- 运行完成输出，各班详细情况，并在结果文件夹生成EXCELL统计文件
![image.png](https://i.loli.net/2020/10/21/ZxTS6I9LuAtCnGY.png)

## 有不是团员的只要在总名单中删除即可
