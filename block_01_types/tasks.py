search_results = [
    {"source": "policy_2024.pdf", "score": 0.91},
    {"source": "faq.pdf", "score": 0.87},
    {"source": "policy_2024.pdf", "score": 0.85},  # дубль
]
unique_sources = {result["source"] for result in search_results}
# → {"policy_2024.pdf", "faq.pdf"}

print(type(unique_sources))
print(unique_sources)

model_limits = {
    "gemini":100000,
    "gemini1":90000,
    "gemini2":190000,
}

large_contex_model = {
    name: context
    for name, context in model_limits.items()
    if context > 100000
}
print(large_contex_model)
large_contex_model1 = {
    # name: name[1]
    name
    for name in model_limits
    # if name[1] > 100000
}
print(large_contex_model1)

