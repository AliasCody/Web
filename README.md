# <span style='font-size:24px;'>整體檔案架構 Project Architecture</span>


```bash
PERSONAL_WEB/
├── config/                    # 專案層設定 (Project Configuration)
│   ├── __init__.py
│   ├── asgi.py                # ASGI entry point (for async / modern servers)
│   ├── settings.py            # 全域設定 (Application Configuration)
│   ├── urls.py                # Root URL dispatcher
│   └── wsgi.py                # WSGI entry point (for production server)
│
├── core/                      # 主要應用程式 (Main App)
│   ├── migrations/            # Database migrations
│   │   └── __init__.py
│   ├── static/                # App-level static files
│   │   └── core/
│   │       └── style.css
│   ├── templates/             # App-level templates
│   │   └── core/
│   │       └── home.html
│   ├── admin.py               # Django admin configuration
│   ├── apps.py
│   ├── models.py              # Database models
│   ├── tests.py
│   ├── urls.py                # App URL dispatcher
│   └── views.py               # View / business logic
│
├── requirements.txt            # 
├── render.yaml (Procfile)      # 
├── .gitignore                  # 
├── db.sqlite3                  
└── manage.py

```

- `__pycache__` 為 Python 自動產生的 bytecode 快取資料夾，
用於提升程式重複執行時的效能，屬於執行期產物，就不丟進repo。


<span style='font-size:24px;'>Reference:</span> 

<span style='font-size:24px;'>- [DAY 26 Django 簡易入門教學(三)-建立 Django 專案與 APP](https://ithelp.ithome.com.tw/m/articles/10252130)</span>