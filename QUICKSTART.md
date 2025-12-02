# Quick Start Guide

Get the Campaign Analytics Dashboard up and running in 5 minutes!

## 🚀 Quick Setup

### 1. Backend Setup (2 minutes)

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Seed database
python seed.py

# Start server
uvicorn main:app --reload --port 8000
```

✅ Backend running at: http://localhost:8000

### 2. Frontend Setup (2 minutes)

```bash
# Navigate to frontend (in a new terminal)
cd frontend

# Install dependencies
npm install

# Create .env.local file
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local

# Start development server
npm run dev
```

✅ Frontend running at: http://localhost:3000

### 3. View Dashboard

Open your browser and navigate to:
- **Home:** http://localhost:3000
- **Campaigns:** http://localhost:3000/campaigns

## 🎯 What You'll See

- A table with 10 sample campaigns
- Filter dropdown (All, Active, Paused)
- Color-coded status badges
- Formatted currency values
- Responsive design

## 📝 Next Steps

1. Check the API docs: http://localhost:8000/docs
2. Test the API: http://localhost:8000/campaigns
3. Read the full README.md for deployment instructions

## 🐛 Troubleshooting

**Backend won't start?**
- Make sure port 8000 is available
- Check that Python 3.9+ is installed
- Verify virtual environment is activated

**Frontend can't connect to backend?**
- Verify backend is running on port 8000
- Check `.env.local` has correct API URL
- Check browser console for errors

**Database errors?**
- Run `python seed.py` again
- Delete `campaigns.db` and re-run seed

---

Happy coding! 🎉

