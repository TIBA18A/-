# quiz_game.py

def run_quiz():
    # クイズの質問と正解を設定
    questions = {
        "日本の首都は？": "東京",
        "富士山の高さは？（メートル）": "3776",
        "パンダの故郷はどこの国？": "中国"
    }

    # スコアを初期化
    score = 0

    # クイズの実行
    for question, correct_answer in questions.items():
        print(question)
        user_answer = input("答えを入力: ")

        if user_answer == correct_answer:
            print("正解！\n")
            score += 1
        else:
            print(f"不正解。正解は {correct_answer} です。\n")

    # 最終スコアを表示
    print(f"あなたのスコアは {score}/{len(questions)} です。")

if __name__ == "__main__":
    run_quiz()
