# 🚀 Complete Deployment Guide

Step-by-step instructions to deploy your Campaign Analytics Dashboard to production.

## 📋 Prerequisites

- GitHub account (you already have the code pushed)
- Vercel account (free) - for frontend
- Railway account (free tier available) - for backend
- Basic understanding of environment variables

---

## 🎯 Deployment Overview

1. **Backend (FastAPI)** → Railway
2. **Frontend (Next.js)** → Vercel
3. **Connect them** via environment variables

---

## 🔧 Part 1: Deploy Backend to Railway

### Step 1: Create Railway Account

1. Go to [railway.app](https://railway.app)
2. Click **"Start a New Project"** or **"Login"**
3. Sign in with your **GitHub account** (recommended)

### Step 2: Create New Project

1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Find and select your repository: **`PrathamJain2002/DataVinci`**
4. Railway will detect it's a Python project

### Step 3: Configure Backend Service

1. Railway will create a service automatically
2. Go to your service → **Settings**
3. Set the following:

   **Root Directory:**
   ```
   backend
   ```

   **Start Command:**
   ```
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

### Step 4: Set Environment Variables (Optional)

Railway automatically sets `PORT`, but you can add custom ones if needed:
- Go to **Variables** tab
- Add any custom environment variables if your app needs them

### Step 5: Initialize Database

1. Go to your service → **Deployments** tab
2. Click on the latest deployment
3. Click **"View Logs"** or open the **Railway Shell**
4. Run the seeder:
   ```bash
   cd backend
   python seed.py
   ```
   Or if you're in the root:
   ```bash
   python backend/seed.py
   ```

### Step 6: Get Your Backend URL

1. Go to your service → **Settings** → **Networking**
2. Railway will provide a URL like: `https://your-app-name.up.railway.app`
3. **Copy this URL** - you'll need it for the frontend!

### Step 7: Test Your Backend

Visit these URLs in your browser:
- **API Health:** `https://your-app-name.up.railway.app/health`
- **API Docs:** `https://your-app-name.up.railway.app/docs`
- **Campaigns:** `https://your-app-name.up.railway.app/campaigns`

✅ **Backend is now live!**

---

## 🎨 Part 2: Deploy Frontend to Vercel

### Step 1: Create Vercel Account

1. Go to [vercel.com](https://vercel.com)
2. Click **"Sign Up"** or **"Login"**
3. Sign in with your **GitHub account** (recommended)

### Step 2: Import Project

1. Click **"Add New..."** → **"Project"**
2. Find and select your repository: **`PrathamJain2002/DataVinci`**
3. Click **"Import"**

### Step 3: Configure Frontend

1. **Framework Preset:** Next.js (auto-detected)
2. **Root Directory:** 
   ```
   frontend
   ```
   (Click "Edit" next to Root Directory and set it to `frontend`)

3. **Build Command:** (auto-filled)
   ```
   npm run build
   ```

4. **Output Directory:** (auto-filled)
   ```
   .next
   ```

5. **Install Command:** (auto-filled)
   ```
   npm install
   ```

### Step 4: Set Environment Variables

**This is crucial!** You need to connect the frontend to your Railway backend.

1. In the **Environment Variables** section, click **"Add"**
2. Add this variable:
   - **Name:** `NEXT_PUBLIC_API_URL`
   - **Value:** `https://your-app-name.up.railway.app` (your Railway backend URL)
   - **Environment:** Production, Preview, Development (select all)

3. Click **"Save"**

### Step 5: Deploy

1. Click **"Deploy"**
2. Wait 2-3 minutes for the build to complete
3. Vercel will provide you with a URL like: `https://your-app.vercel.app`

### Step 6: Test Your Frontend

Visit your Vercel URL:
- **Home:** `https://your-app.vercel.app`
- **Campaigns:** `https://your-app.vercel.app/campaigns`

✅ **Frontend is now live!**

---

## 🔗 Part 3: Update CORS in Backend

### Why This is Needed

Your frontend (Vercel) needs permission to access your backend (Railway). This is done via CORS.

### Update Backend CORS Settings

1. Go to your Railway project
2. Open the **Railway Shell** or use the **Code** tab
3. Edit `backend/main.py`

   Find this section:
   ```python
   origins = [
       "http://localhost:3000",
       "http://localhost:3001",
       "https://*.vercel.app",
       "*",  # Allow all origins (for development)
   ]
   ```

   Replace it with:
   ```python
   origins = [
       "http://localhost:3000",  # Local development
       "https://your-app.vercel.app",  # Your Vercel production URL
       "https://your-app-git-*.vercel.app",  # Vercel preview deployments
       "https://*.vercel.app",  # All Vercel previews
   ]
   ```

   **Or use environment variables (recommended):**
   ```python
   import os
   
   # Get allowed origins from environment variable, fallback to defaults
   allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000,https://*.vercel.app").split(",")
   
   origins = [origin.strip() for origin in allowed_origins]
   ```

4. Commit and push the changes:
   ```bash
   git add backend/main.py
   git commit -m "Update CORS for production"
   git push
   ```

5. Railway will automatically redeploy with the new CORS settings

---

## ✅ Part 4: Verify Everything Works

### Test Checklist

1. **Backend Health Check:**
   - Visit: `https://your-railway-url.up.railway.app/health`
   - Should return: `{"status":"healthy"}`

2. **Backend API:**
   - Visit: `https://your-railway-url.up.railway.app/campaigns`
   - Should return JSON with 10 campaigns

3. **Frontend Home:**
   - Visit: `https://your-app.vercel.app`
   - Should show the home page

4. **Frontend Campaigns:**
   - Visit: `https://your-app.vercel.app/campaigns`
   - Should display the campaigns table with data
   - Filter dropdown should work
   - No CORS errors in browser console

---

## 🔄 Part 5: Future Updates

### How to Update Your Deployment

1. **Make changes** to your code locally
2. **Test locally** to ensure everything works
3. **Commit and push** to GitHub:
   ```bash
   git add .
   git commit -m "Your update message"
   git push
   ```
4. **Automatic Deployment:**
   - Railway will automatically redeploy your backend
   - Vercel will automatically redeploy your frontend
   - Both platforms watch your GitHub repo for changes

---

## 🐛 Troubleshooting

### Backend Issues

**Problem:** Backend not responding
- **Solution:** Check Railway logs → Deployments → View Logs
- Check if database was seeded: Run `python seed.py` in Railway Shell

**Problem:** CORS errors
- **Solution:** Update CORS origins in `backend/main.py` to include your Vercel URL

**Problem:** Database errors
- **Solution:** Run `python seed.py` in Railway Shell to initialize database

### Frontend Issues

**Problem:** "Failed to fetch" error
- **Solution:** 
  1. Check `NEXT_PUBLIC_API_URL` environment variable in Vercel
  2. Verify backend URL is correct
  3. Check CORS settings in backend

**Problem:** Build fails
- **Solution:** Check Vercel build logs for errors
- Ensure all dependencies are in `package.json`

**Problem:** Environment variable not working
- **Solution:** 
  1. Variables starting with `NEXT_PUBLIC_` are exposed to browser
  2. Redeploy after adding/changing environment variables
  3. Clear browser cache

---

## 📊 Monitoring & Logs

### Railway (Backend)
- **Logs:** Service → Deployments → View Logs
- **Metrics:** Service → Metrics (CPU, Memory, Network)

### Vercel (Frontend)
- **Logs:** Project → Deployments → Click on deployment → View Logs
- **Analytics:** Project → Analytics (page views, performance)

---

## 💰 Cost Information

### Free Tiers

**Railway:**
- $5 free credit per month
- Enough for small projects
- Pay-as-you-go after free credit

**Vercel:**
- Free tier includes:
  - Unlimited personal projects
  - 100GB bandwidth
  - Automatic HTTPS
  - Preview deployments

Both platforms are **free to start** and perfect for this project!

---

## 🎉 You're Done!

Your Campaign Analytics Dashboard is now live on the internet! 🚀

- **Frontend:** `https://your-app.vercel.app`
- **Backend:** `https://your-railway-url.up.railway.app`
- **API Docs:** `https://your-railway-url.up.railway.app/docs`

Share your deployed app with others and enjoy! 🎊

---

## 📚 Additional Resources

- [Railway Documentation](https://docs.railway.app)
- [Vercel Documentation](https://vercel.com/docs)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
- [Next.js Deployment](https://nextjs.org/docs/deployment)

---

**Need Help?** Check the logs, verify environment variables, and ensure CORS is properly configured!

