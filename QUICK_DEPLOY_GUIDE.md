# 🚀 Deploy BGuru in 1 Hour - Quick Start Guide

## What You're Building

A **free, public web application** where anyone can consult BGuru for ethical strategic intelligence. Live URL example: `https://yourname-bguru.streamlit.app`

**No coding experience required beyond copy-paste!**

---

## ✅ Prerequisites (5 minutes)

1. **GitHub Account** (free)
   - Go to https://github.com
   - Sign up if you don't have account
   - Verify your email

2. **Streamlit Account** (free)
   - Go to https://streamlit.io/cloud
   - Click "Sign up"
   - Sign in with your GitHub account
   - Authorize Streamlit to access your GitHub

---

## 📦 Step 1: Create Your GitHub Repository (10 minutes)

### 1.1 Create New Repository

1. Go to https://github.com/new
2. **Repository name:** `bguru-public`
3. **Description:** "BGuru - Ethical Strategic Intelligence for Mission-Driven Organizations"
4. **Visibility:** Public ✓
5. **Initialize with README:** ✓ Yes
6. Click **"Create repository"**

### 1.2 Upload BGuru Files

You have two options:

**Option A: Upload via GitHub Web Interface (Easiest)**

1. In your new repo, click **"Add file"** → **"Upload files"**
2. Drag and drop these files:
   - `streamlit_app.py` (the main app)
   - `requirements.txt` (dependencies)
   - `bguru_core_system_prompt.md` (BGuru's brain)
   - `README.md` (documentation)
3. At bottom, enter commit message: "Initial BGuru deployment"
4. Click **"Commit changes"**

**Option B: Use Git Command Line (If you're comfortable with git)**

```bash
# Clone your repository
git clone https://github.com/YOUR_USERNAME/bguru-public.git
cd bguru-public

# Copy BGuru files into this directory
# (Copy streamlit_app.py, requirements.txt, bguru_core_system_prompt.md, README.md)

# Commit and push
git add .
git commit -m "Initial BGuru deployment"
git push origin main
```

### 1.3 Verify Files

Your repo should now contain:
- `streamlit_app.py`
- `requirements.txt`
- `bguru_core_system_prompt.md`
- `README.md`

---

## 🌐 Step 2: Deploy to Streamlit Cloud (5 minutes)

### 2.1 Create New App

1. Go to https://share.streamlit.io
2. Click **"New app"**
3. You'll see a deployment form:

### 2.2 Configure Deployment

Fill in:
- **Repository:** Select `yourname/bguru-public`
- **Branch:** `main`
- **Main file path:** `streamlit_app.py`
- **App URL:** Choose your subdomain (e.g., `bguru` → `bguru.streamlit.app`)
  - Or leave as suggested default

### 2.3 Deploy!

1. Click **"Deploy!"**
2. Wait 2-3 minutes while Streamlit:
   - Installs dependencies
   - Loads your app
   - Generates your public URL

### 2.4 Your App is Live! 🎉

You'll get a URL like: `https://your-username-bguru.streamlit.app`

**This URL is:**
- ✅ Free forever
- ✅ Public (anyone can access)
- ✅ Automatically updates when you push to GitHub
- ✅ Mobile-friendly
- ✅ SSL-secured (https)

---

## 🧪 Step 3: Test Your Deployment (5 minutes)

### 3.1 Get a Claude API Key

1. Go to https://console.anthropic.com
2. Sign up for free account
3. Navigate to **"API Keys"**
4. Click **"Create Key"**
5. Copy your key (starts with `sk-ant-...`)
6. **Note:** Anthropic gives free trial credits!

### 3.2 Test BGuru

1. Open your Streamlit app URL
2. Fill in a test organization:
   - Name: "Test Nonprofit"
   - Type: "Nonprofit"
   - Mission: "Empower youth through education"
3. Ask a question: "Should we expand to new cities?"
4. Paste your API key
5. Click "Consult BGuru"
6. **It works if:** You get a detailed strategic analysis!

---

## 📣 Step 4: Share with the World (Ongoing)

### 4.1 Share Your URL

Your BGuru is now public! Share it:

**LinkedIn Post:**
```
🚀 Excited to launch BGuru - free ethical strategic intelligence for mission-driven organizations!

Unlike conventional business consultants, BGuru prioritizes:
✅ Wisdom over growth
✅ Human agency over automation  
✅ Civic good over profit
✅ Transparency over opacity

Perfect for nonprofits, social enterprises, and educational institutions navigating complex strategic decisions.

Try it free: [your-url].streamlit.app

Built on ethical AI principles. Powered by Claude (Anthropic).

#SocialImpact #EthicalAI #Nonprofits #SocialEnterprise
```

**Twitter/X:**
```
🧭 Launching BGuru - ethical strategic intelligence for orgs that care about mission, not just money.

Free tool helps nonprofits/social enterprises make value-aligned decisions.

Try it: [your-url].streamlit.app

No BS. No growth-at-all-costs. Just honest strategic thinking.
```

**Email to Nonprofit Networks:**
```
Subject: Free Strategic Intelligence Tool for Mission-Driven Organizations

Hi [Network],

I've built a free tool called BGuru that helps nonprofits and social enterprises make strategic decisions without compromising their missions.

Unlike traditional business consultants, BGuru will refuse to recommend profitable strategies that drift from your core values.

Try it at: [your-url].streamlit.app

Perfect for questions like:
- Should we accept funding from [corporation]?
- How do we scale without mission drift?
- Should we partner with [organization]?

It's free, requires no sign-up, and built on ethical AI principles.

Would love your feedback!

Best,
Plato
```

### 4.2 Where to Share

**Academic/Education:**
- EDUCAUSE LISTSERV
- Chronicle of Higher Education forums
- AAC&U networks
- Your university's faculty newsletter

**Nonprofit Sector:**
- Reddit: r/nonprofit, r/socialgood
- Nonprofit Tech Facebook groups
- Local nonprofit leadership networks
- Foundation partner networks

**Social Enterprise:**
- B-Corp community forums
- Social Enterprise Alliance
- Impact investing networks

**Media:**
- LinkedIn (your network)
- Medium article explaining BGuru
- Submit to ProductHunt
- Tweet thread with examples

---

## 🔧 Troubleshooting

### App Won't Deploy

**Error: "No module named 'anthropic'"**
- Solution: Make sure `requirements.txt` is in your repo

**Error: "File not found: bguru_core_system_prompt.md"**
- Solution: Make sure you uploaded this file to your repo

**Error: "Invalid python version"**
- Solution: Streamlit uses Python 3.9+ automatically, should work

### App Deployed But Not Working

**API Error When Testing:**
- Make sure you're using a valid Claude API key
- Check if you have trial credits remaining
- Verify the key starts with `sk-ant-`

**App is Slow:**
- First load after deployment can take 30-60 seconds
- Subsequent loads are faster
- BGuru analysis itself takes 30-60 seconds (AI processing)

**Want to Update the App:**
1. Edit files in your GitHub repo (or push new commits)
2. Streamlit auto-detects changes
3. Reboot app if needed (button in Streamlit Cloud dashboard)

---

## 🎨 Customization (Optional)

### Change App Appearance

Edit `streamlit_app.py`:

**Change Colors:**
```python
# Line ~30, update the CSS
.main-header {
    color: #YOUR_COLOR;  # Change this
}
```

**Change Description:**
```python
# Line ~15
page_title="Your Custom Title",
```

**Add Your Logo:**
```python
# After imports
st.image("your-logo.png", width=200)
```

### Add Your Branding

In the footer section (~line 550), add:
- Your organization's logo
- Link to your website
- Custom messaging

Push changes to GitHub → Streamlit auto-updates!

---

## 📊 Track Impact (Optional but Recommended)

### Simple Analytics

Add to end of `streamlit_app.py`:

```python
# Privacy-respecting usage counter
if 'total_consultations' not in st.session_state:
    st.session_state.total_consultations = 0

# Increment on each consultation
# (Add this after successful BGuru response)
st.session_state.total_consultations += 1

# Display in footer
st.caption(f"🌍 {st.session_state.total_consultations} consultations this session")
```

### More Advanced Analytics

Consider (later):
- Google Analytics (respect privacy)
- Simple database to track:
  - Number of consultations
  - Organization types using BGuru
  - Topics most consulted about
- **Never** store the actual strategic questions (privacy!)

---

## 💰 Costs

### Free Forever Tier (Streamlit Cloud)

✅ **What's FREE:**
- Hosting your app
- Unlimited visitors
- Automatic SSL/security
- Auto-deployment from GitHub
- Community support

✅ **Limits:**
- 1 app on free tier (enough for BGuru!)
- "Made with Streamlit" badge (you can remove with paid plan)
- Sleeps after inactivity (wakes up instantly when visited)

### Claude API Costs

**Anthropic Pricing:**
- Free trial credits (usually $5)
- After trial: ~$0.10-0.15 per long consultation
- If 100 people use BGuru per month = ~$10-15

**Solutions:**
1. Users bring own API keys (recommended for launch)
2. Apply for academic/nonprofit credits
3. Partner with university to cover costs
4. Eventually: freemium model for sustainability

---

## 🚀 Next Steps After Launch

### Week 1: Soft Launch
- [ ] Test thoroughly yourself
- [ ] Share with 10 trusted colleagues
- [ ] Gather feedback
- [ ] Fix any bugs

### Week 2: Public Launch
- [ ] LinkedIn post
- [ ] Email to nonprofit networks
- [ ] Post on relevant subreddits
- [ ] Share in academic circles

### Month 1: Iterate
- [ ] Collect user testimonials
- [ ] Add example case studies
- [ ] Improve based on feedback
- [ ] Track impact metrics

### Month 2-3: Scale
- [ ] Apply for grants to cover API costs
- [ ] Present at conferences
- [ ] Media outreach
- [ ] Build community

---

## ✅ Launch Checklist

Before going fully public:

- [ ] App deploys successfully
- [ ] You can complete a test consultation
- [ ] All links in sidebar work
- [ ] README.md is clear and helpful
- [ ] You have a Claude API key for testing
- [ ] Footer credits are correct
- [ ] App looks good on mobile (test on phone)
- [ ] You've decided on sustainability model (user API keys vs shared)

---

## 🎉 You're Ready to Launch!

In about 1 hour, you've:
✅ Created professional web application  
✅ Deployed to free hosting  
✅ Made BGuru accessible to the world  
✅ Started the ethical business revolution  

**Your BGuru is live at:** `https://[your-username]-bguru.streamlit.app`

**Now go change the world by helping organizations make wisdom-driven decisions!**

---

## 💬 Need Help?

**Streamlit Issues:**
- Docs: https://docs.streamlit.io
- Forum: https://discuss.streamlit.io
- They're very responsive!

**Claude API Issues:**
- Docs: https://docs.anthropic.com
- Support: support@anthropic.com

**BGuru Specific:**
- Review the main README.md
- Check BGURU_PUBLIC_DEPLOYMENT_GUIDE.md
- Email me: [your email]

---

## 📚 What You Just Built

You've created:
1. ✅ **Web Application** - Professional, mobile-friendly interface
2. ✅ **Ethical AI Service** - BGuru accessible worldwide
3. ✅ **Public Good** - Free strategic intelligence for mission-driven orgs
4. ✅ **Movement Starter** - Template others can copy and adapt

**This is just the beginning.** As organizations use BGuru and share their stories, you're building a community committed to ethical business practice.

**Welcome to the ethical strategy revolution!** 🧭

---

**Deploy Time:** ~1 hour  
**Cost:** $0  
**Impact:** Priceless  

**Let's make strategic intelligence serve wisdom, not just wealth.**

*Created by Plato, Indiana University*  
*Part of HAILEI / Timeless Agora Institute*  
*For ethical business practice worldwide*
