# 🚀 Render Deployment - Quick Start

Deploy your backend to Render in 5 minutes!

## ⚡ Quick Steps

### 1. Create Account & Service
1. Go to [render.com](https://render.com) → Sign in with GitHub
2. **New +** → **Web Service**
3. Connect repository: `PrathamJain2002/DataVinci`

### 2. Configure Service

**Settings:**
- **Name:** `campaign-analytics-api`
- **Root Directory:** `backend`
- **Runtime:** `Python 3`

**Build Command:**
```bash
pip install -r requirements.txt
```

**Start Command:**
```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

**Environment Variables:**
- `ALLOWED_ORIGINS` = `http://localhost:3000,https://*.vercel.app`

### 3. Deploy & Seed Database

1. Click **"Create Web Service"**
2. Wait for deployment (2-5 minutes)
3. Open **Shell** tab
4. Run: `python backend/seed.py`

### 4. Get Your URL

Your backend URL: `https://your-service-name.onrender.com`

✅ **Done!** Test it:
- Health: `https://your-service-name.onrender.com/health`
- API Docs: `https://your-service-name.onrender.com/docs`
- Campaigns: `https://your-service-name.onrender.com/campaigns`

---

## 🔗 Connect Frontend

In Vercel, update environment variable:
- `NEXT_PUBLIC_API_URL` = `https://your-service-name.onrender.com`

Then update Render's `ALLOWED_ORIGINS` to include your Vercel URL.

---

## ⚠️ Free Tier Note

Render's free tier spins down after 15 minutes of inactivity. First request after spin-down takes ~30-50 seconds.

**Solution:** Upgrade to Starter ($7/mo) for always-on, or use a ping service to keep it awake.

---

## 📖 Full Guide

See **[RENDER_DEPLOYMENT.md](./RENDER_DEPLOYMENT.md)** for complete instructions with troubleshooting.

---

**That's it! Your backend is live on Render! 🎉**

