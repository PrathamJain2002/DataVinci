# 🚀 Deploy Backend to Render

Complete guide to deploy your FastAPI backend to Render.com

## 📋 Prerequisites

- GitHub account (your code is already pushed)
- Render account (free tier available)
- 10 minutes of time

---

## 🎯 Step-by-Step Guide

### Step 1: Create Render Account

1. Go to [render.com](https://render.com)
2. Click **"Get Started for Free"** or **"Sign In"**
3. Sign in with your **GitHub account** (recommended for easy deployment)

### Step 2: Create New Web Service

1. From your Render dashboard, click **"New +"**
2. Select **"Web Service"**
3. Connect your GitHub account if not already connected
4. Find and select your repository: **`PrathamJain2002/DataVinci`**
5. Click **"Connect"**

### Step 3: Configure Your Service

Fill in the following settings:

#### Basic Settings

- **Name:** `campaign-analytics-api` (or any name you prefer)
- **Region:** Choose closest to you (e.g., `Oregon (US West)`)
- **Branch:** `main` (or `master` if that's your default branch)
- **Root Directory:** `backend`

#### Build & Deploy

- **Runtime:** `Python 3`
- **Build Command:**
  ```bash
  pip install -r requirements.txt
  ```
- **Start Command:**
  ```bash
  uvicorn main:app --host 0.0.0.0 --port $PORT
  ```

#### Environment Variables

Click **"Add Environment Variable"** and add:

1. **ALLOWED_ORIGINS** (for CORS)
   - **Key:** `ALLOWED_ORIGINS`
   - **Value:** `http://localhost:3000,https://*.vercel.app`
   - (You'll update this with your Vercel URL after deploying frontend)

2. **PYTHON_VERSION** (optional, but recommended)
   - **Key:** `PYTHON_VERSION`
   - **Value:** `3.11.0` (or `3.12.0`)

### Step 4: Deploy

1. Scroll down and click **"Create Web Service"**
2. Render will start building and deploying your service
3. This takes 2-5 minutes
4. You'll see build logs in real-time

### Step 5: Initialize Database

After deployment completes:

1. Go to your service dashboard
2. Click on **"Shell"** tab (or **"Open Shell"**)
3. Run the database seeder:
   ```bash
   cd backend
   python seed.py
   ```
   Or if you're already in the root:
   ```bash
   python backend/seed.py
   ```

4. You should see: `Successfully seeded 10 campaigns!`

### Step 6: Get Your Backend URL

1. In your service dashboard, you'll see your service URL
2. It will look like: `https://campaign-analytics-api.onrender.com`
3. **Copy this URL** - you'll need it for the frontend!

### Step 7: Test Your Backend

Visit these URLs in your browser:

- **API Root:** `https://your-service-name.onrender.com/`
- **Health Check:** `https://your-service-name.onrender.com/health`
- **API Documentation:** `https://your-service-name.onrender.com/docs`
- **Campaigns Endpoint:** `https://your-service-name.onrender.com/campaigns`

✅ **Backend is now live on Render!**

---

## 🔗 Connect Frontend (Vercel)

### Update Frontend Environment Variable

1. Go to your Vercel project
2. Go to **Settings** → **Environment Variables**
3. Update `NEXT_PUBLIC_API_URL`:
   - **Value:** `https://your-service-name.onrender.com` (your Render URL)
4. Redeploy your frontend (or it will auto-deploy)

### Update CORS in Render

1. Go to your Render service → **Environment** tab
2. Update the `ALLOWED_ORIGINS` variable:
   - **Value:** `http://localhost:3000,https://your-app.vercel.app,https://*.vercel.app`
3. Render will automatically redeploy with new settings

---

## ⚙️ Render-Specific Configuration

### Automatic Deploys

Render automatically deploys when you push to your connected branch (usually `main`).

### Manual Deploy

1. Go to your service dashboard
2. Click **"Manual Deploy"** → **"Deploy latest commit"**

### Environment Variables

All environment variables are set in:
- Service → **Environment** tab
- Add/Edit/Delete variables as needed

### Logs

View logs in real-time:
- Service → **Logs** tab
- Shows build logs, runtime logs, and errors

### Metrics

Monitor your service:
- Service → **Metrics** tab
- CPU, Memory, Request count, Response times

---

## 🆓 Free Tier Limitations

Render's free tier includes:

- ✅ **750 hours/month** of runtime (enough for 24/7 operation)
- ✅ **Automatic SSL** (HTTPS)
- ✅ **Custom domains**
- ✅ **Auto-deploy from GitHub**
- ⚠️ **Services spin down after 15 minutes of inactivity**
  - First request after spin-down takes ~30-50 seconds
  - Subsequent requests are fast
  - Consider upgrading to paid plan for always-on service

### Handling Spin-Down

If you need always-on service:
1. Upgrade to **Starter Plan** ($7/month) - keeps service always running
2. Or use a service like [UptimeRobot](https://uptimerobot.com) to ping your service every 5 minutes (keeps it awake)

---

## 🔄 Updating Your Deployment

### Automatic Updates

1. Make changes to your code
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Your update message"
   git push
   ```
3. Render automatically detects the push and redeploys
4. Check the **Logs** tab to see deployment progress

### Manual Updates

1. Go to Render dashboard → Your service
2. Click **"Manual Deploy"** → **"Deploy latest commit"**

---

## 🐛 Troubleshooting

### Build Fails

**Problem:** Build command fails
- **Solution:** 
  - Check **Logs** tab for error messages
  - Verify `requirements.txt` has all dependencies
  - Ensure Python version is compatible

**Problem:** Import errors
- **Solution:** 
  - Check that all files are in the `backend` directory
  - Verify Root Directory is set to `backend`

### Service Won't Start

**Problem:** Service crashes on start
- **Solution:**
  - Check **Logs** tab for error messages
  - Verify Start Command is correct: `uvicorn main:app --host 0.0.0.0 --port $PORT`
  - Ensure database file exists (run `python seed.py` in Shell)

### Database Issues

**Problem:** No campaigns returned
- **Solution:**
  1. Open **Shell** tab
  2. Run: `python backend/seed.py`
  3. Verify: `ls -la backend/` shows `campaigns.db`

**Problem:** Database not persisting
- **Solution:** 
  - Render's free tier uses ephemeral filesystem
  - Database file may be lost on redeploy
  - Consider using Render's PostgreSQL (free tier) for production
  - Or re-run `seed.py` after each deploy

### CORS Errors

**Problem:** Frontend can't connect to backend
- **Solution:**
  1. Check `ALLOWED_ORIGINS` environment variable in Render
  2. Include your Vercel URL: `https://your-app.vercel.app`
  3. Include wildcard for previews: `https://*.vercel.app`
  4. Redeploy after updating environment variables

### Slow First Request

**Problem:** First request takes 30-50 seconds
- **Solution:** 
  - This is normal on free tier (service spins down after 15 min inactivity)
  - Subsequent requests are fast
  - Upgrade to paid plan for always-on service

---

## 📊 Monitoring

### View Logs

1. Go to your service dashboard
2. Click **"Logs"** tab
3. See real-time logs, errors, and requests

### View Metrics

1. Go to your service dashboard
2. Click **"Metrics"** tab
3. Monitor:
   - CPU usage
   - Memory usage
   - Request rate
   - Response times

### Set Up Alerts

1. Go to **Account Settings** → **Notifications**
2. Enable email alerts for:
   - Service failures
   - Deployment completions
   - Resource limits

---

## 🔐 Security Best Practices

1. **Environment Variables:**
   - Never commit secrets to GitHub
   - Use Render's Environment Variables for sensitive data

2. **CORS:**
   - Restrict `ALLOWED_ORIGINS` to your actual domains
   - Don't use `*` in production

3. **Database:**
   - For production, use Render's managed PostgreSQL
   - Don't rely on SQLite file in ephemeral filesystem

---

## 🆚 Render vs Railway

| Feature | Render | Railway |
|---------|--------|---------|
| Free Tier | 750 hrs/month | $5 credit/month |
| Spin Down | 15 min inactivity | No spin-down |
| Always On | Paid plan ($7/mo) | Included in paid |
| Database | Managed PostgreSQL | Managed PostgreSQL |
| Auto Deploy | ✅ Yes | ✅ Yes |
| Custom Domain | ✅ Free | ✅ Free |

**For this project:** Both work great! Render is easier to set up, Railway has no spin-down on free tier.

---

## ✅ Checklist

Before going live, verify:

- [ ] Backend deployed successfully on Render
- [ ] Database seeded (run `python seed.py`)
- [ ] Health check works: `/health`
- [ ] Campaigns endpoint works: `/campaigns`
- [ ] API docs accessible: `/docs`
- [ ] CORS configured with frontend URL
- [ ] Frontend environment variable updated
- [ ] Tested end-to-end from frontend

---

## 🎉 You're Done!

Your backend is now live on Render! 🚀

- **Backend URL:** `https://your-service-name.onrender.com`
- **API Docs:** `https://your-service-name.onrender.com/docs`
- **Health Check:** `https://your-service-name.onrender.com/health`

---

## 📚 Additional Resources

- [Render Documentation](https://render.com/docs)
- [FastAPI on Render](https://render.com/docs/deploy-fastapi)
- [Render Python Guide](https://render.com/docs/python)

---

**Need Help?** Check the Logs tab in Render dashboard for detailed error messages!

