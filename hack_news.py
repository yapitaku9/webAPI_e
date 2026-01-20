import requests
import time

# 下記が出力目標
# {'title': 'PYX: The next step in Python packaging', 'link': 'https://astral.sh/pyx'}

# topstoriesから情報を取得
all_topstories = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
# 下記により、all_topstories.json()により、記事番号がリストとして取得できていることを確認
# print(all_topstories.json())
# print(type(all_top.stories.json())

# 下記により、取得したtopstoriesの記事番号のうち、上位３０個を繰り返し取得
for id in all_topstories.json()[:30]:
    # 繰り返し取得した記事番号それぞれについて、該当記事の情報を取得
    response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty")

    # 下記により、タイトルとURL取得できることを確認
    # print(response.json()["title"])
    # print(response.json()["url"])

    # 取得したタイトルとURLを辞書型として整理
    news_info = {"title": response.json()["title"], "link": response.json()["url"]}
    time.sleep(1)  # １秒間隔を空ける
    print(news_info)  # 辞書型として整理したタイトルとURLを出力
