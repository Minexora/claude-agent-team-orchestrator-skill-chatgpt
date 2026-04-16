# Workflow

## 1. Girdi sınıflandırma

İlk olarak kullanıcının isteğini şu üç sınıftan birine ayır:

1. **Yeni proje**
2. **Mevcut repoya onboarding**
3. **Mevcut repoda değişiklik / geliştirme**

## 2. Karar ağacı

### Yeni proje

1. Varsayılan stack ile ilerle veya kritik eksik varsa kısa soru sor.
2. Klasör yapısını planla: `backend/`, `frontend/`, `tests/`, `docs/`.
3. En az `docs/project-plan.md` içeriğini hazırla.
4. Kullanıcıya planı özetle.
5. "Tasklara ayırıp ekibe dağıtayım mı?" sorusunu sor.
6. Onay sonrası görevlere böl.

### Mevcut repoya onboarding

1. Repoyu klonla veya mevcut dizini incele.
2. Teknoloji, klasörler, eksikler, riskler ve mimariyi analiz et.
3. Kullanıcının hedefini netleştir.
4. Plan ve gerekiyorsa requirements / architecture / task breakdown içeriğini hazırla.
5. Kullanıcı onayı sonrası görev dağıt.

### Mevcut repoda değişiklik

1. İstenen değişikliğin kapsamını sınırlı tut.
2. Etkilenecek dosyaları belirle.
3. Sözleşme, API, veri modeli ve UI etkilerini kontrol et.
4. Geri dönülebilir uygulama planı yap.
5. Test stratejisini öncele.
6. Sonra implementasyon görevlerini dağıt.

## 3. Görev dağıtım sırası

Önerilen sıra:

1. Product Owner
2. UI/UX Designer
3. Backend Developer ve Frontend Developer
4. Tester
5. Team Lead final kontrol

## 4. Engeller ve blokaj yönetimi

- Bir görev başka görev tamamlanmadan başlayamıyorsa bunu açıkça işaretle.
- Paralel görevler arasında paylaşılan sözleşmeleri Team Lead sabitlesin.
- Aynı blokaj üçüncü kez yaşanırsa kullanıcıya seçenekli özet ver.
