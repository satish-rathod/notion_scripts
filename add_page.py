import os
import argparse
import sys
from dotenv import load_dotenv
from notion_client import Client
from notion_client.errors import APIResponseError

def setup_arg_parser():
    parser = argparse.ArgumentParser(description="Add a new page to Notion.")
    parser.add_argument("--title", required=True, help="Title of the new page")
    parser.add_argument("--parent-id", help="ID of the parent page or database (overrides env var)")
    parser.add_argument("--type", choices=['page', 'database'], default='page', 
                        help="Type of the parent (page or database). Default is 'page'.")
    return parser

def main():
    load_dotenv()
    
    parser = setup_arg_parser()
    args = parser.parse_args()

    notion_token = os.getenv("NOTION_API_KEY")
    if not notion_token:
        print("Error: NOTION_API_KEY not found in environment variables.")
        sys.exit(1)

    parent_id = args.parent_id or os.getenv("NOTION_PAGE_ID")
    if not parent_id:
        print("Error: Starting Page ID not provided. Use --parent-id or set NOTION_PAGE_ID in .env")
        sys.exit(1)

    notion = Client(auth=notion_token)

    parent_prop = {}
    if args.type == 'database':
        parent_prop = {"database_id": parent_id}
    else:
        parent_prop = {"page_id": parent_id}

    new_page_properties = {
        "title": [
            {
                "text": {
                    "content": args.title
                }
            }
        ]
    }

    try:
        # Note: 'properties' structure depends on the parent. 
        # If parent is a database, 'title' key usually needs to match the property name of the title column (default is 'Name').
        # If parent is a page, 'title' is a top-level property for the new page object creation? 
        # Actually for creating a page inside another page, the properties are just the title.
        # But if creating in a database, we need to match the schema.
        # For simplicity in this script, we assume a simple page creation or a database where the title property is named "Name" or we try to infer.
        # However, the Notion API 'pages.create' endpoint takes 'properties'.
        # For a page parent, 'title' is indeed the property key for the page title.
        # For a database parent, we must use the actual property name. Let's assume 'Name' for database for now or simple title for page.
        
        # Correction: When creating a page with a page parent, the 'title' is specified in 'properties' as 'title'.
        # When creating a page with a database parent, 'properties' keys must match database schema.
        
        props = {}
        if args.type == 'database':
             # Common default name for the title property in databases is "Name"
             # Ideally we would query the database to find the title property name, but let's stick to "Name" for this simple script
             # or allow user to pass it. For now, let's use "Name" as it's standard.
             props = {
                 "Name": {
                     "title": [
                         {
                             "text": {
                                 "content": args.title
                             }
                         }
                     ]
                 }
             }
        else:
             props = {
                "title": [
                    {
                        "text": {
                            "content": args.title
                        }
                    }
                ]
            }

        response = notion.pages.create(
            parent=parent_prop,
            properties=props
        )
        
        print(f"Success! Page created.")
        print(f"URL: {response.get('url')}")
        print(f"ID: {response.get('id')}")

    except APIResponseError as e:
        print(f"Notion API Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
