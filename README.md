# 🎯 大乐透智能分析投注助手

基于中国体彩官方数据的超级大乐透统计分析工具，提供多维度号码分析和投注建议。

## ⚠ 重要声明

彩票开奖是**完全随机**的过程。本工具的建议基于历史数据的统计推算，**仅供参考娱乐**，不构成任何中奖承诺。请理性购彩，量力而行。

## ✨ 功能

- 📡 **自动获取数据**：连接中国体彩官方 API，获取最新开奖数据
- 📊 **多维度分析**：热号、遗漏、区间分布、奇偶比、连号重号等 7 大策略
- 🎯 **智能推荐**：综合评分最高的 1 组单式号码 + 3 套小复式方案
- 🤖 **DeepSeek AI**：可选接入 AI 大模型，深度解读统计数据
- 📱 **响应式设计**：手机和电脑浏览器完美适配
- 💾 **离线缓存**：数据自动缓存 6 小时，减少请求

## 🚀 使用方式

### Windows 用户（推荐）
1. 双击运行 **`start.bat`**
2. 浏览器自动打开 → 即可使用

> 需要 Python 环境，如果没有请运行：`winget install python`

### 手动启动
```bash
# 方式一：Python（推荐）
python -m http.server 8080
# 浏览器打开 http://localhost:8080

# 方式二：Node.js
npx serve -p 8080
```

### Firefox 用户
直接用 Firefox 打开 `index.html` 即可（Firefox 允许本地文件发起网络请求）

### 部署到 GitHub Pages

1. 在 GitHub 创建新仓库（如 `dlt-analyzer`）
2. 上传所有文件到仓库
3. 进入 Settings → Pages → Source 选择 `main` 分支 → Save
4. 等待 1-2 分钟，通过 `https://你的用户名.github.io/仓库名/` 访问

```bash
git init
git add index.html README.md start.bat
git commit -m "大乐透智能分析投注助手 v1.0"
git branch -M main
git remote add origin https://github.com/你的用户名/仓库名.git
git push -u origin main
```

> ⚠ GitHub Pages 可能有 CORS 限制，建议下载到本地使用以获得完整体验。

## 🤖 DeepSeek AI 设置

1. 访问 [platform.deepseek.com](https://platform.deepseek.com) 注册账号
2. 获取 API Key
3. 点击页面右上角 ⚙ 图标，填入 API Key
4. 回到「投注建议」页，点击「AI 分析」按钮

> API Key 仅保存在你的浏览器本地，不会上传到任何服务器。

## 📊 分析策略说明

| 策略 | 权重 | 说明 |
|------|------|------|
| 热号分析 | 30% | 近期出现频率 |
| 遗漏追踪 | 20% | 长期未出号码 |
| 近期趋势 | 25% | 近 10 期动态 |
| 区间均衡 | 15% | 三区分布平衡 |
| 随机扰动 | 10% | 避免确定性 |

## 🛠 技术栈

- 纯前端：HTML + CSS + JavaScript
- 数据源：中国体彩官方 API
- AI：DeepSeek API（可选）

## 📄 许可证

MIT License
