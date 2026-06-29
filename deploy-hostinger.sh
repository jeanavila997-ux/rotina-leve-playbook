#!/bin/bash

# ROTINA LEVE - Deploy to Hostinger via FTP
# Usage: bash deploy-hostinger.sh

echo "🚀 Rotina Leve - Hostinger Deployment"
echo "======================================"

# Check if landing folder exists
if [ ! -d "landing" ]; then
  echo "❌ Error: landing/ folder not found"
  exit 1
fi

echo "📦 Files ready to deploy:"
ls -lh landing/

echo ""
echo "✅ Next steps:"
echo "1. Login to Hostinger File Manager"
echo "2. Navigate to public_html/"
echo "3. Upload landing/index.html"
echo "4. Upload landing/obrigado.html"
echo "5. Upload landing/playbook.html (<- O link do seu playbook!)"
echo "6. Upload landing/assets/ (if exists)"
echo ""
echo "7. Update Checkout Link in index.html:"
echo "   - Find: https://pay.cakto.com.br/..."
echo "   - Replace with your actual Cakto link"
echo ""
echo "8. Configure Cakto Redirect:"
echo "   - Go to Cakto Dashboard"
echo "   - Set Post-Purchase URL: https://yourdomain.com/obrigado.html"
echo ""
echo "9. Test at:"
echo "   - Landing page: https://yourdomain.com"
echo "   - Playbook: https://yourdomain.com/playbook.html"
echo ""
echo "Done! Site is ready for production. 🎉"
