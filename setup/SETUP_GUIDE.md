# OpenClaw Setup Guide 🖥️

**Before starting your AI Upskill course, you need your own OpenClaw instance.**

This guide covers setting up OpenClaw on:
- 🖥️ Old Laptop (Windows/Mac/Linux)
- 📦 Mini PC
- 🐳 Docker Container
- 💻 Windows Subsystem for Linux (WSL)
- 🍎 Mac

---

## What is OpenClaw?

OpenClaw is your personal AI assistant that runs locally. Think of it as an AI operating system that:
- Runs AI agents with persistent memory
- Connects to messaging platforms (Telegram, Discord, WhatsApp)
- Can browse the web and execute commands
- Uses skills that extend its capabilities
- Keeps your data private

---

## Hardware Requirements

| Device | Minimum | Recommended |
|--------|---------|-------------|
| **RAM** | 4GB | 8GB+ |
| **Storage** | 20GB | 50GB SSD |
| **CPU** | Dual-core | Quad-core |
| **Internet** | Required for AI models | Stable connection |

---

## Option 1: Quick Start (All Platforms)

### Install OpenClaw

```bash
# One-line install (Linux/Mac/WSL)
curl -sL https://get.openclaw.ai | bash

# Or via npm
npm install -g @openclaw/cli
openclaw init
```

### Verify Installation

```bash
openclaw --version
openclaw status
```

### Access Dashboard

Once running, access the web dashboard:
```
http://localhost:18789
```

---

## Option 2: Old Laptop Setup

### Windows 10/11

**Option A: Direct Install**

1. Download Node.js 18+ from [nodejs.org](https://nodejs.org)
2. Run installer
3. Open PowerShell:
```powershell
npm install -g @openclaw/cli
openclaw init
```

**Option B: Use WSL (See Option 4 Below)**

### Linux (Ubuntu/Debian)

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

# Install OpenClaw
npm install -g @openclaw/cli
openclaw init

# Start
openclaw gateway start
```

### macOS

```bash
# Using Homebrew
brew install node
npm install -g @openclaw/cli
openclaw init
```

---

## Option 3: Mini PC Setup

Mini PCs are perfect for:
- Low power consumption (always-on)
- Small footprint
- Affordable ($100-300)

### Recommended Mini PCs

| Model | Specs | Price |
|-------|--------|-------|
| **Beelink EQ12** | 8GB RAM, 256GB SSD | ~$200 |
| **GMKtec NucBox G2** | 16GB RAM, 512GB SSD | ~$250 |
| **ASUS PN50** | Ryzen 5, 16GB RAM | ~$350 |

### Setup Steps

1. Install Linux (Ubuntu Server recommended)
```bash
# Download Ubuntu Server
# Create bootable USB with Rufus (Windows) or Etcher (Mac)
# Boot from USB, follow installer

# After installation:
sudo apt update
sudo apt install -y curl nodejs npm
npm install -g @openclaw/cli
openclaw init
```

2. Enable Auto-Start (systemd)
```bash
sudo nano /etc/systemd/system/openclaw.service
```

```ini
[Unit]
Description=OpenClaw Gateway
After=network.target

[Service]
Type=simple
User=YOUR_USERNAME
WorkingDirectory=/home/YOUR_USERNAME
ExecStart=/usr/bin/openclaw gateway start
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable openclaw
sudo systemctl start openclaw
```

3. Access Remotely
```bash
# Find IP
hostname -I

# Access from any browser
# http://MINI_PC_IP:18789
```

---

## Option 4: Docker Container

### Install Docker

**Windows/Mac:**
Download from [docker.com](https://docker.com)

**Linux:**
```bash
curl -fsSL https://get.docker.com | sh
```

### Run OpenClaw Container

```bash
# Create directory for data
mkdir -p ~/openclaw-data

# Run container
docker run -d \
  --name openclaw \
  -p 18789:18789 \
  -v ~/openclaw-data:/data \
  openclaw/openclaw:latest
```

### Docker Compose (Recommended)

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  openclaw:
    image: openclaw/openclaw:latest
    container_name: openclaw
    ports:
      - "18789:18789"  # Dashboard
      - 8765:8765      # API
    volumes:
      - ./openclaw-data:/data
      - /var/run/docker.sock:/var/run/docker.sock  # Optional: Docker in Docker
    environment:
      - TZ=America/New_York
    restart: unless-stopped
```

```bash
# Start
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

---

## Option 5: WSL (Windows Subsystem for Linux)

### Enable WSL

Open PowerShell (Admin):
```powershell
wsl --install
```

Restart computer, then:
```bash
# Install Ubuntu
wsl --install -d Ubuntu

# Or install from Microsoft Store
```

### Setup in WSL

```bash
# Update
sudo apt update && sudo apt upgrade -y

# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

# Install OpenClaw
npm install -g @openclaw/cli
openclaw init

# Start
openclaw gateway start
```

### Access from Windows Browser

Open Windows browser:
```
http://localhost:18789
```

### Useful WSL Commands

```bash
# List distros
wsl --list

# Open Ubuntu
wsl -d Ubuntu

# Access Windows files from Linux
cd /mnt/c

# Access Linux files from Windows
\\wsl$\Ubuntu\home\username
```

---

## Option 6: Mac Setup

### Requirements
- macOS 11 (Big Sur) or later
- Apple Silicon or Intel

### Installation

**Option A: Homebrew (Recommended)**

```bash
# Install Homebrew if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Node.js and OpenClaw
brew install node
npm install -g @openclaw/cli
openclaw init
```

**Option B: Direct Install**

1. Download Node.js from [nodejs.org](https://nodejs.org)
2. Install the package
3. Terminal:
```bash
npm install -g @openclaw/cli
openclaw init
```

### Start OpenClaw

```bash
openclaw gateway start
```

### Access Dashboard

Open browser:
```
http://localhost:18789
```

---

## Post-Installation Setup

### 1. Configure OpenClaw

```bash
# Run setup wizard
openclaw setup

# Or configure manually
openclaw config edit
```

### 2. Install Essential Skills

```bash
# Install useful skills
openclaw skills install weather
openclaw skills install web-search
openclaw skills install calculator
```

### 3. Add Your Agents

Copy your course agents:
```bash
# Clone your agent ecosystem
git clone https://github.com/boktoday/AI-Orchestrator-upskill-ecosystem.git ~/openclaw-agents

# Tell OpenClaw to use them
openclaw agents add ~/openclaw-agents
```

### 4. Configure AI Models

Open dashboard → Settings → Models:

| Provider | Setup |
|----------|-------|
| **OpenRouter** | Get API key from openrouter.ai |
| **OpenAI** | Get API key from platform.openai.com |
| **Anthropic** | Get API key from console.anthropic.com |

### 5. (Optional) Connect Channels

```bash
# Add Telegram bot
openclaw channels add telegram

# Add Discord bot
openclaw channels add discord
```

---

## Troubleshooting

### "Command not found"

```bash
# Check Node.js installed
node --version
npm --version

# Reinstall OpenClaw
npm uninstall -g @openclaw/cli
npm install -g @openclaw/cli
```

### "Port already in use"

```bash
# Find what's using port 18789
lsof -i :18789

# Kill it or use different port
openclaw gateway start --port 18800
```

### "Permission denied"

```bash
# Fix npm permissions
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

### Docker: "Port already allocated"

Edit `docker-compose.yml` to use different port:
```yaml
ports:
  - "18790:18789"  # Host:Container
```

---

## Accessing Your OpenClaw

| Method | URL |
|--------|-----|
| **Local Browser** | http://localhost:18789 |
| **Network** | http://YOUR_IP:18789 |
| **Tunnel** | (Configure ngrok or cloudflare tunnel) |

---

## Next Steps

Once OpenClaw is running:

1. ✅ Access dashboard at http://localhost:18789
2. ✅ Configure your AI model (OpenRouter recommended)
3. ✅ Install the Upskill Ecosystem agents
4. ✅ Start Module 1!

---

## Need Help?

- 📖 [OpenClaw Documentation](https://docs.openclaw.ai/)
- 💬 [OpenClaw Discord](https://discord.gg/openclaw)
- 🐛 [Report Issues](https://github.com/openclaw/openclaw/issues)

---

*This setup guide is part of the AI Upskill Ecosystem*
