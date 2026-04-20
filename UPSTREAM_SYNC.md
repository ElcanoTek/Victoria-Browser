# Upstream Sync Guide

Victoria-Browser is a soft fork of [BrowserOS](https://github.com/browseros-ai/BrowserOS). This doc explains how to keep it in sync with upstream while preserving the Elcano/Victoria branding overlay.

## Philosophy

- **Change only what a user sees.** Keep internal identifiers (`browseros`, `BrowserosFoo`, directory names, feature-group names, patch paths) untouched so upstream diffs apply cleanly.
- **Merge, don't rebase.** Merge commits preserve branching history and let us reason about which patches were rebranding vs. feature work.
- **Branding lives in one feature.** All user-visible branding overrides are collected so they can be audited and re-applied in one pass.

## Remotes

| Remote | URL |
|---|---|
| `origin` | `git@github.com:ElcanoTek/Victoria-Browser.git` |
| `upstream` | `https://github.com/browseros-ai/BrowserOS.git` |

If `upstream` is missing:

```bash
git remote add upstream https://github.com/browseros-ai/BrowserOS.git
```

## Routine sync workflow

```bash
git fetch upstream
git checkout main
git merge upstream/main
```

Resolve conflicts, run the build smoke tests (`bun run typecheck`, etc.), commit the merge, push to `origin`.

When conflicts touch branding files (see inventory below), the Victoria side usually wins — keep our strings, URLs, colors, and logos.

## Branding file inventory

The files below make up the Elcano/Victoria branding overlay. If you touch one during feature work, flag it: the next upstream merge will likely conflict here.

### Agent (`packages/browseros-agent/apps/agent/`)

- `lib/constants/productUrls.ts` — external URLs (docs, GitHub, privacy, etc.)
- `lib/constants/productWebHost.ts` — `PRODUCT_WEB_HOST`
- `assets/product_logo.svg` — in-extension logo
- `entrypoints/newtab/index/NewTabBranding.tsx` — new-tab logo alt
- `entrypoints/sidepanel/index/ChatHeader.tsx` — sidepanel header
- `entrypoints/onboarding/**` — onboarding copy
- `wxt.config.ts` — extension name in manifest
- `styles/global.css` + theme CSS — purple accent colors

### Chromium fork (`packages/browseros/`)

- `chromium_files/chrome/app/theme/chromium/BRANDING.release` — product + bundle IDs
- `chromium_patches/chrome/install_static/chromium_install_modes.h` / `.cc` — Windows installer naming
- `chromium_patches/chrome/app/chromium_strings.grd`
- `chromium_patches/chrome/app/settings_chromium_strings.grdp`
- `chromium_patches/chrome/common/chrome_constants.cc` — product constants
- `chromium_patches/components/vector_icons/chat_orange.icon` — accent-color vector icon
- `resources/icons/` — full icon pyramid (regenerated from `product_logo.svg`)

### Build config

- `packages/browseros/build/features.yaml` — `branding` feature group already declares most of the above; don't remove those entries.

## Regenerating icons

The icon pyramid is regenerated from the Victoria ship SVG:

```bash
python3 scripts/regen-icons.py
```

This writes PNGs into `packages/browseros/resources/icons/` at the sizes Chromium expects.

## Spotting branding drift

After a merge, sanity check with:

```bash
git diff --name-only upstream/main..HEAD -- \
  packages/browseros-agent/apps/agent/lib/constants \
  packages/browseros-agent/apps/agent/entrypoints/newtab \
  packages/browseros/chromium_files/chrome/app/theme \
  packages/browseros/chromium_patches/chrome/app \
  packages/browseros/resources/icons
```

Every file listed there should be an intentional branding change. If something else shows up, it's either (a) a local feature change that should live on its own branch, or (b) drift that needs to be reverted.
