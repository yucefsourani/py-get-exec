سكربت بايثون لجلب أمر تشغيل أي برنامج من خلال إسمه أو فئته 




#################################################################################################################################


مثال جلب أمر تشغيل فايرفوكس من خلال إدخال إسمه أو شيء قريب من إسمه


print_byname(["firefox"])


print_byname(["fire"])




#################################################################################################################################





مثال جلب امر التشغيل لكل البرامج في فئة محدده أو أكثر


print_bycategories(["Network"])

print_bycategories(["Network","Game"])



#################################################################################################################################





كيف نستخدم السكربت نفتحه من خلال أي محرر نصي في أخر السكربت هناك 

#exp1

print ("\n\nex1 :\n")

print_bycategories(["Network"])




#exp2

print ("\n\n\n\n\nex2 :\n")

print_byname(["firefox"])


نكتب ما نريد بدل الكلمات فايرفوكس أو نتوورك ثم نعطي السكربت صلاحيات التنفيذ تم نشغله لاحقا سأضيف إليه argv ليصبح نعطيه إسم البرنامج من سطر الأوامر


#################################################################################################################################
