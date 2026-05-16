# libopencm3 (patched branch)

Ця гілка призначена для змін і виправлень, які не приймаються в основний репозиторій проєкту.
Вона створена переважно для моїх власних проєктів.

## Важливі обмеження

- Підтримка цієї гілки не гарантується.
- Підтримка всіх мікроконтролерів, які підтримує основний проєкт, не гарантується.
- Сумісність з основним проєктом не гарантується.

## Планується

- Відновити збірку документації (зламана в оригінальному проєкті).
- Додати github actions для автоматичного тестування та збірки бібліотеки.
- Покращити підтримку тих мікроконтролерів, які я використовую (зокрема `stm32f446ret6`).
- Покращити систему збірки бібліотеки (видалити `make`).
- Видалити зайві/застарілі файли.

## Збірка через Meson

### Передумови

Потрібно мати встановлені:

- `meson`
- `ninja`
- ARM toolchain `arm-none-eabi-gcc` (та супутні `arm-none-eabi-ar`, `arm-none-eabi-objcopy`, тощо)

У репозиторії вже є cross-file для bare-metal ARM:

- `cross-files/arm-none-eabi.ini`

### Налаштування (configure)

1. У корені репозиторію виконайте:

```bash
meson setup build --cross-file cross-files/arm-none-eabi.ini -Dtarget=all
```

2. Для перебудови конфігурації без видалення каталогу `build`:

```bash
meson setup build --reconfigure --cross-file cross-files/arm-none-eabi.ini -Dtarget=all
```

### Компіляція

```bash
meson compile -C build
```

### Приклад збірки тільки для однієї сім'ї MCU

```bash
meson setup build-stm32f4 --cross-file cross-files/arm-none-eabi.ini -Dtarget=stm32f4
meson compile -C build-stm32f4
```

### Доступні значення `-Dtarget`

На поточний момент:

- `all`
- `stm32f0`
- `stm32f1`
- `stm32f3`
- `stm32f4`
- `stm32f7`
- `stm32l4`
- `lm4f`

Примітка: проєкт очікує саме cross-build і компілятор GCC.
