# design.md — Hirtika Dharma Portfolio Design System

> This file is the single source of truth for all visual decisions across the portfolio.
> Every component, section, and style must derive from this document.
> Do not deviate from these tokens without explicit instruction.

---

## 1. Brand Identity

**Name:** Hirtika Dharma
**Logo mark:** H·D (serif, letter-spaced)
**Tagline:** UI/UX Designer & Frontend Developer
**Tone:** Editorial, confident, clean — not loud or flashy
**Personality:** A designer who codes. Precise, modern, with warmth.

---

## 2. Color Palette

| Token | Hex | Usage |
|---|---|---|
| `--color-bg` | `#F0EDDF` | Page background (warm cream) |
| `--color-surface` | `#E8E4D4` | Cards, input fields, subtle panels |
| `--color-olive` | `#5C6B3A` | Primary accent — buttons, active nav, highlights |
| `--color-olive-dark` | `#3E4A26` | Hover states on olive elements |
| `--color-olive-light` | `#8A9A5B` | Subtle tags, dividers, secondary accents |
| `--color-text-primary` | `#1A1A1A` | Headings, body text |
| `--color-text-secondary` | `#5A5A4A` | Captions, labels, meta text |
| `--color-text-muted` | `#9A9A8A` | Placeholder text, disabled states |
| `--color-white` | `#FFFFFF` | Card backgrounds, form fields |
| `--color-border` | `#D4D0BE` | Dividers, input borders, card outlines |

**Project card background colors (one per card, cycling):**
- Card 1: `#6B7A4A` (olive green)
- Card 2: `#C4967A` (warm terracotta/salmon)
- Card 3: `#8A9E7A` (sage green)

**Rule:** Never use pure black (`#000000`) or pure white (`#FFFFFF`) as backgrounds. Always use cream or warm tones.

---

## 3. Typography

### Font Families

```css
/* Headings — Serif editorial display */
font-family: 'Playfair Display', Georgia, serif;

/* Body — Clean humanist sans */
font-family: 'Inter', 'DM Sans', system-ui, sans-serif;

/* Logo / Monogram */
font-family: 'Playfair Display', serif;
font-weight: 700;
letter-spacing: 0.1em;
```

Import via Google Fonts:
```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
```

### Type Scale

| Token | Size | Weight | Line Height | Usage |
|---|---|---|---|---|
| `--text-hero` | `clamp(56px, 10vw, 120px)` | 900 | 0.9 | Hero name (HIRTIKA DHARMA) |
| `--text-display` | `clamp(36px, 5vw, 64px)` | 700 | 1.1 | Section headings |
| `--text-heading` | `clamp(24px, 3vw, 40px)` | 700 | 1.2 | Sub-headings, card titles |
| `--text-subheading` | `20px` | 600 | 1.3 | Project titles, labels |
| `--text-body-lg` | `18px` | 400 | 1.7 | About section body text |
| `--text-body` | `16px` | 400 | 1.6 | General body text |
| `--text-small` | `14px` | 400 | 1.5 | Captions, tags, meta |
| `--text-xs` | `12px` | 500 | 1.4 | Labels, badges, overlines |

**Rules:**
- Hero name uses Playfair Display 900 weight, uppercase
- Section headings use Playfair Display 700, title case
- All body text uses Inter
- Nav links use Inter 500, `14px`, letter-spacing `0.04em`
- Overline labels (e.g. "01 / 03", "ABOUT ME") use Inter 500 uppercase, `12px`, `letter-spacing: 0.12em`

---

## 4. Spacing System

All spacing uses an 8px base unit.

```css
--space-1:  4px;
--space-2:  8px;
--space-3:  12px;
--space-4:  16px;
--space-5:  24px;
--space-6:  32px;
--space-7:  48px;
--space-8:  64px;
--space-9:  80px;
--space-10: 96px;
--space-11: 120px;
--space-12: 160px;
```

**Section padding:** `padding: var(--space-11) 0` (120px top and bottom)
**Container horizontal padding:** `padding: 0 var(--space-8)` (64px each side)
**Card internal padding:** `var(--space-7)` (48px)
**Form field padding:** `var(--space-4) var(--space-5)` (16px 24px)
**Gap between columns:** `var(--space-8)` (64px)
**Gap between cards:** `var(--space-5)` (24px)

---

## 5. Layout

### Container

```css
.container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 64px;
}

@media (max-width: 768px) {
  .container {
    padding: 0 24px;
  }
}
```

### Grid

- **2-column layout:** `display: grid; grid-template-columns: 1fr 1fr; gap: 64px`
- **3-column layout:** `display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px`
- **Project cards (full bleed):** full viewport width with content inside container

### Breakpoints

```css
--bp-mobile:  480px;
--bp-tablet:  768px;
--bp-desktop: 1024px;
--bp-wide:    1280px;
```

---

## 6. Navigation

**Style:** Fixed top, full width, background `var(--color-bg)` with subtle bottom border `1px solid var(--color-border)`
**Height:** `72px`
**Layout:** Logo left | Nav links centered | CTA button right

```
[H·D]          Home  About  Work  Skills  Experience  Contact          [Contact Me →]
```

**Logo:**
- Font: Playfair Display 700
- Size: `20px`
- Letter spacing: `0.12em`
- Color: `var(--color-text-primary)`
- Text: `H·D`

**Nav links:**
- Font: Inter 500
- Size: `14px`
- Color: `var(--color-text-secondary)`
- Hover: `var(--color-text-primary)`
- Active/current page: underline with `var(--color-olive)`, color `var(--color-text-primary)`
- Letter spacing: `0.04em`
- Gap between links: `40px`

**CTA Button (Contact Me →):**
- Background: `var(--color-olive)`
- Color: `#FFFFFF`
- Font: Inter 600, `14px`
- Padding: `12px 24px`
- Border radius: `100px` (pill shape)
- Hover: background `var(--color-olive-dark)`
- Transition: `background 0.2s ease`

**Body offset:** All page content must have `padding-top: 72px` to account for fixed navbar.

---

## 7. Sections

### 7.1 Hero Section

**Background:** `var(--color-bg)`
**Min height:** `100vh`
**Layout:** Centered, name spans full width with photo in the middle

```
┌────────────────────────────────────────────────────┐
│                                                    │
│   HIRTIKA    [circular photo]    DHARMA            │
│                                                    │
│   [role badge]      [stats row]                    │
│                                                    │
└────────────────────────────────────────────────────┘
```

**Name text:**
- Font: Playfair Display 900
- Size: `clamp(56px, 10vw, 120px)`
- Color: `var(--color-text-primary)`
- Uppercase
- Letter spacing: `-0.02em`
- Both words on one row, photo centered between them
- Use `display: flex; align-items: center; justify-content: center; gap: 40px`

**Profile photo circle:**
- Size: `clamp(160px, 18vw, 260px)` diameter
- Shape: perfect circle (`border-radius: 50%`)
- Border: `4px solid var(--color-border)`
- Object fit: cover
- Background: `#E8C4A8` (warm blush placeholder)

**Role badge (bottom left):**
- Background: `var(--color-surface)`
- Border radius: `16px`
- Padding: `16px 20px`
- Emoji icon + text
- Font: Inter 600, `16px`

**Stats row:**
- 4 stats: Projects Completed / Happy Clients / Years Learning / CGPA
- Values: `10` / `289` / `8` / `8.43`
- Number font: Playfair Display 700, `clamp(36px, 5vw, 56px)`
- Label font: Inter 400, `11px` uppercase, letter-spacing `0.1em`, color `var(--color-text-secondary)`
- Separated by `1px solid var(--color-border)` vertical dividers
- Bottom margin before next section: `var(--space-9)` (80px)

**Decorative elements:**
- Small olive star/sparkle SVG near DHARMA — position absolute, `24px` size
- Subtle olive dot accent near stats — `12px` circle, `var(--color-olive)`
- NO ghost circle overflow — remove the faded background circle entirely

---

### 7.2 About Section

**Background:** `var(--color-bg)`
**Layout:** 2-column grid (text left, visual/stats right) inside container

**Section overline:** `ABOUT ME` — Inter 500, `12px`, uppercase, letter-spacing `0.12em`, color `var(--color-olive)`
**Heading:** `Delivering Excellence Through My Expertise` — Playfair Display 700, `clamp(32px, 4vw, 52px)`
**Body text:** Inter 400, `18px`, line-height `1.7`, color `var(--color-text-secondary)`, max-width `560px`

**Content (from resume):**
> I'm Hirtika Dharma, a Computer Science graduate passionate about designing beautiful, functional digital experiences. Currently interning as an AI Design Intern at E2M Solutions, I blend UI/UX expertise with hands-on AI tooling and frontend development to build products people love.

**Expertise list (4 items with icon):**
- UI/UX Design
- Frontend Development
- AI Design Tooling
- Product Strategy

Each item: icon (olive color) + label (Inter 600, `16px`) + brief description (Inter 400, `14px`, muted)

**Right column:** Repeat the mini stats or a stylized image — keep consistent with hero stats style.

---

### 7.3 Experience Section

**Background:** `var(--color-surface)`
**Layout:** Timeline style, single column centered or 2-col (dates left, content right)

**Section overline:** `EXPERIENCE`
**Heading:** `Where I've Worked` — Playfair Display 700

**Experience entry:**

```
[olive dot + vertical line]

Mar 2026 – May 2026
E2M Solutions Pvt Ltd — AI Intern (Design)

- Designed user interfaces in Figma focused on usability and accessibility
- Used AI tools: Gemini, Google AI Studio, Claude, Cursor, Antigravity
- Generated design components and optimized workflows via prompt engineering
- Evaluated AI outputs and refined designs for intuitive navigation
```

**Entry styling:**
- Company name: Inter 700, `18px`
- Role: Inter 600, `16px`, color `var(--color-olive)`
- Date: Inter 400, `13px`, color `var(--color-text-muted)`, uppercase
- Bullet points: Inter 400, `15px`, line-height `1.6`
- Timeline dot: `12px` circle, `var(--color-olive)` fill
- Timeline line: `1px solid var(--color-border)`

---

### 7.4 Work / Projects Section

**Background:** Full-bleed colored cards alternating
**Layout:** Each project is a full-width card with 2 columns (text left, image right) — image and text swap on alternate cards

**Card structure:**
```
┌─────────────────────────────────────────────────────────────┐
│ [card background color — full bleed]                        │
│                                                             │
│  [overline: 01 / 03 + categories]    [large project image] │
│  [Project Title — large serif]                              │
│  [Description — body text, white/light]                     │
│  [tag chips]                                                │
│  [View Case Study →] button                                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Card min-height:** `560px`
**Card padding:** `80px 64px`
**Image:** right-aligned, `max-height: 480px`, object-fit cover, slight drop shadow

**Text on colored cards:**
- All text: `#FFFFFF` or `rgba(255,255,255,0.85)`
- Overline: Inter 500, `12px`, uppercase, letter-spacing `0.1em`, `rgba(255,255,255,0.6)`
- Title: Playfair Display 700 italic, `clamp(32px, 4vw, 52px)`, white
- Description: Inter 400, `15px`, line-height `1.7`, `rgba(255,255,255,0.8)`, max-width `480px`

**Tag chips:**
- Background: `rgba(255,255,255,0.15)`
- Border: `1px solid rgba(255,255,255,0.3)`
- Color: `white`
- Font: Inter 500, `12px`
- Padding: `6px 14px`
- Border radius: `100px`
- Gap: `8px`

**CTA Button on card:**
- Background: `var(--color-olive)`
- Color: white
- Pill shape, same as navbar CTA

**Projects (from resume):**

**Card 1 — Olive Green (`#6B7A4A`)**
- Title: *Splitter — Expense Splitting App*
- Tags: Figma, Wireframing, Prototyping, UX Research
- Description: Designed a mobile UI/UX for splitting and settling shared expenses. Features real-time receipt scanning, UPI payment integration, and a clean dashboard — focused on the UI/UX design layer in Figma.
- Button: View Case Study →

**Card 2 — Terracotta (`#C4967A`)**
- Title: *Amazon Review Scraper*
- Tags: Python, Playwright, FastAPI, React
- Description: Full-stack scraper extracting 1,000+ reviews per product with real-time progress tracking, interruption recovery, CAPTCHA handling, and exports to CSV and Excel.
- Button: View Project →

**Card 3 — Sage (`#8A9E7A`)**
- Title: *Knowledge Base AI Assistant*
- Tags: Python, LangChain, RAG, ChromaDB
- Description: AI-powered assistant using RAG architecture with automated email workflows and optimized ChromaDB knowledge bases for context-aware responses.
- Button: View Project →

---

### 7.5 Skills Section

**Background:** `var(--color-bg)`
**Layout:** 2-column grid or 3-column grid of skill category cards

**Section overline:** `SKILLS`
**Heading:** `Tools & Technologies I Work With` — Playfair Display 700

**Skill categories:**

| Category | Skills |
|---|---|
| Programming | SQL, Python, Git |
| Design | Figma, Wireframing, Prototyping, UX Research |
| Data & BI | Power BI, Excel, Prompt Engineering |
| Frontend | React, HTML, CSS |

**Skill card:**
- Background: `var(--color-white)`
- Border: `1px solid var(--color-border)`
- Border radius: `16px`
- Padding: `32px`
- Category label: Inter 700, `13px`, uppercase, letter-spacing `0.1em`, `var(--color-olive)`
- Skill tags: pill chips, background `var(--color-surface)`, border `var(--color-border)`, Inter 500, `14px`

**Certifications strip (below skills):**
- Google Cybersecurity Certificate — Coursera
- Google AI Essentials — Coursera
- Claude Skills Certification — Anthropic
- Style: horizontal scrolling strip with small badge icons and Inter 400, `14px`

---

### 7.6 Contact Section

**Background:** `var(--color-bg)`
**Layout:** 2-column — form left, info card right

**Section overline:** `CONTACT`
**Heading:** `Let's Work Together` — Playfair Display 700, `clamp(32px, 4vw, 52px)`
**Subtext:** Inter 400, `16px`, color `var(--color-text-secondary)`
> Have a project, an idea, or just want to connect? I'd love to hear from you.

**Form fields (left column):**
- Full Name + Email — side by side on one row
- Subject — full width
- Message — full width, `min-height: 140px`, resizable vertically only
- Field style: background `var(--color-white)`, border `1px solid var(--color-border)`, border-radius `10px`, padding `14px 20px`, Inter 400, `15px`
- Focus state: border `var(--color-olive)`, `outline: none`
- Placeholder: Inter 400, `15px`, color `var(--color-text-muted)`
- Submit button: full width, background `var(--color-olive)`, white text, Inter 600, `15px`, padding `16px`, border-radius `10px`, hover `var(--color-olive-dark)`

**Get In Touch card (right column):**
- Background: `var(--color-white)`
- Border: `1px solid var(--color-border)`
- Border radius: `20px`
- Padding: `40px`
- Title: Inter 700, `20px`

**Contact rows:**
Each row: circular icon badge (olive bg, white icon, `44px`) + label + value, separated by `1px solid var(--color-border)` divider

| Label | Value |
|---|---|
| Email | dharmahirtika@gmail.com |
| Phone | +91 9016288070 |
| Location | Navi Mumbai, Maharashtra, India |
| LinkedIn | linkedin.com/in/hirtika-dharma |

**Available for chips (bottom of card):**
- UI/UX Design Projects
- Frontend Development
- AI Design Consulting
- Style: olive background, white text, pill shape, Inter 500, `12px`
- Below chips: `Currently open to full-time roles and freelance projects.` — Inter 400, `13px`, muted

---

## 8. Buttons

### Primary (Olive filled)
```css
background: var(--color-olive);
color: #FFFFFF;
font: 600 14px/1 'Inter', sans-serif;
padding: 12px 24px;
border-radius: 100px;
border: none;
cursor: pointer;
transition: background 0.2s ease;
```
Hover: `background: var(--color-olive-dark)`

### Secondary (Outline)
```css
background: transparent;
color: var(--color-text-primary);
border: 1.5px solid var(--color-border);
font: 500 14px/1 'Inter', sans-serif;
padding: 12px 24px;
border-radius: 100px;
```
Hover: `border-color: var(--color-olive); color: var(--color-olive)`

### Ghost (text link)
```css
background: none;
border: none;
color: var(--color-olive);
font: 600 14px/1 'Inter', sans-serif;
text-decoration: none;
```
Arrow `→` appended inline.

---

## 9. Cards

```css
.card {
  background: var(--color-white);
  border: 1px solid var(--color-border);
  border-radius: 16px;
  padding: var(--space-7); /* 48px */
  transition: box-shadow 0.2s ease, transform 0.2s ease;
}

.card:hover {
  box-shadow: 0 8px 32px rgba(0,0,0,0.08);
  transform: translateY(-2px);
}
```

---

## 10. Decorative Elements

**Olive star / sparkle:**
- SVG, 4-point star shape
- Color: `var(--color-olive)`
- Size: `20px–28px`
- Used: near hero name, section transitions
- Do NOT use more than 3 across the entire page

**Olive dot:**
- Circle, `10px–14px`
- Color: `var(--color-olive)`
- Used: timeline, stat separators

**Divider lines:**
- `1px solid var(--color-border)`
- Full width of container
- Used between major sections

**Background texture:**
- Subtle dot grid: `radial-gradient(circle, var(--color-border) 1px, transparent 1px)` at `24px 24px`
- Opacity `0.4`, position absolute, pointer-events none
- Used ONLY in hero section

---

## 11. Animations & Transitions

**Scroll reveal:** Elements fade up on scroll into view
```css
/* Initial state */
opacity: 0;
transform: translateY(24px);

/* Revealed state */
opacity: 1;
transform: translateY(0);
transition: opacity 0.5s ease, transform 0.5s ease;
```

**Stagger delay for lists/cards:** `0.1s` per item

**Hover on nav links:** `color` transition `0.15s ease`
**Hover on buttons:** `background` transition `0.2s ease`
**Hover on cards:** `box-shadow + transform` transition `0.2s ease`

**Respect reduced motion:**
```css
@media (prefers-reduced-motion: reduce) {
  * { transition: none !important; animation: none !important; }
}
```

---

## 12. Footer

**Background:** `var(--color-text-primary)` (near black `#1A1A1A`)
**Text color:** `rgba(255,255,255,0.6)`
**Layout:** Logo left | nav links center | social icons right
**Height:** `80px`
**Font:** Inter 400, `13px`
**Logo color:** `#FFFFFF`
**Divider above footer:** `1px solid var(--color-border)`

---

## 13. Responsive Rules

| Breakpoint | Changes |
|---|---|
| `< 1024px` | Container padding → `40px`, reduce hero text size |
| `< 768px` | All 2-col grids → single column, project cards stack vertically |
| `< 480px` | Container padding → `20px`, nav collapses to hamburger, hero name wraps to 2 rows |

**Mobile nav:** Hamburger icon (olive), full-screen overlay, links centered, Inter 600, `24px`

---

## 14. CSS Variables — Full Reference

Paste this into your global CSS root:

```css
:root {
  /* Colors */
  --color-bg: #F0EDDF;
  --color-surface: #E8E4D4;
  --color-olive: #5C6B3A;
  --color-olive-dark: #3E4A26;
  --color-olive-light: #8A9A5B;
  --color-text-primary: #1A1A1A;
  --color-text-secondary: #5A5A4A;
  --color-text-muted: #9A9A8A;
  --color-white: #FFFFFF;
  --color-border: #D4D0BE;

  /* Project cards */
  --card-olive: #6B7A4A;
  --card-terracotta: #C4967A;
  --card-sage: #8A9E7A;

  /* Typography */
  --font-display: 'Playfair Display', Georgia, serif;
  --font-body: 'Inter', 'DM Sans', system-ui, sans-serif;

  --text-hero: clamp(56px, 10vw, 120px);
  --text-display: clamp(36px, 5vw, 64px);
  --text-heading: clamp(24px, 3vw, 40px);
  --text-subheading: 20px;
  --text-body-lg: 18px;
  --text-body: 16px;
  --text-small: 14px;
  --text-xs: 12px;

  /* Spacing */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 24px;
  --space-6: 32px;
  --space-7: 48px;
  --space-8: 64px;
  --space-9: 80px;
  --space-10: 96px;
  --space-11: 120px;
  --space-12: 160px;

  /* Layout */
  --container-max: 1280px;
  --navbar-height: 72px;
  --section-padding: var(--space-11);
  --card-padding: var(--space-7);
  --border-radius-sm: 8px;
  --border-radius-md: 16px;
  --border-radius-lg: 20px;
  --border-radius-pill: 100px;
}
```

---

## 15. Sections Order

1. Navbar (fixed)
2. Hero — full viewport
3. About — 2 column
4. Experience — timeline
5. Work / Projects — full bleed cards
6. Skills — grid cards + certs strip
7. Contact — form + info card
8. Footer

---

*End of design.md — refer to this file for every design decision. Do not invent new tokens or styles outside this system.*