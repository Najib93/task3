# istifadeciden boy melumatini alin
boy = float(input("Zehmet olmasa, boyunuzu metr cinsinde daxil edin (numune: 1.75): "))

# ideal ceki araliigi ucun formullasdirilmis funksiya
ideal_min_ceki = 18.5 * (boy ** 2)
ideal_max_ceki = 24.9 * (boy ** 2)

# cixisi cap edin
print("ideal ceki araligi:", ideal_min_ceki, "-", ideal_max_ceki, "kilogram")

# istifadeciye uygun meslehet verin
if ideal_min_ceki <= 0 or ideal_max_ceki <= 0:
    print("Xeta: Boy daxil etdiyiniz ucun ideal ceki araligi hesablanmir. zehmett olmasa dugun melumat daxil edin.")
else:
    print("eger ceki bu araliqda deyilse saglamliginiz ucun hekime muraciet edin.")
