# Notion Automation Scripts

A collection of scripts to automate various tasks in Notion, focusing on managing pages and databases efficiently.

## 🚀 Features

- **Database Management**: Automate entries, updates, and queries for Notion databases.
- **Page Operations**: Create, update, and manage Notion pages programmatically.
- **Workflow Automation**: Streamline repetitive tasks and integrate Notion with other workflows.

## 🛠️ Prerequisites

Before running the scripts, ensure you have the following:

1.  **Notion API Key**: Create an internal integration at [Notion My Integrations](https://www.notion.so/my-integrations) and obtain your `Internal Integration Secret`.
2.  **Access Rights**: Share the target Notion pages or databases with your integration (click `...` > `Connections` > `Connect to`).
3.  **Environment**: 
    - [Python 3.x](https://www.python.org/downloads/) (recommended)
    - `requests` or `notion-client` library (depending on implementation)

## 📦 Installation

1.  Clone this repository:
    ```bash
    git clone https://github.com/yourusername/notion_scripts.git
    cd notion_scripts
    ```

2.  Install dependencies (example):
    ```bash
    pip install -r requirements.txt
    ```

3.  Set up environment variables:
    Create a `.env` file in the root directory:
    ```env
    NOTION_API_KEY=your_secret_key_here
    NOTION_DATABASE_ID=your_database_id_here
    ```

## 📂 Scripts Available

*(This section will be populated as scripts are added)*

| Script Name | Description | Usage |
| `add_page.py` | Adds a new page to a parent page or database. | `python add_page.py --title "My Page" --parent-id <ID>` |

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or new scripts.

## 📄 License

This project is licensed under the MIT License.
