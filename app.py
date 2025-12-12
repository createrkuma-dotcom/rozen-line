# ---- メッセージ受信時の処理 ----
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_text = event.message.text

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "丁寧にわかりやすく答えてください。"},
                {"role": "user", "content": user_text}
            ]
        )

        # ✨ここが最新仕様
        reply_text = response.choices[0].message.content

    except Exception as e:
        print("OpenAI error:", e)
        reply_text = "OpenAI APIでエラーが発生しました。"

    try:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text)
        )
    except Exception as e:
        print("LINE reply error:", e)
