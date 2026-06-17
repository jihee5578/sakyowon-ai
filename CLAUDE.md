# 나의 작업 컨텍스트 — 주민역량강화를 위한 망남마을 청년층의 선진지 견학

## 내가 누구
- 이름: 김지희
- 역할: 망남앵커조직 실무자, 기획 및 실행 담당
- 일정: 2026년 7월 중 2박 3일

## 우리가 만들 5종 자산 (내가 직접 손에 들 것)
1. GitHub 레포
2. 위키 URL (옵시디언 + Quartz + CF Pages)
3. Supabase DB 테이블
4. 한 페이지 사이트 URL
5. 작동하는 자동화 1개

## 전체 프로그램 (참조)
https://wiki.poomasi.org/주민역량강화/선진지 견학 2박 3일

## 너(Claude)에게 부탁하는 톤
- 한국어로
- 한 번에 1개 단계만, 명령어는 코드블록
- 모르면 "모른다" 먼저 말해라
- 내가 "다음" 하기 전엔 다음 단계로 안 넘어감
- 내 폴더 밖 파일은 건드리지 마라
- 정답 기계 아닌 동료처럼, 내가 왜 막혔는지 짚어라

## 지금 단계
M1 진행 중

## 내 현장 문제 (M6 자동화에서 씀)
[본인이 한 줄로 적어두기]## "정리해" 명령어 정의
- 핸드오버 문서 작성
- 스킬 & 레슨 정리
- 위키 배포 (M3 환경 구축 후 자동수행 가능)

## M1 핸드오버 — 2026-06-16

### 완료한 것
- Windows 11 Pro 환경 확인
- Git 2.54.0 설치
- Node.js v24.16.0 설치
- VSCode 1.124.2 설치
- PowerShell 7.6.2 설치
- 옵시디언 설치
- sakyowon-ai 폴더 생성
- CLAUDE.md 작성
- Claude Code v2.1.178 설치 & 로그인
- CLAUDE.md 컨텍스트 확인 완료

### 스킬 & 레슨
- PowerShell 5.1에서 `||` 문법 안 됨 → PowerShell 7로 업그레이드 필요
- Claude Code 실행은 `pwsh` → `cd ~/sakyowon-ai` → `claude` 순서
- CLAUDE.md가 있으면 Claude Code가 컨텍스트를 자동으로 읽음

### 다음 단계
- M2: GitHub 레포 생성## M2 핸드오버 — 2026-06-16

### 완료한 것
- GitHub 계정 생성 (jihee5578)
- sakyowon-ai 레포 생성 (Public)
- git init + 첫 커밋 (aa7fff0)
- git remote add origin 연결
- PAT 발급 (90일, repo 권한)
- push 완료 → README.md + CLAUDE.md GitHub에 올라감

### 스킬 & 레슨
- git commit 전에 user.email / user.name 설정 필요
- PAT는 생성 직후 한 번만 보임 → 메모장에 저장해둘 것
- push 명령어: `git push https://유저명:토큰@github.com/유저명/레포.git master`
- GitHub는 한국어 지원됨 (설정에서 변경 가능)

### 다음 단계
- M3: 옵시디언 + Quartz + CF Pages → 위키 URL 만들기

## 지금 단계
M3 진행 예정## M3 핸드오버 — 2026-06-17

### 완료한 것
- Quartz v5 시도 → 불안정으로 v4로 다운그레이드
- Quartz v4.5.2 fork (jihee5578/quartz) + clone
- npm install 완료
- content/index.md 생성 (망남마을 선진지 견학 위키)
- 로컬 미리보기 확인 (localhost:8080)
- GitHub push (v4 브랜치)
- Cloudflare Pages 배포 완료
- 위키 URL: https://quartz-1jz.pages.dev

### 스킬 & 레슨
- Quartz v5는 Node 24와 호환 안 됨 → v4 사용
- PAT에 repo + workflow 두 권한 필요 (workflow가 repo 포함)
- CF Pages는 Workers & Pages → Get started → Import Git repository 순서
- Production branch를 v4로 설정해야 함
- Build command: npx quartz build / Output directory: public

### 다음 단계
- M4: Supabase DB 테이블 만들기

## 지금 단계
M4 진행 예정## M4 핸드오버 — 2026-06-17

### 완료한 것
- Supabase 가입 (5578@sakyowon.co.kr)
- 프로젝트 생성: mangnam-wiki (ap-south-1 Mumbai)
- Project ID: bmhionfbvjbshynveryu
- notes 테이블 생성 (id uuid PK, title text, body text, created_at timestamptz)
- RLS 켜기 + anon SELECT 정책 설정
- 테스트 데이터 1줄 INSERT
- curl로 REST GET 확인 → JSON 응답 성공

### 스킬 & 레슨
- Supabase 비밀번호는 대문자 필수
- anon 키 = 공개 OK, service_role 키 = 절대 노출 금지
- curl GET: apikey + Authorization Bearer 헤더 둘 다 필요
- RLS 없으면 빈 배열 [] 반환됨
- anon 키 위치: Settings → API Keys → Legacy anon, service_role API keys

### 프로젝트 정보
- URL: https://bmhionfbvjbshynveryu.supabase.co
- anon 키: 메모장에 저장됨

### 다음 단계
- M5: 한 페이지 사이트 URL 만들기

## 지금 단계
M5 진행 예정## M5 핸드오버 — 2026-06-17

### 완료한 것
- Claude Code로 index.html 생성 (망남마을 청년층 선진지 견학 2026)
- sakyowon-ai 레포에 push
- Cloudflare Pages 연결 (sakyowon-ai 레포 / master 브랜치)
- 한 페이지 사이트 배포 완료
- 사이트 URL: https://sakyowon-ai-ebx.pages.dev

### 스킬 & 레슨
- CF Pages는 첫 커밋만 배포할 수 있음 → 빈 커밋으로 재배포 트리거 가능
- `git commit --allow-empty -m "trigger"` → push 하면 CF Pages 자동 재배포
- Build command / Output directory 비워두면 HTML 파일 그대로 배포됨
- index.html 하나로 CSS 포함한 완성된 페이지 가능

### 다음 단계
- M6: 작동하는 자동화 1개 만들기

## 지금 단계
M6 진행 예정