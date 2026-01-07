member = [{"name": "Fahim", "phone": "0187"}, {"name": "Rahim", "phone": "0178"},{"name": "Zarir", "phone": "0167"}, {"name": "Huzaifa", "phone": "0176"}, {"name": "Talha", "phone": "0197"}]
for idx in range(0, len(member)):
    if member[idx].get("phone") == "0176":
        print(f"Name : {member[idx].get("name")} Phone: {member[idx].get("phone")}")
    print(member[idx].get("phone"))
    # print(member[idx].keys())

for data in member:
    print(data.values())

#key methods return dict all keys