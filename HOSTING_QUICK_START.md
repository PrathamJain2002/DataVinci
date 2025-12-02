# 🚀 Quick Hosting Guide

## TL;DR - Get Your App Live in 10 Minutes

### 1️⃣ Deploy Backend (Railway) - 5 minutes

1. Go to [railway.app](https://railway.app) → Sign in with GitHub
2. **New Project** → **Deploy from GitHub repo** → Select `DataVinci`
3. In **Settings**:
   - **Root Directory:** `backend`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Open **Railway Shell** → Run: `python backend/seed.py`
5. Copy your Railway URL (e.g., `https://your-app.up.railway.app`)

### 2️⃣ Deploy Frontend (Vercel) - 5 minutes

1. Go to [vercel.com](https://vercel.com) → Sign in with GitHub
2. **Add New Project** → Import `DataVinci` repository
3. Configure:
   - **Root Directory:** `frontend`
   - **Framework:** Next.js (auto-detected)
4. **Environment Variables:**
   - Add: `NEXT_PUBLIC_API_URL` = `https://your-app.up.railway.app` (your Railway URL)
5. Click **Deploy**

### 3️⃣ Update CORS (Railway) - 2 minutes

1. In Railway, go to **Variables** tab
2. Add environment variable:
   - **Name:** `ALLOWED_ORIGINS`
   - **Value:** `http://localhost:3000,https://your-app.vercel.app,https://*.vercel.app`
3. Railway will auto-redeploy

### ✅ Done!

- **Frontend:** `https://your-app.vercel.app`
- **Backend:** `https://your-app.up.railway.app`
- **API Docs:** `https://your-app.up.railway.app/docs`

---

## 📖 Need More Details?

See **[DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)** for complete step-by-step instructions with screenshots and troubleshooting.

---

## 🎯 What You Get

✅ **Free hosting** on both platforms  
✅ **Automatic HTTPS** (SSL certificates)  
✅ **Auto-deploy** on every git push  
✅ **Custom domains** (optional)  
✅ **Production-ready** infrastructure  

---

**That's it! Your app is live! 🎉**

