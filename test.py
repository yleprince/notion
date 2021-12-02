from notion.client import NotionClient

client = NotionClient()

print(client.get_block("cc7e60738e1143169432b3f75c6cc564"))

print("\n\n")
print(client.get_block("2a6a830f-0739-4b24-a632-4a75bc1966ed"))
