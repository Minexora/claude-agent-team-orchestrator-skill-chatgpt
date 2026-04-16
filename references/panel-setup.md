# Panel Setup

Amaç: Claude Code içinde ekip üyelerini görünür şekilde ayırmak ve her paneli net rol adıyla etiketlemek.

## Hedef panel adları

- Team Lead
- Product Owner
- UI/UX Designer
- Frontend Developer
- Backend Developer
- Tester

## Davranış kuralı

1. Önce ortamın panel bölme veya çoklu terminal desteğini kontrol et.
2. Destek varsa panelleri otomatik oluşturmayı dene.
3. Her paneli ilgili rol adıyla isimlendir.
4. Rol başına tek bir ana panel kullan.
5. Panel oluşturma otomatik değilse kullanıcıya manuel kurulum için kısa ve uygulanabilir adımlar ver.

## Fallback davranışı

Otomatik panel kurulumu mümkün değilse şu formatta çıktı ver:

- Oluşturulacak panel adı
- Rolün görevi
- Bu panelde yürütülecek ana iş türü

## Örnek panel amaçları

### Team Lead

- planlama
- koordinasyon
- bağımlılık takibi
- kullanıcı ile karar noktaları

### Product Owner

- gereksinim netleştirme
- kabul kriterleri
- task kapsamı

### UI/UX Designer

- ekran akışı
- component kararları
- etkileşim notları

### Frontend Developer

- Vue implementasyonu
- store ve component geliştirme

### Backend Developer

- Django servis ve API geliştirme

### Tester

- test senaryoları
- regresyon kontrolü
- doğrulama raporu
