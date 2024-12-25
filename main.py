import pyjokes

# جلب نكتة عشوائية
joke = pyjokes.get_joke(language="en", category="neutral")

# عرض النكتة
print("إليك نكتة ممتعة للمبرمجين:")
print(joke)
