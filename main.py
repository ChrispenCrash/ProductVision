import os
import ollama

# content = """Please return a brief description of this product, then separated by a hyphen return a list of true or false values separated by commas for the following statements:
# 	1. Is this product edible?
# 	2. Is this product a fruit?
# 	3. Is this product a vegetable?
# 	4. Is this product a meat?
# 	5. Is this product a dairy product?
# 	6. Is this product an alcoholic beverage?
#     7. Is this product healthy?
# 	8. Is this product vegan?
# """

content = """Return a comma-separated list of "true" or "false" for the following:
Edible?
Fruit?
Vegetable?
Meat?
Dairy product?
Alcoholic beverage?
Healthy?
Vegan?

Here is an example of how to format your response:
true, true, false, false, false, false, true, true
"""

for image in os.listdir("images"):
    print(f"Processing: {image}...")

    res = ollama.chat(
        model="llava:13b",
        messages=[
            {
                "role": "user",
                "content": content,
                "images": [f"images/{image}"],
            }
        ],
    )

    print(res["message"]["content"])
    print()
