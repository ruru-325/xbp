
import random

def number_guessing_game():
    print("数当てゲームへようこそ！")
    print("1から100の間の数を当ててください。")

    # コンピュータが1から100の間のランダムな数を選ぶ
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        # プレイヤーに数を入力させる
        guess = input("あなたの予想は？ (終了するには 'exit' と入力): ")

        if guess.lower() == 'exit':
            print("ゲームを終了します。")
            break

        # 入力が数値かどうかを確認
        if not guess.isdigit():
            print("無効な入力です。1から100の間の数を入力してください。")
            continue

        guess = int(guess)
        attempts += 1

        # 予想が正しいかどうかをチェック
        if guess < secret_number:
            print("もっと大きい数です。")
        elif guess > secret_number:
            print("もっと小さい数です。")
        else:
            print(f"おめでとうございます！ {attempts} 回目の試行で正解しました！")
            break
