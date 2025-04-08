# 🏦 IntelliBank: Intelligent Expense Analysis with Blockchain Privacy 🔒💸

![IntelliBank Banner](https://via.placeholder.com/800x200?text=IntelliBank+AI+%2B+Blockchain+Privacy)  
*Work in progress*

## 📌 Description  

**IntelliBank** is an advanced application for tracking and analyzing personal expenses, integrating with banking systems **without compromising privacy**.  
Thanks to **artificial intelligence** and a **hybrid blockchain** (on-chain/off-chain), it offers:  

- 🔐 **Private purchase details**: Banks only see the amount and recipient, not the specific products.  
- 🗂 **Advanced categorization**: Macro-areas (shopping, travel) and detailed sub-categories (e.g. "kg of pasta").  

---

## 🛒 Examples of Blockchain-Protected Analysis  

### **Supermarket**  
- **Encrypted data (off-chain)**: `"2kg of Barilla pasta, 1L of Parmalat milk"`  
- **On-chain data for the bank**: `"Payment to Esselunga - 15€"`  

### ✈️ **Travel**  
- **Encrypted data**: `"Frecciarossa train ticket Milan-Rome"`  
- **Data shared with the bank**: `"Transaction to Trenitalia - 50€"`  

---

## 🚀 Key Features  

### **🔐 Privacy-preserving expense analysis**  
- Encrypted purchase details stored on **IPFS** (off-chain).  
- Transaction hashes recorded on **Hyperledger Fabric** (on-chain).  
- **🧾 Smart OCR**: Data extraction from receipts using *Tesseract* + encryption.  
- **📊 User dashboard**: Access to details only with private key.  
- **🏦 Secure banking integration**: Only amounts and senders/recipients shared.  

---

## ⚙️ Technologies Used  

| **Area**       | **Technologies**               | **Role in Privacy**                          |  
|----------------|-----------------------------|------------------------------------------------|  
| *Backend*      | Python, Flask              | End-to-end encryption                        |  
| *Blockchain*   | Hyperledger Fabric         | Immutable ledger for transaction hashes       |  
| *Storage*      | IPFS + PostgreSQL          | Encrypted off-chain purchase details         |  
| *AI*           | TensorFlow, Tesseract OCR  | Data analysis without third-party exposure   |  
| *Security*     | AES-256, Auth0             | Authentication and data protection           |  

---

## 📅 Development Phases  

1. **🛠 Initial setup**: Environment configuration + private blockchain.  
2. **🔗 Banking API integration**: Connection with *selective disclosure*.  
3. **🤖 AI + Encryption development**: ML for categorization + encryption pipeline.  
4. **🎨 User interface**: React dashboard with access via private key.  
5. **🧪 Testing**: GDPR compliance and attack resistance.  
6. **🚀 Deployment**: Hosting on AWS with Docker.  

---

## ✅ Benefits for the User  

- **🛡 Full control**: You decide who sees what you've bought.  
- **🚫 No banking profiling**: No access to specific habits.  
- **💡 Personalized suggestions**: AI analyzes data locally (*edge computing*).  

---

## 🔗 Problems Solved by Off-Chain Blockchain  

| **Traditional Problem**               | **IntelliBank Solution**                          |  
|----------------------------------------|--------------------------------------------------|  
| Banks see everything (where + what)    | Encrypted details off-chain, only hashes on-chain. |  
| Centralized data at risk of hacks      | Decentralized storage (IPFS).                     |  
| Privacy law compliance                 | *Selective disclosure* for regulatory authorities.  |  

---

## ❓ Why Choose IntelliBank?  

> *"With our hybrid architecture, we get the power of AI without sacrificing privacy. Banks only see what’s needed, you control the rest."*  

---

## 📜 License  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
