import json
from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
async def github_trend():
    schema = {
        "name": "Github trending",
        "baseSelector": ".Box-row",
        "fields": [
            {
                "name": "repository",
                "selector": ".lh-condensed a[href]",
                "type": "text",
            },
            {
                "name": "description",
                "selector": "p",
                "type": "text",
            },
            {
                "name": "lang",
                "type": "text",
                "selector": "span[itemprop='programmingLanguage']",
            },
            {
                "name": "stars",
                "type": "text",
                "selector": "a[href*='/stargazers']"
            },
            {
                "name": "today_star",
                "type": "text",
                "selector": "span.float-sm-right",
            },
        ],
    }
    extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)

    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url="https://github.com/trending",
            extraction_strategy=extraction_strategy,
            bypass_cache=True,
        )
        assert result.success, "github 数据抓取失败"
        github_trending = json.loads(result.extracted_content)
        for ele in github_trending:
            ele['repository'] = 'https://github.com/' + ''.join(ele['repository'].split())

        return github_trending
