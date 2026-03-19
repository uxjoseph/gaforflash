"""
이정환(너바나) 대표님 LinkedIn 게시글 기반 대화 에이전트
Flask 웹 앱 + Anthropic Claude API
"""

import os
import json
from flask import Flask, request, jsonify, render_template_string
from anthropic import Anthropic
from posts_data import PROFILE_INFO, COMPANY_INFO, LINKEDIN_POSTS

app = Flask(__name__)

client = Anthropic()

# Build context from collected data
def build_system_prompt():
    posts_text = ""
    for post in LINKEDIN_POSTS:
        posts_text += f"\n---\n[{post['date']}] {post.get('title', '')}\n좋아요: {post.get('likes', 'N/A')} | 댓글: {post.get('comments', 'N/A')}\n{post['content']}\n"

    revenue_history = "\n".join(
        f"  - {year}: {rev}" for year, rev in COMPANY_INFO["revenue_history"].items()
    )
    employee_history = "\n".join(
        f"  - {year}: {count}" for year, count in COMPANY_INFO["employees"].items()
    )

    return f"""당신은 월급쟁이부자들의 이정환(너바나) 대표의 LinkedIn 게시글과 공개된 정보를 기반으로 대화하는 AI 어시스턴트입니다.

## 역할
- 이정환 대표님의 LinkedIn 게시글에 담긴 인사이트, 철학, 경험을 기반으로 질문에 답변합니다.
- 이정환 대표님의 말투와 어조를 반영하되, AI 어시스턴트임을 명확히 합니다.
- 수집된 게시글 데이터를 근거로 답변하며, 데이터에 없는 내용은 "수집된 게시글에서는 해당 내용을 찾을 수 없습니다"라고 안내합니다.

## 프로필 정보
- 이름: {PROFILE_INFO['name']} (닉네임: {PROFILE_INFO['nickname']})
- 직함: {PROFILE_INFO['title']} at {PROFILE_INFO['company']}
- 학력: {PROFILE_INFO['education']}
- 배경: {PROFILE_INFO['bio']}

## 회사 정보
- 회사명: {COMPANY_INFO['name']}
- 설립: {COMPANY_INFO['founded']}
- 비전: {COMPANY_INFO['vision']}
- 미션: {COMPANY_INFO['mission']}
- 2024년 실적: 매출 {COMPANY_INFO['revenue_2024']}, 영업이익 {COMPANY_INFO['operating_profit_2024']} (영업이익률 {COMPANY_INFO['operating_margin_2024']})
- 매출 추이:
{revenue_history}
- 임직원 수:
{employee_history}
- 주요 서비스: {', '.join(COMPANY_INFO['services'])}

## 수집된 LinkedIn 게시글 ({len(LINKEDIN_POSTS)}개)
{posts_text}

## 답변 가이드라인
1. 한국어로 답변합니다.
2. 이정환 대표님의 게시글에서 관련 내용을 찾아 인용하며 답변합니다.
3. 투자, 재테크, 창업, 조직문화, 성장 관련 질문에 특히 풍부하게 답변합니다.
4. 게시글 날짜를 함께 언급하여 출처를 명확히 합니다.
5. 친근하지만 전문적인 어조로 답변합니다.
"""


SYSTEM_PROMPT = build_system_prompt()

# Store conversations in memory (per session)
conversations = {}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>이정환(너바나) 대표 LinkedIn 인사이트 챗봇</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #0a0a0a;
            color: #e0e0e0;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }
        .header {
            background: linear-gradient(135deg, #0077B5 0%, #005885 100%);
            padding: 16px 24px;
            display: flex;
            align-items: center;
            gap: 16px;
            box-shadow: 0 2px 12px rgba(0,119,181,0.3);
        }
        .header-avatar {
            width: 48px; height: 48px;
            background: #fff;
            border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 22px; font-weight: bold; color: #0077B5;
        }
        .header-info h1 {
            font-size: 18px; font-weight: 700; color: #fff;
        }
        .header-info p {
            font-size: 13px; color: rgba(255,255,255,0.8); margin-top: 2px;
        }
        .chat-container {
            flex: 1;
            overflow-y: auto;
            padding: 20px 16px;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }
        .message {
            max-width: 85%;
            padding: 14px 18px;
            border-radius: 18px;
            font-size: 15px;
            line-height: 1.6;
            animation: fadeIn 0.3s ease;
            white-space: pre-wrap;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(8px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .message.bot {
            background: #1a1a2e;
            border: 1px solid #16213e;
            align-self: flex-start;
            border-bottom-left-radius: 4px;
        }
        .message.user {
            background: #0077B5;
            color: #fff;
            align-self: flex-end;
            border-bottom-right-radius: 4px;
        }
        .message.bot .source {
            display: inline-block;
            background: rgba(0,119,181,0.15);
            color: #4db8ff;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 12px;
            margin-top: 8px;
        }
        .suggestions {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            padding: 0 16px 8px;
        }
        .suggestion-chip {
            background: #1a1a2e;
            border: 1px solid #2a2a4a;
            color: #8ab4f8;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 13px;
            cursor: pointer;
            transition: all 0.2s;
        }
        .suggestion-chip:hover {
            background: #0077B5;
            color: #fff;
            border-color: #0077B5;
        }
        .input-area {
            padding: 12px 16px;
            background: #111;
            border-top: 1px solid #222;
            display: flex;
            gap: 10px;
        }
        .input-area input {
            flex: 1;
            background: #1a1a2e;
            border: 1px solid #2a2a4a;
            border-radius: 24px;
            padding: 12px 20px;
            font-size: 15px;
            color: #e0e0e0;
            outline: none;
            transition: border-color 0.2s;
        }
        .input-area input:focus {
            border-color: #0077B5;
        }
        .input-area input::placeholder {
            color: #666;
        }
        .input-area button {
            background: #0077B5;
            border: none;
            border-radius: 50%;
            width: 44px; height: 44px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: background 0.2s;
        }
        .input-area button:hover { background: #005885; }
        .input-area button:disabled { background: #333; cursor: not-allowed; }
        .input-area button svg { fill: #fff; width: 20px; height: 20px; }
        .typing-indicator {
            display: none;
            align-self: flex-start;
            padding: 14px 18px;
            background: #1a1a2e;
            border: 1px solid #16213e;
            border-radius: 18px;
            border-bottom-left-radius: 4px;
        }
        .typing-indicator.show { display: flex; gap: 4px; }
        .typing-indicator span {
            width: 8px; height: 8px;
            background: #4db8ff;
            border-radius: 50%;
            animation: bounce 1.4s infinite;
        }
        .typing-indicator span:nth-child(2) { animation-delay: 0.2s; }
        .typing-indicator span:nth-child(3) { animation-delay: 0.4s; }
        @keyframes bounce {
            0%, 60%, 100% { transform: translateY(0); }
            30% { transform: translateY(-8px); }
        }
        .post-count {
            text-align: center;
            padding: 8px;
            font-size: 12px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="header-avatar">JH</div>
        <div class="header-info">
            <h1>이정환(너바나) 대표 LinkedIn 인사이트</h1>
            <p>월급쟁이부자들 CEO | LinkedIn 게시글 기반 AI 챗봇</p>
        </div>
    </div>
    <div class="post-count">수집된 LinkedIn 게시글 {{ post_count }}개 기반으로 대화합니다</div>
    <div class="chat-container" id="chatContainer">
        <div class="message bot">안녕하세요! 저는 월급쟁이부자들 이정환(너바나) 대표님의 LinkedIn 게시글을 학습한 AI 챗봇입니다. 🏠💰

대표님의 투자 철학, 월급쟁이부자들 성장 스토리, 조직문화, 프롭테크 사업, AI/바이브코딩 경험 등에 대해 물어보세요!

수집된 {{ post_count }}개의 LinkedIn 게시글을 기반으로 답변해 드립니다.</div>
    </div>
    <div class="suggestions" id="suggestions">
        <div class="suggestion-chip" onclick="askSuggestion(this)">작은 월급으로 부자되는 법은?</div>
        <div class="suggestion-chip" onclick="askSuggestion(this)">월급쟁이부자들 성장 비결은?</div>
        <div class="suggestion-chip" onclick="askSuggestion(this)">이정환 대표의 투자 철학은?</div>
        <div class="suggestion-chip" onclick="askSuggestion(this)">프롭테크 구해줘내집이 뭔가요?</div>
    </div>
    <div class="input-area">
        <input type="text" id="userInput" placeholder="질문을 입력하세요..." onkeydown="if(event.key==='Enter')sendMessage()">
        <button id="sendBtn" onclick="sendMessage()">
            <svg viewBox="0 0 24 24"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
        </button>
    </div>

    <script>
        const sessionId = 'session_' + Math.random().toString(36).substr(2, 9);
        const chatContainer = document.getElementById('chatContainer');
        const userInput = document.getElementById('userInput');
        const sendBtn = document.getElementById('sendBtn');
        const suggestions = document.getElementById('suggestions');

        function addMessage(text, isUser) {
            const div = document.createElement('div');
            div.className = 'message ' + (isUser ? 'user' : 'bot');
            div.textContent = text;
            chatContainer.appendChild(div);
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }

        function showTyping(show) {
            let indicator = document.querySelector('.typing-indicator');
            if (!indicator) {
                indicator = document.createElement('div');
                indicator.className = 'typing-indicator';
                indicator.innerHTML = '<span></span><span></span><span></span>';
                chatContainer.appendChild(indicator);
            }
            indicator.classList.toggle('show', show);
            if (show) chatContainer.scrollTop = chatContainer.scrollHeight;
        }

        function askSuggestion(el) {
            userInput.value = el.textContent;
            sendMessage();
        }

        async function sendMessage() {
            const text = userInput.value.trim();
            if (!text) return;

            addMessage(text, true);
            userInput.value = '';
            sendBtn.disabled = true;
            suggestions.style.display = 'none';
            showTyping(true);

            try {
                const res = await fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: text, session_id: sessionId })
                });
                const data = await res.json();
                showTyping(false);
                addMessage(data.response, false);
            } catch (err) {
                showTyping(false);
                addMessage('죄송합니다. 오류가 발생했습니다. 다시 시도해주세요.', false);
            }
            sendBtn.disabled = false;
            userInput.focus();
        }
    </script>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE, post_count=len(LINKEDIN_POSTS))


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    session_id = data.get("session_id", "default")

    if session_id not in conversations:
        conversations[session_id] = []

    conversations[session_id].append({"role": "user", "content": user_message})

    # Keep last 20 messages for context
    recent_messages = conversations[session_id][-20:]

    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=recent_messages,
        )
        assistant_message = response.content[0].text
    except Exception as e:
        assistant_message = f"죄송합니다. API 호출 중 오류가 발생했습니다: {str(e)}"

    conversations[session_id].append(
        {"role": "assistant", "content": assistant_message}
    )

    return jsonify({"response": assistant_message})


@app.route("/posts")
def posts():
    return jsonify(
        {
            "profile": PROFILE_INFO,
            "company": COMPANY_INFO,
            "posts": LINKEDIN_POSTS,
            "total": len(LINKEDIN_POSTS),
        }
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
