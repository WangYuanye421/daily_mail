import asyncio
from github_trending import github_trend_json
from github_trending import github_trend_md
from github_trending import github_trend_html
from send_email import send_email 

def build_github_trend(data):
    # 定义 HTML 模板，使用占位符填充数据
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Github Trending</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            table, th, td {{
                border: 1px solid black;
            }}
            th, td {{
                padding: 10px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <h1>今日github趋势</h1>
        <table>
            <tr>
                <th>Repository</th>
                <th>Description</th>
                <th>Language</th>
                <th>Stars</th>
                <th>Stars Today</th>
            </tr>
            {rows}
        </table>
    </body>
    </html>
    """
    
    # 用于存放表格行数据的占位符
    rows = ""
    
    # 遍历数据列表，生成每个 repository 的 HTML 表格行
    for item in data:
        row = f"""
        <tr>
            <td><a href="{item['repository']}">{item['repository'].split('/')[-1]}</a></td>
            <td>{item.get('description', 'N/A')}</td>
            <td>{item.get('lang', 'N/A')}</td>
            <td>{item.get('stars', 'N/A')}</td>
            <td>{item.get('today_star', 'N/A')}</td>
        </tr>
        """
        rows += row

    # 填充 HTML 模板中的占位符
    html_content = html_template.format(rows=rows)
    
    return html_content


async def main():
   #data_html = await github_trend_html()
   data_json = await github_trend_json()
   #data_md = await github_trend_md()
   #print(data_json)
   html = build_github_trend(data_json)
   send_email(subject="每日邮件",
        body=html,
        to_email="yuanye.wang@foxmail.com")


if __name__ == "__main__":
    asyncio.run(main())

