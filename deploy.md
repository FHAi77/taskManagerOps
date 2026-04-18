# 任务管理系统 - 部署运维文档

## 环境要求

- macOS
- Docker 已安装
- Docker Compose 已安装

## 启动项目

在项目根目录执行：

```bash
docker-compose up -d --build
```

启动后访问：http://localhost:8080

## 停止项目

```bash
docker-compose down
```

## 重启项目

```bash
docker-compose restart
```

## 查看日志

```bash
docker-compose logs -f
```

## 查看容器状态

```bash
docker-compose ps
```
