# Launch Guide: Rotina Leve Playbook

This guide provides the exact steps and configurations needed to take the project from the current repository state to a live, selling product.

## 1. Visual Assets (Action Required)
Since the automated image generation tool is currently unavailable, these assets must be created manually or via an external AI tool (Midjourney, DALL-E 3, Canva).

### Assets to Create:
- [ ] **Ebook Cover**: 
  - **Ratio**: 3:4
  - **Style**: Modern, minimalist, professional.
  - **Colors**: Deep Indigo (`#4F46E5`) and White.
  - **Text**: "Rotina Leve: Playbook Anti-Procrastinação para Mentes Aceleradas".
  - **Path**: Save as `landing/assets/cover.jpg` (or `.png`).
- [ ] **3D Device Mockups**:
  - Create images of a Laptop, Tablet, and Mobile displaying the PDF content.
  - **Path**: Save in `landing/assets/mockups/`.
- [ ] **Social Sharing Image**:
  - 1200x630px image showcasing the product.
  - **Path**: Save as `landing/assets/og-image.jpg`.

---

## 2. Cakto Integration (Technical Config)
Configure the payment flow in your Cakto dashboard.

### Redirection Setup:
1. Go to your **Product Settings** $\rightarrow$ **Thank You Page/URL**.
2. Set the **Redirect URL** to: `https://rotinaleve.com.br/obrigado.html`.
   - *This ensures that immediately after payment, the customer lands on our dedicated thank you page.*

### Digital Delivery:
1. Configure the **Automatic Email Delivery**.
2. Attach the PDF file located at `content/rotina-leve-playbook.pdf`.
3. Set the email trigger to "Payment Approved".

---

## 3. Publication & Hosting
The project is designed as a static site for maximum speed.

### Deployment Options (Recommended):
- **Vercel / Netlify**: Connect your GitHub repository and select the `landing/` folder as the root directory.
- **GitHub Pages**: Enable "GitHub Pages" in the repository settings and serve from the `landing/` directory.

### Domain & SSL:
1. Point your domain `rotinaleve.com.br` (via DNS A/CNAME records) to the hosting provider.
2. Ensure the **SSL Certificate (HTTPS)** is active (Automatic on Vercel/Netlify/GitHub Pages).

---

## 4. Final Validation Checklist
Perform these tests after publication:
- [ ] **Checkout Flow**: Buy a test product $\rightarrow$ Verify redirect to `/obrigado.html`.
- [ ] **Download Link**: On the thank you page, click "Baixar Playbook" $\rightarrow$ Verify the PDF opens.
- [ ] **Email Delivery**: Check if the PDF arrived in the email inbox.
- [ ] **Responsiveness**: Open the site on a physical iPhone and Android device.
- [ ] **Social Preview**: Share the link on WhatsApp/LinkedIn and verify the `og:image` appears.
