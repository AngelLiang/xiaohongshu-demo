# 小红书文案生成器示例项目（无数据库版）

小红书文案生成器示例代码，一键生成小红书文案，可部署在vercel和zeabur等

体验地址：

- zeabur: https://xiaohongshu-demo.zeabur.app
- render: https://xiaohongshu-demo.onrender.com
- vercel: https://xiaohongshu-demo.vercel.app

vercel由于服务器的限制，只能有10s的请求时间，所以流式响应超过10s可能会被中断，render和zeabur暂时无此限制。

## 开发环境和依赖

- Python310
- FastAPI
- Jinja2

## 目录结构

```
static/             # 存放静态文件，包括js代码和css样式
templates/          # 存放html模板文件，主要是index主页
.env.example        # 环境变量示例，存放大模型的APIKEY等，使用时需要改名为.env
.gitignore          # 配置git忽略不提交的文件
main.py             # 主文件，web服务器代码
RADME.md            # 说明文件
services.py         # 存放web服务代码，主要是对接大模型的代码
requirements.txt    # 依赖文件，在别的环境可以迁移
vercel_build.sh     # vercel构建文件，用于配制vercel的构建命令
vercel.json         # vercel配置文件，用于配置vercel
zbpack.json         # zeabur配置文件，用于配置zeabur
```
