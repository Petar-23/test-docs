---
title: Petars Test
---
# N﻿ew Page

T﻿his is a small list 

* i﻿tem 1
* i﻿tem 2 
* i﻿tem 3

## This is a code block

```yaml
backend:
  name: git-gateway
  branch: main

media_folder: "docs/assets"
public_folder: "/assets"

collections:
  - name: "pages"
    label: "Pages"
    folder: "docs"
    create: true
    slug: "{{slug}}"
    fields:
      - { label: "Title", name: "title", widget: "string" }
      - { label: "Body", name: "body", widget: "markdown" }
```

## T﻿his is an Image

![](/assets/glassmorph-loading.gif "Glassmorphism Loader")