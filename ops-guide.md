# TaskManager 运维文档

## 项目简介
基于 Flask + Python 的任务管理系统，使用 Docker 部署。

## 环境要求
- macOS
- Docker（已安装）
- Docker Compose

## 快速操作

### 启动项目
```bash
cd /Users/qidazhong/workspace/treatesting/taskManagerOps
docker-compose up -d
```
启动后访问：http://localhost:8080

### 停止项目
```bash
cd /Users/qidazhong/workspace/treatesting/taskManagerOps
docker-compose down
```

### 重启项目
```bash
cd /Users/qidazhong/workspace/treatesting/taskManagerOps
docker-compose restart
```

## 常用命令

### 查看运行状态
```bash
docker-compose ps
```

### 查看日志
```bash
docker-compose logs -f
```

### 重新构建并启动
```bash
docker-compose up -d --build
```

## 文件说明
- `Dockerfile` - 镜像构建配置
- `docker-compose.yml` - 容器编排配置
- `tasks.db` - SQLite 数据库文件（数据持久化）
