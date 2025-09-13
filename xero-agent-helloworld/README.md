# OpenAI Agents SDK + Xero MCP Integration

This project demonstrates how to integrate the **OpenAI Agents SDK** with the **Xero MCP (Model Context Protocol)** to interact with Xero’s accounting data programmatically.

---

## 🚀 Prerequisites

- Python 3.10+
- [OpenAI API Key](https://platform.openai.com/)
- [Xero Free Trial Account](https://www.xero.com/signup/)
- [Xero Developer Account](https://developer.xero.com/)

---

## 📝 Setup Instructions

### 1. Create a Xero Trial Account
1. Sign up for a free 30-day trial: [Xero Signup](https://www.xero.com/signup/).  
2. After login, you’ll see the **dashboard**.  
3. On the very left, click the **organization dropdown**.  
4. Select **Demo Company (Global)** – this is the sandbox organization with dummy data provided by Xero.

---

### 2. Create a Xero Developer Account
1. Go to the [Xero Developer Portal](https://developer.xero.com/).  
2. Create your developer account.  
3. Navigate to **My Apps** → **New App**.  

---

### 3. Create a New App in Xero
1. In the modal, provide:
   - **App Name** → any name (e.g., `xero-openai-integration`).  
   - **App Type** → select **Custom Connection** (last option).  
   - **Company URL** → e.g., `https://panaversity.org/` (placeholder).  
   - **Redirect URL** → same as above or any valid URL.  
2. Accept terms, then **Create App**.

---

### 4. Configure App Scopes & Authorization
1. On the app’s page, select the **scopes/permissions** your app requires.  
   > You may select **all scopes** for testing.  
2. Click **Save & Connect** (top-right).  
3. Xero will send you an **authorization request email**.  
4. Open the email → Click **Connect**.  
5. You’ll be redirected to a page asking to select an organization.  
6. Select **Demo Company (Global)** → Click **Allow Access**.  

Your app is now authorized ✅

---

### 5. Get API Credentials
1. Go back to the **Developer Portal**.  
2. Refresh the configuration page.  
3. You should see status = **Authorized**.  
4. Copy your:
   - **Client ID**  
   - **Client Secret**  
5. Add them to your `.env` file in the project root:

```env
XERO_CLIENT_ID=your-xero-client-id
XERO_CLIENT_SECRET=your-xero-client-secret
OPENAI_API_KEY=your-openai-api-key
