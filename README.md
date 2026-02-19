# Personal Web Project

<span style='font-size:24px;'>**I use google's antigravity to generate the structure of this README file.**</span>

## Project Architecture (MTV Logic)


<span style='font-size:24px;'>Django use **MTV(Model-Template-View)** structure as its main design pattern.</span>

### 1. **Models (Data structure of each sheet in database)**
- **位置:** `core/models.py`
- **職責:** 定義資料庫的結構。
- **範例:** `Comment` 類別代表了資料庫中的一張表，包含 `author` (作者)、`content` (內容) 和 `created_at` (建立時間) 等欄位。

### 2. **Templates (Website's appearance)**
- **位置:** `core/templates/core/home.html` (及 `config/settings.py` 中設定的 `templates` 目錄)
- **職責:** 定義使用者看到的 HTML 頁面結構。
- **範例:** `home.html` 是這個網站的首頁模板。Views 會將資料（Context）傳遞給它，它再利用 Django Template Language (DTL) 動態渲染出最終的 HTML。

### 3. **Views (Transfer the website's static html file according to ruls you setting in this file)**
- **位置:** `core/views.py`
- **職責:** 處理請求的核心邏輯。接收使用者的請求，決定要讀取什麼資料、做什麼處理，最後回傳回應（HTML 頁面或 JSON 資料）。
- **範例:**
    - `home(request)`: 負責渲染首頁模板。
    - `comments_api(request)`: 負責處理留言的 API 邏輯（取得清單、新增留言、刪除留言）。

---

## <span style='font-size:24px;'>The Request-Response Flow</span>


Ex. **Create a new messege (API POST Request)**

1.  **URL Request:**
    使用者在前端填寫表單並送出，瀏覽器發送一個 `POST` 請求到網址：`/api/comments/`。

2.  **`config/urls.py` (專案入口路由):**
    Django 收到請求，首先檢查根目錄的 `urls.py`。
    它看到 `path('', include('core.urls'))` 這行設定（雖然這行是掛載根目錄，但在我們的設定中 `/api` 路徑通常會由 `core.urls` 進一步處理，或者我們直接在 `config/urls.py` 分流）。
    根據本專案設定，`config/urls.py` 包含 `path('', include('core.urls'))`，這表示所有請求都會轉發給 `core` App 處理。

3.  **`core/urls.py` (App 路由):**
    請求進入 `core` App 的路由設定。
    Django 匹配到 `path('api/comments/', views.comments_api)`。
    這告訴 Django：請執行 `views.py` 裡的 `comments_api` 函式。

4.  **`core/views.py` (邏輯處理):**
    `comments_api(request)` 函式被呼叫。
    - 函式檢查 `request.method` 是否為 `"POST"`。
    - 讀取 `request.body` 中的 JSON 資料（作者、內容）。
    - 呼叫 `Comment.objects.create(...)` 將資料寫入資料庫。
    - 回傳一個 `JsonResponse({"status": "ok"})`。

5.  **Running Response:**
    Django 將 `JsonResponse` 轉換成標準的 HTTP Response，回傳給使用者的瀏覽器，前端 JavaScript 接收到回應後更新畫面。

---

## Key Dependencies

在 `requirements.txt` 中，這三個套件扮演著關鍵角色：

1.  **Django**
    - **角色:** 核心網頁框架。
    - **功能:** 提供上述的 MTV 架構、路由系統、ORM (資料庫操作)、以及強大的管理後台。它是整個專案的基礎。

2.  **python-dotenv**
    - **角色:** 環境變數管理。
    - **功能:** 讓我們能從 `.env` 檔案中讀取設定（如 `SECRET_KEY`, `DEBUG` 模式, 資料庫連線字串）。這對於保護敏感資訊和區分開發/生產環境至關重要（參考 `config/settings.py` 裡的 `load_dotenv`）。

3.  **whitenoise**
    - **角色:** 靜態檔案服務 (Static Files Serving)。
    - **功能:** 在部署環境（如 Render）中，Django 本身不擅長處理 CSS/JS/圖片等靜態檔案。WhiteNoise 允許 Python 網頁應用程式自行高效地服務這些檔案，簡化了部署過程。

---

## Learning Milestones

根據這個專案的結構，建議你的學習順序如下：

### Phase 1: 基礎架構 (The Basics)
- **目標:** 理解「網址 -> 函式 -> 畫面」的流程。
- **行動:**
    1. 修改 `core/views.py` 的 `home` 函式，試著傳遞一個變數（例如 `context = {'message': 'Hello Django'}`）。
    2. 修改 `core/templates/core/home.html` 來顯示這個變數 (`{{ message }}`)。
    3. 觀察瀏覽器畫面的變化。

### Phase 2: 資料庫與模型 (Models & ORM)
- **目標:** 學會如何定義和操作資料。
- **行動:**
    1. 在 `core/models.py` 中新增一個簡單的欄位到 `Comment` 模型（例如 `is_approved = models.BooleanField(default=True)`）。
    2. 執行 `python manage.py makemigrations` 和 `python manage.py migrate` 來更新資料庫。
    3. 使用 `python manage.py shell` 練習用指令新增和查詢 Comment。

### Phase 3: API 開發 (Views Logic)
- **目標:** 理解後端 API 如何運作。
- **行動:**
    1. 研究 `core/views.py` 中的 `comments_api` 函式。
    2. 試著新增一個功能：讓 API 支援「修改留言」 (`PUT` request)。你需要解析 JSON 資料並更新現有的 `Comment` 物件。

### Phase 4: 部署與設定 (Configuration)
- **目標:** 了解專案如何上線。
- **行動:**
    1. 閱讀 `config/settings.py`，了解 `DEBUG`、`ALLOWED_HOSTS` 和 `DATABASES` 是如何透過環境變數動態設定的。
    2. 理解為什麼我們需要 `whitenoise` 來處理靜態檔案。


# <span style='font-size:24px;'>Reference:</span>

- <span style='font-size:24px;'>[Django in 2024: Django架構深度解析](https://ithelp.ithome.com.tw/m/articles/10350252)</span>
