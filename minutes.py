import os
import sys
from datetime import date
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()

if len(sys.argv) < 2:
    print("사용법: python minutes.py <메모파일.txt>")
    sys.exit(1)

filepath = sys.argv[1]
if not os.path.exists(filepath):
    print(f"파일을 찾을 수 없어요: {filepath}")
    sys.exit(1)

with open(filepath, "r", encoding="utf-8") as f:
    raw = f.read().strip()

if not raw:
    print("파일이 비어 있어요. 종료합니다.")
    sys.exit(1)

response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": (
            "다음 회의 메모를 마크다운 회의록으로 정리해줘.\n"
            "섹션: 날짜, 참석자, 안건, 결정사항, 다음 할 일\n"
            "없는 항목은 '미기재'로 표시.\n\n"
            f"{raw}"
        )
    }]
)

minutes = response.content[0].text
filename = f"meeting_{date.today().strftime('%Y%m%d')}.md"

with open(filename, "w", encoding="utf-8") as f:
    f.write(minutes)

print(f"\n저장 완료 → {filename}")
print("\n" + "─" * 40)
print(minutes)
