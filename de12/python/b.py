#pip install ytmusicapi コマプロに入力



from ytmusicapi import YTMusic

def search_playlist_by_mood_and_genre(mood, genre):
    """
    ユーザーが指定した気分とジャンルを使ってYouTube Musicからプレイリストを検索する。

    Parameters:
        mood (str): ユーザーの気分 (例: "relaxing", "happy", "sad")
        genre (str): 音楽ジャンル (例: "pop", "rock", "jazz")
    
    Returns:
        list: 該当するプレイリストのタイトルとURL
    """
    # YTMusicの初期化
    ytmusic = YTMusic()

    # 検索クエリの作成
    query = f"{mood} {genre} playlist"

    # 検索結果の取得
    search_results = ytmusic.search(query, filter="playlists")

    # 結果の整形
    playlists = []
    for result in search_results:
        if "playlistId" in result:
            playlists.append({
                "title": result["title"],
                "url": f"https://music.youtube.com/playlist?list={result['playlistId']}"
            })
    
    return playlists


# 使用例
if __name__ == "__main__":
    mood = input("気分を入力してください (例: relaxing, happy, sad): ").strip()
    genre = input("ジャンルを入力してください (例: pop, rock, jazz): ").strip()

    playlists = search_playlist_by_mood_and_genre(mood, genre)
    if playlists:
        print("\n該当するプレイリスト:")
        for idx, playlist in enumerate(playlists, start=1):
            print(f"{idx}. {playlist['title']} - {playlist['url']}")
    else:
        print("該当するプレイリストが見つかりませんでした。")
