# OpenAI Agents SDK + Xero MCP Integration

This project demonstrates how to integrate the **OpenAI Agents SDK** with the **Xero MCP (Model Context Protocol)** to interact with Xero’s accounting data programmatically.  
It has been **containerized with Docker** and can be deployed to **Kubernetes via Rancher Desktop**.

⚠️ **Note**: This app is console-based. When deployed to Kubernetes, you cannot interact with it like a typical web service. You can still run it locally in interactive mode using Rancher Desktop.

---

## 🚀 Prerequisites

- Python 3.10+
- [OpenAI API Key](https://platform.openai.com/)
- [Xero Free Trial Account](https://www.xero.com/signup/)
- [Xero Developer Account](https://developer.xero.com/)
- [Rancher Desktop](https://rancherdesktop.io/) with Kubernetes enabled
- `kubectl` installed and configured for your Rancher Desktop cluster
- Docker installed ([Get Docker](https://docs.docker.com/get-docker/))  

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
5. Add them to your Kubernetes secrets:

```bash
kubectl create secret generic xero-secrets \
  --from-literal=openai_api_key=your-openai-api-key \
  --from-literal=xero_client_id=your-xero-client-id \
  --from-literal=xero_client_secret=your-xero-client-secret
```

6. Build and tag your Docker image, then push it to Docker Hub:
nerdctl build -t aneeqkhatri/xero-uv-demo:latest .
nerdctl push aneeqkhatri/xero-uv-demo:latest

7. Apply the Kubernetes manifests:
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml


8. Check that pods are running:
kubectl get pods

9. Check the service:
kubectl get svc
Your app is exposed via NodePort 30080 on your local machine (through Rancher Desktop).

## Running Interactively (Console Mode)

Since this app is console-based, normal interaction through a web browser is not supported.
To run it interactively inside the container:

```bash
kubectl run -it --rm xero-uv-demo \
  --image=aneeqkhatri/xero-uv-demo:latest \
  --env="OPENAI_API_KEY=your-openai-api-key" \
  --env="XERO_CLIENT_ID=your-xero-client-id" \
  --env="XERO_CLIENT_SECRET=your-xero-client-secret" \
  -- bash
```
Then inside the container:
```
uv run main.py
```

Alternatively, if already deployed, you can exec into the running pod:

kubectl exec -it <pod-name> -- python main.py

Replace <pod-name> with the actual pod name from:

kubectl get pods


