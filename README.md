# WebSimulateLogin
网站模拟登录

# 使用说明

## 依赖
chormedriver
python3+

## 使用步骤
1. git clone
2. pip install -p requestment.txt
3. cd WebSimulateLogin
4. python main -h 查看命令行帮助信息
5. 通过命令行参数方式启动
   python main -u www.github.com/login -a xxx -p yyy
   执行该命令后，会有chorme浏览器窗口打开，并尝试登录github。最终在终端输出登录信息
6. 通过excel文件方式启动
   python -t excel -i src/input_parser/test/test_input_excel.xlsx
   执行该命令，会读取excel中的网站信息，逐个进行模拟登录。最终会将结果输出到当前文件夹的result.xlsx文件，你也可以指定输出位置，需要在命令行中使用-o选型
