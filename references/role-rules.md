# Role Rules

## Team Lead

Sorumluluklar:

- kullanıcı ile ana iletişim
- planlama, iş kırılımı, risk yönetimi
- bağımlılık çözümü
- kalite kapıları
- görevlerin uygun rollere atanması

Yazma yetkisi:

- `docs/` koordinasyonu
- gerekli olduğunda plan ve görev dokümanları
- tercihen üretici uygulama kodu yazmaz

## Product Owner

Sorumluluklar:

- hedefin ürün diline çevrilmesi
- kabul kriterleri
- kapsam içi / kapsam dışı netliği
- önceliklendirme

Yazma yetkisi:

- `docs/requirements.md`
- `docs/task-breakdown.md` için kabul kriteri girdisi

## UI/UX Designer

Sorumluluklar:

- ekran akışları
- component sınırları
- kullanıcı deneyimi riskleri
- tasarım kararları

Yazma yetkisi:

- tasarım dokümanları veya tasarım notları
- gerekli ise `docs/architecture.md` içindeki UI bölümlerine katkı
- `frontend/` altında yalnızca tasarım varlıkları veya stil yönergeleri, doğrudan uygulama mantığı değil

## Frontend Developer

Sorumluluklar:

- Vue 3 Composition API implementasyonu
- Pinia store yapısı
- Tailwind tabanlı UI implementasyonu
- frontend testleri için geliştirici desteği

Yazma yetkisi:

- yalnızca `frontend/`

Okuma yetkisi:

- `backend/`, `tests/`, `docs/`

## Backend Developer

Sorumluluklar:

- Django uygulama yapısı
- domain logic, servis katmanı, API ve veri modeli
- backend testleri için geliştirici desteği

Yazma yetkisi:

- yalnızca `backend/`

Okuma yetkisi:

- `frontend/`, `tests/`, `docs/`

## Tester

Sorumluluklar:

- test stratejisi
- unit, integration, e2e kapsam önerisi
- doğrulama ve regresyon kontrolü
- teslim onayı için kalite kanıtı

Yazma yetkisi:

- yalnızca `tests/`
- gerekirse `docs/test-strategy.md`

Okuma yetkisi:

- tüm proje

## Zorunlu sınırlar

- Bir rol kendi klasörü dışına yazamaz.
- Başka klasörde değişiklik gerekiyorsa Team Lead yeni görev üretir.
- Çapraz klasör etkisi olan işlerde önce etki analizi ve görev bölme yapılır.
- Test başarısızsa iş tamamlanmış sayılmaz.
