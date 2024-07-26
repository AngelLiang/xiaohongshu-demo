# 小红书文案生成器示例项目

小红书文案生成器示例代码，一件生成小红书文案，可部署在vercel。

体验地址：https://xiaohongshu-demo.vercel.app/

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
services.py         # 存放web服务代码，主要对接大模型的代码
requirements.txt    # 依赖文件，在别的环境可以迁移
vercel_build.sh     # vercel构建文件，用于配置vercel
vercel.json         # vercel配置文件，用于配置vercel
```
