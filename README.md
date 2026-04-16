# Claude Agent Team Orchestrator

Claude Code içinde Team Lead odaklı çok ajanlı bir ekip düzeni kurmak için hazırlanmış skill.

## Ne yapar?

- GitHub reposunu projeye ekleme ve onboarding akışını yönetir
- Team Lead, Product Owner, UI/UX Designer, Frontend Developer, Backend Developer ve Tester rollerini kurgular
- Plan, gereksinim, mimari, görev kırılımı ve test stratejisi belgelerini yönlendirir
- Görevleri rol bazlı dağıtır
- Test tamamlanmadan görevi done saymaz
- Mevcut yapıyı bozmadan, katmanlı ve geri dönülebilir değişiklik akışı uygular
- Üç hata sonrası kullanıcıya seçenekli özet sunar
- Mümkünse terminal panellerini rol bazlı adlandırılmış şekilde kurar

## Claude Code'a nasıl dahil edilir?

1. Bu skill klasörünü `skill.zip` olarak paketleyin.
2. Skill'i GitHub reposuna yükleyin veya doğrudan saklayın.
3. Claude Code içinde skill ekleme akışında bu paketi kullanın.
4. Skill aktif olduktan sonra örnek istemlerden biriyle başlatın.

## Örnek promptlar

- Şu GitHub reposunu projeye ekle ve ekibi kur.
- Bu repoyu analiz et, docs altında planı çıkar, sonra görevlere bölelim.
- Bu projede yeni özellik ekle ama mevcut yapıyı bozma, katmanlı ilerle.
- Panel bazlı ekip düzeni kur ve Team Lead üzerinden yönet.
- Frontend, backend ve tester görevlerini ayır; test bitmeden işi tamamlanmış sayma.

## Davranış kuralları

- Tüm iletişim Team Lead üzerinden yürür.
- Yeni projede başlangıç dosyaları için ayrıca izin istenmez.
- Mevcut projede yalnızca kritik belirsizliklerde soru sorulur.
- Kapsam dışına çıkılmaz.
- Breaking change riski kullanıcıya raporlanır.
- Değişiklikler geri dönülebilir şekilde yapılır.
- Test başarısızsa görev done sayılmaz.

## Klasör ve rol yetkileri

- `frontend/` → Frontend Developer yazar
- `backend/` → Backend Developer yazar
- `tests/` → Tester yazar
- `docs/` → Team Lead koordinasyonunda plan ve dokümantasyon
- Herkes diğer klasörleri okuyabilir ama kendi alanı dışına yazamaz
