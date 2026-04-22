import os
import requests
from dotenv import load_dotenv

# 加载配置
load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
API_URL = "https://api.deepseek.com/v1/chat/completions"

def generate_light_strategy(space_type, style):
    prompt = f"""
    你是专业室内光环境设计师。
    空间类型：{space_type}
    装修风格：{style}
    请生成简洁实用的光环境策略，必须包含4点：
    1. 主光源（色温、亮度）
    2. 辅助光源（灯带/筒灯/落地灯等）
    3. 重点照明区域
    4. 氛围总结
    语言专业、简短、不废话。
    """

    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"请求失败：{str(e)}"

if __name__ == "__main__":
    print("==== 光环境策略生成工具 ====")
    space = input("请输入空间类型：")
    style = input("请输入装修风格：")
    
    print("\n正在生成建议...\n")
    strategy = generate_light_strategy(space, style)
    
    print("=" * 40)
    print(strategy)
    print("=" * 40)