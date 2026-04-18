# 运维文档

## 环境要求
- macOS 系统
- Docker 已安装并启动

## 启动项目
1. 进入项目目录：
   ```bash
   cd /Users/qidazhong/workspace/treatesting/taskManagerOps
   ```

2. 执行启动命令：
   ```bash
   docker-compose up -d
   ```

3. 访问应用：
   打开浏览器访问：http://localhost:8080

## 停止项目
1. 进入项目目录：
   ```bash
   cd /Users/qidazhong/workspace/treatesting/taskManagerOps
   ```

2. 执行停止命令：
   ```bash
   docker-compose down
   ```

## 重启项目
1. 进入项目目录：
   ```bash
   cd /Users/qidazhong/workspace/treatesting/taskManagerOps
   ```

2. 执行重启命令：
   ```bash
   docker-compose restart
   ```

## 查看运行状态
```bash
docker-compose ps
```

## 查看日志
```bash
docker-compose logs -f
```
