<!--
  Este archivo lo genera scripts/build_readme.py a partir de README.template.es.md, data/*.json y data/i18n/es.json.
  Edita la plantilla o los datos y luego ejecuta: python3 scripts/build_readme.py
  Palabras clave: prompts nsfw, prompts de imagen ia nsfw, prompts para ia de adultos, generador de imágenes ia sin censura,
  prompts para imágenes sin censura, generador de prompts nsfw, prompts para editar imágenes con ia, editor de imágenes ia sin censura,
  imagen a prompt nsfw, prompts boudoir ia, prompts anime nsfw, prompts hentai ia, prompts qwen image, prompts seedream nsfw,
  prompts z-image, nsfw ai image prompts, nsfw prompts, uncensored ai image prompts, nsfw image prompt generator,
  nsfw image to prompt, nsfw ai image editor prompts, uncensored ai image generator
-->

<p align="center"><a href="README.md">English</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.fr.md">Français</a> · <b>Español</b> · <a href="README.ru.md">Русский</a></p>

<h1 align="center">NSFW AI Image Prompts</h1>

<p align="center">
  <b>104 prompts de imagen con IA NSFW para copiar y pegar (incluidos 15 prompts de edición sin censura) y 72 resultados reales junto a los prompts que los generaron, para Qwen Image 2.1, Seedream 5.0, Qwen Image 3.0 Pro, Z-Image Spicy y otros modelos de imagen sin censura.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/image%20prompts-104-ff4d6d" alt="104 prompts de imagen">
  <img src="https://img.shields.io/badge/edit%20prompts-15-8b5cf6" alt="15 prompts de edición">
  <img src="https://img.shields.io/badge/showcase-72-10b981" alt="72 ejemplos reales">
  <img src="https://img.shields.io/badge/updated-2026-09-27-blue" alt="Actualizado: 2026-09-27">
  <img src="https://img.shields.io/badge/18%2B-adults%20only-red" alt="18+">
</p>

<p align="center">
  <a href="#mejores-modelos-para-imágenes-nsfw">Modelos</a> ·
  <a href="#ejemplos-reales-resultados-y-sus-prompts">Ejemplos</a> ·
  <a href="#los-prompts">Prompts</a> ·
  <a href="#de-imagen-nsfw-a-prompt">Imagen → prompt</a> ·
  <a href="#guía-rápida">Guía rápida</a> ·
  <a href="#ejecuta-un-prompt-en-60-segundos">Ejecutar</a> ·
  <a href="#preguntas-frecuentes">Preguntas frecuentes</a>
</p>

> **Solo para mayores de 18 años. Todos los personajes de este repositorio son adultos.** Los prompts indican una edad adulta y evitan a propósito las descripciones que sugieran juventud. Los prompts de edición son para imágenes tuyas, de adultos que den su consentimiento o de personajes ficticios que hayas generado. Nunca los uses para "desvestir" o sexualizar la foto de una persona real. Consulta las [Reglas](#reglas).

> Lo mantiene el equipo de [SpicyAPI](https://spicyapi.ai/es?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=disclosure-es), donde puedes ejecutar todos los prompts de aquí. Los prompts son texto plano y funcionan con cualquier modelo de imagen que los acepte.

---

## Por qué existe este repositorio

La mayoría de las listas de prompts NSFW son montones de etiquetas de la época de Stable Diffusion. Los modelos de imagen actuales (Qwen Image, Seedream, Z-Image) leen **frases completas**: quién aparece, qué lleva puesto, dónde está, la luz, el objetivo. Todos los prompts de aquí están escritos así e incluyen:

- el **modelo** para el que se escribió, elegido a partir de los resultados de prueba publicados por SpicyAPI,
- los **ajustes** exactos (relación de aspecto, resolución o tamaño, y el LoRA cuando se usa),
- el **costo de una imagen** con los precios actuales del catálogo,
- un **consejo** que explica por qué funciona.

Los consejos son recomendaciones prácticas, no resultados de benchmarks. Los [ejemplos reales](#ejemplos-reales-resultados-y-sus-prompts) son la parte de este repositorio con resultados reales.

## Contenido

- [Mejores modelos para imágenes NSFW](#mejores-modelos-para-imágenes-nsfw)
- [Ejemplos reales: resultados y sus prompts](#ejemplos-reales-resultados-y-sus-prompts)
- [Cómo escribir un prompt de imagen NSFW](#cómo-escribir-un-prompt-de-imagen-nsfw)
- [Los prompts](#los-prompts)
  - [Boudoir y dormitorio](#boudoir-y-dormitorio) (15)
  - [Lencería y editorial de moda](#lencería-y-editorial-de-moda) (10)
  - [Desnudo artístico y estudio de la figura](#desnudo-artístico-y-estudio-de-la-figura) (12)
  - [Parejas e intimidad](#parejas-e-intimidad) (10)
  - [Contenido de creadores y selfis](#contenido-de-creadores-y-selfis) (10)
  - [Fantasía, ciencia ficción y cosplay](#fantasía-ciencia-ficción-y-cosplay) (10)
  - [Anime e ilustración (Qwen Image 2.1 LoRA)](#anime-e-ilustración-qwen-image-21-lora) (10)
  - [Boudoir masculino y fitness](#boudoir-masculino-y-fitness) (6)
  - [Portadas, pósteres y rotulación](#portadas-pósteres-y-rotulación) (6)
  - [Prompts para editar imágenes sin censura](#prompts-para-editar-imágenes-sin-censura) (15)
- [De imagen NSFW a prompt](#de-imagen-nsfw-a-prompt)
- [Guía rápida](#guía-rápida)
- [Ejecuta un prompt en 60 segundos](#ejecuta-un-prompt-en-60-segundos)
- [Deja que un LLM escriba tus prompts](#deja-que-un-llm-escriba-tus-prompts)
- [De imagen a video](#de-imagen-a-video)
- [Preguntas frecuentes](#preguntas-frecuentes)
- [Reglas](#reglas)

---

## Mejores modelos para imágenes NSFW

Recomendaciones probadas, sacadas de las [clasificaciones públicas de SpicyAPI](https://spicyapi.ai/es/leaderboards?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=picks-es) (metodología v2.1, 2026-09-27):

- **[Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=picks-es)** (recomendado): Spicy Index 73, Freedom 96.3, desde $0.024 por imagen. Prompts largos (hasta 5000 caracteres), 15 relaciones de aspecto y edición a partir de 1 a 10 imágenes de referencia dentro de la misma familia.
- **[Qwen Image 2.1 LoRA](https://spicyapi.ai/es/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=picks-es)**: #1 en el Spicy Index de imagen (80.5), Freedom 92. Hasta tres LoRAs; aquí se usa en todos los prompts de anime.
- **[MiniMax H3 Image LoRA](https://spicyapi.ai/es/models/minimax-h3-image-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=picks-es)**: Freedom 100, generó todos los prompts de prueba explícitos; trae tu propio LoRA.
- **[Seedream 5.0 Pro](https://spicyapi.ai/es/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=picks-es)**: Freedom 94.3, el acabado más "fotográfico" para looks editoriales y de campaña.
- **[Qwen Image 3.0 Pro](https://spicyapi.ai/es/models/qwen-image-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=picks-es)**: Freedom 98, la mejor opción cuando la imagen lleva texto (portadas, pósteres).
- **🌶️ [Z-Image Spicy](https://spicyapi.ai/es/models/z-image-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=picks-es)**: Freedom 98.8 a $0.01235, el más barato para borradores y grandes volúmenes; anatomía más floja.
- No recomendados para NSFW: Krea 2 (Freedom 10), Wan 2.7 de texto a imagen (suaviza casi siempre los desnudos), FLUX.1 Dev LoRA (explícito 0/6). Prefect Pony XL todavía tiene muy pocos datos de prueba.

Todos los modelos de imagen sin censura, en el orden del catálogo (primero los más populares). ✅ Freedom 90+ · ◐ 70–89 · ⚠️ menos de 70 · 🧪 menos de 15 pruebas.

| Modelo | Tipo | Tareas | Desde | Spicy Index | Freedom |
|---|---|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=model-table-es) | Estándar | Edit, T2I | $0.024/imagen | 73 | ✅ 96.3 |
| [Qwen Image 2.1 LoRA](https://spicyapi.ai/es/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=model-table-es) | Estándar | Edit, T2I | $0.03/imagen | 80.5 | ✅ 92 |
| [MiniMax H3 Image LoRA](https://spicyapi.ai/es/models/minimax-h3-image-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=model-table-es) | Estándar | Edit, T2I | $0.042/imagen | 74.5 | ✅ 100 |
| [Qwen Image 3.0 Pro](https://spicyapi.ai/es/models/qwen-image-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=model-table-es) | Estándar | Edit, T2I | $0.04/imagen | 56 | ✅ 98 |
| [Qwen Image 3.0](https://spicyapi.ai/es/models/qwen-image-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=model-table-es) | Estándar | Edit, T2I | $0.03/imagen | 56 | ✅ 96 |
| [Seedream 5.0 Pro](https://spicyapi.ai/es/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=model-table-es) | Estándar | Edit, T2I | $0.036/imagen | 73 | ✅ 94.3 |
| [Qwen Image Edit Spicy](https://spicyapi.ai/es/models/qwen-image-spicy-edit?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=model-table-es) | 🌶️ Spicy | Edit | $0.038/imagen | 14 | ✅ 96 |
| [Seedream 5.0 Lite](https://spicyapi.ai/es/models/seedream-5-0-lite?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=model-table-es) | Estándar | Edit, T2I | $0.0345/imagen | 73 | ✅ 96 |
| [Qwen Image 2](https://spicyapi.ai/es/models/alibaba-qwen-image-2?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=model-table-es) | Estándar | Edit, T2I | $0.035/imagen | 34 | ✅ 96.7 |
| [Qwen Image 2512 LoRA](https://spicyapi.ai/es/models/qwen-image-2512-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=model-table-es) | Estándar | Edit, T2I | $0.03/imagen | 50.5 | ✅ 92.5 |
| [Z-Image Spicy Pro](https://spicyapi.ai/es/models/z-image-spicy-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=model-table-es) | 🌶️ Spicy | T2I | $0.019/imagen | 38 | ✅ 100 |
| [Z-Image Spicy](https://spicyapi.ai/es/models/z-image-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=model-table-es) | 🌶️ Spicy | T2I | $0.01235/imagen | 32 | ✅ 98.8 |
| [Z-Image](https://spicyapi.ai/es/models/z-image?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=model-table-es) | Estándar | T2I | $0.01/imagen | 17 | ✅ 100 |
| [Z-Image Turbo LoRA](https://spicyapi.ai/es/models/z-image-turbo-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=model-table-es) | Estándar | Edit, T2I | $0.012/imagen | 46.5 | ✅ 95 |
| [Seedream 4.0](https://spicyapi.ai/es/models/seedream-4-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=model-table-es) | Estándar | Edit, T2I | $0.03/imagen | 74 | ◐ 74.7 |
| [Prefect Pony XL](https://spicyapi.ai/es/models/prefect-pony-xl?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=model-table-es) | Estándar | T2I | $0.015/imagen | 30 | 🧪 36 |
| [FLUX.1 Dev LoRA](https://spicyapi.ai/es/models/flux-1-dev-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=model-table-es) | Estándar | T2I | $0.018/imagen | 32.5 | ◐ 75 |

---

## Ejemplos reales: resultados y sus prompts

72 casos reales sacados de las páginas de los modelos y de la [biblioteca de prompts](https://spicyapi.ai/es/prompts?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es) de SpicyAPI, cada uno generado con el modelo indicado. Cada caso muestra un resultado junto al prompt exacto que lo generó; los casos de edición también muestran la imagen de entrada. Los modelos aparecen de más a menos popular. Haz clic en una imagen para verla en tamaño completo.

### Qwen Image 2.1

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Vista previa no disponible en GitHub.<br><a href="https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es">Míralo en spicyapi.ai</a></sub></td><td valign="top"><b>Slats slip dress</b><br><sub><code>alibaba/qwen-image-2.1/edit</code></sub><br><br>Keep the bed, the linen, the blinds, the striped light and her pose exactly as they are. Dress her in a sheer ivory slip that the striped light passes through, the strap fallen off one shoulder, the hem gathered at her thigh. Match the existing grain, colour grade and the way the sun falls across the fabric. Change nothing else in the frame.</td></tr>
<tr><td width="250" align="center" valign="top"><sub>Vista previa no disponible en GitHub.<br><a href="https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es">Míralo en spicyapi.ai</a></sub></td><td valign="top"><b>Boudoir window slats</b><br><sub><code>alibaba/qwen-image-2.1/text-to-image</code></sub><br><br>Photograph of an adult woman lying on her side across rumpled white linen, seen from behind, one arm folded under her head and a sheet gathered across her hip. Late morning sun through venetian blinds lays hard parallel stripes across her back, her shoulder and the bedding. Medium-format film look, soft grain, honey and cream palette, warm skin against cool shadow. Calm and unposed.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/9026afbc1b31b054.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/9026afbc1b31b054.webp" alt="Lace and lamplight" width="230"></a></td><td valign="top"><b>Lace and lamplight</b><br><sub><code>alibaba/qwen-image-2.1/text-to-image</code></sub><br><br>Low-key studio portrait of an adult woman kneeling on a dark velvet chaise in a black lace bodysuit and sheer stockings, seen from behind, looking back over her shoulder. A single hard lamp from the left gives one edge of her body and drops the rest to near black; lace texture catches the light where it crosses her spine. 85mm, shallow depth of field, heavy grain, oxblood and black.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/076b9798c6725479.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/076b9798c6725479.webp" alt="Dawn to candlelight" width="230"></a></td><td valign="top"><b>Dawn to candlelight</b><br><sub><code>alibaba/qwen-image-2.1/edit</code></sub><br><br>Keep both figures, the bed, their poses and the framing exactly as they are. Change the dawn window light to a single group of candles on the left nightstand: warm flickering light raking low across both bodies, the room falling to deep amber and black behind them, highlights only along the edges of skin and sheet. Keep the shadows consistent with the new light source.<br><sub>Imagen(es) de entrada:</sub> <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/5be97dddae40fea1.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/5be97dddae40fea1.webp" width="60" alt="input"></a></td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/5be97dddae40fea1.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/5be97dddae40fea1.webp" alt="Two figures one sheet" width="230"></a></td><td valign="top"><b>Two figures one sheet</b><br><sub><code>alibaba/qwen-image-2.1/text-to-image</code></sub><br><br>Intimate two-figure composition on a bed at dawn: a woman lying on her back with her eyes closed, the white sheet drawn up and gathered across her chest and tucked under her arms, and a man beside her propped on one elbow, bare shoulders above the sheet, his hand resting on the sheet over her stomach. Cool blue window light from the left, one warm bedside lamp still on behind them. Skin tones held apart by the two light sources. Shallow focus, fine grain, unhurried and quiet, tasteful and covered.</td></tr>
<tr><td width="250" align="center" valign="top"><sub>Vista previa no disponible en GitHub.<br><a href="https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es">Míralo en spicyapi.ai</a></sub></td><td valign="top"><b>Two references one chaise</b><br><sub><code>alibaba/qwen-image-2.1/edit</code></sub><br><br>Merge the two references into a single frame. Place the woman from the first image, lying on her side in the same pose, on the dark velvet chaise from the second image. Keep her face and body from the first reference, and the chaise, the single hard lamp and the oxblood palette from the second. Cinematic, shallow depth of field, heavy film grain.</td></tr>
</table>

### Qwen Image 2.1 LoRA

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Vista previa no disponible en GitHub.<br><a href="https://spicyapi.ai/es/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es">Míralo en spicyapi.ai</a></sub></td><td valign="top"><b>Boudoir into anime</b><br><sub><code>alibaba/qwen-image-2.1-lora/edit</code></sub><br><br>Transform into anime. Flat cel shading, clean linework, anime illustration. Keep her pose, the sheet across her hip, the bed, the blinds and the striped direction of the light.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/aa7226a5cb0b02ab.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/aa7226a5cb0b02ab.webp" alt="Anime boudoir lora" width="230"></a></td><td valign="top"><b>Anime boudoir lora</b><br><sub><code>alibaba/qwen-image-2.1-lora/text-to-image</code></sub><br><br>storybook anime illustration of an adult woman reclining across rumpled linen in a sunlit attic room, seen from behind over her bare back and shoulder, one arm folded behind her head, a sheet drawn up across her hip and waist. Morning light through a slatted window falling in stripes across her back. Soft cel-shaded figure, warm hand-painted background, honey and cream palette, tasteful and covered.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/4b43e7a4c1c22600.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/4b43e7a4c1c22600.webp" alt="Relight the chaise" width="230"></a></td><td valign="top"><b>Relight the chaise</b><br><sub><code>alibaba/qwen-image-2.1-lora/edit</code></sub><br><br>Relight the scene: a low warm candle cluster from the right at mattress level and cool blue moonlight through a window behind her. Keep her pose, the lace, the chaise and the framing unchanged.<br><sub>Imagen(es) de entrada:</sub> <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/9026afbc1b31b054.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/9026afbc1b31b054.webp" width="60" alt="input"></a></td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/fc557b745f18eaa8.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/fc557b745f18eaa8.webp" alt="Watercolor lace lora" width="230"></a></td><td valign="top"><b>Watercolor lace lora</b><br><sub><code>alibaba/qwen-image-2.1-lora/text-to-image</code></sub><br><br>watercolor anime of an adult woman kneeling on a dark velvet chaise in a black lace bodysuit and sheer stockings, seen from behind, glancing back over her shoulder. Transparent washes, pale paper texture, a single warm lamp from the left leaving most of the figure in deep wash, oxblood and ink.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/00a929d320ae30f7.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/00a929d320ae30f7.webp" alt="Impressionist bathers lora" width="230"></a></td><td valign="top"><b>Impressionist bathers lora</b><br><sub><code>alibaba/qwen-image-2.1-lora/text-to-image</code></sub><br><br>Monet Style, two bathers at the edge of a still pond at first light, both seen from behind — one seated on the bank wrapped in a pale towel with her bare shoulders showing, one standing waist-deep in the water with her back to us. Mist dissolving the far shore, loose impressionist brushwork, dappled light on wet skin and towel, pastel palette.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/201aee2b06812453.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/201aee2b06812453.webp" alt="Next scene after dark" width="230"></a></td><td valign="top"><b>Next scene after dark</b><br><sub><code>alibaba/qwen-image-2.1-lora/edit</code></sub><br><br>Next Scene: hours later, exactly the same two people — one woman and one man, no other figures in the room — asleep and turned toward each other under the same sheet on the same bed. The window has gone full dark and only the low bedside lamp is still burning. Same framing, same bedding, same lens, same two faces.<br><sub>Imagen(es) de entrada:</sub> <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/5be97dddae40fea1.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/5be97dddae40fea1.webp" width="60" alt="input"></a></td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/6c0bbae0930616ba.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/6c0bbae0930616ba.webp" alt="Two weights stacked" width="230"></a></td><td valign="top"><b>Two weights stacked</b><br><sub><code>alibaba/qwen-image-2.1-lora/text-to-image</code></sub><br><br>watercolor anime of an adult woman stepping out of a claw-foot bath in a winter bathroom at dusk, seen from behind, steam rising and fogging the window, a large towel wrapped and held at her chest with her bare back and shoulders showing, warm lamplight behind fogged glass, transparent washes, pale paper texture, soft ink linework.</td></tr>
</table>

### MiniMax H3 Image LoRA

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/minimax-h3-image-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-image-lora/e290cf84e4acb5af.webp"><img src="https://cdn.spicyapi.ai/models/examples/minimax-h3-image-lora/e290cf84e4acb5af.webp" alt="Same woman new scene" width="230"></a></td><td valign="top"><b>Same woman new scene</b><br><sub><code>minimax/h3-image-lora/edit</code></sub><br><br>Picture 1 is the woman. Put her on a sunlit balcony in a white linen shirt, wind in her hair, late afternoon light. Keep her face and hairstyle.<br><sub>Imagen(es) de entrada:</sub> <a href="https://cdn.spicyapi.ai/models/examples/inputs/21de8c392ac051af.jpeg"><img src="https://cdn.spicyapi.ai/models/examples/inputs/21de8c392ac051af.jpeg" width="60" alt="input"></a></td></tr>
</table>

### Qwen Image 3.0 Pro

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/qwen-image-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3.0-pro/3e2e7cb4bb7e5476.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-3.0-pro/3e2e7cb4bb7e5476.webp" alt="A woman with her eyes closed sprays perfume at her neck, the mist glowing in backlight, with the line THE HOUR BEFORE set in the empty space to the right." width="230"></a></td><td valign="top"><b>Perfume ad with a one-line tagline in the negative space</b><br><sub><code>alibaba/qwen-image-3.0-pro/text-to-image</code></sub><br><br>Cinematic beauty still, perfume advertising spread. The instant a perfume is sprayed at the side of a woman&#x27;s throat, the mist still suspended above the skin, her chin lifted and eyes closed; soft backlight turns the mist into a halo. One line of elegant type set in the negative space on the right reading THE HOUR BEFORE. 100mm macro, very shallow depth of field, heavy grain, champagne and shadow palette, restrained and tasteful.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3.0-pro/545482ab5f890d6f.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-3.0-pro/545482ab5f890d6f.webp" alt="The same perfume advertisement with its tagline changed to AFTER MIDNIGHT, the pose, mist and lighting left as they were." width="230"></a></td><td valign="top"><b>Retype an ad tagline without touching the picture</b><br><sub><code>alibaba/qwen-image-3.0-pro/edit</code></sub><br><br>Cast: one woman. Take this advertising frame and retype the line in the negative space to read AFTER MIDNIGHT. Change nothing else: keep the pose, the suspended mist, the lighting and the grain exactly as they are.<br><sub>Imagen(es) de entrada:</sub> <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3.0-pro/3e2e7cb4bb7e5476.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-3.0-pro/3e2e7cb4bb7e5476.webp" width="60" alt="input"></a></td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0-pro/ad46353eca0136c7.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0-pro/ad46353eca0136c7.webp" alt="A moody portrait of a woman in a dark green blazer with the cover line AFTER HOURS in small spaced capitals at the bottom left." width="230"></a></td><td valign="top"><b>Swap a magazine cover line, keeping the portrait intact</b><br><sub><code>alibaba/qwen-image-3.0-pro/edit</code></sub><br><br>Keep the portrait, wardrobe, lighting and grade exactly as they are. Change the cover line from &#x27;THE LATE SHIFT&#x27; to &#x27;AFTER HOURS&#x27; in the same small caps and the same position, and leave the masthead untouched.<br><sub>Imagen(es) de entrada:</sub> <a href="https://cdn.spicyapi.ai/models/examples/inputs/5f610609bb5dd6a5.png"><img src="https://cdn.spicyapi.ai/models/examples/inputs/5f610609bb5dd6a5.png" width="60" alt="input"></a></td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0-pro/bbfab34deec5085a.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0-pro/bbfab34deec5085a.webp" alt="Fashion magazine cover with a large condensed SPICY masthead and small-caps cover lines over a studio portrait" width="230"></a></td><td valign="top"><b>Fashion magazine cover with masthead and cover lines</b><br><sub><code>alibaba/qwen-image-3.0-pro/text-to-image</code></sub><br><br>A glossy fashion magazine cover, full-bleed portrait of an adult woman in a black lace bodysuit under a sheer open kimono, arms raised adjusting her hair, studio rim light on a deep charcoal background; masthead text &#x27;SPICY&#x27; in large condensed type across the top, cover lines reading &#x27;THE LATE SHIFT&#x27; and &#x27;ISSUE 07&#x27; in small caps, high-end print typography, razor-sharp 2K detail.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0-pro/e08fa83007734f3b.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0-pro/e08fa83007734f3b.webp" alt="Night motel forecourt: a woman in a translucent pink rain poncho by a lit vending machine under a neon VACANCY sign reading POOL, ICE, CABLE TV" width="230"></a></td><td valign="top"><b>Neon VACANCY motel sign and amenity board, both legible</b><br><sub><code>alibaba/qwen-image-3.0-pro/text-to-image</code></sub><br><br>Neon-drenched night photograph outside a roadside motel. An adult woman in a translucent pink rain poncho worn over a black bikini stands in the glow of a humming vending machine, holding a cold can against her cheek and looking sideways at the camera. Behind her a tall motel sign reads &#x27;VACANCY&#x27; in pink neon script with a smaller board underneath reading &#x27;POOL • ICE • CABLE TV&#x27;. Wet asphalt reflections, magenta and cyan, moths in the light, razor-sharp signage typography, 2K detail.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0-pro/098445b2705a7762.png"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0-pro/098445b2705a7762.png" alt="A woman in a loose indigo kimono over a camisole kneels beside a low table in a lantern-lit tatami room with paper screens." width="230"></a></td><td valign="top"><b>Place a portrait in a lantern-lit tatami room, in an indigo kimono</b><br><sub><code>alibaba/qwen-image-3.0-pro/edit</code></sub><br><br>Keep the face, hair and pose from the first image. Dress her in a deep indigo silk kimono worn loose off both shoulders over a matching camisole, and place her kneeling beside the low table in the second image&#x27;s machiya room. Relight her with the warm paper-lantern glow from the screens behind, keeping the second image&#x27;s green-cyan shadow cast so both read as one photograph.<br><sub>Imagen(es) de entrada:</sub> <a href="https://cdn.spicyapi.ai/models/examples/inputs/87ce5292f52a0c1b.png"><img src="https://cdn.spicyapi.ai/models/examples/inputs/87ce5292f52a0c1b.png" width="60" alt="input"></a> <a href="https://cdn.spicyapi.ai/models/examples/inputs/9d7ff897cbbe08af.jpeg"><img src="https://cdn.spicyapi.ai/models/examples/inputs/9d7ff897cbbe08af.jpeg" width="60" alt="input"></a></td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0-pro/9ad98997e355a094.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0-pro/9ad98997e355a094.webp" alt="First-person view down a bed on a grey morning: legs in black socks on a white duvet and a handwritten note propped against a coffee cup on the nightstand." width="230"></a></td><td valign="top"><b>POV morning in bed with a legible handwritten note</b><br><sub><code>alibaba/qwen-image-3.0-pro/text-to-image</code></sub><br><br>First-person point of view photograph looking down the bed on a grey morning, soft window light, shallow depth of field. In the foreground on a rumpled white duvet lie a woman&#x27;s smooth bare crossed ankles in black over-the-knee socks, slim feminine calves, and a black lace slip draped over the corner of the bed. On the nightstand just beyond, a handwritten note is propped against a coffee cup, the handwriting large and perfectly legible in blue ink: &quot;GONE FOR COFFEE — DON&#x27;T MOVE. BACK IN TEN. — J&quot;. Beside it a brass key and a paperback face-down. Muted grey-green palette, real 35mm grain, razor-sharp handwriting, no logos, no brand names.</td></tr>
</table>

### Qwen Image 3.0

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/qwen-image-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3.0/7a046426d3e70c90.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-3.0/7a046426d3e70c90.webp" alt="Chalk handwriting reading TODAY’S DRAUGHT – MOONWELL on a rain-beaded shop window, behind it a woman holding up a glowing green potion bottle." width="230"></a></td><td valign="top"><b>Chalk lettering on a rainy apothecary window at night</b><br><sub><code>alibaba/qwen-image-3.0/text-to-image</code></sub><br><br>Cinematic film still, an apothecary shop window at night. Chalk handwriting on the glass reads TODAY&#x27;S DRAUGHT - MOONWELL; behind it a woman tilts a glowing potion bottle, one camisole strap slipped to her elbow, the liquid&#x27;s green light thrown up under her jaw. Rain beads on the outside of the glass. 35mm, shallow depth of field, heavy grain, potion green against night blue, restrained and tasteful.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3.0/65565e51cbb615be.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-3.0/65565e51cbb615be.webp" alt="A man in a soaked, open overcoat stands in a rainy neon alley under a sign reading LATE HOURS, one hand on a wet shop window." width="230"></a></td><td valign="top"><b>Merge a portrait and a storefront, then retype the sign</b><br><sub><code>alibaba/qwen-image-3.0/edit</code></sub><br><br>Cast: one man. Merge these two references into one frame: place the figure from the first image in the doorway of the storefront from the second, at night in the rain, neon running down a wet overcoat, and change the shop sign to read LATE HOURS. The soaked overcoat clings and hangs open over bare skin, collar turned up against the rain, medium close. Cinematic, shallow depth of field, heavy film grain.<br><sub>Imagen(es) de entrada:</sub> <a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/36b1a32feba49df3.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy/36b1a32feba49df3.webp" width="60" alt="input"></a> <a href="https://cdn.spicyapi.ai/models/examples/alibaba-qwen-image-2/9944fb81c5b817b4.webp"><img src="https://cdn.spicyapi.ai/models/examples/alibaba-qwen-image-2/9944fb81c5b817b4.webp" width="60" alt="input"></a></td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0/39fb6ffcab5965d8.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0/39fb6ffcab5965d8.webp" alt="The words WAIT UP FOR ME written in red lipstick on a steamed bathroom mirror beside the reflection of a woman wrapped in a towel." width="230"></a></td><td valign="top"><b>Add lipstick lettering to a fogged bathroom mirror</b><br><sub><code>alibaba/qwen-image-3.0/edit</code></sub><br><br>Keep the bathroom, the mirror, the steam, the woman&#x27;s reflection, the basin, the lighting and the whole composition exactly as they are. On the blank fogged area of the mirror to the left of her reflection, add two lines of writing drawn in bold red lipstick, thick glossy strokes with clear dark glass showing through where the fog is wiped away, slightly dripping at the ends: the first line reads &#x27;WAIT UP&#x27; and the second line below reads &#x27;FOR ME&#x27;. The lettering is large, hand-drawn, neatly spelled and clearly legible, and catches the warm bathroom light. Change nothing else.<br><sub>Imagen(es) de entrada:</sub> <a href="https://cdn.spicyapi.ai/models/examples/inputs/5ff8dac975db638e.png"><img src="https://cdn.spicyapi.ai/models/examples/inputs/5ff8dac975db638e.png" width="60" alt="input"></a></td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0/fcc469278572a2f5.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0/fcc469278572a2f5.webp" alt="Woman in a navy satin slip dress on a hotel bed, a brass door hanger reading DO NOT DISTURB sharp in the foreground" width="230"></a></td><td valign="top"><b>DO NOT DISTURB door hanger in a moody hotel portrait</b><br><sub><code>alibaba/qwen-image-3.0/text-to-image</code></sub><br><br>Editorial photograph, an adult woman sitting on a hotel bed in a navy satin slip dress, city lights blurred through the window behind her, a brass door hanger hanging in sharp foreground reading &#x27;DO NOT DISTURB&#x27;, warm tungsten bedside lamp, cinematic 35mm, shallow focus, moody blue and amber palette.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0/a783301887d90ff5.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0/a783301887d90ff5.webp" alt="ROUND SIX and STILL STANDING drawn by fingertip on fogged glass in a locker room, a boxer with wrapped hands sitting on the bench beside it." width="230"></a></td><td valign="top"><b>Add fingertip lettering to a fogged locker-room window</b><br><sub><code>alibaba/qwen-image-3.0/edit</code></sub><br><br>Keep the woman, the bench, the lockers, the pose, the lighting and the whole composition exactly as they are. On the large fogged glass panel behind her, add big letters drawn with a fingertip through the condensation, clear dark glass showing through each stroke, reading &#x27;ROUND SIX&#x27; on the first line and &#x27;STILL STANDING&#x27; in smaller letters underneath, with faint water drips running down from the strokes. Change nothing else.<br><sub>Imagen(es) de entrada:</sub> <a href="https://cdn.spicyapi.ai/models/examples/inputs/84162b719b5f5709.png"><img src="https://cdn.spicyapi.ai/models/examples/inputs/84162b719b5f5709.png" width="60" alt="input"></a></td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0/5c9fd693a9294fc8.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0/5c9fd693a9294fc8.webp" alt="Woman in a green bandeau top and cream sarong among monstera leaves in a Victorian glasshouse, a shaft of sun through the glass roof" width="230"></a></td><td valign="top"><b>Swimwear editorial in a steamy Victorian glasshouse</b><br><sub><code>alibaba/qwen-image-3.0/text-to-image</code></sub><br><br>Fashion editorial photograph shot inside a humid Victorian glasshouse. An adult woman in an emerald bandeau bikini top and a sheer chiffon sarong knotted low on one hip stands among giant monstera leaves, one hand parting a frond, condensation fogging the glass panes behind her. Cool green ambient light cut by a single warm shaft from a broken pane, medium-format sharpness, magazine crop, botanical detail.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0/8d2f7c95974547a2.png"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0/8d2f7c95974547a2.png" alt="A woman in a sand-beige ribbed tube top and a long white linen skirt stands in a pale studio lit by a north window." width="230"></a></td><td valign="top"><b>Dress a portrait in a garment from a second image</b><br><sub><code>alibaba/qwen-image-3.0/edit</code></sub><br><br>Keep the face, hair, body and pose from the first image. Dress her in the sand-beige ribbed tube top from the second image, matching its rib texture and matte finish, and pair it with a floor-length chalk-white linen skirt. Keep the first image&#x27;s north-window light direction, cool grey-blue fill and desaturated grade unchanged.<br><sub>Imagen(es) de entrada:</sub> <a href="https://cdn.spicyapi.ai/models/examples/inputs/99478b4975952633.png"><img src="https://cdn.spicyapi.ai/models/examples/inputs/99478b4975952633.png" width="60" alt="input"></a> <a href="https://cdn.spicyapi.ai/models/examples/inputs/c1394b68801d3f85.png"><img src="https://cdn.spicyapi.ai/models/examples/inputs/c1394b68801d3f85.png" width="60" alt="input"></a></td></tr>
</table>

### Seedream 5.0 Pro

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Vista previa no disponible en GitHub.<br><a href="https://spicyapi.ai/es/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es">Míralo en spicyapi.ai</a></sub></td><td valign="top"><b>Bathhouse marble two</b><br><sub><code>bytedance/seedream-5.0-pro/text-to-image</code></sub><br><br>Cinematic film still, Roman marble bathhouse. Close two-shot on the stepped ledges: a woman on the upper step tips a brass basin of water over her shoulder and it sheets down her bare back, while the man on the step below watches from a hand&#x27;s breadth away, her knee almost at his chest; everything below the chest is lost in thick steam. One hard clerestory shaft cuts the vapour and catches wet skin and wet Carrara marble alike. 65mm, shallow depth of field, warm amber against stone grey, heavy grain, restrained and tasteful.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-5.0-pro/8f96701b135f64c0.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5.0-pro/8f96701b135f64c0.webp" alt="Champagne satin back" width="230"></a></td><td valign="top"><b>Champagne satin back</b><br><sub><code>bytedance/seedream-5.0-pro/text-to-image</code></sub><br><br>Cinematic film still, a woman sits at a tall window wrapped in champagne satin, seen entirely from behind so the frame is one unbroken line of back; the satin has slipped from the shoulder blade to the small of the back and pools there. Cold morning light from the window, warm lamp from inside. 85mm, shallow depth of field, heavy grain, champagne and slate palette, restrained and tasteful.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-5.0-pro/f6d4199b5b34eb3a.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5.0-pro/f6d4199b5b34eb3a.webp" alt="Face gown ballroom" width="230"></a></td><td valign="top"><b>Face gown ballroom</b><br><sub><code>bytedance/seedream-5.0-pro/edit</code></sub><br><br>Compose one frame from these three references: the face from the first, the open-backed gold gown from the second, the domed Byzantine hall from the third. She is walking away from camera and turning her head back; the candle stands along the aisle light her spine into a single gold line. Cinematic, shallow depth of field, heavy film grain.<br><sub>Imagen(es) de entrada:</sub> <a href="https://cdn.spicyapi.ai/models/examples/inputs/953656aeab446b5d.webp"><img src="https://cdn.spicyapi.ai/models/examples/inputs/953656aeab446b5d.webp" width="60" alt="input"></a> <a href="https://cdn.spicyapi.ai/models/examples/seedream-5.0-pro/8f96701b135f64c0.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5.0-pro/8f96701b135f64c0.webp" width="60" alt="input"></a> <a href="https://cdn.spicyapi.ai/models/examples/seedream-4.0/60d1a0037b703de4.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-4.0/60d1a0037b703de4.webp" width="60" alt="input"></a></td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-5-0-pro/5b4c16f28e9502f3.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5-0-pro/5b4c16f28e9502f3.webp" alt="Colour to monochrome relight" width="230"></a></td><td valign="top"><b>Colour to monochrome relight</b><br><sub><code>bytedance/seedream-5.0-pro/edit</code></sub><br><br>Keep the woman, her seated pose, her face and the framing exactly as they are. Convert the photograph to high-contrast black and white fine-art, relight it with a single hard key light from camera right so one side of her face and shoulder is bright and the other falls into deep shadow, and replace the cream cable-knit blanket with heavy wet black silk that clings and pools around her in sharp folds. Emphasise skin texture, the grain of the silk and the sculptural light. Deep blacks, luminous highlights, medium format monochrome.<br><sub>Imagen(es) de entrada:</sub> <a href="https://cdn.spicyapi.ai/models/examples/inputs/93760a36efffbd06.jpeg"><img src="https://cdn.spicyapi.ai/models/examples/inputs/93760a36efffbd06.jpeg" width="60" alt="input"></a></td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-5-0-pro/c8981a25695ad4d4.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5-0-pro/c8981a25695ad4d4.webp" alt="Wet beauty portrait" width="230"></a></td><td valign="top"><b>Wet beauty portrait</b><br><sub><code>bytedance/seedream-5.0-pro/text-to-image</code></sub><br><br>High-resolution beauty editorial photograph, close portrait of an adult woman with wet hair slicked back, water beading on her collarbone and bare shoulders, a heavy ivory silk robe slipping off one shoulder, arms folded across her chest, dramatic single softbox from camera left, glossy skin texture, deep black background, luxury fragrance campaign look.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-5-0-pro/e46bf30a84501996.jpeg"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5-0-pro/e46bf30a84501996.jpeg" alt="Subject into set" width="230"></a></td><td valign="top"><b>Subject into set</b><br><sub><code>bytedance/seedream-5.0-pro/edit</code></sub><br><br>Keep the woman and her black silk slip from the first image. Place her seated on the edge of the bed in the second image&#x27;s candlelit room, turned slightly toward the candles. Relight her entirely with that candlelight — warm amber key from the nightstand, deep brown falloff on the far side — so the two images read as one photograph.<br><sub>Imagen(es) de entrada:</sub> <a href="https://cdn.spicyapi.ai/models/examples/inputs/60e0508caa77bc0e.png"><img src="https://cdn.spicyapi.ai/models/examples/inputs/60e0508caa77bc0e.png" width="60" alt="input"></a> <a href="https://cdn.spicyapi.ai/models/examples/inputs/fff7c1b021f6ad32.png"><img src="https://cdn.spicyapi.ai/models/examples/inputs/fff7c1b021f6ad32.png" width="60" alt="input"></a></td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-5-0-pro/29f6845c8b668487.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5-0-pro/29f6845c8b668487.webp" alt="Candlelit bedroom" width="230"></a></td><td valign="top"><b>Candlelit bedroom</b><br><sub><code>bytedance/seedream-5.0-pro/text-to-image</code></sub><br><br>Candlelit bedroom at night, dozens of pillar candles on the floor and dresser. An adult woman in a sheer black slip sits on the edge of the bed half-turned away, her silhouette and the curve of her back rendered mostly in warm shadow, a single candle flame sharp in the foreground. Deep amber and black, heavy chiaroscuro, film grain, intimate and restrained, medium format look.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-5-0-pro/bbf4eaf4d9da1edd.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5-0-pro/bbf4eaf4d9da1edd.webp" alt="Dinner after closing" width="230"></a></td><td valign="top"><b>Dinner after closing</b><br><sub><code>bytedance/seedream-5.0-pro/text-to-image</code></sub><br><br>An empty candlelit restaurant after closing: an adult woman in a backless black velvet gown sits turned away from the camera, one long glove dropped on the tablecloth, while at the far end of the table an adult man pours two glasses of red wine. Low amber light, deep burgundy walls, slow-shutter candle glow.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-5-0-pro/00f03225bc11c853.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5-0-pro/00f03225bc11c853.webp" alt="Deco staircase shadow" width="230"></a></td><td valign="top"><b>Deco staircase shadow</b><br><sub><code>bytedance/seedream-5.0-pro/text-to-image</code></sub><br><br>A hard monochrome art deco stairwell: an adult woman in a floor-length satin gown descends slowly, a single spotlight throwing her long shadow up the curved wall, one gloved hand trailing the chrome banister. Deep blacks, silvery highlights, classic noir framing.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-5-0-pro/3902f4e09898d95d.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5-0-pro/3902f4e09898d95d.webp" alt="Candle profile rain window" width="230"></a></td><td valign="top"><b>Candle profile rain window</b><br><sub><code>bytedance/seedream-5.0-pro/text-to-image</code></sub><br><br>Low-key portrait of an adult man in an open-collared black silk shirt beside a rain-streaked window, a single candle carving his profile out of the dark while his gaze drifts past the lens. Chiaroscuro, deep umber palette, fine grain.</td></tr>
</table>

### Qwen Image Edit Spicy

<sub>🌶️ Edición Spicy · <a href="https://spicyapi.ai/es/models/qwen-image-spicy-edit?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/5ae28cdb921ffbef.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/5ae28cdb921ffbef.webp" alt="Boudoir i2i" width="230"></a></td><td valign="top"><b>Boudoir i2i</b><br><sub><code>alibaba/qwen-image-spicy-edit/edit</code></sub><br><br>Change the light to a warm sunset glow raking across her skin from the window, keep the pose and the room, cinematic colour, 35mm film grain<br><sub>Imagen(es) de entrada:</sub> <a href="https://cdn.spicyapi.ai/models/examples/seedream-5.0-pro/61ee3cb871442de4.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5.0-pro/61ee3cb871442de4.webp" width="60" alt="input"></a></td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/5511ef893ad0395f.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/5511ef893ad0395f.webp" alt="Lingerie and hanger" width="230"></a></td><td valign="top"><b>Lingerie and hanger</b><br><sub><code>alibaba/qwen-image-spicy-edit/edit</code></sub><br><br>Keep the woman, the bed and the hotel room exactly as they are. Change her outfit to a black lace bodysuit with sheer black stockings, and change the brass door hanger text to read &#x27;BACK AT MIDNIGHT&#x27;. Keep the same pose, framing, lighting and colour grade.<br><sub>Imagen(es) de entrada:</sub> <a href="https://cdn.spicyapi.ai/models/examples/inputs/e4dac453d76bb2b8.png"><img src="https://cdn.spicyapi.ai/models/examples/inputs/e4dac453d76bb2b8.png" width="60" alt="input"></a></td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/0b8d123323790a2b.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/0b8d123323790a2b.webp" alt="Latex and neon" width="230"></a></td><td valign="top"><b>Latex and neon</b><br><sub><code>alibaba/qwen-image-spicy-edit/edit</code></sub><br><br>Keep the rider, the motorcycle and the neon garage exactly as they are. Change her outfit to a glossy black latex bodysuit with a deep front zip and long gloves, add sheer black stockings, and change the neon sign on the back wall to read &#x27;AFTER HOURS&#x27;. Keep the same pose, framing, magenta and cyan lighting and colour grade.<br><sub>Imagen(es) de entrada:</sub> <a href="https://cdn.spicyapi.ai/models/examples/inputs/d1794334e1998b66.png"><img src="https://cdn.spicyapi.ai/models/examples/inputs/d1794334e1998b66.png" width="60" alt="input"></a></td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/c6eb2b0782685ed4.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/c6eb2b0782685ed4.webp" alt="Midday to candlelit" width="230"></a></td><td valign="top"><b>Midday to candlelit</b><br><sub><code>alibaba/qwen-image-spicy-edit/edit</code></sub><br><br>Keep the woman, her pose at the railing, the balcony, the iron rail and the geranium pots exactly as they are, and keep the same framing and camera angle. Change the time of day from hard midday sun to late night: the sky becomes deep blue-black with stars, the sea goes dark, and the whole scene is now lit only by a cluster of candles standing along the balcony rail, so warm amber candlelight rakes across her from below and everything else falls into deep shadow. Change her white cotton sundress to a black silk slip dress. Keep her face and body identical.<br><sub>Imagen(es) de entrada:</sub> <a href="https://cdn.spicyapi.ai/models/examples/inputs/64e2cf0a92f25c51.png"><img src="https://cdn.spicyapi.ai/models/examples/inputs/64e2cf0a92f25c51.png" width="60" alt="input"></a></td></tr>
</table>

### Seedream 5.0 Lite

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/seedream-5-0-lite?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-5.0-lite/3fd75a8e556e62d1.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5.0-lite/3fd75a8e556e62d1.webp" alt="Two refs poster size" width="230"></a></td><td valign="top"><b>Two refs poster size</b><br><sub><code>bytedance/seedream-5.0-lite/edit</code></sub><br><br>Cast: one man. Build one poster-shaped frame from these two references: the figure from the first, the location from the second, shot backlit and soaking wet so water traces the line of the body and the rim light does the rest. Cinematic, shallow depth of field, heavy film grain.<br><sub>Imagen(es) de entrada:</sub> <a href="https://cdn.spicyapi.ai/models/examples/inputs/a89f0ee3314c7a0b.webp"><img src="https://cdn.spicyapi.ai/models/examples/inputs/a89f0ee3314c7a0b.webp" width="60" alt="input"></a> <a href="https://cdn.spicyapi.ai/models/examples/seedream-5.0-pro/15490cbd9b223f34.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5.0-pro/15490cbd9b223f34.webp" width="60" alt="input"></a></td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-5.0-lite/b8735fe777c8eb31.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5.0-lite/b8735fe777c8eb31.webp" alt="Siren rocks strip" width="230"></a></td><td valign="top"><b>Siren rocks strip</b><br><sub><code>bytedance/seedream-5.0-lite/text-to-image</code></sub><br><br>Cinematic film still, 21:9 ultra-wide. Close on the two of them: her scaled hip and his soaked shirt pressed together, water sheeting off both, her head tipped back. On black sea rocks a mermaid and a sailor are hit by the same breaking wave, scales and soaked cloth pressed together, both drenched; the horizon line runs the full width of the frame under a storm-lit sky. Lighthouse beam raking across the spray. 65mm anamorphic, heavy grain, storm green and pewter palette, restrained and tasteful.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-5-0-lite/249dca7c555aeba2.jpeg"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5-0-lite/249dca7c555aeba2.jpeg" alt="Keep her swap everything" width="230"></a></td><td valign="top"><b>Keep her swap everything</b><br><sub><code>bytedance/seedream-5.0-lite/edit</code></sub><br><br>Keep this woman&#x27;s face, body, pose and framing exactly as they are. Replace everything else: put her in a rain-soaked back alley at 2 a.m., wet asphalt throwing magenta and cyan neon reflections, steam rising from a grate behind her, a buzzing sign just out of frame. Relight her with that neon as the only key, add the red halation bloom of Cinestill 800T around the highlights, and regrade to teal shadows with warm skin.<br><sub>Imagen(es) de entrada:</sub> <a href="https://cdn.spicyapi.ai/models/examples/inputs/b93f6318cf42b8dc.png"><img src="https://cdn.spicyapi.ai/models/examples/inputs/b93f6318cf42b8dc.png" width="60" alt="input"></a></td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-5-0-lite/cc8822c0f6580dd9.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5-0-lite/cc8822c0f6580dd9.webp" alt="Bunny croupier" width="230"></a></td><td valign="top"><b>Bunny croupier</b><br><sub><code>bytedance/seedream-5.0-lite/text-to-image</code></sub><br><br>Anime illustration, an adult bunny-girl croupier at a velvet casino table, black satin leotard with a white collar and cuffs, sheer black tights and bunny-ear headband, fanning a deck of cards with a confident smirk, chandelier bokeh and stacked chips, rich crimson and gold palette, crisp cel shading, cinematic rim light, detailed linework.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-5-0-lite/56d56759fe941460.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5-0-lite/56d56759fe941460.webp" alt="Mirrored elevator" width="230"></a></td><td valign="top"><b>Mirrored elevator</b><br><sub><code>bytedance/seedream-5.0-lite/text-to-image</code></sub><br><br>High-contrast black-and-white photograph, hard single-source flash. An adult woman in a black one-piece swimsuit with a fur coat slung off both shoulders stands alone in a mirrored hotel elevator, one hand on the brass rail, staring straight down the lens; her reflection repeats into infinity on either side. Grainy 400-speed monochrome, deep blacks, blown highlights on skin, floor-number panel glowing.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-5-0-lite/a863d789a1b332be.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5-0-lite/a863d789a1b332be.webp" alt="Silver silk rooftop" width="230"></a></td><td valign="top"><b>Silver silk rooftop</b><br><sub><code>bytedance/seedream-5.0-lite/text-to-image</code></sub><br><br>High-fashion editorial on a windy rooftop at dusk: an adult model in a flowing liquid-silver silk gown, the fabric streaming sideways like smoke while the city lights come on below. Low angle, dramatic sky, glossy magazine finish.</td></tr>
</table>

### Qwen Image 2

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/alibaba-qwen-image-2?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/alibaba-qwen-image-2/9944fb81c5b817b4.webp"><img src="https://cdn.spicyapi.ai/models/examples/alibaba-qwen-image-2/9944fb81c5b817b4.webp" alt="Cyber alley bilingual" width="230"></a></td><td valign="top"><b>Cyber alley bilingual</b><br><sub><code>alibaba/qwen-image-2/text-to-image</code></sub><br><br>Cinematic film still, rain-soaked cyberpunk alley at 3am. A woman stands behind a fogged shopfront window looking back over her shoulder; her thin white shirt is soaked through and clings to her shoulder blades, a faint glowing chrome port at the nape of her neck. Bilingual neon signage in Chinese and English reading 夜宵 NIGHT NOODLES and 义体维修 CHROME REPAIR throws hard magenta and cyan across the wet fabric and across the patch of condensation she has wiped clear with one palm. 35mm anamorphic, shallow depth of field, heavy film grain, teal and magenta palette, restrained and tasteful.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/alibaba-qwen-image-2/1fc5ed49b5c763d4.webp"><img src="https://cdn.spicyapi.ai/models/examples/alibaba-qwen-image-2/1fc5ed49b5c763d4.webp" alt="Midnight fox bar" width="230"></a></td><td valign="top"><b>Midnight fox bar</b><br><sub><code>alibaba/qwen-image-2/text-to-image</code></sub><br><br>Photorealistic cinematic still of a real adult woman in a dim neon cocktail bar at night, wearing a loose chocolate satin robe slipping off one shoulder, and a large fluffy orange-and-white faux fox tail accessory clipped at the small of her back, curving up behind her hip. She leans on the bar and glances back over her shoulder at the camera with a teasing half-smile. Red paper lanterns overhead, a neon sign on the back wall reading &#x27;MIDNIGHT FOX&#x27;, bottles bokeh, 35mm film grain, warm amber and crimson light.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/alibaba-qwen-image-2/4ee5114e2f8f7ad6.webp"><img src="https://cdn.spicyapi.ai/models/examples/alibaba-qwen-image-2/4ee5114e2f8f7ad6.webp" alt="Subject plus set" width="230"></a></td><td valign="top"><b>Subject plus set</b><br><sub><code>alibaba/qwen-image-2/edit</code></sub><br><br>Keep the woman and her satin robe from the image. Place her leaning on the bar of a narrow neon-lit cocktail lounge, and match the warm red lantern light onto her face and shoulders so it reads as one photograph.<br><sub>Imagen(es) de entrada:</sub> <a href="https://cdn.spicyapi.ai/models/examples/inputs/9d01eb685add1832.jpeg"><img src="https://cdn.spicyapi.ai/models/examples/inputs/9d01eb685add1832.jpeg" width="60" alt="input"></a></td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/alibaba-qwen-image-2/285e36eea7b99512.webp"><img src="https://cdn.spicyapi.ai/models/examples/alibaba-qwen-image-2/285e36eea7b99512.webp" alt="Do not knock corridor" width="230"></a></td><td valign="top"><b>Do not knock corridor</b><br><sub><code>alibaba/qwen-image-2/text-to-image</code></sub><br><br>Photorealistic cinematic still, late night in an art-deco hotel corridor lit by dim brass wall sconces, patterned carpet and dark lacquered doors receding into a deep vignette. An adult woman leans back against one door with one shoulder to the frame, wearing a black lace-trimmed champagne silk slip with a fur-collared coat hanging open off her shoulders, bare legs, barefoot on the carpet, one black high heel dangling from a fingertip while the other lies kicked over on the carpet at her feet. She looks back down the empty corridor over her shoulder. On the door beside her head a polished brass plate reads &#x27;214&#x27;, and a card hanger looped over the handle reads &#x27;DO NOT KNOCK&#x27;. Warm amber light, 35mm, shallow focus, crisp evenly spaced legible lettering.</td></tr>
</table>

### Qwen Image 2512 LoRA

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/qwen-image-2512-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2512-lora/37125836822ec18f.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2512-lora/37125836822ec18f.webp" alt="Storybook onsen" width="230"></a></td><td valign="top"><b>Storybook onsen</b><br><sub><code>alibaba/qwen-image-2512-lora/text-to-image</code></sub><br><br>storybook anime illustration of a gay couple, two rugged men in their mid thirties with stubble and broad shoulders, relaxing together at the edge of an outdoor hot spring at dusk, loose yukata open at the chest and slipping off their shoulders, one resting his head on the other&#x27;s shoulder, steam rising, lanterns glowing, soft pastel palette.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2512-lora/5a8b765771d2cf0f.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2512-lora/5a8b765771d2cf0f.webp" alt="Watercolor balcony" width="230"></a></td><td valign="top"><b>Watercolor balcony</b><br><sub><code>alibaba/qwen-image-2512-lora/text-to-image</code></sub><br><br>watercolor anime of two elegant women in their thirties on a balcony at sunset, one in a low-cut silk slip dress leaning back against the railing, the other close beside her tucking a strand of hair behind her ear, glasses of red wine, wind in their hair, loose washes and paper texture.</td></tr>
</table>

### Z-Image Spicy Pro

<sub>🌶️ Edición Spicy · <a href="https://spicyapi.ai/es/models/z-image-spicy-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Vista previa no disponible en GitHub.<br><a href="https://spicyapi.ai/es/models/z-image-spicy-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es">Míralo en spicyapi.ai</a></sub></td><td valign="top"><b>Moon pool two silhouettes</b><br><sub><code>alibaba/z-image-spicy-pro/text-to-image</code></sub><br><br>Cast: one man and one woman. Cinematic film still, a moonlit spirit spring at night. Two wet silhouettes stand at the water&#x27;s edge in near-total backlight, reduced to pure outline, water tracking down the line of the waist; glowing sigils drift on the water surface and cast faint light upward. 65mm, shallow depth of field, heavy grain, moon silver and spirit cyan, restrained and tasteful.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/f212667ed7d0360d.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/f212667ed7d0360d.webp" alt="High key pov" width="230"></a></td><td valign="top"><b>High key pov</b><br><sub><code>alibaba/z-image-spicy-pro/text-to-image</code></sub><br><br>First-person POV photograph from the foot of a bed: an adult woman reclining back against white pillows in an ivory silk slip, her bare legs stretched toward the camera in the foreground, red pedicure, a thin gold ankle chain, soft blown-out window light flooding the white sheets, minimal high-key composition, editorial portrait, 35mm.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/1cb429fdef1fd514.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/1cb429fdef1fd514.webp" alt="Garter product still" width="230"></a></td><td valign="top"><b>Garter product still</b><br><sub><code>alibaba/z-image-spicy-pro/text-to-image</code></sub><br><br>Luxury product-advertising still, immaculate studio lighting, no logos. Cropped from ribs to mid-thigh: an adult woman&#x27;s hands rest on a black satin belt at her hip; she wears a matching black silk outfit and sheer stockings against a seamless charcoal backdrop. A single hard key light rakes across the satin, catching every fibre and the sheen of the stockings; a faceted crystal perfume bottle stands on a small plinth in the near foreground, in razor focus. Commercial editorial finish, deep shadow.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/fa9a364011f6e14c.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/fa9a364011f6e14c.webp" alt="Backlit curtain shadow" width="230"></a></td><td valign="top"><b>Backlit curtain shadow</b><br><sub><code>alibaba/z-image-spicy-pro/text-to-image</code></sub><br><br>Photograph shot from inside a dark bedroom looking at a floor-to-ceiling gauzy linen curtain lit from behind by a cluster of candles on the floor. The silhouette of an adult woman is projected onto the fabric from the far side: she stands in profile, arms raised, a loose robe around her shoulders, hair loose. Only the soft dark shape and a warm amber rim read through the cloth — pure backlit shadow play. A second smaller silhouette of a candle flame flickers at the lower left, wax pooling on a saucer in the sharp near foreground. Deep black room, honey-gold glow through the weave, visible linen texture, faint smoke drifting. Vertical composition, 50mm, shallow focus on the fabric. No text, no logos.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/61b5c56ad845ab07.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/61b5c56ad845ab07.webp" alt="Full size portrait" width="230"></a></td><td valign="top"><b>Full size portrait</b><br><sub><code>alibaba/z-image-spicy-pro/text-to-image</code></sub><br><br>Editorial portrait, an adult woman in a sheer black slip standing against a bare plaster wall, single hard window light from camera right raking across the fabric, deep shadow filling the left of the frame, medium format film look, fine grain, cream and charcoal palette.</td></tr>
</table>

### Z-Image Spicy

<sub>🌶️ Edición Spicy · <a href="https://spicyapi.ai/es/models/z-image-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/36b1a32feba49df3.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy/36b1a32feba49df3.webp" alt="Leather studs low key" width="230"></a></td><td valign="top"><b>Leather studs low key</b><br><sub><code>alibaba/z-image-spicy/text-to-image</code></sub><br><br>Cinematic portrait, low key. A man in a studded leather jacket worn open over bare skin, a single hard light from one side giving only half the body and dropping the rest to black; studs catch as small specular points. 85mm, shallow depth of field, heavy grain, black and oxblood palette, restrained and tasteful.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/2da39b210f7cb985.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy/2da39b210f7cb985.webp" alt="Blind stripe boudoir" width="230"></a></td><td valign="top"><b>Blind stripe boudoir</b><br><sub><code>alibaba/z-image-spicy/text-to-image</code></sub><br><br>Photograph of an adult woman lying on her side across rumpled white linen in a black lace bodysuit, morning sun through venetian blinds casting hard stripes across her skin and the sheets, one arm stretched above her head, eyes closed, calm and warm, medium format film look, soft grain, honey and cream palette.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/aa3ba7ea60addfbc.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy/aa3ba7ea60addfbc.webp" alt="Fire escape dusk" width="230"></a></td><td valign="top"><b>Fire escape dusk</b><br><sub><code>alibaba/z-image-spicy/text-to-image</code></sub><br><br>35mm film photograph, warm grain and halation, Portra colour. An adult woman sits out on a Brooklyn fire escape at dusk in a black lace-trim slip and an unbuttoned men&#x27;s dress shirt, bare feet resting through the metal grating, an ashtray and a longneck beer beside her, head tipped back against the railing with her eyes closed. Brick wall, string lights, blue-hour sky, shallow focus.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/642b40ccba5d8d2f.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy/642b40ccba5d8d2f.webp" alt="Own legs pov" width="230"></a></td><td valign="top"><b>Own legs pov</b><br><sub><code>alibaba/z-image-spicy/text-to-image</code></sub><br><br>First-person point of view from a low chair looking down at my own crossed legs, morning sun cutting in through a tall window in hard bright stripes. Bare legs in sheer black lace-top stockings and black satin shorts, one foot in a slipper half hanging off the toes, a chipped ceramic coffee mug held between my knees, a book open on my thigh. Warm parquet floor, dust in the sunbeam, wide 24mm perspective, natural skin texture, 35mm colour film grain, unposed and lazy. Adult woman. No text, no logos.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/1585120b8cb8ed01.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy/1585120b8cb8ed01.webp" alt="Expanded one liner" width="230"></a></td><td valign="top"><b>Expanded one liner</b><br><sub><code>alibaba/z-image-spicy/text-to-image</code></sub><br><br>Adult woman in a silk robe at a rain-streaked window, candlelight.</td></tr>
</table>

### Z-Image

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/z-image?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image/67dac9fb93f37737.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image/67dac9fb93f37737.webp" alt="Gym mirror selfie" width="230"></a></td><td valign="top"><b>Gym mirror selfie</b><br><sub><code>alibaba/z-image-turbo/text-to-image</code></sub><br><br>iPhone mirror selfie, an adult woman in a charcoal sports bra and low-slung grey joggers standing in an empty late-night gym, midriff bare, one hand holding the phone, hair damp, casual confident smirk, overhead fluorescent light, slight motion blur, authentic amateur snapshot look.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image/8e4b5893c40270e8.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image/8e4b5893c40270e8.webp" alt="Motel pool lounger" width="230"></a></td><td valign="top"><b>Motel pool lounger</b><br><sub><code>alibaba/z-image-turbo/text-to-image</code></sub><br><br>1970s film still, heavy halation and faded Kodak colour, full-bleed frame with no border. An adult woman in a burnt-orange bikini and enormous tinted aviator sunglasses reclines on a floral vinyl lounger beside a kidney-shaped motel pool, a paperback lying face-down on her stomach, one knee drawn up, sipping something through a striped straw. Palm shadows across the hot concrete, chlorine sparkle, warm amber grade, soft focus and thick grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-turbo/9e31e626106155af.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-turbo/9e31e626106155af.webp" alt="Vanity mirror before curtain" width="230"></a></td><td valign="top"><b>Vanity mirror before curtain</b><br><sub><code>alibaba/z-image-turbo/text-to-image</code></sub><br><br>An old theatre dressing room before the show with only two vanity bulbs lit: an adult woman in a champagne satin slip dress is seen only in the mirror, pinning up her hair while her gaze meets the lens. Warm haze, powder hanging in the air, soft grain, intimate and restrained.</td></tr>
</table>

### Z-Image Turbo LoRA

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/z-image-turbo-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-turbo-lora/d6887daba464dd40.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-turbo-lora/d6887daba464dd40.webp" alt="Realism rain window" width="230"></a></td><td valign="top"><b>Realism rain window</b><br><sub><code>alibaba/z-image-turbo-lora/text-to-image</code></sub><br><br>Realism, a beautiful mature woman in her early thirties with sharp cheekbones and red lipstick, wearing a low-cut black satin slip dress, sits on a window ledge at night, one strap slipping off her shoulder, rain on the glass, city lights blurred behind her, one knee drawn up, soft lamp light on her face, 35mm film grain.</td></tr>
</table>

### Seedream 4.0

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/seedream-4-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-4.0/c70db7252425c84e.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-4.0/c70db7252425c84e.webp" alt="Coat street person merge" width="230"></a></td><td valign="top"><b>Coat street person merge</b><br><sub><code>bytedance/seedream-4.0/edit</code></sub><br><br>Compose one frame from these three references: the woman from the first, wearing the long coat from the second, standing on the street from the third at night. Waist-up: the coat hangs open over a thin camisole and the streetlight behind drives straight through the fabric. The coat hangs open over a thin camisole and a streetlight behind her throws the light straight through the fabric. Cinematic, shallow depth of field, heavy film grain.<br><sub>Imagen(es) de entrada:</sub> <a href="https://cdn.spicyapi.ai/models/examples/inputs/953656aeab446b5d.webp"><img src="https://cdn.spicyapi.ai/models/examples/inputs/953656aeab446b5d.webp" width="60" alt="input"></a> <a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/36b1a32feba49df3.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy/36b1a32feba49df3.webp" width="60" alt="input"></a> <a href="https://cdn.spicyapi.ai/models/examples/alibaba-qwen-image-2/9944fb81c5b817b4.webp"><img src="https://cdn.spicyapi.ai/models/examples/alibaba-qwen-image-2/9944fb81c5b817b4.webp" width="60" alt="input"></a></td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-4-0/dd1b49b5b3dc7a82.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-4-0/dd1b49b5b3dc7a82.webp" alt="Window light boudoir" width="230"></a></td><td valign="top"><b>Window light boudoir</b><br><sub><code>bytedance/seedream-4.0/text-to-image</code></sub><br><br>Editorial boudoir photograph, an adult woman in an ivory silk slip sitting on the edge of an unmade linen bed, late-afternoon window light raking across her shoulders, sheer curtain glow, soft film grain, muted cream and honey palette, 50mm lens, shallow depth of field.</td></tr>
</table>

### FLUX.1 Dev LoRA

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/flux-1-dev-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/flux-1-dev-lora/f5710c5884856f03.webp"><img src="https://cdn.spicyapi.ai/models/examples/flux-1-dev-lora/f5710c5884856f03.webp" alt="Mj mix red gown" width="230"></a></td><td valign="top"><b>Mj mix red gown</b><br><sub><code>black-forest-labs/flux-1-dev-lora/text-to-image</code></sub><br><br>MJ v6, editorial fashion photograph of a beautiful woman in a red satin gown with a plunging neckline and an open back, descending marble stairs and glancing over her bare shoulder, dramatic side light, glossy magazine look.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/flux-1-dev-lora/6d70b1c53035890c.webp"><img src="https://cdn.spicyapi.ai/models/examples/flux-1-dev-lora/6d70b1c53035890c.webp" alt="Xlabs realism beach" width="230"></a></td><td valign="top"><b>Xlabs realism beach</b><br><sub><code>black-forest-labs/flux-1-dev-lora/text-to-image</code></sub><br><br>Candid film photograph of a handsome man in his early thirties, shirtless in low-slung swim shorts, walking out of the surf at golden hour, hair slicked back, water droplets on his chest, sun glow, soft grain.</td></tr>
</table>


Algunos resultados contienen desnudos; en esos casos aquí solo se muestra el prompt, y el resultado está en spicyapi.ai.

---

## Cómo escribir un prompt de imagen NSFW

```
[Shot type] of [an adult, age range, look] + [wardrobe or state] + [pose / action]
+ [setting] + [light: source and direction] + [lens / film look] + [mood or style]
```

Es decir: tipo de plano + un adulto (rango de edad, aspecto) + vestuario o estado + pose / acción + escenario + luz (fuente y dirección) + objetivo / acabado de película + ambiente o estilo. Los prompts se escriben en inglés.

| Sí | No |
|---|---|
| "Photorealistic boudoir portrait of a woman in her early 30s…" | "Hot girl, sexy, beautiful" |
| Nombra la fuente de luz y el lado: *window light from the left* | "Good lighting" |
| Nombra un objetivo o un acabado de película: *85mm, shallow depth of field, 35mm film* | "High quality, 8k, masterpiece" |
| Describe la tela: *black lace, ivory silk, sheer mesh, satin* | "Sexy outfit" |
| Una sola pose, con las manos haciendo algo: *hands on her knees*, *holding a coffee cup* | Poses complicadas con las dos manos en el encuadre |
| Indica una edad adulta siempre: *in her 30s*, *adult man in his 40s* | Descripciones que sugieran juventud |
| Pon entre comillas las palabras exactas de carteles y portadas | Esperar que el modelo invente un texto correcto |

Qwen Image y Seedream prefieren frases naturales a listas de etiquetas. Deja las palabras negativas fuera del prompt principal (escribir "no clothes" puede confundir a los modelos; describe lo que *sí* hay). Qwen Image 3.0 Pro acepta un campo `negative_prompt` si lo necesitas.

---

## Los prompts

Cada prompt indica el modelo para el que se escribió; la mayoría funcionan en cualquiera de los modelos recomendados. Cambia a Z-Image Spicy para borradores baratos y vuelve a Qwen Image 2.1 o Seedream 5.0 Pro para las versiones finales.

### Boudoir y dormitorio

Luz suave, un solo sujeto adulto, una cama o una silla, lencería o una bata. Es la categoría NSFW más fácil: empieza aquí para ver cómo trata un modelo la piel, la tela y la luz.

#### B01 · Encaje con luz de ventana

```text
Photorealistic boudoir portrait of a woman in her early 30s sitting on the edge of an unmade bed in black lace lingerie, soft window light from the left, warm neutral bedroom, relaxed hands on her knees, looking at the camera, 85mm lens, shallow depth of field, natural skin texture.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=b01-es) | `aspect_ratio=2:3` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Indicar de qué lado está la ventana da sombras coherentes. "Natural skin texture" evita el aspecto de plástico.

#### B02 · Bata de seda en el tocador

```text
An adult woman in her late 20s in an ivory silk robe slipping off one shoulder, seated at a candlelit vanity, warm amber light, reflection in an oval mirror, soft bokeh, calm expression, editorial beauty photography.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=b02-es) | `aspect_ratio=2:3` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Los espejos son un punto fuerte de Qwen Image 2.1; si importa, describe lo que muestra el reflejo.

#### B03 · Recostada en satén rojo

```text
Wide editorial photograph of an adult woman lying on her side on red satin sheets in a red lace bodysuit, crimson key light from the right, cool blue fill from the left, full body in frame, one arm stretched above her head, high-end fashion photography.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=b03-es) | `aspect_ratio=3:2` `resolution=1.5k` | $0.048 | Intermedio |

**Consejo:** La iluminación en dos colores (luz principal cálida, relleno frío) tiene un aspecto profesional al instante.

#### B04 · Sábanas por la mañana

```text
An adult woman in her 30s waking up in white linen sheets, wearing a loose camisole, one strap fallen, soft morning light through sheer curtains, messy hair, sleepy smile, airy pastel tones, lifestyle film photography.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=b04-es) | `aspect_ratio=4:5` `resolution=1k` | $0.024 | Principiante |

**Consejo:** La luz de la mañana en tonos pastel y sobreexpuesta resulta íntima sin ser explícita.

#### B05 · Luz entre persianas

```text
Low-key photograph of an adult woman lying face-down on a bed in sheer black lingerie, hard slatted light from window blinds striping across her back and the sheets, dark room, film noir mood, 50mm lens.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=b05-es) | `aspect_ratio=3:4` `resolution=1k` | $0.024 | Intermedio |

**Consejo:** La luz dura con patrones (persianas, sombras de encaje) añade dramatismo y disimula las imperfecciones de la piel.

#### B06 · Medias y tacones

```text
An adult woman in black lingerie, sheer stockings and stiletto heels sitting on a velvet armchair with her legs crossed, dim hotel suite, warm lamp light, city lights behind the curtains, confident gaze, 35mm film look.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=b06-es) | `aspect_ratio=2:3` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Las poses sentadas mantienen las manos y las piernas en posiciones naturales.

#### B07 · Diván a la luz de las velas

```text
An adult woman in her 30s reclining on a dark velvet chaise in a black lace bodysuit, seen from behind as she glances over her shoulder, a cluster of candles on the floor as the only light, deep shadows, oxblood and gold palette.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=b07-es) | `aspect_ratio=4:5` `resolution=1k` | $0.024 | Intermedio |

**Consejo:** Una sola fuente de luz baja desde el suelo favorece y crea ambiente.

#### B08 · Camisa extragrande

```text
An adult woman in an oversized unbuttoned white men's shirt and lace underwear standing at a kitchen counter in the early morning, holding a coffee cup, soft daylight, lived-in apartment, candid feel, 35mm.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=b08-es) | `aspect_ratio=3:4` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Los objetos cotidianos (café, un libro) hacen que el boudoir parezca natural.

#### B09 · Alfombra de pelo junto al fuego

```text
An adult woman lying on a white fur rug in front of a stone fireplace, wearing a cream silk slip, firelight flickering on her skin, cozy winter cabin, warm orange and deep brown palette, shallow depth of field.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=b09-es) | `aspect_ratio=3:2` `resolution=1.5k` | $0.048 | Intermedio |

**Consejo:** La luz del fuego como única fuente da calidez al instante; menciona la chimenea en el encuadre.

#### B10 · Lluvia en la ventana

```text
An adult woman in an open white shirt sitting on a window seat watching rain run down the glass, knees drawn up, cool blue daylight, soft interior shadows, quiet melancholy mood.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=b10-es) | `aspect_ratio=2:3` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Luz fría más un tono de piel cálido es un contraste fácil y cinematográfico.

#### B11 · Cartel de puerta de hotel

```text
An adult woman in black lace lingerie and stockings sitting on a hotel bed at night, a door hanger reading "DO NOT DISTURB" in the foreground, city skyline through floor-to-ceiling windows, warm bedside lamp, editorial photography.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=b11-es) | `aspect_ratio=2:3` `resolution=1k` | $0.024 | Intermedio |

**Consejo:** Qwen Image 2.1 renderiza bien los textos cortos; pon las palabras exactas entre comillas.

#### B12 · Apoyada en albornoz

```text
Photorealistic portrait of an adult woman in her 30s in a white terry bathrobe tied loosely, leaning in a doorway after a shower, wet hair, soft steam, warm bathroom light behind her.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Z-Image Spicy](https://spicyapi.ai/es/models/z-image-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=b12-es) | `width=832` `height=1216` | $0.01235 | Principiante |

**Consejo:** Z-Image Spicy es la opción más barata para borradores rápidos; vuelve a renderizar las buenas en Qwen Image 2.1.

#### B13 · Retrato con venda en los ojos

```text
Black and white boudoir portrait of an adult woman kneeling on white sheets in black lingerie, a black satin blindfold over her eyes, soft diffused light, high contrast, elegant and minimal.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=b13-es) | `aspect_ratio=4:5` `resolution=1k` | $0.024 | Principiante |

**Consejo:** El blanco y negro elimina las dominantes de color y resulta atemporal.

#### B14 · Balcón al anochecer

```text
An adult woman in a sheer black negligee on a hotel balcony at dusk, leaning on the railing and looking back over her shoulder, city lights blurred behind, backlit rim light outlining her figure, gentle breeze in the fabric.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=b14-es) | `aspect_ratio=2:3` `resolution=1.5k` | $0.048 | Intermedio |

**Consejo:** El contraluz con tela transparente es sugerente sin mostrar detalles explícitos.

#### B15 · Arreglándose frente al espejo

```text
An adult woman in lingerie adjusting a garter strap in front of a full-length mirror, her reflection visible, warm dressing-room bulbs, pastel robe on a chair, candid behind-the-scenes feel.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=b15-es) | `aspect_ratio=3:4` `resolution=1k` | $0.024 | Intermedio |

**Consejo:** Describe tanto al sujeto como el reflejo para que el espejo sea coherente.

### Lencería y editorial de moda

Fotos de lencería y trajes de baño con calidad de revista. Nombra la tela, la luz y el objetivo; el lenguaje editorial eleva toda la imagen.

#### L01 · Catálogo en un apartamento parisino

```text
High-end lingerie campaign photo: an adult model in an ivory silk and lace set standing by a tall window in a sunlit Parisian apartment, herringbone floor, soft daylight, clean luxury aesthetic, magazine-grade color.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Seedream 5.0 Pro](https://spicyapi.ai/es/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=l01-es) | `aspect_ratio=2:3` `resolution=1k` | $0.036 | Principiante |

**Consejo:** Seedream 5.0 Pro da el acabado más "fotográfico" para fotos de estilo campaña.

#### L02 · Ciclorama de estudio

```text
Clean e-commerce photograph of an adult model in a black mesh bodysuit on a white studio cyclorama, even soft lighting, full body, neutral pose, catalog style, sharp fabric detail.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=l02-es) | `aspect_ratio=2:3` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Las fotos de catálogo necesitan luz uniforme y una pose neutra; escribe "sharp fabric detail".

#### L03 · Traje de baño junto a la piscina

```text
Summer swimwear editorial: an adult woman in a white one-piece swimsuit at the edge of a turquoise infinity pool, wet hair slicked back, bright midday sun, hard shadows, luxury villa, low camera angle.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Seedream 5.0 Pro](https://spicyapi.ai/es/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=l03-es) | `aspect_ratio=4:5` `resolution=1k` | $0.036 | Principiante |

**Consejo:** El sol duro del mediodía da brillos nítidos y satinados en la piel.

#### L04 · Detalle de corsé

```text
Close-up editorial shot of an adult woman's waist and hands lacing a black satin corset, ribbon laces in focus, candlelit boudoir behind, shallow depth of field, rich shadows.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=l04-es) | `aspect_ratio=4:5` `resolution=1k` | $0.024 | Intermedio |

**Consejo:** Los planos de detalle (manos, tela) son la forma más fácil de conseguir una anatomía impecable.

#### L05 · Látex y neón

```text
An adult woman in glossy black latex lingerie and thigh-high boots standing in an underground parking garage, magenta and cyan neon tubes, wet concrete reflections, confident pose, cyberpunk fashion editorial.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=l05-es) | `aspect_ratio=2:3` `resolution=1k` | $0.024 | Intermedio |

**Consejo:** El látex y los reflejos de neón causan mucho impacto; nombra los dos colores.

#### L06 · Abrigo de piel en el pasillo

```text
An adult woman in a long faux-fur coat worn open over black lingerie, standing in a dim hotel corridor with patterned carpet, warm wall sconces, glossy floor reflections, glamorous noir mood.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Seedream 5.0 Pro](https://spicyapi.ai/es/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=l06-es) | `aspect_ratio=2:3` `resolution=1k` | $0.036 | Intermedio |

**Consejo:** Una prenda exterior abierta enmarca la lencería y cuenta una historia.

#### L07 · Perlas y satén

```text
Macro beauty shot of layered pearl necklaces resting on an adult woman's collarbone above ivory satin, soft high-key studio light, creamy tones, luxury jewelry advertising.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=l07-es) | `aspect_ratio=1:1` `resolution=1k` | $0.024 | Principiante |

**Consejo:** El encuadre macro evita por completo las manos y las caras.

#### L08 · Foto de producto de liguero

```text
Product still of an adult model's hips and thighs in black stockings and a satin garter belt against a charcoal backdrop, a perfume bottle on a black plinth, precise studio lighting, commercial photography.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=l08-es) | `aspect_ratio=3:4` `resolution=1k` | $0.024 | Principiante |

**Consejo:** El encuadre recortado de producto es apto para marcas y vende el artículo.

#### L09 · Bata transparente a contraluz

```text
An adult woman in a sheer white robe standing in front of a bright window, backlit so her silhouette shows through the fabric, soft glow, minimal white room, fine-art fashion photography.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Seedream 5.0 Pro](https://spicyapi.ai/es/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=l09-es) | `aspect_ratio=2:3` `resolution=1k` | $0.036 | Intermedio |

**Consejo:** La tela transparente a contraluz es sugerente y elegante.

#### L10 · Sesión pin-up vintage

```text
1950s pin-up style photograph of an adult woman in high-waisted retro lingerie and seamed stockings, red lipstick, victory rolls, polka-dot backdrop, bright studio light, Kodachrome colors.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=l10-es) | `aspect_ratio=4:5` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Las referencias de época (Kodachrome, victory rolls) orientan todo el aspecto.

### Desnudo artístico y estudio de la figura

El desnudo tratado como arte: luz escultórica, siluetas, poses clásicas, estilos pictóricos. Las sombras y la composición hacen de censura, así que también pasan en plataformas con normas más estrictas.

#### F01 · Venus clásica

```text
Fine-art photograph of a nude adult woman reclining on draped white linen in the pose of a Renaissance Venus, soft north-window light, oil-painting palette, gentle film grain, museum-quality composition.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=f01-es) | `aspect_ratio=3:2` `resolution=1.5k` | $0.048 | Intermedio |

**Consejo:** Las poses de la historia del arte le dan al modelo una composición sólida que seguir.

#### F02 · Torso entre sombras de persiana

```text
High-contrast black and white photograph of an adult woman's torso in a dark room, hard striped light from window blinds across her skin, face out of frame, abstract and sculptural.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=f02-es) | `aspect_ratio=1:1` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Caras fuera de plano más luz dura = resultado artístico y apto para plataformas.

#### F03 · Silueta al atardecer

```text
Full-body silhouette of a nude adult woman standing in profile against a glowing orange sunset window, arms raised as she stretches, no visible detail, pure shape and gradient.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Seedream 5.0 Pro](https://spicyapi.ai/es/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=f03-es) | `aspect_ratio=2:3` `resolution=1k` | $0.036 | Principiante |

**Consejo:** Las siluetas se leen como desnudo sin mostrar nada.

#### F04 · Estudio de figura masculina

```text
Black and white fine-art figure study of a nude adult man in his 30s seated on a wooden stool, grey seamless backdrop, single large softbox from above left, sculpted shadows, classical pose.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=f04-es) | `aspect_ratio=3:4` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Una sola luz cenital esculpe la definición muscular.

#### F05 · Pintura corporal dorada

```text
Art photograph of an adult woman's bare back and shoulders streaked with metallic gold paint, matte black backdrop, hard key light catching the drips, gallery aesthetic.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=f05-es) | `aspect_ratio=4:5` `resolution=1k` | $0.024 | Intermedio |

**Consejo:** Los metálicos líquidos sobre la piel parecen caros y a otros modelos les cuestan.

#### F06 · Ninfa del bosque

```text
A nude adult woman with ivy woven into her long hair standing in a misty forest clearing at dawn, partly hidden by ferns in the foreground, shafts of sunlight, fairy-tale mood.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Seedream 5.0 Pro](https://spicyapi.ai/es/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=f06-es) | `aspect_ratio=3:2` `resolution=1k` | $0.036 | Principiante |

**Consejo:** El follaje en primer plano sirve también de censura natural.

#### F07 · Seda bajo el agua

```text
Underwater fine-art photograph of an adult woman floating in a flowing white silk sheet, fabric billowing around her body, light rays from the surface above, hair drifting, blue-green tones, dreamlike.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=f07-es) | `aspect_ratio=2:3` `resolution=1k` | $0.024 | Avanzado |

**Consejo:** Escribe "underwater" al principio; la física de la tela es lo que lo hace creíble.

#### F08 · Humo y forma

```text
Colored smoke in violet and teal curling around the nude figure of an adult woman standing in a black studio, the smoke veiling her body, low-key light, surreal fashion-art mood.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=f08-es) | `aspect_ratio=3:4` `resolution=1k` | $0.024 | Principiante |

**Consejo:** El humo aporta pudor y profundidad de serie.

#### F09 · Baño de leche cenital

```text
Top-down photograph of an adult woman lying in a milk bath scattered with pink rose petals, only her face, shoulders and hands above the surface, soft overhead light, pastel palette.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=f09-es) | `aspect_ratio=1:1` `resolution=1k` | $0.024 | Principiante |

**Consejo:** La superficie opaca de la leche controla la exposición y el pudor.

#### F10 · Odalisca al óleo

```text
Classical oil painting of a reclining nude adult woman on red velvet in a baroque interior, candlelight, visible brush strokes, rich chiaroscuro, museum masterpiece style.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 3.0 Pro](https://spicyapi.ai/es/models/qwen-image-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=f10-es) | `aspect_ratio=3:2` `resolution=1k` | $0.04 | Intermedio |

**Consejo:** Los estilos pictóricos son una forma segura de publicar desnudos; Qwen Image 3.0 Pro mantiene bien las pinceladas.

#### F11 · Dunas del desierto

```text
Wide shot of a nude adult woman walking away from the camera across rippled golden sand dunes at sunset, a long sheer scarf trailing in the wind, long shadows, epic scale.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Seedream 5.0 Pro](https://spicyapi.ai/es/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=f11-es) | `aspect_ratio=21:9` `resolution=1k` | $0.036 | Intermedio |

**Consejo:** Los paisajes amplios hacen que la figura sea pequeña y gráfica.

#### F12 · Pareja esculpida en arcilla

```text
Fine-art photograph of an adult couple in their 30s, both nude and partly covered in pale grey clay, sitting back to back on a studio floor like a living sculpture, soft top light, monochrome stone tones.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=f12-es) | `aspect_ratio=3:2` `resolution=1k` | $0.024 | Intermedio |

**Consejo:** Espalda con espalda mantiene los dos cuerpos claramente separados.

### Parejas e intimidad

Dos adultos que dan su consentimiento. Dale a cada persona ropa o un color distinto, describe dónde está cada una y mantén una pose sencilla para que los cuerpos no se fundan.

#### C01 · Abrazo a la luz de las velas

```text
Cinematic photograph of an adult couple in their 30s standing close in a candlelit bedroom, she wears a black slip dress, he wears an open white shirt, foreheads touching, side view, warm candlelight, shallow depth of field.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=c01-es) | `aspect_ratio=3:2` `resolution=1k` | $0.024 | Principiante |

**Consejo:** La ropa contrastada (negro frente a blanco) mantiene separadas a las dos personas.

#### C02 · Bajo la misma sábana

```text
An adult man and woman lying together under a white sheet on a bed at blue hour, her head on his bare chest, his arm around her shoulders, soft window light, quiet intimate mood, 35mm film.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=c02-es) | `aspect_ratio=3:2` `resolution=1k` | $0.024 | Intermedio |

**Consejo:** Describe exactamente dónde está cada cabeza y cada brazo.

#### C03 · Dos mujeres en un sofá

```text
Editorial photograph of two adult women in their late 20s sitting face to face on a burgundy velvet sofa, one in black lace, one in white satin, soft smiles, warm candlelight, rich interior.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=c03-es) | `aspect_ratio=3:2` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Un color distinto para cada persona evita que se mezclen las identidades.

#### C04 · Beso en el cuello

```text
An adult man standing behind an adult woman in a dim loft, kissing the side of her neck, her eyes closed and head tilted back against him, her hand in his hair, moody blue and amber light.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=c04-es) | `aspect_ratio=4:5` `resolution=1k` | $0.024 | Intermedio |

**Consejo:** Colocar a una persona detrás de la otra mantiene las caras separadas y legibles.

#### C05 · Bañera para dos

```text
An adult couple relaxing in a large freestanding bathtub full of foam, she leans back against his chest, candles around the tub, steam rising, warm golden tones.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Seedream 5.0 Pro](https://spicyapi.ai/es/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=c05-es) | `aspect_ratio=3:2` `resolution=1k` | $0.036 | Intermedio |

**Consejo:** La espuma y el vapor se encargan del pudor y la continuidad.

#### C06 · Beso en la azotea

```text
Two adult men in their 30s kissing against a rooftop railing at night, one loosening the other's tie, city skyline glittering behind, cool blue tones with warm bokeh.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=c06-es) | `aspect_ratio=3:2` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Las manos sobre la ropa (corbatas, cuellos) se leen con claridad.

#### C07 · Siluetas tras el cristal de la ducha

```text
Behind a steamed-up glass shower door, the blurred silhouettes of an adult couple embracing under running water, droplets streaking the glass, warm backlight, suggestive and soft.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=c07-es) | `aspect_ratio=2:3` `resolution=1k` | $0.024 | Principiante |

**Consejo:** El cristal esmerilado censura y disimula los errores de anatomía.

#### C08 · Cremallera del vestido

```text
Close-up from behind: an adult man's hand drawing down the zipper of an adult woman's emerald evening dress, the fabric parting across her bare back, warm lamp light, jewel tones.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=c08-es) | `aspect_ratio=4:5` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Un encuadre cerrado sobre la acción hace manejables las dos manos.

#### C09 · La mañana siguiente en la cocina

```text
An adult woman in an oversized men's shirt sitting on a kitchen counter, an adult man in grey sweatpants leaning in for a kiss, morning sun, coffee mugs, relaxed domestic intimacy.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=c09-es) | `aspect_ratio=3:2` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Los escenarios domésticos hacen que la intimidad parezca auténtica.

#### C10 · Pareja de mascarada

```text
An adult couple at a candlelit Venetian masquerade, she in a gold lace mask and low-backed black gown, he in a black mask and tuxedo, his hand on her bare back as they dance, baroque ballroom.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Seedream 5.0 Pro](https://spicyapi.ai/es/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=c10-es) | `aspect_ratio=2:3` `resolution=1k` | $0.036 | Intermedio |

**Consejo:** Las máscaras ocultan los artefactos de la cara y añaden misterio.

### Contenido de creadores y selfis

Aspecto de cámara de móvil para creadores de contenido para adultos: selfis en el espejo, aro de luz, fotos informales en el dormitorio y en el gimnasio. El realismo sale de la imperfección: un poco de grano, luz mezclada, habitaciones corrientes.

#### S01 · Selfi en el espejo

```text
Realistic smartphone mirror selfie of an adult woman in her late 20s in matching black lingerie, phone covering part of her face, messy bedroom behind her, warm ring-light glow mixed with daylight, slight grain, candid.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=s01-es) | `aspect_ratio=9:16` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Menciona el móvil en la mano y un poco de grano para que el selfi sea creíble.

#### S02 · Dormitorio con aro de luz

```text
Casual vertical photo of an adult woman in a silk robe sitting cross-legged on her bed, ring light reflected in her eyes, fairy lights on the wall, playful expression, realistic phone photo.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=s02-es) | `aspect_ratio=9:16` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Los reflejos del aro de luz en los ojos dicen "contenido de creador" al instante.

#### S03 · Espejo del gimnasio

```text
Gym mirror selfie of an adult woman in a sports bra and leggings, phone in hand, rows of machines behind her, harsh overhead fluorescent light, glistening skin after a workout, realistic phone camera.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=s03-es) | `aspect_ratio=9:16` `resolution=1k` | $0.024 | Principiante |

**Consejo:** La luz fluorescente dura resulta más creíble que una luz de estudio perfecta.

#### S04 · POV en la habitación de hotel

```text
First-person view looking down at an adult woman's own legs in black stockings stretched across a hotel bed, a coffee cup in her hand and a book open beside her, morning light, lifestyle POV.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=s04-es) | `aspect_ratio=4:5` `resolution=1k` | $0.024 | Intermedio |

**Consejo:** El encuadre POV evita las caras y resulta personal.

#### S05 · Selfi en la bañera

```text
Overhead phone photo of an adult woman relaxing in a bubble bath, foam covering her body, a glass of wine on the tub edge, candles, soft warm light, casual and cozy.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=s05-es) | `aspect_ratio=9:16` `resolution=1k` | $0.024 | Principiante |

**Consejo:** La espuma lo mantiene apto para plataformas en los adelantos.

#### S06 · Provocación en el asiento del coche

```text
Realistic phone photo of an adult woman in a leather jacket over a lace top sitting in the passenger seat of a car at night, city lights through the window, dashboard glow on her face, candid smile.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=s06-es) | `aspect_ratio=9:16` `resolution=1k` | $0.024 | Principiante |

**Consejo:** La luz práctica mezclada (salpicadero, farolas) resulta auténtica.

#### S07 · Tumbona junto a la piscina

```text
Photorealistic shot of an adult woman in a red bikini on a vintage floral sun lounger beside a motel pool, oversized sunglasses, bright afternoon sun, retro summer vibe.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Z-Image Spicy](https://spicyapi.ai/es/models/z-image-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=s07-es) | `width=1216` `height=832` | $0.01235 | Principiante |

**Consejo:** Z-Image Spicy es lo bastante barato para generar muchas variaciones para un feed.

#### S08 · Detrás de cámaras

```text
Behind-the-scenes photo of an adult woman in a black bodysuit posing on a bed during a boudoir shoot, a softbox and photographer's shadow visible, laughing between poses, candid documentary style.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=s08-es) | `aspect_ratio=3:2` `resolution=1k` | $0.024 | Principiante |

**Consejo:** El encuadre de detrás de cámaras hace que las imperfecciones parezcan intencionadas.

#### S09 · Escalera de incendios al anochecer

```text
An adult woman in a black slip dress and an open white shirt sitting barefoot on a city fire escape at dusk, string lights, a glass of wine, head tilted back, relaxed candid mood.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=s09-es) | `aspect_ratio=2:3` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Los escenarios urbanos aportan historia a las sesiones de creadores.

#### S10 · Recorte de adelanto

```text
Tight crop of an adult woman's lips and a finger raised to them in a 'shh' gesture, red lipstick, lace strap on her shoulder, soft ring light, playful teaser for a creator profile.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=s10-es) | `aspect_ratio=1:1` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Los recortes de adelanto funcionan en redes sociales con normas más estrictas y atraen clics.

### Fantasía, ciencia ficción y cosplay

Personajes de fantasía adultos y cosplay. Los materiales del vestuario y un solo elemento mágico o tecnológico sostienen la imagen; deja claro que todos los personajes son adultos.

#### X01 · Hechicera elfa oscura

```text
Fantasy photograph of an adult dark elf woman with silver hair and pointed ears in revealing black leather and silver armor, standing in a ruined candlelit temple, violet magic glowing in her open hands, dramatic rim light.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=x01-es) | `aspect_ratio=2:3` `resolution=1k` | $0.024 | Intermedio |

**Consejo:** Un solo efecto mágico cada vez mantiene la imagen legible.

#### X02 · Cámara de la súcubo

```text
Dark fantasy portrait of an adult succubus with curved horns, folded black wings and a slender tail, wearing black lingerie, standing in a red-lit gothic chamber, smoke, dramatic backlight.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=x02-es) | `aspect_ratio=2:3` `resolution=1k` | $0.024 | Intermedio |

**Consejo:** Nombra los cuernos, las alas y la cola de forma explícita o el modelo puede olvidar alguno.

#### X03 · Condesa vampira

```text
An adult vampire countess in a low-cut crimson velvet gown descending a candlelit stone staircase in a gothic castle, pale skin, a hint of fangs in her smile, deep reds and blacks.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Seedream 5.0 Pro](https://spicyapi.ai/es/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=x03-es) | `aspect_ratio=2:3` `resolution=1k` | $0.036 | Intermedio |

**Consejo:** Los interiores góticos y la luz de las velas son el punto fuerte de Seedream.

#### X04 · Bailarina cyberpunk

```text
An adult cyberpunk dancer with glowing circuit tattoos in a holographic bodysuit on a neon stage in a futuristic club, holograms flickering around her, cyan and magenta light, rain on the window behind.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=x04-es) | `aspect_ratio=2:3` `resolution=1k` | $0.024 | Intermedio |

**Consejo:** Los detalles luminosos quedan muy bien y disimulan el detalle de la piel.

#### X05 · Sirena en las rocas

```text
An adult mermaid with long red hair resting on a rock in a moonlit sea, long hair covering her chest, iridescent tail in the water, silver moonlight, gentle waves, fantasy realism.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Seedream 5.0 Pro](https://spicyapi.ai/es/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=x05-es) | `aspect_ratio=3:2` `resolution=1k` | $0.036 | Intermedio |

**Consejo:** El pelo largo es el recorte natural clásico.

#### X06 · Androide en la mesa del laboratorio

```text
Sci-fi photograph of an adult female android with a seamless white synthetic body and faint blue seams lying on a clean white lab table, eyes closed, cool clinical light, minimalist lab.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=x06-es) | `aspect_ratio=3:2` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Los paneles de piel sintética se leen como ciencia ficción y esquivan los problemas de realismo.

#### X07 · Reina guerrera

```text
An adult warrior queen in her 30s in minimal bronze armor and a fur cape standing on a cliff above a battlefield at dawn, wind in her cape and hair, sword raised, epic low-angle shot.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=x07-es) | `aspect_ratio=2:3` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Una capa al viento añade movimiento a una imagen fija.

#### X08 · Cosplay con catsuit

```text
An adult cosplayer in her 20s in a fitted black catsuit with cat ears posing in a photo studio, pink and blue gel lights, looking over her shoulder, convention photoshoot vibe.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=x08-es) | `aspect_ratio=2:3` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Indica la edad y "adult cosplayer" en cada prompt de cosplay.

#### X09 · Diosa de la primavera

```text
An adult goddess with flowers woven into her hair standing in a sunlit meadow, draped only in trailing vines and petals, soft golden light, floating pollen, painterly fantasy.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Seedream 5.0 Pro](https://spicyapi.ai/es/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=x09-es) | `aspect_ratio=3:2` `resolution=1k` | $0.036 | Principiante |

**Consejo:** Las enredaderas y los pétalos son una cobertura natural y suave.

#### X10 · Pin-up en la estación espacial

```text
An adult astronaut in a half-unzipped white flight suit floating by a large window on a space station, Earth glowing below, hair drifting in zero gravity, retro sci-fi pin-up style.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=x10-es) | `aspect_ratio=3:2` `resolution=1k` | $0.024 | Principiante |

**Consejo:** La gravedad cero justifica cualquier pose extraña.

### Anime e ilustración (Qwen Image 2.1 LoRA)

Imágenes fijas de anime, estilo hentai e ilustración con Qwen Image 2.1 LoRA y LoRAs de anime abiertos. Todos los personajes tienen un diseño adulto con proporciones adultas. Empieza el prompt con la frase de estilo del LoRA.

#### A01 · Noche en el onsen

```text
storybook anime illustration of an adult woman in her 20s with long purple hair relaxing in an outdoor hot spring at night, a towel wrapped around her, steam drifting, cherry petals on the water, paper lanterns glowing, soft smile, clean cel shading.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 LoRA](https://spicyapi.ai/es/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=a01-es) | `aspect_ratio=3:2` `resolution=1k` · LoRA: [storybook-anime LoRA](https://huggingface.co/neonforestmist/qwen-image-2512-storybook-anime-lora) × 1 | $0.03 | Principiante |

**Consejo:** Empieza con la frase de estilo del LoRA ("storybook anime illustration of").

#### A02 · Mañana en el ático

```text
storybook anime illustration of an adult woman reclining across rumpled linen in a sunlit attic room, seen from behind over her bare back and shoulder, a sheet drawn across her hip, striped morning light through a slatted window, soft cel shading.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 LoRA](https://spicyapi.ai/es/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=a02-es) | `aspect_ratio=3:4` `resolution=1k` · LoRA: [storybook-anime LoRA](https://huggingface.co/neonforestmist/qwen-image-2512-storybook-anime-lora) × 1 | $0.03 | Intermedio |

**Consejo:** Es muy parecido al ejemplo de boudoir anime que SpicyAPI ha probado.

#### A03 · Encaje en acuarela

```text
watercolor anime of an adult woman kneeling on a dark velvet chaise in a black lace bodysuit and sheer stockings, seen from behind, glancing back over her shoulder, transparent washes, pale paper texture, a single warm lamp, oxblood and ink.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 LoRA](https://spicyapi.ai/es/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=a03-es) | `aspect_ratio=4:5` `resolution=1k` · LoRA: [watercolor-anime LoRA](https://huggingface.co/neonforestmist/qwen-image-2512-watercolor-anime-lora) × 1 | $0.03 | Intermedio |

**Consejo:** Las aguadas de acuarela suavizan la piel y dan un aspecto premium.

#### A04 · Reina demonio

```text
watercolor anime of an adult demon queen with curved horns, red eyes and a slender tail in a black lace outfit, seated on a throne lit by purple fire braziers, confident expression, deep ink shadows.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 LoRA](https://spicyapi.ai/es/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=a04-es) | `aspect_ratio=2:3` `resolution=1k` · LoRA: [watercolor-anime LoRA](https://huggingface.co/neonforestmist/qwen-image-2512-watercolor-anime-lora) × 1 | $0.03 | Intermedio |

**Consejo:** Caras y proporciones adultas: escribe "adult" y dale una expresión madura.

#### A05 · Carrera en la playa

```text
storybook anime illustration of an adult woman with short blonde hair in a red bikini running along the shoreline, water splashing, bright summer sky, sparkling sea, dynamic pose, vivid colors.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 LoRA](https://spicyapi.ai/es/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=a05-es) | `aspect_ratio=3:2` `resolution=1k` · LoRA: [storybook-anime LoRA](https://huggingface.co/neonforestmist/qwen-image-2512-storybook-anime-lora) × 1 | $0.03 | Principiante |

**Consejo:** Las poses dinámicas funcionan mejor en ilustración que en fotorrealismo.

#### A06 · Dormitorio de pelo plateado

```text
storybook anime illustration of an adult woman with long silver hair lying on her side on a bed in an oversized shirt, propped on one elbow, afternoon light through curtains, soft smile, cozy detailed room.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 LoRA](https://spicyapi.ai/es/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=a06-es) | `aspect_ratio=3:2` `resolution=1k` · LoRA: [storybook-anime LoRA](https://huggingface.co/neonforestmist/qwen-image-2512-storybook-anime-lora) × 1 | $0.03 | Principiante |

**Consejo:** Los interiores acogedores dan profundidad a las escenas de anime.

#### A07 · Azotea de neón

```text
watercolor anime of an adult woman in a cropped leather jacket and bodysuit on a rooftop in a neon city at night, rain falling, wind in her hair, looking back over her shoulder, pink and cyan washes.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 LoRA](https://spicyapi.ai/es/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=a07-es) | `aspect_ratio=3:2` `resolution=1k` · LoRA: [watercolor-anime LoRA](https://huggingface.co/neonforestmist/qwen-image-2512-watercolor-anime-lora) × 1 | $0.03 | Intermedio |

**Consejo:** La lluvia y el neón quedan muy bien en acuarela.

#### A08 · Baño al anochecer

```text
watercolor anime of an adult woman stepping out of a claw-foot bath in a winter bathroom at dusk, seen from behind, steam rising and fogging the window, a towel in her hand, soft blue and amber washes.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 LoRA](https://spicyapi.ai/es/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=a08-es) | `aspect_ratio=2:3` `resolution=1k` · LoRA: [watercolor-anime LoRA](https://huggingface.co/neonforestmist/qwen-image-2512-watercolor-anime-lora) × 1 | $0.03 | Intermedio |

**Consejo:** El encuadre de espaldas mantiene de buen gusto el desnudo ilustrado.

#### A09 · Súcubo en la ventana

```text
storybook anime illustration of an adult succubus with bat wings perched on a moonlit window sill in black lingerie, her tail curling, playful smile, blue moonlight and pink rim light.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 LoRA](https://spicyapi.ai/es/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=a09-es) | `aspect_ratio=2:3` `resolution=1k` · LoRA: [storybook-anime LoRA](https://huggingface.co/neonforestmist/qwen-image-2512-storybook-anime-lora) × 1 | $0.03 | Principiante |

**Consejo:** Escribe "adult" también delante de cada criatura de fantasía.

#### A10 · Dos estilos combinados

```text
watercolor anime of an adult woman in a silk kimono loosened at the shoulders, kneeling by a paper lantern in a tatami room at night, looking at the viewer, soft cel shading with watercolor texture.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 LoRA](https://spicyapi.ai/es/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=a10-es) | `aspect_ratio=2:3` `resolution=1k` · LoRA: [watercolor-anime LoRA](https://huggingface.co/neonforestmist/qwen-image-2512-watercolor-anime-lora) × 0.9 + [storybook-anime LoRA](https://huggingface.co/neonforestmist/qwen-image-2512-storybook-anime-lora) × 0.45 | $0.03 | Avanzado |

**Consejo:** Combina dos LoRAs: acuarela a 0.9 y storybook a 0.45, como en el ejemplo de dos pesos de SpicyAPI.

### Boudoir masculino y fitness

Hombres adultos: boudoir, fitness, editorial. Las reglas son las mismas: una pose clara, una luz con nombre y un escenario real.

#### M01 · Boudoir masculino entre sábanas

```text
Photorealistic boudoir portrait of an adult man in his 30s lying back on white sheets, bare chest, grey sweatpants, soft morning window light, relaxed smile, shallow depth of field, editorial style.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=m01-es) | `aspect_ratio=2:3` `resolution=1k` | $0.024 | Principiante |

**Consejo:** La luz suave también funciona con hombres; no marques demasiado los músculos.

#### M02 · Cuero con tachuelas

```text
Low-key portrait of an adult man in an open studded leather jacket with a bare chest, single hard light from the side, black background, intense gaze, rock editorial.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=m02-es) | `aspect_ratio=3:4` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Una sola luz lateral dura define los músculos con limpieza.

#### M03 · Vapor de la ducha

```text
An adult man standing in a steamy shower, water running over his shoulders and chest, eyes closed, cropped at the waist, warm backlight through the steam, fitness editorial.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Seedream 5.0 Pro](https://spicyapi.ai/es/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=m03-es) | `aspect_ratio=2:3` `resolution=1k` | $0.036 | Principiante |

**Consejo:** Los recortes por la cintura mantienen los desnudos masculinos aptos para plataformas.

#### M04 · Boxeador tras el asalto

```text
An adult boxer in his 30s with wrapped hands and a sweat-soaked bare torso sitting on a locker-room bench, hard overhead light, gritty green tiles, determined expression.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=m04-es) | `aspect_ratio=4:5` `resolution=1k` | $0.024 | Principiante |

**Consejo:** El sudor y la luz dura venden el aspecto fitness.

#### M05 · Atardecer en la playa

```text
An adult man in his 30s walking out of the sea at sunset in swim shorts, water dripping from his chest, golden backlight, relaxed smile, lifestyle photography.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=m05-es) | `aspect_ratio=3:2` `resolution=1k` | $0.024 | Principiante |

**Consejo:** El contraluz de la hora dorada favorece a todos los tonos de piel.

#### M06 · Bata de seda en el hotel

```text
An adult man in an open black silk robe sitting on the edge of a hotel bed at night, city lights behind, a glass of whiskey in his hand, warm lamp light, confident relaxed pose.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=m06-es) | `aspect_ratio=3:2` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Los objetos les dan a las manos algo natural que hacer.

### Portadas, pósteres y rotulación

Portadas de revistas para adultos, páginas de calendario y pósteres en los que el texto tiene que salir bien escrito. Pon las palabras exactas entre comillas y di dónde van.

#### P01 · Portada de revista

```text
Adult lifestyle magazine cover: an adult model in a black lace bodysuit and sheer robe, hands in her hair, masthead reading "SPICY" in huge white letters at the top, cover lines "THE LATE SHIFT" and "ISSUE 07" at the left, studio lighting.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 3.0 Pro](https://spicyapi.ai/es/models/qwen-image-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=p01-es) | `aspect_ratio=3:4` `resolution=1k` | $0.04 | Intermedio |

**Consejo:** Qwen Image 3.0 Pro es el que renderiza las letras con más fiabilidad; pon cada palabra entre comillas.

#### P02 · Página de calendario pin-up

```text
Retro pin-up calendar page: an adult woman in a red polka-dot swimsuit sitting on a beach umbrella stand, bright 1950s illustration style, the month "JULY" in bold script at the bottom and a grid of dates below.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 3.0 Pro](https://spicyapi.ai/es/models/qwen-image-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=p02-es) | `aspect_ratio=2:3` `resolution=1k` | $0.04 | Principiante |

**Consejo:** Di dónde va cada fragmento de texto.

#### P03 · Anuncio de perfume

```text
Luxury perfume advertisement: an adult woman with bare shoulders spraying perfume on her neck, eyes closed, soft grey backdrop, the words "AFTER MIDNIGHT" in thin elegant serif type on the right, soft beauty lighting.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 3.0 Pro](https://spicyapi.ai/es/models/qwen-image-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=p03-es) | `aspect_ratio=3:4` `resolution=1k` | $0.04 | Intermedio |

**Consejo:** Las fuentes serif finas parecen premium; nombra el estilo.

#### P04 · Mensaje en el espejo empañado

```text
An adult woman wrapped in a towel in a steamy bathroom, looking at a fogged mirror where the words "WAIT UP FOR ME" are written in lipstick, warm light, cinematic.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 3.0 Pro](https://spicyapi.ai/es/models/qwen-image-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=p04-es) | `aspect_ratio=2:3` `resolution=1k` | $0.04 | Principiante |

**Consejo:** El texto dentro de la escena (en un espejo, en un cartel) resulta natural y fácil de compartir.

#### P05 · Póster de burlesque

```text
Vintage burlesque show poster: an adult performer with large white feather fans on a red-curtained stage, art deco border, headline "THE VELVET ROOM" at the top and "ONE NIGHT ONLY" at the bottom, gold and crimson.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 3.0 Pro](https://spicyapi.ai/es/models/qwen-image-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=p05-es) | `aspect_ratio=2:3` `resolution=1k` | $0.04 | Intermedio |

**Consejo:** Los marcos art déco enmarcan bien el texto.

#### P06 · Letrero de neón de motel

```text
An adult woman in a sheer pink raincoat over black lingerie standing by a vending machine outside a motel at night, a neon sign reading "VACANCY" above her, wet pavement reflections.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=p06-es) | `aspect_ratio=2:3` `resolution=1k` | $0.024 | Principiante |

**Consejo:** Qwen Image 2.1 maneja bien una palabra corta de rotulación.

### Prompts para editar imágenes sin censura

Instrucciones para Qwen Image 2.1 Edit: cambiar la ropa, cambiar la iluminación, mover la escena, cambiar el estilo o crear una serie coherente a partir de imágenes de referencia. Edita solo imágenes tuyas, de adultos que den su consentimiento o de personajes ficticios que hayas generado. Nunca "desvistas" la foto de una persona real.

#### E01 · Cambio de ropa

```text
Change her outfit to a black lace lingerie set with sheer stockings. Keep her face, hair, pose, the room and the lighting exactly the same.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 Edit](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=e01-es) | `aspect_ratio=2:3` `resolution=1k` | $0.036 | Principiante |

**Entrada:** Una foto tuya, de un adulto que da su consentimiento o de un personaje generado.  
**Consejo:** Enumera siempre lo que debe quedarse igual; el modelo conserva lo que nombras.

#### E02 · Iluminar con velas

```text
Relight the scene: turn midday light into warm candlelight from a cluster of candles on the right, deepen the shadows, keep her pose, outfit and the framing unchanged.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 Edit](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=e02-es) | `aspect_ratio=4:5` `resolution=1k` | $0.036 | Principiante |

**Entrada:** Una foto de dormitorio o boudoir tomada de día.  
**Consejo:** Cambiar la iluminación es la edición más fiable y cambia el ambiente por completo.

#### E03 · Nuevo lugar

```text
Put the woman from image 1 into the hotel suite from image 2, sitting on the bed by the window. Keep her face, body and outfit; match the warm lamp light of the room.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 Edit](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=e03-es) | `aspect_ratio=3:2` `resolution=1k` | $0.036 | Intermedio |

**Entrada:** Imagen 1: el sujeto. Imagen 2: una foto del lugar.  
**Consejo:** Refiérete a las referencias como "image 1", "image 2", en orden.

#### E04 · Mismo personaje, escena nueva

```text
Same woman as in the reference images, now in a red satin slip dress on a rooftop at dusk, leaning on the railing and looking back at the camera. Same face, same hair, same skin tone.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 Edit](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=e04-es) | `aspect_ratio=2:3` `resolution=1k` | $0.036 | Intermedio |

**Entrada:** Dos o tres imágenes del mismo personaje generado.  
**Consejo:** Más referencias del mismo personaje = identidad más fija.

#### E05 · De foto a anime

```text
Transform into anime: flat cel shading, clean linework, anime illustration. Keep her pose, the sheet across her hip, the bed, the blinds and the direction of the light.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 Edit](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=e05-es) | `aspect_ratio=3:4` `resolution=1k` | $0.036 | Intermedio |

**Entrada:** Una imagen de boudoir generada.  
**Consejo:** Para un estilo más marcado, usa la edición de Qwen Image 2.1 LoRA con un LoRA de edición de anime.

#### E06 · Del día a la noche

```text
Make it night: the window shows city lights, the only light is a warm bedside lamp. Keep the people, their poses and the framing.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 Edit](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=e06-es) | `aspect_ratio=3:2` `resolution=1k` | $0.036 | Principiante |

**Entrada:** Cualquier foto de interior con una ventana.  
**Consejo:** Cambiar la hora del día es una forma barata de crear una serie.

#### E07 · Escena siguiente

```text
Next scene, hours later: exactly the same two people lying together under the same sheet on the same bed, turned toward each other and talking quietly. The window has gone dark and only the bedside lamp is lit. Same framing, same faces, no other people.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 Edit](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=e07-es) | `aspect_ratio=3:2` `resolution=1k` | $0.036 | Avanzado |

**Entrada:** Una imagen generada de una pareja adulta en la cama.  
**Consejo:** Escribe "exactly the same two people" y "no other figures" para evitar personas de más.

#### E08 · Añadir agua y vapor

```text
Make her skin wet with water droplets and add soft steam around her, as if just out of the shower. Keep her face, pose and the background.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 Edit](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=e08-es) | `aspect_ratio=2:3` `resolution=1k` | $0.036 | Principiante |

**Entrada:** Un retrato de estudio.  
**Consejo:** Añadir ambiente es más seguro que cambiar el cuerpo.

#### E09 · Cambiar la tela

```text
Change the fabric of her bodysuit from lace to glossy black latex. Keep the cut, her pose and the lighting.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 Edit](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=e09-es) | `aspect_ratio=4:5` `resolution=1k` | $0.036 | Principiante |

**Entrada:** Una foto de lencería o de un vestido.  
**Consejo:** Cambiar el material mantiene la silueta y cambia la sensación.

#### E10 · Fondo desenfocado de estudio

```text
Replace the background with a dark grey studio backdrop and add a soft key light from the left. Keep her, her outfit and her pose exactly.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 Edit](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=e10-es) | `aspect_ratio=2:3` `resolution=1k` | $0.036 | Principiante |

**Entrada:** Una foto casera informal.  
**Consejo:** Convierte fotos de móvil en fotos de estudio.

#### E11 · Blanco y negro artístico

```text
Convert to high-contrast black and white fine-art photography with deep shadows and soft film grain. Keep everything else unchanged.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 Edit](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=e11-es) | `aspect_ratio=3:4` `resolution=1k` | $0.036 | Principiante |

**Entrada:** Cualquier foto de boudoir.  
**Consejo:** La forma más rápida de dar coherencia a una sesión.

#### E12 · Ampliar a vertical

```text
Extend the image to a tall vertical frame: continue the bed, the sheets and the wall above and below naturally. Keep the subject unchanged and centered.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 Edit](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=e12-es) | `aspect_ratio=9:16` `resolution=1k` | $0.036 | Principiante |

**Entrada:** Una imagen cuadrada u horizontal.  
**Consejo:** Pon aspect_ratio en 9:16 para portadas de historias y reels.

#### E13 · Accesorios

```text
Add a thin gold body chain, gold hoop earrings and a black satin choker. Keep her face, outfit and the lighting.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 Edit](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=e13-es) | `aspect_ratio=4:5` `resolution=1k` | $0.036 | Principiante |

**Entrada:** Un retrato.  
**Consejo:** Los añadidos pequeños son las ediciones más fiables.

#### E14 · Cambio de estación

```text
Change the season to winter: snow falling outside, frost on the window, a cozy fur throw on the chair. Keep her and her pose.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 Edit](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=e14-es) | `aspect_ratio=3:2` `resolution=1k` | $0.036 | Principiante |

**Entrada:** Una foto en exteriores.  
**Consejo:** Crea contenido de temporada a partir de una sola sesión.

#### E15 · De grupo a una sola persona

```text
Remove everyone except the woman in the red dress and fill the background naturally. Keep her pose, lighting and position.
```

| Modelo | Ajustes | Costo por imagen | Nivel |
|---|---|---|---|
| [Qwen Image 2.1 Edit](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=e15-es) | `aspect_ratio=2:3` `resolution=1k` | $0.036 | Intermedio |

**Entrada:** Una foto generada con varias personas.  
**Consejo:** Quitar personas es más fácil que añadirlas.


---

## De imagen NSFW a prompt

¿Quieres recrear el aspecto de una imagen de referencia? Descríbela en este orden y ya tienes un prompt:

1. **Plano:** retrato, cuerpo entero, primer plano, cenital, POV, plano general.
2. **Sujeto:** adulto, rango de edad, complexión, pelo, expresión. Nunca describas a una persona real identificable.
3. **Vestuario:** prenda, tela, color, cómo se lleva (abierta, caída del hombro).
4. **Pose:** dónde están las manos, dónde carga el peso, adónde mira.
5. **Escenario:** habitación, objetos, hora del día.
6. **Luz:** fuente, dirección, temperatura de color, dura o suave.
7. **Cámara:** distancia focal, profundidad de campo, película o aspecto de móvil.
8. **Estilo:** fotorrealista, editorial, cine negro, anime (y entonces añade el LoRA), pintura al óleo.

O pega tu descripción en el [redactor de prompts con LLM](#deja-que-un-llm-escriba-tus-prompts) de más abajo. Para conservar exactamente un personaje o un conjunto, sáltate el prompt y usa un [prompt de edición](#prompts-para-editar-imágenes-sin-censura) con la propia imagen como referencia (solo con imágenes tuyas, de adultos que den su consentimiento o de personajes generados).

---

## Guía rápida

**Objetivos y cámara**

| Escribe | Efecto |
|---|---|
| `85mm, shallow depth of field` | Retrato favorecedor, fondo desenfocado |
| `35mm film` | Natural, documental, algo de grano |
| `50mm` | Neutro, perspectiva fiel al ojo |
| `macro` | Detalle extremo: encaje, joyas, piel |
| `wide shot, 24mm` | Entorno, figura pequeña en el encuadre |
| `overhead / top-down` | Gráfico, plano, ideal para camas y bañeras |
| `POV` | Primera persona, cercano |
| `smartphone photo, slight grain` | Contenido de creador creíble |

**Luz**

| Ambiente | Escribe |
|---|---|
| Suave, romántico | window light, sheer curtains, golden hour |
| Dramático | single hard key light, deep shadows, chiaroscuro |
| Noir | slatted light from blinds, black and white |
| Cálido, íntimo | candlelight, firelight, tungsten lamp |
| Glamour | softbox, beauty dish, high key |
| Neón | magenta and cyan neon, wet reflections |
| Contraluz | rim light, silhouette, glowing edges |

**Looks y estilos** (escríbelos en inglés): editorial fashion photography · boudoir photography · fine-art nude photography · Kodachrome / Portra 400 film · black and white · film noir · 1950s pin-up · oil painting · watercolor anime (LoRA) · storybook anime illustration (LoRA) · cyberpunk.

**Realismo**: natural skin texture · visible pores · slight film grain · imperfect lived-in room · mixed practical light. Evita "flawless", "perfect skin" y "8k", que empujan hacia un aspecto de plástico.

---

## Ejecuta un prompt en 60 segundos

**Sin código:** pega cualquier prompt en el [generador de imágenes con IA sin censura de SpicyAPI Studio](https://spicyapi.ai/es/create/uncensored-ai-image-generator?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=run-es) y revisa el precio antes de generar.

**cURL:**

```bash
export SPICY_API_KEY="sk-spicy-..."   # https://spicyapi.ai/es/console

curl -s https://api.spicyapi.ai/api/v1/jobs/createTask \
  -H "Authorization: Bearer $SPICY_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $(uuidgen)" \
  -d '{
    "model": "alibaba/qwen-image-2.1/text-to-image",
    "input": {
      "prompt": "Photorealistic boudoir portrait of a woman in her early 30s in black lace lingerie, soft window light from the left, 85mm, natural skin texture",
      "aspect_ratio": "2:3",
      "resolution": "1k"
    }
  }'

# Consulta hasta que data.state sea "succeeded" y luego descarga data.output.assets[0].url
curl -s "https://api.spicyapi.ai/api/v1/jobs/recordInfo?taskId=TASK_ID" \
  -H "Authorization: Bearer $SPICY_API_KEY"
```

**Anime con un LoRA** (Qwen Image 2.1 LoRA): añade `"loras": [{"path": "https://huggingface.co/neonforestmist/qwen-image-2512-storybook-anime-lora/resolve/main/qwen_image_2512_storybook_anime_lora.safetensors", "scale": 1}]` a `input` y usa `"model": "alibaba/qwen-image-2.1-lora/text-to-image"`.

**Edición** (Qwen Image 2.1 Edit): usa `"model": "alibaba/qwen-image-2.1/edit"` con `"image_urls": ["https://.../your-image.jpg"]` y la instrucción de edición como `prompt`.

¿Prefieres pedírselo a un agente? Instala **[nsfw-ai-skill](https://github.com/Spicy-API/nsfw-ai-skill/blob/main/README.es.md)** en Claude Code, Cursor o Codex y di: *"genera el prompt B01 de nsfw-ai-image-prompts con Qwen Image 2.1"*.

---

## Deja que un LLM escriba tus prompts

Pega este prompt de sistema en cualquier modelo de chat (en SpicyAPI, [Grok 4.7](https://spicyapi.ai/es/models/grok-4-7?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=llm-es) y [Grok 4.3](https://spicyapi.ai/es/models/grok-4-3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=llm-es) obtuvieron las puntuaciones más altas en las pruebas de escritura para adultos):

```text
You write prompts for adult text-to-image models. Every character is an adult aged 21 or older; never use
descriptors that suggest youth and never depict real, identifiable people.
Given a short idea (or a description of a reference image), return ONE prompt of 40–90 words in this order:
shot type, subject (with adult age), wardrobe and fabric, pose and hands, setting, light source and direction,
lens or film look, style. Use natural sentences, not tag lists. Put any on-image text in quotes.
```

---

## De imagen a video

Cualquier imagen fija de aquí puede convertirse en un clip. Úsala como primer fotograma en un modelo de imagen a video; el repositorio **[nsfw-ai-video-prompts](https://github.com/Spicy-API/nsfw-ai-video-prompts/blob/main/README.es.md)** tiene 116 prompts de movimiento escritos para eso. En las pruebas de SpicyAPI, el mejor modelo de video NSFW para todo es [Wan 3.0](https://spicyapi.ai/es/models/wan-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=i2v-es) (Freedom 96, $0.45 por clip de 5 segundos a 720p).

---

## Preguntas frecuentes

### ¿Cuál es el mejor modelo de IA para imágenes NSFW?
En las pruebas publicadas por SpicyAPI: **Qwen Image 2.1** (Spicy Index 73, Freedom 96.3, desde $0.024) para la mayoría de los casos, **Qwen Image 2.1 LoRA** (#1 en el índice de imagen) y **MiniMax H3 Image LoRA** (Freedom 100) para tus propios estilos, **Seedream 5.0 Pro** para un acabado fotográfico, **Qwen Image 3.0 Pro** cuando la imagen lleva texto y **Z-Image Spicy** para los borradores más baratos. Consulta [Mejores modelos para imágenes NSFW](#mejores-modelos-para-imágenes-nsfw).

### ¿Cómo se escribe un buen prompt de imagen NSFW con IA?
Escribe frases completas en este orden: plano, sujeto adulto con su edad, vestuario y tela, pose, escenario, luz, objetivo, estilo. Nombra la fuente de luz y un objetivo; olvídate de "8k masterpiece". Consulta [Cómo escribir un prompt de imagen NSFW](#cómo-escribir-un-prompt-de-imagen-nsfw).

### ¿Puedo editar una foto con un editor de imágenes con IA sin censura?
Sí, con Qwen Image 2.1 Edit: envía de 1 a 10 imágenes de referencia y una instrucción ("change the outfit to…", "relight to candlelight…"). Edita solo imágenes tuyas, de adultos que den su consentimiento o de personajes generados; está prohibido "desvestir" fotos de personas reales. Consulta los [prompts de edición](#prompts-para-editar-imágenes-sin-censura).

### ¿Cómo se hacen imágenes de anime o de estilo hentai con IA?
Usa Qwen Image 2.1 LoRA con un LoRA de anime abierto (los LoRAs storybook-anime y watercolor-anime que usa SpicyAPI en sus propios ejemplos), empieza el prompt con la frase de estilo del LoRA y diseña todos los personajes como adultos. Consulta [Anime e ilustración](#anime-e-ilustración-qwen-image-21-lora).

### ¿Estos prompts funcionan en Stable Diffusion, ComfyUI o Midjourney?
Los prompts en forma de frases funcionan en cualquier modelo moderno, incluidos Qwen-Image y Z-Image autoalojados en ComfyUI. Los checkpoints SDXL/Pony prefieren listas de etiquetas, así que allí conviértelos en etiquetas más cortas. Midjourney no permite contenido para adultos.

### ¿Cuánto cuesta una imagen NSFW con IA?
En SpicyAPI (2026-09-27): Z-Image Spicy $0.01235, Qwen Image 2.1 $0.024 (1k), Qwen Image 2.1 LoRA $0.03, Seedream 5.0 Pro $0.036, Qwen Image 3.0 Pro $0.04, Qwen Image 2.1 Edit $0.036. Sin suscripción; las imágenes fallidas se reembolsan.

### ¿Hay algún generador de prompts de imagen NSFW?
Usa el [prompt de sistema para LLM](#deja-que-un-llm-escriba-tus-prompts) con cualquier modelo de chat, o describe una imagen de referencia con la [lista de imagen a prompt](#de-imagen-nsfw-a-prompt).

---

## Reglas

- **Solo adultos.** Nada de contenido sexual que involucre a menores de 18 años o a quien parezca menor de 18, en ningún estilo, incluido el anime. Una edad declarada no cambia el aspecto de un personaje.
- **Nada de personas reales sin consentimiento documentado.** Nada de deepfakes sexuales, de cambios de cara de personas reales en contenido sexual ni de fotos reales "desvestidas". Las figuras públicas no son una excepción.
- **Cumple la ley** del lugar donde vives y donde vive tu público, y las normas de las plataformas donde publiques.
- Normas completas de SpicyAPI: [Política de contenidos](https://spicyapi.ai/es/legal/content-policy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=rules-es) · [Política de uso aceptable](https://spicyapi.ai/es/legal/acceptable-use?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=rules-es).

## Relacionados

- **[awesome-nsfw-ai](https://github.com/Spicy-API/awesome-nsfw-ai/blob/main/README.es.md)**: lista, ordenada según pruebas, de herramientas, APIs y modelos de IA sin censura para imagen, video y texto.
- **[nsfw-ai-video-prompts](https://github.com/Spicy-API/nsfw-ai-video-prompts/blob/main/README.es.md)**: prompts de video NSFW, prompts para el primer fotograma y 128 casos con resultados reales.
- **[nsfw-ai-skill](https://github.com/Spicy-API/nsfw-ai-skill/blob/main/README.es.md)**: genera imágenes y videos NSFW desde Claude Code, Cursor, Codex y otros agentes.
- Datos legibles por máquina: [`data/image-prompts.json`](data/image-prompts.json), [`data/showcase.json`](data/showcase.json).

## Cómo contribuir

Se aceptan pull requests con prompts. Añádelos a `data/image-prompts.json` (solo personajes adultos, modelo + ajustes + consejo) y luego ejecuta `python3 scripts/build_readme.py`. Las comprobaciones están en `scripts/check_prompts.py`.

## Licencia

Prompts y documentación: [CC0 1.0](LICENSE). Las imágenes de los ejemplos están alojadas en SpicyAPI y se enlazan, no se redistribuyen.

<p align="center"><sub>⭐ Dale una estrella al repositorio si algún prompt te ha ahorrado unos cuantos intentos.</sub></p>
