from ytmusicapi import YTMusic

def get_recommended_playlists():
    """
    YouTube Musicのホーム画面からおすすめのプレイリストを取得する。

    Returns:
        list: おすすめプレイリストのタイトルとURL
    """
    # YTMusicの初期化
    ytmusic = YTMusic()

    # ホーム画面のおすすめコンテンツを取得
    home_content = ytmusic.get_home()

    # プレイリスト情報を抽出
    playlists = []
    for content in home_content:
        if content['title'] == 'Your playlists' or content['title'] == 'Mixed for you':
            for item in content['contents']:
                if "playlistId" in item:
                    playlists.append({
                        "title": item["title"],
                        "url": f"https://music.youtube.com/playlist?list={item['playlistId']}"
                    })
    return playlists


# 使用例
if __name__ == "__main__":
    playlists = get_recommended_playlists()
    if playlists:
        print("\nおすすめプレイリスト:")
        for idx, playlist in enumerate(playlists, start=1):
            print(f"{idx}. {playlist['title']} - {playlist['url']}")
    else:
        print("おすすめのプレイリストが見つかりませんでした。")
