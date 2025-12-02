# Campaign Analytics Dashboard

A full-stack Campaign Analytics Dashboard built with Next.js, React, TailwindCSS, FastAPI, and SQLite. This is a simplified version of Grippi's Campaign Analytics Dashboard.

## 🏗️ Project Structure

```
DataVinci/
├── frontend/                 # Next.js 14 frontend application
│   ├── app/                 # App Router pages
│   │   ├── campaigns/      # Campaigns page
│   │   ├── layout.tsx      # Root layout
│   │   ├── page.tsx        # Home page
│   │   └── globals.css     # Global styles
│   ├── components/         # Reusable React components
│   │   ├── CampaignTable.tsx
│   │   ├── FilterDropdown.tsx
│   │   └── Layout.tsx
│   ├── package.json
│   └── tsconfig.json
├── backend/                 # FastAPI backend application
│   ├── main.py             # FastAPI app entry point
│   ├── database.py         # Database configuration
│   ├── models.py           # SQLAlchemy models
│   ├── schemas.py          # Pydantic schemas
│   ├── seed.py             # Database seeder
│   ├── routers/            # API routers
│   │   └── campaigns.py    # Campaign endpoints
│   └── requirements.txt    # Python dependencies
└── database.sql            # SQL script for database setup
```

## 🚀 Features

- **Frontend:**
  - Responsive dashboard UI with TailwindCSS
  - Campaign table with sorting and filtering
  - Status badges (Active/Paused) with color coding
  - Currency formatting for cost values
  - Loading and error states
  - TypeScript for type safety

- **Backend:**
  - RESTful API with FastAPI
  - SQLite database
  - Pydantic models for validation
  - CORS enabled for frontend integration

## 📋 Prerequisites

- **Node.js** 18+ and npm/yarn
- **Python** 3.9+
- **Git**

## 🛠️ Local Development Setup

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Create environment file:**
   ```bash
   cp .env.local.example .env.local
   ```

4. **Update `.env.local` with your backend URL:**
   ```env
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

5. **Run development server:**
   ```bash
   npm run dev
   # or
   yarn dev
   ```

6. **Open browser:**
   Navigate to [http://localhost:3000](http://localhost:3000)

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment (recommended):**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize database:**
   ```bash
   # Run the seeder script to create tables and insert sample data
   python seed.py
   ```

   Alternatively, you can use the SQL script:
   ```bash
   sqlite3 campaigns.db < ../database.sql
   ```

5. **Run FastAPI server:**
   ```bash
   uvicorn main:app --reload --port 8000
   ```

6. **Verify API is running:**
   - API: [http://localhost:8000](http://localhost:8000)
   - API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Health Check: [http://localhost:8000/health](http://localhost:8000/health)

## 🌐 Deployment

### Frontend Deployment (Vercel)

1. **Install Vercel CLI (optional):**
   ```bash
   npm i -g vercel
   ```

2. **Deploy via Vercel Dashboard:**
   - Go to [vercel.com](https://vercel.com)
   - Sign in with GitHub
   - Click "New Project"
   - Import your repository
   - Set root directory to `frontend`
   - Add environment variable:
     - `NEXT_PUBLIC_API_URL` = Your Railway backend URL (e.g., `https://your-app.railway.app`)

3. **Deploy via CLI:**
   ```bash
   cd frontend
   vercel
   ```

4. **Configure Environment Variables:**
   - In Vercel dashboard, go to Project Settings → Environment Variables
   - Add `NEXT_PUBLIC_API_URL` with your Railway backend URL

### Backend Deployment (Railway)

1. **Install Railway CLI (optional):**
   ```bash
   npm i -g @railway/cli
   ```

2. **Deploy via Railway Dashboard:**
   - Go to [railway.app](https://railway.app)
   - Sign in with GitHub
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Set root directory to `backend`

3. **Configure Railway:**
   - Go to your service → Settings
   - Set **Start Command:**
     ```
     uvicorn main:app --host 0.0.0.0 --port $PORT
     ```
   - Add environment variable (if needed):
     - `PORT` (usually set automatically by Railway)

4. **Run Database Migration:**
   - In Railway, go to your service → Deployments
   - Open the shell/console
   - Run:
     ```bash
     python seed.py
     ```

5. **Get your Railway URL:**
   - Railway will provide a URL like: `https://your-app.railway.app`
   - Use this URL in your frontend's `NEXT_PUBLIC_API_URL`

### CORS Configuration

The backend is already configured with CORS middleware. For production:

1. **Update `backend/main.py`:**
   ```python
   # Replace the origins list with your Vercel domain
   origins = [
       "https://your-app.vercel.app",
       "https://your-app-git-main.vercel.app",  # Preview deployments
   ]
   ```

2. **Or use environment variable:**
   ```python
   import os
   origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")
   ```

## 📊 API Endpoints

### GET /campaigns

Returns a list of all campaigns.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Summer Sale 2024",
    "status": "Active",
    "clicks": 15234,
    "cost": 3421.50,
    "impressions": 125000
  },
  ...
]
```

## 🗄️ Database Schema

### campaigns Table

| Column      | Type    | Description                    |
|-------------|---------|--------------------------------|
| id          | INTEGER | Primary key (auto-increment)   |
| name        | TEXT    | Campaign name                  |
| status      | TEXT    | Status: "Active" or "Paused"   |
| clicks      | INTEGER | Number of clicks               |
| cost        | REAL    | Cost in dollars                |
| impressions | INTEGER | Number of impressions          |

## 🧪 Testing

### Test Frontend Locally

1. Start backend: `cd backend && uvicorn main:app --reload`
2. Start frontend: `cd frontend && npm run dev`
3. Navigate to [http://localhost:3000/campaigns](http://localhost:3000/campaigns)

### Test API Endpoint

```bash
# Using curl
curl http://localhost:8000/campaigns

# Or visit in browser
http://localhost:8000/docs
```

## 📝 Environment Variables

### Frontend (.env.local)

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### Backend

No environment variables required for local development. For production, you may want to add:
- `ALLOWED_ORIGINS`: Comma-separated list of allowed CORS origins

## 🐛 Troubleshooting

### Frontend Issues

- **API connection errors:** Check that `NEXT_PUBLIC_API_URL` is set correctly
- **Build errors:** Ensure all dependencies are installed (`npm install`)
- **TypeScript errors:** Run `npm run lint` to check for issues

### Backend Issues

- **Database not found:** Run `python seed.py` to create the database
- **Port already in use:** Change the port: `uvicorn main:app --port 8001`
- **CORS errors:** Verify CORS origins in `main.py` match your frontend URL

## 📚 Tech Stack

- **Frontend:**
  - Next.js 14 (App Router)
  - React 18
  - TypeScript
  - TailwindCSS

- **Backend:**
  - FastAPI
  - SQLAlchemy
  - Pydantic
  - SQLite

- **Deployment:**
  - Vercel (Frontend)
  - Railway (Backend)

## 📄 License

This project is created for educational purposes.

## 👨‍💻 Development Notes

- All code is commented for clarity
- Follows best practices for folder structure
- Production-ready and scalable
- Easy to understand for junior developers

---

**Happy Coding! 🚀**

