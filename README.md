# 🤖 AI学习助手

一个基于 Google Gemini 大模型的AI学习助手网页应用，支持多轮对话和上下文记忆。

## 功能
- 多轮对话：能记住上下文，进行连续问答
- 角色设定：通过 System Prompt 将AI设定为耐心、善于用比喻的老师
- 网页界面：基于 Streamlit 搭建，浏览器直接访问

## 技术栈
- Python
- Streamlit（前端框架）
- Google Gemini API（大模型）
- python-dotenv（密钥管理）

## 如何运行
1. 克隆仓库：`git clone https://github.com/wanqiu-cloud/ai_tutor.git`
2. 安装依赖：`pip install streamlit openai python-dotenv`
3. 创建 `.env` 文件，填入你的 Gemini API Key（格式见下方）
4. 运行：`streamlit run tutor_web.py`

## 环境变量配置（.env）
GEMINI_API_KEY=你的Gemini Key
GEMINI_BASE_URL=https://generativelanguage.googleapis.com/v1/

## 项目结构
ai_tutor/ 
├── tutor_web.py # 主程序 
├── .env # 密钥文件（已排除版本控制） 
├── .gitignore # Git忽略规则 
└── README.md # 项目说明