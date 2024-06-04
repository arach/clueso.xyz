import asyncio
from playwright.async_api import async_playwright


async def getTrendingRepos(language=None, since=None):
  async with async_playwright() as p:
    # Launch the browser
    browser = await p.chromium.launch()
    page = await browser.new_page()
    
    gh_trending_url = 'https://github.com/trending'
    if language:
      gh_trending_url = f'{gh_trending_url}/{language}'
    if since:
      gh_trending_url = f'{gh_trending_url}?since={since}'
    await page.goto(gh_trending_url)

    repos = await page.locator("article.Box-row").all()
    trending_repos = []

    for repo in repos:
      title = await repo.locator("h2").locator("a").inner_text()
      link = await repo.locator("h2").locator("a").get_attribute('href')
      stargazers = await repo.locator(".f6").locator("a").nth(0).inner_text()
      forks = await repo.locator(".f6").locator("a").nth(1).inner_text()
      #in python join "github.com" and link to form url
      url = "https://github.com" + link
      trending_repo = {
          'title': title,
          'link': url,
          'stargazers': stargazers,
          'forks': forks
      }
      trending_repos.append(trending_repo)

    await page.screenshot(path='screenshot.png')
    print('Screenshot captured and saved as screenshot.png')
    # Close the browser
    await browser.close()
    return trending_repos