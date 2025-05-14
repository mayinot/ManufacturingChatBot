# Manufacturing ChatBot and MCP Server

This project is a manufacturing control center built using FastAPI, Gradio, and MCP (Model Context Protocol). It includes features like machine control, quality checks, inventory management, and real-time chat functions with OpenAI integration.

---

## 🚀 Features

- **Manufacturing Control Center** with Gradio front-end.
- **Machine Control** using MCP servers.
- **Chat Functionality** with OpenAI GPT models.
- **Inventory, Quality, and Work Order Management**.
- **MCP Integration** for real-time machine communication.

---

## 📂 Project Structure

backend/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── routers/
│ │ ├── inventory_router.py
│ │ ├── machine_router.py
│ │ ├── product_router.py
│ │ ├── quality_router.py
│ │ ├── work_order_router.py
│ │ └── chat_router.py
│ └── utils/
│ ├── init.py
│ ├── logging.py
│ └── config.py
├── database/
│ ├── init.py
│ ├── connection.py
│ ├── models/
│ │ ├── inventory.py
│ │ ├── machine.py
│ │ ├── product.py
│ │ └── work_order.py
│ └── simulators/
│ ├── inventory_simulator.py
│ ├── machine_simulator.py
│ ├── product_simulator.py
│ └── work_order_simulator.py
├── mcp/
│ ├── init.py
│ ├── mcp_server.py
│ └── handlers.py
└── requirements.txt



---

## 🛠️ Setup

### Prerequisites

- Python 3.12+
- Docker (optional for production)
- OpenAI API key

### Installation

```bash
git clone https://github.com/yourusername/ManufacturingChatBot.git
cd ManufacturingChatBot/backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
