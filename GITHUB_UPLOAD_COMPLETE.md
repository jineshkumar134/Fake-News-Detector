# 📤 Complete GitHub Upload & Deployment Guide

## ✅ Your Files Are Here:
```
/tmp/fake-news-detector/
├── backend/
│   ├── main.py
│   ├── fact_check.py
│   ├── domain_check.py
│   ├── headline_corroboration.py
│   └── image_analysis.py
├── frontend/
│   ├── Dockerfile
│   ├── nginx.conf
│   └── public/
│       └── index.html
├── Dockerfile.backend
├── docker-compose.yml
└── requirements.txt
```

---

## 📋 Step-by-Step GitHub Upload

### STEP 1: Initialize Git (First Time Only)

```bash
cd /tmp/fake-news-detector

# Initialize git repository
git init

# Check git status
git status
```

**Expected output:**
```
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        backend/
        frontend/
        docker-compose.yml
        ...
```

### STEP 2: Add All Files to Git

```bash
cd /tmp/fake-news-detector

# Add all files
git add .

# Check status again
git status
```

**Expected output:**
```
Changes to be committed:
  new file:   Dockerfile.backend
  new file:   backend/main.py
  new file:   backend/fact_check.py
  ...
```

### STEP 3: Create Initial Commit

```bash
git commit -m "Initial commit: Multi-Modal Fake News Detector

- FastAPI backend with 5 analysis modules
- Interactive HTML/CSS/JS frontend
- Docker Compose orchestration
- Ready for deployment"
```

### STEP 4: Create GitHub Repository

1. Go to **https://github.com/new**
2. **Repository name**: `fake-news-detector`
3. **Description**: Multi-Modal Fake News Detector - Analyzes news using text, domain, and image verification
4. **Visibility**: Public (recommended) or Private
5. **DO NOT** check any "Initialize" options
6. Click **"Create repository"**

You'll see a page with commands. Copy your repository URL.

### STEP 5: Connect Local Project to GitHub

Replace `YOUR_USERNAME` with your actual GitHub username:

```bash
cd /tmp/fake-news-detector

# Set main branch
git branch -M main

# Add GitHub as remote
git remote add origin https://github.com/YOUR_USERNAME/fake-news-detector.git

# Verify remote added
git remote -v
```

**Expected output:**
```
origin  https://github.com/YOUR_USERNAME/fake-news-detector.git (fetch)
origin  https://github.com/YOUR_USERNAME/fake-news-detector.git (push)
```

### STEP 6: Push to GitHub (Using Personal Access Token)

Since password authentication is disabled, you need a Personal Access Token.

#### Create PAT (Personal Access Token):

1. Go to **https://github.com/settings/tokens/new**
2. **Token name**: `fake-news-detector-upload`
3. **Expiration**: 90 days (or No expiration)
4. **Select scopes** (check these boxes):
   - ✅ `repo` (Full control of private repositories)
   - ✅ `write:packages`
5. Click **"Generate token"**
6. **COPY THE TOKEN** (You won't see it again!)

#### Push Using Token:

```bash
cd /tmp/fake-news-detector

# Replace YOUR_TOKEN with the token you just copied
git push -u origin main https://shanittiwari11:YOUR_TOKEN@github.com/shanittiwari11/fake-news-detector.git
```

Or more simply:

```bash
# This method is safer (token won't be in command history)
git push -u origin main
# When prompted for username: your GitHub username
# When prompted for password: paste your token (it will be invisible)
```

### STEP 7: Verify Upload

1. Go to **https://github.com/YOUR_USERNAME/fake-news-detector**
2. You should see all your files listed!
3. Click each folder to verify files are there

---

## 🚀 Deploy to Railway (After GitHub Upload)

### Option 1: Deploy Automatically (Recommended)

1. Go to **https://railway.app/**
2. Click **"Start New Project"**
3. Select **"Deploy from GitHub repo"**
4. Click **"Connect GitHub"** and authorize
5. Select your **`fake-news-detector`** repository
6. Railway auto-detects Docker Compose
7. Click **"Deploy"**
8. Your app is live in ~3 minutes at: `https://fake-news-detector-xxxx.railway.app`

### Option 2: Alternative Platforms

**Render:**
1. Go to **https://render.com/**
2. Click **"+ New"** → **"Web Service"**
3. Connect GitHub
4. Select repository
5. Deploy

**DigitalOcean:**
1. Go to **https://cloud.digitalocean.com/apps**
2. Click **"Create App"**
3. Connect GitHub
4. Deploy

---

## 📝 Git Commands You'll Need

### After First Upload:

**Make changes to a file:**
```bash
# Edit a file (e.g., backend/main.py)
nano backend/main.py
```

**Upload changes:**
```bash
cd /tmp/fake-news-detector

# Check what changed
git status

# Stage changes
git add .

# Create commit
git commit -m "Fixed bug in fact-checking module"

# Push to GitHub
git push
```

### View your commits:
```bash
git log --oneline
```

### Create a new branch for features:
```bash
git checkout -b feature/new-feature
# Make changes
git add .
git commit -m "Add new feature"
git push origin feature/new-feature
# Then create Pull Request on GitHub
```

---

## ✅ Troubleshooting GitHub Upload

### Problem: "Repository not found"
**Solution:**
- Verify your GitHub username is correct
- Verify repository exists at github.com/YOUR_USERNAME/fake-news-detector
- Make sure you used `git branch -M main`

### Problem: "Authentication failed"
**Solution:**
- Verify you're using Personal Access Token (not password)
- Token must have `repo` scope checked
- Token must not be expired

### Problem: "fatal: refusing to merge unrelated histories"
**Solution:**
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### Problem: "error: src refspec main does not match any"
**Solution:**
```bash
git branch -M main
git push -u origin main
```

---

## 📦 Complete File Structure (Verify You Have These)

```
/tmp/fake-news-detector/
│
├── backend/
│   ├── main.py ..................... FastAPI app (215 lines)
│   ├── fact_check.py ............... Fact-checking (79 lines)
│   ├── image_analysis.py ........... Image analysis (72 lines)
│   ├── domain_check.py ............. Domain reputation (83 lines)
│   └── headline_corroboration.py ... News sources (50 lines)
│
├── frontend/
│   ├── Dockerfile .................. Nginx Alpine container
│   ├── nginx.conf .................. Nginx configuration
│   └── public/
│       └── index.html .............. Web interface (224 lines)
│
├── Dockerfile.backend .............. Python FastAPI container
├── docker-compose.yml .............. Container orchestration
├── requirements.txt ................ Python dependencies
│
└── (Optional, to create):
    ├── README.md ................... Project overview
    ├── .gitignore .................. Git ignore rules
    ├── .env.example ................ API key template
    └── LICENSE ..................... MIT License
```

---

## 🎯 Quick Summary

1. **Initialize**: `git init`
2. **Add files**: `git add .`
3. **Commit**: `git commit -m "Initial commit..."`
4. **Create repo** on GitHub at https://github.com/new
5. **Connect**: `git remote add origin https://github.com/YOUR_USERNAME/fake-news-detector.git`
6. **Push**: `git push -u origin main` (with PAT when prompted)
7. **Deploy**: Go to Railway.app and connect GitHub repo
8. **Done!** Your app is live!

---

## 🔐 Security Notes

- ✅ Never commit `.env` file (it has API keys)
- ✅ Use `.env.example` as template
- ✅ Personal Access Token should not be shared
- ✅ Token expires after 90 days (or no expiration if selected)
- ✅ Can regenerate token anytime at https://github.com/settings/tokens

---

## 📞 Need Help?

**Command to test current setup:**
```bash
cd /tmp/fake-news-detector
git status
ls -la
docker compose up -d
```

**Verify app works locally:**
- Frontend: http://localhost:3000
- API: http://localhost:8000/docs

---

**Ready to upload? Start with STEP 1!** 🚀
